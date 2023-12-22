//
// Created by tinsuki on 15/12/23.
//
#include "dft.h"
#include <math.h>

void dft(frame s, spectrum S){
    for(int h=0; h<NH; h++){
        S[h] = 0;
        for(int n=0; n<N; n++){
            S[h] += s[n] * cexp(-2*M_PI*I*h*n/N);
        }
    }
}