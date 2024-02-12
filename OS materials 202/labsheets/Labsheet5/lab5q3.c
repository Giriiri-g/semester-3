#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pc1[2], pc2[2], cp1[2], cp2[2];

    if (pipe(pc1) == -1 || pipe(pc2) == -1 || pipe(cp1) == -1 || pipe(cp2) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid_t child1_pid, child2_pid;

    if ((child1_pid = fork()) == -1) {
        perror("Fork failed");
        return 1;
    }

    if (child1_pid == 0) {  // Child 1 process
        close(pc1[1]);
        close(cp1[0]);
        close(pc2[0]);
        close(pc2[1]);
        close(cp2[0]);
        close(cp2[1]);

        int sum = 0, num;

        while (read(pc1[0], &num, sizeof(int)) > 0) {
            sum += num * num;
        }
        close(pc1[0]);
        write(cp1[1], &sum, sizeof(int));
        close(cp1[1]);

        exit(0);
    } 
    else {  // Parent process
        if ((child2_pid = fork()) == -1) {
            perror("Fork failed");
            return 1;
        }

        if (child2_pid == 0) {  // Child 2 process
            close(pc1[0]);
            close(pc1[1]);
            close(cp1[0]);
            close(cp1[1]);
            close(pc2[1]);
            close(cp2[0]);

            int count = 0, num;

            while (read(pc2[0], &num, sizeof(int)) > 0) {
                count++;
            }
            close(pc2[0]);
            write(cp2[1], &count, sizeof(int));
            close(cp2[1]);

            exit(0);
        } else {  // Parent process
            close(pc1[0]);
            close(pc2[0]);
            close(cp1[1]);
            close(cp2[1]);

            int num;

            printf("Enter integers: ");
            while (scanf("%d", &num) == 1) {
                write(pc1[1], &num, sizeof(int));
                write(pc2[1], &num, sizeof(int));
            }
            close(pc1[1]);
            close(pc2[1]);

            int sum, count;

            read(cp1[0], &sum, sizeof(int));
            read(cp2[0], &count, sizeof(int));

            close(cp1[0]);
            close(cp2[0]);

            if (count != 0) {
                float mean = (float)sum / count;
                printf("Mean of squares: %.2f\n", mean);
            } else {
                printf("No numbers were entered.\n");
            }

            wait(NULL); 
            wait(NULL);
        }
    }

    return 0;
}
