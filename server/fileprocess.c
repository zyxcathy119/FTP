#include "global.h"
#include "fileprocess.h"

bool downloadfile(struct Client* client, struct FileInfo* file)
{
    printf("downloadfile begin\n");
    if(connectDataSocket(client) ==false)
    {
        printf("发起客户端连接失败");
        return false;
    }
    
    FILE* fp = fopen(file->filepath,"rb");
    if(fp == NULL)
    {
        printf("找不到[%s]文件...\n",file->filepath);
        serverReply(client->controlfd, "找不到文件...\n");
    } 
        //获取文件大小
        fseek(fp, 0, SEEK_END);
        file->filesize = ftell(fp);
        fseek(fp, 0, SEEK_SET);
        //分割文件路径
        splitpath( file->filepath, file->drive, file->dir, file->filename); //linux下无_splitpath
        serverReply(client->controlfd, "The file is found\n");
        printf("read: filesize: %d filename: %s\n",file->filesize,file->filename);

        //读取文件
        file->filebuf = calloc(file->filesize+1,sizeof(char));
        if(file->filebuf == NULL)
        {
            printf("内存不足\n");
            return false;
        }
        int count;
        while((count = fread(file->filebuf,sizeof(char), 8192, fp)) > 0) {
            send(client->datafd, file->filebuf, count, 1);
            printf("发送文件了\n");
        }

        //     fread(file->filebuf, sizeof(char),8190, fp);
        // //发送文件
 
        //     if(send(client->controlfd, file->filebuf, 8190, 0) == -1)
        //     {
        //         printf("文件发送失败\n");
        //     }
  
        
        
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

bool connectDataSocket(struct Client* client)
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
	if (inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr) <= 0) {			
		printf("Error inet_pton(): %s(%d)\n", strerror(errno), errno);
		return false;
	}

	//连接上目标主机，阻塞函数
	if (connect(client->datafd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
		printf("Error connect(): %s(%d)\n", strerror(errno), errno);
		return false;
	}
	// char sentence[8192];
	// int len;
	// int p;
	// printf("和客户端建立数据连接\n");

	// strcpy(sentence,"datatrip success!!!");
    // len = strlen(sentence);
	// sentence[len] = '\n';
	// sentence[len + 1] = '\0';
	// //把键盘输入写入socket
	// p = 0;
	// while (p < len) {
    //     printf("写入\n");
	// 	int n = write(client->datafd, sentence + p, len + 1 - p);		//write函数不保证所有数据写完，可能会中途退出
	// 	if (n < 0) {
	// 		printf("Error write(): %s(%d)\n", strerror(errno), errno);
	// 		return 1;
 	// 	} else {
	// 		p += n;
	// 	}			
	// }
    // printf("发送datafd\n");
    // p = 0;
	// while (1) {
	// 	int n = read(client->datafd, sentence + p, 8191 - p);
	// 	if (n < 0) {
	// 		printf("Error read(): %s(%d)\n", strerror(errno), errno);	//read不一定依次读完
	// 		return 1;
	// 	} else if (n == 0) {
	// 		break;
	// 	} else {
	// 		p += n;
	// 		if (sentence[p - 1] == '\n') {
	// 			break;
	// 		}
	// 	}
	// }

	// //read不会将字符串添加上'\0'，需要手动添加
	// sentence[p - 1] = '\0';

	// printf("FROM SERVER: %s", sentence);

    return true;
}