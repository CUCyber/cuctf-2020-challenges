all:
	gcc anti-re.c -o binary
	./mess.py binary anti-re
	rm -f binary
	chmod +x anti-re

binary:
	gcc anti-re.c -o binary

test: all
	./anti-re < flag.txt

clean:
	rm -f binary
	rm -f anti-re
