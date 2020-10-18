#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{
	int i;
	char alphabet[] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

	if (argc != 2) {
		fprintf(stderr, "usage: %s <length>\n", argv[0]);
		return EXIT_FAILURE;
	}

	srand(time(NULL));

	for (i = 0; i < atoi(argv[1]); i++)
		putchar(alphabet[rand() % sizeof(alphabet)]);
	putchar('\n');

	return EXIT_SUCCESS;
}