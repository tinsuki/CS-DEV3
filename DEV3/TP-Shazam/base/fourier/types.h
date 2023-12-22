#ifndef __TYPES_H__
#define __TYPES_H__

#include <complex.h>
#include <fftw3.h>

#define N 1024
//#define N 2048

#define _real double
#define _complex fftw_complex

typedef _real frame[N];
#define NH ((N/2)+1)
typedef _complex spectrum[NH];  /* only non-redundant part */

#endif /* !__TYPES_H__ */

/* End Of File */
