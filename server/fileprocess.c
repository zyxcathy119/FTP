#include "global.h"
#include "fileprocess.h"

bool downloadfile(struct Client* client, struct FileInfo* file)//所有RETR的报错返回
{
    printf("downloadfile begin\n");
	//选择连接方式
	if(client->dataMode == PORT)
	{
    	if(buildPortConnetion(client) ==false)
    	{
        	printf("PORT发起客户端连接失败\n");
			serverReply(client->controlfd, "425  Failed:TCP connection was not established\r\n");
        	return false;
    	}
	}
	else if (client->dataMode == PASV )
	{
		if(client->pasvServerfd == -1 && buildPasvConnection(client) == false)
		{
			printf("PASV发起客户端连接失败\n");
			serverReply(client->controlfd, "425  Failed:TCP connection was not established\r\n");
        	return false;
		}
		if((client->datafd = accept(client->pasvServerfd, NULL, NULL)) == -1) //成功时，返回非负整数，该整数是接收到套接字的描述符；出错时，返回－1，相应地设定全局变量errno
	    {
			printf("Error accept(): %s(%d)\n", strerror(errno), errno);
			serverReply(client->controlfd, "425  Failed:TCP connection was not established\r\n");
			return false;
		}
	}
	else
	{
		serverReply(client->controlfd, "530  Failed:Please choose datamode:'PASV/PORT'\r\n");
		return false;
	}

    FILE* fp = fopen(file->filepath,"rb");
    if(fp == NULL)
    {
        printf("找不到[%s]文件...\n",file->filepath);
        serverReply(client->controlfd, "451 Failed:server had trouble reading the file from disk\r\n");
		return false;
    } 
        //获取文件大小
    fseek(fp, 0, SEEK_END);
    file->filesize = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    //分割文件路径
    splitpath( file->filepath, file->drive, file->dir, file->filename); //linux下无_splitpath
    printf("read: filesize: %d filename: %s\n",file->filesize,file->filename);
    //读取文件
    file->filebuf = calloc(file->filesize+1,sizeof(char));
    if(file->filebuf == NULL)
    {
        printf("内存不足\n");
		serverReply(client->controlfd, "451 Failed:server had trouble reading the file from disk\r\n");
        return false;
    }
    int count;
    while((count = fread(file->filebuf,sizeof(char), 8192, fp)) > 0) {
        send(client->datafd, file->filebuf, count, 1);
        printf("发送文件了\n");
    }
    fclose(fp);

    return true;
}

bool uploadfile(struct Client* client, struct FileInfo* file)//所有STOR的报错返回
{
    printf("uploadfile begin\n");
	if(client->dataMode == PORT)
	{
    	if(buildPortConnetion(client) ==false)
    	{
        	printf("发起客户端连接失败");
			serverReply(client->controlfd, "425  Failed:TCP connection was not established\r\n");
        	return false;
    	}
	}
	else if (client->dataMode == PASV)
	{
		if(client->pasvServerfd == -1 && buildPasvConnection(client) == false)
		{
			printf("发起客户端连接失败");
			serverReply(client->controlfd, "425  Failed:TCP connection was not established\r\n");
        	return false;
		}
		if((client->datafd = accept(client->pasvServerfd, NULL, NULL)) == -1) //成功时，返回非负整数，该整数是接收到套接字的描述符；出错时，返回－1，相应地设定全局变量errno
	    {
			printf("Error accept(): %s(%d)\n", strerror(errno), errno);
			serverReply(client->controlfd, "425  Failed:TCP connection was not established\r\n");
			return false;
		}
	}
	else
	{
		serverReply(client->controlfd, "530  Failed:Please choose datamode:'PASV/PORT'\r\n");
		return false;
	}
    
    FILE* fp = fopen(file->filepath,"ab+");
    if(fp == NULL)
    {
        printf("无法建立[%s]文件...\n",file->filepath);
        serverReply(client->controlfd, "451 Failed:server had trouble reading the file from disk\r\n");
		return false;
    } 
    file->filebuf = calloc(SENTENCELENGTH,sizeof(char));
    if(file->filebuf == NULL)
    {
        printf("内存不足\n");
		serverReply(client->controlfd, "451 Failed:server had trouble reading the file from disk\r\n");
        return false;
    }

    int count;
    while((count = read(client->datafd,file->filebuf,SENTENCELENGTH)) > 0) {
        if(fwrite(file->filebuf,sizeof(char), count, fp) <= 0)
			break;
        printf("写入文件了\n");
		if(count <SENTENCELENGTH)
			break;
    }
	printf("文件成功关闭\n");
    fclose(fp);
    return true;
}

void splitpath(char *path, char *drive, char *dir, char *filename)
{
	drive[0] = '\0', dir[0] = '\0', filename[0] = '\0';//先全部初始化为空
	if (NULL == path)
    {
        printf("Filepath is empty\n");
        return;
    }
    char *fname_start = rindex(path, '/');
    fname_start++;
	if (fname_start == NULL)
	{
	    strcpy(filename, path);
	}
	else
	{
        strcpy(filename, fname_start);
	}
    return;
}

bool buildPortConnetion(struct Client* client)
{
	struct sockaddr_in addr;

	//创建socket
	if ((client->datafd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1) {
		printf("Error socket(): %s(%d)\n", strerror(errno), errno);
		return 1;
	}

	//设置目标主机的ip和port
	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = htons(client->clientport);
	if (inet_pton(AF_INET, client->clientip, &addr.sin_addr) <= 0) {			
		printf("Error inet_pton(): %s(%d)\n", strerror(errno), errno);
		return false;
	}

	//连接上目标主机，阻塞函数
	if (connect(client->datafd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
		printf("Error connect(): %s(%d)\n", strerror(errno), errno);
		return false;
	}

    return true;
}

bool buildPasvConnection(struct  Client* client)
{
	int on=1;
	if ((client->pasvServerfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1) {
		printf("Error socket(): %s(%d)\n", strerror(errno), errno);
		return -1;
	}
	setsockopt(serfd, SOL_SOCKET, SO_REUSEADDR, &on, sizeof(int));
	struct sockaddr_in addr;
	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;  //和创建socket指定的一样
	addr.sin_port = htons(client->dataPort); //htons把本地字节序转换成网络字节序 
	addr.sin_addr.s_addr = htonl(INADDR_ANY);//监听所有IP地址

	printf("建立socket了\n");
	if (bind(client->pasvServerfd, (struct sockaddr*)&addr, sizeof(addr)) == -1) {
		printf("Error bind(): %s(%d)\n", strerror(errno), errno);
		return false;
	}

	//创建队列长度为10的监听序列
	if (listen(client->pasvServerfd, 10) == -1) {
		printf("Error listen(): %s(%d)\n", strerror(errno), errno);
		return false;
	}
	printf("listened\n");
	return true;
};
