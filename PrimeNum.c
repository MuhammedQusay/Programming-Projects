#include <stdio.h>

int main()
{
    int num, a=0;

    printf("Enter a number(just positive integers): ");
    scanf("%d",&num);

    if (num < 0){
        printf("Its not a prime number");
    }

    else{

        for (int i = 1; i <= num; ++i)
        {
            if (num % i  == 0){
                a += i;
            }
        }
        
        if (a == num+1){
            printf("Its a prime number.\n");
        }
        else{
            printf("Its not a prime number");
        }
    }

return 0;
}
