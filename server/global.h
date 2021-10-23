#ifndef GLOBAL_H
#define GLOBAL_H

#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <errno.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <memory.h>
#include <stdio.h>
#include <stdbool.h>
#include <fcntl.h>
#include <sys/select.h>
#include <pthread.h>



#define SENTENCELENGTH 8190
#define MAXPATH  256

enum MsgTag
{
    Msg_Ready = 1,
    Msg_Send = 2,
    Msg_Successed = 3
};
struct FileInfo{   //封装消息头
    char filepath[MAXPATH];
    int filesize;
    bool isopen;
    char drive[MAXPATH];  
    char dir[MAXPATH];  
    char filename[MAXPATH];  
    char ext[MAXPATH];  
    char *filebuf;
};
struct Client
{
    int controlfd; //控制连接
    int datafd;    //数据传输连接
    int clientport;
    char clientip[32];
    bool isSignIn;
    bool isPass;
    char rsvCMD[SENTENCELENGTH];
    char rplMSG[SENTENCELENGTH];
    int  rpllen;
  
};
    void serverReply(int controlfd,char* rplmsg);
    void closeSocket(int fd);
    // void replycode(int controlfd, int code);
    int serPort;
    char serRoot[32];
    int serfd;
    char serverIp[32];
    int  serverPort;


#endif