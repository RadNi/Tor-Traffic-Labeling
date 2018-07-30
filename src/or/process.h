#ifndef PROCESS_H
#define PROCESS_H
#include <unistd.h>
#define die(e) do { fprintf(stderr, "%s\n", e); exit(EXIT_FAILURE); } while (0);

extern int arr[100];
extern void* MY_chunks[10000];
extern char MY_chunks_body[10000][10000];
extern int MY_chunks_body_size[10000];
extern int MY_chunks_size = 0;
extern void* MY_current_chunks[100];
extern int MY_current_chunks_size = 0;

int find_ap_from_port(char* port, char* app_name);

int find_ap_from_port(char* port, char* app_name) {
	int link[2];
	pid_t pid;
	char foo[4096];
	
	if (pipe(link)==-1)
		die("pipe");
	
	if ((pid = fork()) == -1)
		die("fork");
	if(pid == 0) {
		dup2 (link[1], STDOUT_FILENO);
		close(link[0]);
		close(link[1]);
		execl("/bin/netstat", "netstat", "-lnpa", (char *)0);
		die("execl");
	} else {
	    
		close(link[1]);
		if( read(link[0], foo, sizeof(foo)) < 0 ){
			return -1;
		}
		FILE* fd = fopen("/tmp/find_app.out", "a+");
		fprintf(fd, "%s", foo);
		fclose(fd);
		close(link[0]);
		close(link[1]);
		if( pipe(link) == -1)
			return -1;
		pid = fork();
		if(pid == 0)
		{
			dup2 (link[1], STDOUT_FILENO);
			close(link[0]);
			close(link[0]);
			execl("/bin/grep", "grep", (const char*)port, "/tmp/find_app.out", (char*)0);
			die("execl");
			//if( read(link[0], foo, sizeof(app)) >= 0 ){
			//	fprintf(stdout, "app_name output: %s", app);
			//	return 1;
			//}

		}
		else{
			int nbytes = read( link[0], foo, sizeof(foo));
			if( nbytes ){
				int flag = 0;
				int app_ind = 0;
				unsigned int i;
				for ( i=0; i < strlen(foo);i++)
				{
					if (flag == 1)
					{
						if(foo[i] == '\n' || foo[i] == ' ')
						{
							app_name[app_ind] = '\0';
							if(strcmp(app_name, "tor") == 0)
							{
								app_ind = 0;
							}
							else{
								break;
							}
							flag = 0;
						}
						else{
							app_name[app_ind] = foo[i];
							app_ind ++;
						}
					}
					if(foo[i] == '/')
						flag = 1;
				}
				return 1;
			}
		}
	    }  
	return 1;
}
#endif
