#include "global.h"

    // int serfd = 0, controlfd = 0; //套接字的描述符
    // bool isSignIn = false;
    // bool isPass = false;
	// char rsvCMD[SENTENCELENGTH];
    // char rplmsg[SENTENCELENGTH];
    // int  rpllen = 0;
void serverReply(int controlfd,char* rplmsg)
{
	int p = 0;
    int rpllen = strlen(rplmsg);
	printf("serverReply msg is %s\n",rplmsg);
	while (p < rpllen) {
		int n = write(controlfd, rplmsg + p, rpllen + 1 - p);
		if (n < 0) {
			printf("Error write(): %s(%d)\n", strerror(errno), errno);
			return;
		} else {
			p += n;
		}			
	}
	return;
}
void closeSocket(int fd)
{
	printf("connct closed\n");
    close(fd);
	return;
}