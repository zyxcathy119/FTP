#ifndef FILEPROCESS_H
#define FILEPROCESS_H
//处理命令

bool downloadfile(struct Client* client, struct FileInfo* file);

bool uploadfile(struct Client* client, struct FileInfo* file);

void splitpath(char *path, char *drive, char *dir, char *filename);

bool buildPortConnetion(struct Client* client);

bool buildPasvConnection(struct  Client* client);
#endif