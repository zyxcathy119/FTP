#include "global.h"
#include "command.h"
#include "fileprocess.h"

void signIn(struct Client* client)
{

    printf("Sign in begin rsvCMDis: %s\n",client->rsvCMD);
    char *cmd = strtok(client->rsvCMD, " ");
    char *rest= strtok(NULL, " ");
    printf("cmd is:%s rest is %s\n",cmd, rest);
    if (strcmp(cmd, "USER") == 0 && strcmp(rest, "anonymous") == 0)
    {
        client->isSignIn = true;
        serverReply(client->controlfd, "230 Username exist, send your complete e-mail address as password.\r\n");
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

void dealtoCMD(struct Client* client)
{ 
    char *cmd = strtok(client->rsvCMD, " ");
    char *rest= strtok(NULL, " ");

    printf("deatoCMD:cmd:%s rest:%s\n",cmd,rest);

    if (strcmp(cmd, "RETR") == 0)
    {
        struct FileInfo file;
        if(rest == NULL)
        {
            serverReply(client->controlfd, "501 \r\n");
            return;
        }
        strcpy(file.filepath, serRoot);
        strcat(file.filepath, rest);
        if(downloadfile(client, &file))
            printf("Successly download\n");
        serverReply(client->controlfd, "233 Successly download\n");
        return;
    }
    if (strcmp(cmd, "PORT") == 0)
    {
        if(rest == NULL)
        {
            serverReply(client->controlfd, "501 \r\n");
            return;
        }
        getPORT(client, rest);
        serverReply(client->controlfd, "233 port method ok\n");
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

void getPORT(struct Client* client, char* rest)
{
    int h1, h2, h3, h4, p1, p2;
    int count;
    printf("getPort begin\n");
    count = sscanf(rest, "%d,%d,%d,%d,%d,%d", &h1, &h2, &h3, &h4, &p1, &p2);
    if (count != 6 ||h1<0||h1>256||h2<0||h2>256||h3<0||h3>256||h4<0||h4>256)
    {
        serverReply(client->controlfd,"501 \r\n");
        printf("ssanf error\n");
        return;
    }
    if(client->datafd != -1)
    {
        closeSocket(client->datafd);
    }
    printf("sprintf");
    sprintf(client->clientip, "%d.%d.%d.%d", h1,h2,h3,h4);
    client->clientport = p1*256+p2;
    printf("ip:%s, port:%d\n", client->clientip, client->clientport);
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
    return;
}