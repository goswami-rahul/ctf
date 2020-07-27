#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <assert.h>

int
main(int argc, char **argv)
{
    int seed = time(NULL);
    srand(seed);
    int balance = 999999999;
    printf("Welcome to the secure pseudorandom number generator!\n");
    while (1)
      {
        printf("1. Generate some numbers ($500000000 each).\n");
        printf("2. Generate the flag ($1000000000 each).\n");
        printf("3. Quit.\n");
        printf("Your current balance is $%d.\n", balance);
        printf("===========================================\n");
        char c = '\0';
        int count;
        // fflush(stdout);
        while (c = getchar(), !('1' <= c && c <= '3'));
        switch(c)
          {
            case '1':
                printf("Each generated number costs $500000000.\n");
                printf("How many numbers would you like to generate (max 20)?\n");
                // fflush(stdout);
                while (scanf("%d", &count) != 1);
                if (!(1 <= count && count <= 20))
                  {
                    printf("Number %d not in range.\n", count);
                    return 1;
                  }
                else if (500000000 * count > balance)
                  {
                    printf("You do not have enough money!\n");
                    return 1;
                  }
                balance -= 500000000 * count;
                fprintf(stderr, "Success!\nHere are your %d numbers.\n", count);
                for (int i = 1; i <= count; i++)
                  {
                    fprintf(stderr, "%d\n", rand());
                  }
                break;
            case '2':
                balance -= 1000000000LL;
                if (balance < 0)
                  {
                    printf("You do not have enough money!\n");
                    return 1;
                  }
                printf("Enter the secret code: ");
                // fflush(stdout);
                while (scanf("%d", &count) != 1);
                // fprintf(stderr, "got %d, need %d, seed %d\n", 
                //   count, rand(), seed);
                if (count != rand())
                  {
                    fprintf(stderr, "\nFailed :(");
                    printf("Wrong number!\n");
                    return 1;
                  }
                FILE *fp = fopen(argv[1], "r");
                if (fp == NULL)
                  {
                    printf("Could not open flag file.\n");
                    return 3;
                  }
                char flag[100];
                fgets(flag, 80, fp);
                flag[strlen(flag) - 1] = '\0';

                printf("Success!\nHere is your flag: %s\n", flag);
                fprintf(stderr, "Here is your flag %s", flag);
                return 0;
            case '3':
                return 1;
          }
        fflush(stdout);
      }
    return 1;
}
