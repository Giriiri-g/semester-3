#include <stdio.h>
#include <unistd.h>

int main(){
   printf("Please enter a number: ");
   int num;
   scanf("%d", &num);
   int sum=0;
   while(num>0){
        int k=num%10;
        sum+=k;
        num=num/10;
   }
    printf("Sum of the digits: %d\n", sum);
    return 0;
}
