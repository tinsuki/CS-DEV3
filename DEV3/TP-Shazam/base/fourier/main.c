#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "dft.h"
#include "fft.h"
#include "time_chrono.h"

int main (void)
{
  frame s;

  /* sample */

  for(int i=0; i<N; i++)
    {
      s[i] = sin(2*M_PI*440*i/44100);
    }

  spectrum S;

  /* Discrete Fourier Transform */

  printf("DFT\n");

  time_chrono_start();

  for (int i=0; i<100; i++)
    {
      dft(s, S);
    }

  time_chrono_stop();

  /* Fast Fourier Transform */

  fft_init();

    printf("FFT\n");

  time_chrono_start();

  for (int i=0; i<100; i++)
    {
      fft(s, S);
    }

  time_chrono_stop();

  fft_exit();

  return 0;
}

/* End Of File */
