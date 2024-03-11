#include<stdio.h>

int main() {
    int num,small;
    int i,j,sizelist,list[10],pos,temp;
    printf("\nEnter the size of list :\n ");
    scanf("%d",&sizelist);
    for(i=0;i<sizelist;i++) {
        printf("\nEnter the number");
        scanf ("%d",&list[i]);
    }
    for(i=0;i<sizelist;i++) {
        small=list[i];
        pos=i;
        for(j=i+1;j<sizelist;j++) {
            if(small>list[j]) {
                small=list[j];
                pos=j;
            }
        }
        temp=list[i];
        list[i]=list[pos];
        list[pos]=temp;
    }
    int xxx = 2;
    printf("\nList of the numbers in ascending order : ");
    for(i=0;i<sizelist;i++)
        printf("\n%d",list[i]);
    return 0;
}
