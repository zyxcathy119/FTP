#include "global.h"
#include "server.h"
#include "command.h"
#include "fileprocess.h"


int main(int argc,char *argv[])
{
	// int serfd;
	serPort = 21;
	strcpy(serRoot, "/home/cathy/tmp/");
	if(getParameter(argc,argv) == 0)
	{
		printf("%d, %s\n",serPort,serRoot);
		initServer(serPort);
		recieveCommand(serfd);
		close(serfd);
	}


    return 0;
}

int getParameter(int argc, char **argv)
{

	if(argc == 1)
		return 0;
	if(argc >= 3 && strcmp("-port", argv[1]) == 0)
	{
		serPort = atoi(argv[2]);
		if(serPort < 0 && serPort > 65535)
		{
			return -1;
		}
		if(argc == 5 && strcmp("-root", argv[3]) == 0)
		{
			strcpy(serRoot, argv[4]);
		}
		return 0;
	}
	
	if(argc >= 3 && strcmp("-root", argv[1]) == 0)
	{
		strcpy(serRoot, argv[2]);
		if(argc == 5 && strcmp("-port", argv[3]) == 0)
		{
			serPort = atoi(argv[4]);
			if(serPort < 0 && serPort > 65535)
			{
				return 0;
			}
		}
		return 0;
	}
	return -1;
}

int initServer(int port)
{
	int on=1;
	if ((serfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1) {
		printf("Error socket(): %s(%d)\n", strerror(errno), errno);
		return -1;
	}
	setsockopt(serfd, SOL_SOCKET, SO_REUSEADDR, &on, sizeof(int));
	struct sockaddr_in addr;
	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;  //和创建socket指定的一样
	addr.sin_port = htons(port); //htons把本地字节序转换成网络字节序 
	addr.sin_addr.s_addr = htonl(INADDR_ANY);//监听所有IP地址


	if (bind(serfd, (struct sockaddr*)&addr, sizeof(addr)) == -1) {
		printf("Error bind(): %s(%d)\n", strerror(errno), errno);
		return -1;
	}

	//创建队列长度为10的监听序列
	if (listen(serfd, 10) == -1) {
		printf("Error listen(): %s(%d)\n", strerror(errno), errno);
		return -1;
	}

	return 0;
}

void recieveCommand(int serfd)
{   
	while (true) {	
		struct Client client;
		initClient(&client);
		//提取出所监听套接字的等待连接队列中第一个连接请求，创建一个新的套接字(之后可以直接用这个进行收发），并返回指向该套接字的文件描述符
        if((client.controlfd = accept(serfd, NULL, NULL)) == -1) //成功时，返回非负整数，该整数是接收到套接字的描述符；出错时，返回－1，相应地设定全局变量errno
	    {
			printf("Error accept(): %s(%d)\n", strerror(errno), errno);
			continue;
		}
		//发欢迎回复
	    serverReply(client.controlfd, "220 Anonymous FTP server ready.\n");
		getLocalIp(&client);
		printf("accepted\n");
		int p = 0;//p是一共收到的总字节数
		while (1) {
			/*read(int fd,void * buf ,size_t count)
			 read()会把参数fd 所指的文件传送count个字节到buf指针所指的内存中。
			若参数count为0，则read()不会有作用并返回0。返回值为实际读取到的字节数，
			如果返回0，表示已到达文件尾或是无可读取的数据，此外文件读写位置会随读取到的字节移动。*/
			int n = read(client.controlfd, client.rsvCMD + p, SENTENCELENGTH -1 - p); //可能8192装不下，要多收几次
            printf("received message: %s\n",client.rsvCMD);
			//客户端出现问题，强制退出！！！！！！！！！！
			if(strcmp(client.rsvCMD,"exit\r\n") == 0)
			{
				closeSocket(client.controlfd);
				closeSocket(serfd);
			}
			if (n < 0) {
				printf("Error read(): %s(%d)\n", strerror(errno), errno);
				close(client.controlfd);
				continue;
			} else if (n == 0) {
				break;
			} else {
				p=p+n;
				if(client.rsvCMD[p-1]=='\n' && client.rsvCMD[p-2]=='\r')
				{
					client.rsvCMD[p-1]='\0';
					client.rsvCMD[p-2]='\0';
					p=0;
					//!!!!!!!!!!!!!!!!!!!!!!
					client.isSignIn = true;
					client.isPass = true;
					if(client.isSignIn == false)
				    {
				    	signIn(&client);
				    }
				    else if(client.isPass == false)
				    {
				    	password(&client);
				    }
					else
					{
						printf("into else\n");
						dealtoCMD(&client);
					}
				}
				else
				{
					continue;
				}
				
			}
		}

		
		// dealtoCMD(rsvCMD,p);
	}
    return;
}

void getLocalIp(struct Client* client)
{
    struct sockaddr_in serv;  
    char serv_ip[20]; 
    socklen_t serv_len = sizeof(serv);   
    getsockname(client->controlfd, (struct sockaddr *)&serv, &serv_len);  
    inet_ntop(AF_INET, &serv.sin_addr, serv_ip, sizeof(serv_ip));  
    printf("host %s:%d\n", serv_ip, ntohs(serv.sin_port));  
    strcpy(serverIp, serv_ip);
    return;
}

void initClient(struct Client* client)
{
	client->dataMode = NoMode;
	client->isSignIn = false;
	client->isPass = false;
	client->controlfd = -1;
	client->datafd = -1;
	return;
}