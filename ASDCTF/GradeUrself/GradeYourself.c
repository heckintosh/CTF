#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

struct Student {
    long uid;
    char name[10];
    char grade;
};

void add_student(struct Student *s){
    char grade = 'F'; //While we can't give F's, everyone starts out getting one
    s->uid = 1;
    while (grade < 'B' || grade > 'E'){ //Loop until grade is valid
        //Get grade from user
        printf("What grade is %d getting?\n", s->uid);
        scanf("%c", &grade);
        if (grade == 'A'){ //The print statement says it all
            printf("No student deserves an A!!\nPick a new grade\n");
        }
    }
    //Set the students grade
    s->grade = grade;

    //Get the students name
    printf("What is the name of student %d?\n", s->uid);
    scanf("%s",s->name);
}

void print_student(struct Student *s){
    printf("_____ Info got student %d _____\n",s->uid);
    printf("Name: %s\n", s->name);
    printf("Grade: %c\n", s->grade);
}

int main(){
    struct Student s;
    printf("Welcome to the Human\nAided\nRational\nSpeedy\nHelper\n(HARSH)\nstudent grading system!\n");
    add_student(&s);
    print_student(&s);
    if (s.grade == 'A'){ //No student should ever get this flag
        int fd;
        char flag [64];
        fd = open("flag.txt",O_RDONLY);
        read(fd,&flag,64);
        printf("%s\n",flag);
    } else { //Encourage the user to reconsider the given grade
        printf("%s got an %c... Are you sure you shouldn't make it a little lower?\n", s.name,s.grade);
    }
}