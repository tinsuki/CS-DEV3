#ifndef __FFT_H__
#define __FFT_H__

#include "types.h"

extern void fft_init(void);
extern void fft(frame s, spectrum S);
extern void fft_exit(void);

#endif /* !__FFT_H__ */

/* End Of File */
