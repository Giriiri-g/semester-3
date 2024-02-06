#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    pid_t pid = getpid();
    pid_t ppid = getppid();
    printf("Label -> A PID -> %d PPID -> %d\n", getpid(), getppid());
    if(fork()){
        wait(NULL);
        if(fork()){
            wait(NULL);
            if(!fork()){
                printf("label -> D PID ->  %d PPID -> %d\n", getpid(), getppid());
                if(!fork()){
                    printf("label -> G PID -> %d PPID -> %d\n", getpid(), getppid());
                    if(fork()){
                        wait(NULL);
                        if(!fork()){printf("label -> I PID -> %d PPID -> %d\n", getpid(), getppid());}
                        else{wait(NULL);}}
                    else { printf("label -> H PID -> %d PPID -> %d\n", getpid(), getppid()); }}
                else { wait(NULL); }}
            else { wait(NULL); }}
        else{
            printf("label -> C PID -> %d PPID -> %d\n", getpid(), getppid());
            if(fork()){
                wait(NULL);
                if(!fork()) { printf("label -> F PID -> %d PPID -> %d\n", getpid(), getppid()); }
                else { wait(NULL); }}
            else { printf("label -> E PID -> %d PPID -> %d\n", getpid(), getppid()); }}}
    else{printf("label -> B PID -> %d PPID -> %d\n", getpid(), getppid());}
    return 0;}
