#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include "time_chrono.h"

void bad_sleep(int s)
{
    struct timespec before, after;

    clock_gettime(CLOCK_REALTIME, &before);
    while (1) /* ATTENTE ACTIVE... */
    {
        clock_gettime(CLOCK_REALTIME, &after);
        double elapsed_secs = (after.tv_sec - before.tv_sec) +
                              (after.tv_nsec - before.tv_nsec) * 0.000000001;
        if (elapsed_secs > s) break;
    }
}
void good_sleep(int s)
{
    sleep(s);
}

struct timespec BEFORE;

void time_chrono_start()
{
    clock_gettime(CLOCK_REALTIME, &BEFORE);
}

void time_chrono_stop()
{
    struct timespec after;
    clock_gettime(CLOCK_REALTIME, &after);
    double elapsed_secs = (after.tv_sec - BEFORE.tv_sec) +
                            (after.tv_nsec - BEFORE.tv_nsec) * 0.000000001;
    printf("temps écoulé : %f\n", elapsed_secs);
}
