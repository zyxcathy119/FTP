#ifndef COMMAND_H
#define COMMAND_H
//处理命令

void signIn(struct Client* client);

void password(struct Client* client);
//对客户端发的command进行分类处理
void dealtoCMD(struct Client* client);
//PORT模式获取设置客户端端口
bool getPORT(struct Client* client,char* rest);
//PASV模式发送端口给客户端
char* portFormat(struct Client* client);


#endif