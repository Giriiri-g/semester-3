#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    int a;
    printf("Enter the Value for a: ");
    scanf("%d" ,&a);

    if(!fork()){
		printf("Label -> CIRCLE PID -> %d PPID -> %d\n" , getpid() , getppid());
        printf("The area of circle is %f and perimeter is %f\n", 3.14*a*a, 2*3.14*a);
        }
    else{
		if(!fork()){
			printf("Label -> SQUARE PID -> %d PPID -> %d\n", getpid(), getppid());
			printf("Area of square is %d and perimeter is %d\n", (a*a), (4 * a));
		}
		else{wait(NULL);} // parent has to wait until both children finishes, otherwise child will force exits with incomplete output
    }
    return 0;}
