all: ipc

CFLAGS=-Wall

ipc: ipc.c
	cc ${CFLAGS} -o $@ -DPROGNAME=\"$@\" ipc.c -lpthread
