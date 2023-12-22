#include <stdio.h>
#include <strings.h>
#include <fftw3.h>
#include <assert.h>
#include "fft.h"

static _real *_signal = NULL;
static _complex *_spectrum = NULL;

static fftw_plan plan = NULL;

void
fft_init(void)
{
  _signal = (_real *) fftw_malloc(N * sizeof(_real));
  assert(_signal);

  _spectrum = (_complex *) fftw_malloc(NH * sizeof(_complex));
  assert(_spectrum);

  plan = fftw_plan_dft_r2c_1d(N, _signal, _spectrum, FFTW_ESTIMATE);
  assert(plan);
}

void
fft_exit(void)
{
  fftw_destroy_plan(plan); plan = NULL;

  fftw_free(_signal); _signal = NULL;

  fftw_free(_spectrum); _spectrum = NULL;
}

void
fft(frame s, spectrum S)
{
  bcopy(s, _signal, N * sizeof(_real));

  fftw_execute(plan);

  bcopy(_spectrum, S, NH * sizeof(_complex));
}

/* End Of File */
