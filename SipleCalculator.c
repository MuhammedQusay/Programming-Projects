#include <stdio.h> 

int main()
{
    float a, b;
    char ch;
    printf("Enter the numbers you want to calculate and the operation between them:\n");
    scanf("%f\t%c\t%f",&a,&ch,&b);

    switch(ch)
    {

        case('+'):{
            printf("%.2f",a+b);
            break;
        }

        case('-'):{
            printf("%.2f",a-b);
            break;
        }

        case('*'):{
            printf("%.2f",a*b);
            break;
        }
        
        case('/'):{
            if (b != 0){
                printf("%.2f",a/b);
              break;
            }
            else{
                printf("Cant divide by zero");
                break;
            }
            
        }

    }

    return 0;
}
