#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    if(!fork()){ // first child
		execl("./happynewyear","./happynewyear", NULL);
	}
	else{
		wait(NULL);
		if(!fork()){ // second child waits until first child finishes
			execl("./sum","./sum",NULL);
		}
		else{ // parent waits until both children finishes
			wait(NULL);
			printf("Parent process exiting");
		}
	}
	return 0;
}
