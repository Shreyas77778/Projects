#include<stdio.h>
void main()
{
int a,b;
printf("enter value of a and b");
scanf("%d %d",&a,&b);
a=a^b^a;
b=b^a^b;
printf("%d %d",a,b);
}