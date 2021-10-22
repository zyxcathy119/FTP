all:server

server:server.c command.c global.c fileprocess.c server.h command.h global.h fileprocess.h
	gcc -o server -Wall server.c command.c global.c fileprocess.c

clean:
	rm server
