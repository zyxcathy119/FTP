#ifndef GLOBAL_H
#define GLOBAL_H

#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/sendfile.h>
#include <sys/stat.h>
#include <unistd.h>
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
#include <time.h>


#define SENTENCELENGTH 8190
#define MAXPATH  256

enum MsgTag
{
    Msg_Ready = 1,
    Msg_Send = 2,
    Msg_Successed = 3,
    PASV = 4,
    PORT = 5,
    NoMode = 6,
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
    int dataMode;
    int pasvServerfd; //PASV模式下server创建的服务器data socket
    int  dataPort;  //PASV模式下服务器随机生成的数据传输端口
    int clientport;  //PORT模式下获取的客户端port
    char clientip[32];//PORT模式下获取的客户端ip
    bool isSignIn;  //是否输入用户名
    bool isPass;   //是否输入密码
    char rsvCMD[SENTENCELENGTH];
    char rplMSG[SENTENCELENGTH];
    int  rpllen;

};
    void serverReply(int controlfd,char* rplmsg);
    void closeSocket(int fd);
    int serPort; //最开始服务器建立的控制端口
    char serverIp[32];//查询到的服务器ip
    char serRoot[32];//服务器上的文件夹根路径
    int serfd;    //最开始建立的数据传输socket



#endif