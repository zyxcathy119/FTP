#ifndef SERVER_H
#define SERVER_H
//服务器的主要操作

//获取命令行参数
int getParameter(int argc, char **argv);

//初始化服务器socket并监听
int initServer(int port);

//接收客户端命令
void recieveCommand(int serfd);

//关闭服务器socket


#endif