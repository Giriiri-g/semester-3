#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    pid_t first_child, second_child;
    first_child=fork();

    if(first_child==0){
       execl("./happynewyear","./happynewyear", NULL);
      }else{
        wait(NULL);
        second_child=fork();

        if(second_child==0){
              execl("./sum","./sum",NULL);
        } else{
             wait(NULL);
             printf("Parent process exiting\n");
        }
}
return 0;
}
