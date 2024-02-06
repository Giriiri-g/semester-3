#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
    printf("Label -> 0 PID -> %d PPID -> %d\n", getpid(), getppid());
    if(!fork()){ // process 1
        printf("Label -> 1 PID -> %d PPID -> %d\n", getpid(), getppid());
        if(!fork()){ // process 2
            printf("Label -> 2 PID -> %d PPID -> %d\n", getpid(), getppid());
            if(!fork()){ // process 4
                printf("Label -> 4 PID -> %d PPID -> %d\n", getpid(), getppid());
                if(!fork()){ // process 6
					printf("Label -> 6 PID -> %d PPID -> %d\n", getpid(), getppid());}
                else{ // process 4
					wait(NULL);
					if(!fork()){ // process 7
                        printf("Label -> 7 PID -> %d PPID -> %d\n", getpid(), getppid());}
                    else{wait(NULL);}}}
            else{wait(NULL);}} // process 2
        else{ // process 1
            wait(NULL);
            if(!fork()){ // process 3
				printf("Label -> 3 PID -> %d PPID -> %d\n", getpid(), getppid());
				if(!fork()){ // process 5
					printf("Label -> 5 PID -> %d PPID -> %d\n", getpid(), getppid());
					
					if(!fork()){ // process 8
						printf("Label -> 8 PID -> %d PPID -> %d\n", getpid(), getppid());}
					else{ // process 5
						wait(NULL);
						if(!fork()){printf("Label -> 9 PID -> %d PPID -> %d\n", getpid(), getppid());} // process 9
						else {wait(NULL);}}} // process 8
				else{wait(NULL);}} // process 3
			else{wait(NULL);}}}  // process 1
    else {wait(NULL);} // process 0
    return 0;}

