all: ipc

LIBCITADEL=/build/kernel/linux-5.6/security/citadel/daemon/libcitadel
CFLAGS=-Wall

ipc: ipc.c
	cc ${CFLAGS} -o $@ -DPROGNAME=\"$@\" ipc.c -lpthread -I${LIBCITADEL}/include -L${LIBCITADEL} -lcitadel 
