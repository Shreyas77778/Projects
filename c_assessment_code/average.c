//program to print
#include<stdio.h>
void main()
{
int a, b, c, d, e;
printf("enter values");
scanf("%d %d %d %d %d",&a,&b,&c,&d,&e);
int sum= a+b+c+d+e;
printf("%d\n",sum);
float avg = sum/5.0;
printf("%f",avg);

}