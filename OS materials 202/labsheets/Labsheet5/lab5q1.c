#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <ctype.h>

#define BUFFER_SIZE 1024

int main() {
    int pfd[2];
    char buffer[BUFFER_SIZE];
    pipe(pfd);
    pid_t pid = fork();
    if (pid == -1){
        perror("fork");
        exit(EXIT_FAILURE);}
    else if (pid == 0){
        close(pfd[0]); // Close unused read end
        printf("Enter a string: ");
        fgets(buffer, sizeof(buffer), stdin);
        write(pfd[1], buffer, sizeof(buffer));
        close(pfd[1]);} // Close write end
    else{
        close(pfd[1]); // Close unused write end
        read(pfd[0], buffer, sizeof(buffer));
        for (int i = 0; buffer[i]; i++){
            buffer[i] = toupper(buffer[i]);}
        printf("Uppercase string received from child: %s\n", buffer);
        close(pfd[0]); // Close read end
        wait(NULL);}
    return 0;}
