#include "global.h"
#include "command.h"
#include "fileprocess.h"
void dealtoCMD(struct Client* client) //所有成功的返回都放在本函数里，报错返回后一定要接return
{ 
    char *cmd = strtok(client->rsvCMD, " ");
    char *rest= strtok(NULL, " ");
    printf("deatoCMD:cmd:%s rest:%s\n",cmd,rest);

    if (strcmp(cmd, "PORT") == 0)
    {
        if(rest == NULL)
        {
            serverReply(client->controlfd, "501 Wrong format parameter\r\n");
            return;
        }
        if(getPORT(client, rest))
        {
            client->dataMode = PORT;
            serverReply(client->controlfd, "200 Port Command Successful\n");
        }
        return;
    }

    if (strcmp(cmd, "PASV") == 0)
    {
        client->dataMode = PASV;
        closeSocket(client->pasvServerfd);//重新连接PASV
        client->pasvServerfd = -1;
        char* rpl = portFormat(client);
        serverReply(client->controlfd, rpl);
        return;
    }

    if (strcmp(cmd, "RETR") == 0)
    {
        struct FileInfo file;
        if(rest == NULL)
        {
            serverReply(client->controlfd, "501 Wrong format parameter\r\n");
            return;
        }
        strcpy(file.filepath, serRoot);//处理文件路径
        strcat(file.filepath, rest);
        if(downloadfile(client, &file)) //主功能
        {
            printf("Successly download\n");
            serverReply(client->controlfd, "226 Successly download\n");
        }
        else
        {
            printf("download wrong\n");
        }
        closeSocket(client->datafd);
        return;
    }

    if (strcmp(cmd, "STOR") == 0)
    {
        struct FileInfo file;
        if(rest == NULL)
        {
            serverReply(client->controlfd, "501 Wrong format parameter\r\n");
            return;
        }
        strcpy(file.filepath, serRoot);//处理文件路径
        strcat(file.filepath, rest);
        if(uploadfile(client, &file))//主功能
        {
            printf("Successly upload\n");
            serverReply(client->controlfd, "233 Successly upload\n");
        }
        else{
            printf("upload wrong\n");
        }
        closeSocket(client->datafd);
        return;
    }
    if (strcmp(cmd, "SYST") == 0)
    {
        if(rest != NULL)
        {
            serverReply(client->controlfd, "504 Wrong format parameter\r\n");
            return;
        }
        serverReply(client->controlfd, "215 UNIX Type:L8\r\n");
        return;
    }
    if (strcmp(cmd, "TYPE") == 0)
    {
        if(strcmp(rest, "I") == 0)
        {
            serverReply(client->controlfd, "200 Type set to I\r\n");
            return;
        }
        else{
            serverReply(client->controlfd, "504 Wrong format parameter\r\n");
        }
        return;
    }
    

    
    // if (strcmp(cmd, "USER anonymous") == 0)
    // {
    //     return 1;
    // }
    // if (strcmp(cmd, "USER anonymous") == 0)
    // {
    //     return 1;
    // }
    // if (strcmp(cmd, "USER anonymous") == 0)
    // {
    //     return 1;
    // }
    return;
}

void signIn(struct Client* client)
{

    printf("Sign in begin rsvCMDis: %s\n",client->rsvCMD);
    char *cmd = strtok(client->rsvCMD, " ");
    char *rest= strtok(NULL, " ");
    printf("cmd is:%s rest is %s\n",cmd, rest);
    if (strcmp(cmd, "USER") == 0 && strcmp(rest, "anonymous") == 0)
    {
        client->isSignIn = true;
        serverReply(client->controlfd, "331 Username exist, send your complete e-mail address as password.\r\n");
        return;
    }
    else{
        // serverReply(client->controlfd, "332 User error, please sign in again.\r\n");
    }
    return;
}
void password(struct Client* client)
{
    char *cmd = strtok(client->rsvCMD, " ");
    // char *rest= strtok(NULL, " ");
    if (strcmp(cmd, "PASS") == 0)
    {
        client->isPass = true;
        serverReply(client->controlfd, "230 Password OK\r\n");
        client->datafd = -1;
        return;
    }
    else{
        serverReply(client->controlfd, "Password error\r\n");
    }
    return;
}



bool getPORT(struct Client* client, char* rest)
{
    if(client->datafd != -1)
    {
        closeSocket(client->datafd);
    }
    int h1, h2, h3, h4, p1, p2;
    int count;
    printf("getPort begin\n");
    count = sscanf(rest, "%d,%d,%d,%d,%d,%d", &h1, &h2, &h3, &h4, &p1, &p2);//失败返回-1
    if (count != 6 ||h1<0||h1>256||h2<0||h2>256||h3<0||h3>256||h4<0||h4>256)
    {
        serverReply(client->controlfd,"501 \r\n");
        printf("ssanf error\n");
        return false;
    }
    sprintf(client->clientip, "%d.%d.%d.%d", h1,h2,h3,h4);//获取客户端ip
    client->clientport = p1*256+p2;//获取客户端port
    printf("ip:%s, port:%d\n", client->clientip, client->clientport);
    return true;
}

char* portFormat(struct Client* client)
{
    if(client->datafd != -1)
    {
        closeSocket(client->datafd);
    }
    int h1, h2, h3, h4, p1, p2;
    int count;
    srand((unsigned)time(NULL));
    p1 = rand()%100+100;
    p2 = rand()%256;
    client->dataPort = p1*256+p2;
    count = sscanf(serverIp, "%d.%d.%d.%d", &h1, &h2, &h3, &h4);
    char* reply = calloc(64,sizeof(char));
    if(count != 4)
    {
        printf("ssanf error\n");
        return reply;
    }
    sprintf(reply, "227 =%d,%d,%d,%d,%d,%d\r\n", h1, h2, h3, h4, p1, p2);
    return reply;
}

