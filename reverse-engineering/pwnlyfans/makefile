default:
	emcc pwnlyfans.c -s WASM=1 -o pwnlyfans.html -s NO_EXIT_RUNTIME=1  -s "EXTRA_EXPORTED_RUNTIME_METHODS=['ccall']"
run:
	python2 -m SimpleHTTPServer
