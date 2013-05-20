.PHONY: all clean

all: offbyone offbyone-debug

clean: 
	@rm -f offbyone offbyone-debug

offbyone: offbyone.c
	gcc -O -ansi --pedantic-errors -DNDEBUG offbyone.c -o offbyone

offbyone-debug: offbyone.c
	gcc -O -ansi --pedantic-errors offbyone.c -o offbyone-debug
