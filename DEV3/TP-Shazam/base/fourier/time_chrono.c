//
// Created by tinsuki on 15/12/23.
//
#include "time_chrono.h"
#include <time.h>
#include <stdio.h>

struct timespec start, end;

void time_chrono_stop(){
    clock_gettime(CLOCK_MONOTONIC_RAW, &end);
    int delt = (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_nsec - start.tv_nsec) / 1000;
    printf("time: %d ns\n", delt);

}

void time_chrono_start(){
    clock_gettime(CLOCK_MONOTONIC_RAW, &start);
}
