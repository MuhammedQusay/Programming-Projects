#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int npc, plyr = 0;

    srand(time(0));
    npc = rand() % 3 + 1; // 1 = Rock, 2 = Paper, 3 = Scissors

    while (plyr != 1 && plyr != 2 && plyr != 3) {
        printf("What is your choice? (1.R | 2.P | 3.S): ");
        scanf("%d", &plyr);
        if (plyr != 1 && plyr != 2 && plyr != 3) {
            printf("Invalid choice. Please try again.\n");
        }
    }

    if ((plyr == 1 && npc == 3) || (plyr == 2 && npc == 1) || (plyr == 3 && npc == 2)) {
        printf("Congratulations, YOU WIN\n");
    } else if (plyr == npc) {
        printf("It's a Draw\n");
    } else {
        printf("You lose\n");
    }

    printf("Your choice: %d\nComputer's choice: %d\n", plyr, npc);
    printf("(1.R | 2.P | 3.S)\n");

    return 0;
}
