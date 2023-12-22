CPUPROFILE=main.prof LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprofiler.so.0 ./main
google-pprof --pdf ./main main.prof > time-profile.pdf
rm -f main.prof