#pragma GCC optimize("O0")
#include <stdio.h>
#include <stdlib.h>

void
win()
{
    char buf[64];
    FILE *f = fopen("flag", "r");
    if (f == NULL)
      {
        printf("Failed to open flag file.\n");
        exit(1);
      }

    fgets(buf, 63, f);
    fprintf(stderr, buf);
}

void
vuln()
{
    char buf[100];
    gets(buf);
    puts(buf);
}

int
main()
{
    printf("%p\n", win);
    fflush(stdout);
    vuln();
    return 0;
}

