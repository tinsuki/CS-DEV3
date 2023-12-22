HEAPPROFILE=main.prof LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc.so.4 ./main
google-pprof --pdf ./main main.prof.*.heap > memory-profile.pdf
rm -f main.prof.*.heap