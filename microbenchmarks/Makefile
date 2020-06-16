all:
	$(MAKE) -C vanilla/io
	$(MAKE) -C vanilla/ipc
	$(MAKE) -C citadel/io
	$(MAKE) -C citadel/io

samples:
	$(MAKE) -C vanilla/io
	@mkdir ./samples
	@./vanilla/io/io -c ./samples/16MiB.txt
