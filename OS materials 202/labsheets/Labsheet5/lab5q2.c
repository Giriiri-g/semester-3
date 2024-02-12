#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdbool.h>

#define BUFFER_SIZE 1024

int main(){
    int pfd[2];
    char buffer[BUFFER_SIZE];
    if (pipe(pfd) == -1){
        perror("pipe");
        return 1;}
    pid_t pid = fork();
    if (pid == -1){
        perror("fork");
        return 1;}
    else if (pid == 0){
        close(pfd[1]); // Close unused write end
        int sum = 0;
        while(1){
            read(pfd[0], buffer, sizeof(buffer));
            if (buffer[0] == '$') // Special character to indicate end
                break;
            int num = atoi(buffer);
            sum += num;}
        printf("Sum of numbers received from parent: %d\n", sum);
        close(pfd[0]); // Close read end
        exit(EXIT_SUCCESS);}
    else{
        close(pfd[0]); // Close unused read end
        printf("Enter integers (type any special characters to stop): \n");
        char input[BUFFER_SIZE];
        while(1){
            scanf("%s", input);
            write(pfd[1], input, sizeof(input));
            if (buffer[0] == '$') // Special character to indicate end
                break;}
        close(pfd[1]); // Close write end
        wait(NULL);} // Wait for child to finish
    return 0;}
