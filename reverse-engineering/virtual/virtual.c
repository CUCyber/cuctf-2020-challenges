#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define NUM_REGS 2
#define STACK_SIZE 512

// VM Variables
unsigned regs[NUM_REGS];
unsigned stack[STACK_SIZE];
unsigned size_check_prog[] = {0x1000,0x7100,0x6100,0xe000,0x1000,0x8000,0x2000,0x6100,0x1001,0x4000,0x7100,0xa102,0x6100,0x1031,0x5000,0xa012,0xd100,0x0000,0xd101,0x0000};
unsigned flag_check_prog[] = {0x1000,0x7100,0x1002,0x6100,0xc000,0xa015,0x2000,0x100a,0x6100,0xc000,0xb000,0x6100,0xf000,0x5000,0x101b,0x8000,0x6100,0xe000,0x5000,0xa023,0x0000,0x2000,0x6100,0xf000,0x1006,0xb000,0x1007,0x4000,0x4000,0x1008,0x8000,0x6100,0xe000,0x5000,0xa114,0x6100,0x1001,0x4000,0x7100,0x2000,0x6100,0x102f,0x5000,0x2000,0xa102,0xd001,0x000};

// CUCTF{v1rtual_eyez_v1rtual1ze_v1rtu4l_li3ss!!!}
char flag_buf[64];
unsigned enc_buf[64] = {0x3c,0x4f,0x3c,0x51,0x3f,0x65,0x6f,0x37,0x6b,0x91,0x6e,0x7b,0x55,0x46,0x5e,0x67,0x5e,0x6e,0x48,0x8f,0x2a,0x6a,0x6d,0x70,0x5a,0x7c,0x2a,0x6e,0x5e,0x66,0x6f,0x2b,0x6b,0x71,0x6e,0x34,0x55,0x51,0x55,0x94,0x2c,0x69,0x6c,0x3c,0x1a,0x3f,0x66};
int size_check = 0;
int flag_check = 0;


/*
 *	This will be a basic stack-based virtual machine.
 *	It will have a very limited instruction set, mostly because 
 *	it is for a CTF challenge.
 */
int fib(int n) 
{ 
    if (n <= 1) 
	return n; 
    return fib(n-1) + fib(n-2); 
}

void vm(unsigned program[])
{
    /* 
     *	Couple of important variables
     *	ip -> instruction pointer, points to next instruction that is going to be executed
     *	sp -> stack pointer, points to the top of the stack
     *	state -> not a register, just keeps track if the program is currently running
     *	0 == not running , 1 == running, by default set to 1
     *	zf is zero flag
    */
    int ip = 0;
    int sp = 0;
    int state = 1;
    int zf = 0;

    //	Important functions for our stack based VM: push and pop
    //	Many instructions use these for the operations
    void push(int v)
    {
	stack[sp++] = v;
    }
    int pop()
    {
	return(stack[--sp]);
    }
    //	Helper function to view the stack
    /*
    void viewStack()
    {
	for(int i=0; i < sp; i++)
	{
	    printf(" 0x%x |", stack[i]);
	}
	printf("\n");
    }
    */
    //	Fetch -> grabs instruction at ip and increments ip
    int fetch()
    {
	return(program[ip++]);
    }

    /*
     *	Decode -> decodes instruction
     *	INSTRUCTION FORMAT
     *	12-15 bits -> instruction
     *	8-11  bits -> destination register
     *	4-7   bits -> immeadiate value, or source register
     *	0-3   bits -> immeadiate value, or secondary source register (rare)
     */	
    int instr=0, imm=0, reg1=0, reg2=0, reg3=0, tmp1=0, tmp2=0;
    void decode(int bc)
    {
	instr = (bc & 0xf000) >> 12;
	reg1  = (bc & 0xf00) >>  8;
	reg2  = (bc & 0xf0) >>  4;
	reg3  = (bc & 0xf);
	imm   = (bc & 0xff);
    }

    //	Eval -> evaluates last decoded instruction
    void eval()
    {
	switch(instr)
	{
	    case 0:
		// Halt - stop execution
		state = 0;
		break;
	    case 1:
		// Push - pushes value onto stack
		//printf("push %d\n", imm);
		push(imm);
		break;
	    case 2:
		// Pop - pops value off stack
		//printf("pop\n");
		pop();
		break;
	    case 3:
		// Dup - duplicates value on top of stack
		//printf("dup\n");
		tmp1 = pop();
		push(tmp1);
		push(tmp1);
		break;
	    case 4:
		// Add - adds two values from top of stack, stores on top of stack
		tmp1 = pop();
		tmp2 = pop();
		push(tmp1 + tmp2);
		//printf("add %d %d\n", tmp1, tmp2);
		break;
	    case 5:
		// Sub - subtracts two values from top of stack, stores on top of stack
		tmp1 = pop();
		tmp2 = pop();
		//printf("sub %d - %d\n", tmp1, tmp2);
		tmp1 = tmp1 - tmp2;
		zf = tmp1==0 ? 1 : 0;
		push(tmp1);
		break;
	    case 6:
		// Load - push value to stack from register
		//printf("load r%d\n", reg1);
		push(regs[reg1]);
		break;
	    case 7:
		// Store - pop value off stack into register
		//printf("store r%d\n", reg1);
		regs[reg1] = pop();
		break;
	    case 8:
		// XOR - xor two values from top of stack, stores on top of stack
		tmp1 = pop();
		tmp2 = pop();
		//printf("xor %d ^ %d\n", tmp1, tmp2);
		tmp1 = tmp1 ^ tmp2;
		zf = tmp1==0 ? 1 : 0;
		push(tmp1);
		break;
	    case 9:
		// AND - and two values from top of stack, stores on top of stack
		tmp1 = pop();
		tmp2 = pop();
		//printf("and %d & %d\n", tmp1, tmp2);
		tmp1 = tmp1 & tmp2;
		zf = tmp1==0 ? 1 : 0;
		push(tmp1);
		break;
	    case 10:
		// Jump (Z | NZ) - jumps to immeadiate if zero flag set/not set
		if(reg1)
		{
		    if(!zf)
		    {
			//printf("jnz\n");
			ip = imm;
		    }
		}
		else
		{
		    if(zf)
		    {
			//printf("jz\n");
			ip = imm;
		    }
		}
		break;
	    case 11:
		//printf("fib %d\n", stack[sp-1]);
		// Calculate nth most fibonacci number, push onto stack
		push(fib(pop()));
		break;
	    case 12:
		// Modulo
		tmp1 = pop();
		tmp2 = pop();
		//printf("mod %d mod %d\n", tmp1, tmp2);
		tmp1 = tmp1 % tmp2;
		zf = tmp1==0 ? 1 : 0;
		push(tmp1);
		break;
	    case 13:
		// Set check - returns value at imm
		//printf("set flag");
		if(reg1) size_check = imm;
		else flag_check = imm;
		break;
	    case 14:
		// Load flag value - pushes value from flag_buf onto stack, offset equal to value on top of stack
		//printf("flag\n");
		push(flag_buf[pop()]);
		break;
	    case 15:
		// Load encrypted flag value - pushes value from enc_buf onto stack, offset equal to value on top of stack
		//printf("enc\n");
		push(enc_buf[pop()]);
		break;

	}
    }

    // Run - runs the VM until state=0
    void run()
    {
	while(state)
	{
	    int i = fetch();
	    decode(i);
	    eval();
	}
    }

    run();
}

int main(void)
{
    puts("Enter Password:");
    fgets(flag_buf, 64, stdin);

    // Stop angr
    void *y[128], *z[128];
    for (int x = 0; x < 128; x++)
    {
      if(flag_buf[x] == 'y')
	y[x] = malloc(SHRT_MAX);
      else if(flag_buf[x] == 'z')
	z[x] = malloc(SHRT_MAX);
    }

    vm(size_check_prog);
    vm(flag_check_prog);
    if(flag_check && size_check)
    {
	puts("GG!");
    }
    else
    {
	puts("Incorrect.");
    }
}
