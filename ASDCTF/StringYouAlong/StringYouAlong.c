#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

int main(){
    int index;
    char flag[64]; //Create flag here
    char edit_me[64];
    int fd;

    fd = open("flag.txt", O_RDONLY);
    read(fd,flag,63);

    //Set all letters in string to 'A'
    for (int i=0;i<63;i++){
        edit_me[i] = 'A';
    }
    //Set our null byte so we stop here
    edit_me[63] = '\x00';

    //Get user to tell us what letter we are changing
    printf("What index would you like to make 'B'?\n");
    scanf("%d",&index);

    //Change that letter
    edit_me[index] = 'B';

    //Print our string
    printf("Now the string looks like this!\n%s\n", edit_me);
}