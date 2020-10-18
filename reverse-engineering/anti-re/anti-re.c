#include <stdio.h>
#include <sys/ptrace.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

void __attribute__((constructor)) antidebug();

int main(void) {

    // CUCTF{n0_d1s4ss3mBly_f0r_Y0U}
    unsigned char flag[] = {107, 125, 107, 124, 110, 163, 150, 88, 135, 140, 89, 155, 92, 155, 155, 91, 149, 106, 148, 161, 135, 142, 88, 154, 135, 129, 88, 125, 165};

    int len = strlen((char*)flag);

    char input[len];

    printf("Enter the password: ");
    fgets(input, len, stdin);

    // Simple re challenge
    for (int i = 0; i < strlen(input); i++) {
        if (flag[i] - 0x28 != input[i]) {
            printf("Not flag!\n");
            exit(EXIT_FAILURE);
        }
    }

    printf("Yay that's the flag!!!!!\n");

    return 0;
}

void antidebug() {
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        _exit(EXIT_SUCCESS);
    }
}
