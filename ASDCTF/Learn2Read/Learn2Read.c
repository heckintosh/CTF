#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>


int main(){
    int index = 0;
    int fd;
    unsigned int secret;
    unsigned int user_input;
    int arr_ints[] = {1,2,3,4,5};
    
    //Read a random number (don't bother trying to guess it)
    fd = open("/dev/urandom",O_RDONLY);
    read(fd,&secret,sizeof(int));

    //Print banner and read index from user
    printf("Welcome to the random array filler\n");
    printf("Which index would you like to inspect?\n");
    scanf("%d",&index);

    //Print info about index in the 'array' user wants
    printf("The element at index %d is %u\n",index,arr_ints[index]);

    //Ask for passcode from user
    printf("Please enter the secret passcode\n");
    scanf("%u",&user_input);

    //If user correctly 'guessed' the completely random passcode print flag
    if (user_input == secret){
        int fd2;
        char flag [64];
        fd2 = open("flag.txt",O_RDONLY);
        read(fd2,&flag,64);
        printf("%s\n",flag);
    } else { //Otherwise rub their noses in the lack of correct guess
        printf("No flag for you, try again next time!\nThe secret was %u\n",secret);
    }
    return 0;
}