#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdbool.h>

#define BUFFER_SIZE 1024

bool is_special_char(char c) {
	const char *special_chars = "!@#$%^&*()_+{}[]/\\|><,.?\'\'\"\"*-";
    for (int i = 0; special_chars[i] != '\0'; ++i) {
        if (c == special_chars[i]) {
            return true;
        }
    }
    return false;
}

int main() {
    int pfd[2];
    char buffer[BUFFER_SIZE];

    // Create pipe
    if (pipe(pfd) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid_t pid = fork();

    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // Child process
        close(pfd[1]); // Close unused write end
        int sum = 0;

        while (1) {
            read(pfd[0], buffer, sizeof(buffer));

            if (is_special_char(buffer[0])) // Special character to indicate end
                break;

            int num = atoi(buffer);
            sum += num;
        }

        printf("Sum of numbers received from parent: %d\n", sum);
        close(pfd[0]); // Close read end
        exit(EXIT_SUCCESS);
    } else {
        // Parent process
        close(pfd[0]); // Close unused read end

        printf("Enter integers (type any special characters to stop): \n");
        char input[BUFFER_SIZE];
        while (1) {
            scanf("%s", input);
            write(pfd[1], input, sizeof(input));

            if (is_special_char(input[0])) // Special character to indicate end
                break;
        }

        close(pfd[1]); // Close write end
        wait(NULL); // Wait for child to finish
    }

    return 0;
}
