#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include "time_chrono.h"

void countdown()
{
    int timeStart = 10;
    for(int i = timeStart-1; i >= 0 ; i--)
    {
        sleep(1);
        printf("%ds\n",i);
    }
}

int main()
{
    good_sleep(3);
    bad_sleep(3);
    return 0;
}