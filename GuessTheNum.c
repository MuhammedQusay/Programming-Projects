#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int num, ges;

    srand(time(0));
    num  = rand() % 100 + 1;

    printf("Guess a number between 0-100:");
    scanf("%d", &ges);
    
    while (1) {

        if (0 > ges || ges > 100) {
            printf("\n1Invalid guess. Please try again between 0-100:\n");
            scanf("%d", &ges);
        }
        else if (ges > num){
            printf("\nToo high, try lower:");
            scanf("%d", &ges);
        }
        else if (ges < num){
            printf("\nToo low, try higher:");
            scanf("%d", &ges);
        }
        else{
            printf("\nCorecct!,YOU WIN\n");
            printf("The number was: %d",num);
            break;
        }
    }
    
    

return 0;
}
