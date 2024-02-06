#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {    
    int r;
    float Carea, Cperimeter;

    printf("Enter the radius of the circle: ");
    scanf("%d" , &r);
    
    int a;
    printf("Enter the side of the square: ");
    scanf("%d" ,&a);

    if(fork()){
		printf("Label -> CIRCLE PID -> %d PPID -> %d\n" , getpid() , getppid());
		Carea = 3.14 * r * r;
	    Cperimeter = 2 * 3.14 * r;
        printf("The area of circle is %f and perimeter is %f\n", Carea, Cperimeter);
        }
    else{
        printf("Label -> SQUARE PID -> %d PPID -> %d\n", getpid(), getppid());
        printf("Area of square is %d and perimeter is %d\n", (a*a), (4 * a));
    }
    return 0;}
