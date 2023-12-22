#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "dft.h"

void dft(frame s, spectrum S)
{
    for(int m = 0 ; m < N/2+1 ; m++)
    {
        S[m] = 0;
        for(int n = 0 ; n < N ; n++ )
        {
            S[m] += s[n] * cexp(-2*I*M_PI*n*m/N);
        }
    }
    
}