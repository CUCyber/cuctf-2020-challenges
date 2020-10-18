final:
	gcc dr_xorisaurus.c -Wl,-z,relro,-z,now -o dr_xorisaurus -pie -fstack-protector
	patchelf --set-interpreter ./ld-2.32.so dr_xorisaurus
	patchelf --set-rpath ./ dr_xorisaurus
	strip dr_xorisaurus
	

debug:
	gcc dr_xorisaurus.c -o dr_xorisaurus -g
	patchelf --set-interpreter ./ld-2.32.so dr_xorisaurus
	patchelf --set-rpath ./ dr_xorisaurus

poc:
	gcc poc.c -o poc -no-pie
	