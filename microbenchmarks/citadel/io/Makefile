
all: io

LIBCITADEL=/build/kernel/linux-5.6/security/citadel/daemon/libcitadel

io: io.c
	cc -Wall -o $@ -DPROGNAME=\"$@\" io.c -I${LIBCITADEL}/include -L${LIBCITADEL} -lcitadel 
