#ifndef COMMAND_H
#define COMMAND_H
//处理命令

void signIn(struct Client* client);

void password(struct Client* client);
//对客户端发的command进行分类处理
void dealtoCMD(struct Client* client);

void getPORT(struct Client* client,char* rest);

void getLocalIp(struct Client* client);
#endif