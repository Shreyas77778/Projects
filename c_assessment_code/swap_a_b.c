#include<stdio.h>
void main()
{
int a,b;
printf("enter value of a and b");
scanf("%d %d",&a,&b);
int c;
c=a+b;
a=c-a;
b=c-a;
printf("%d %d",a,b);
}

