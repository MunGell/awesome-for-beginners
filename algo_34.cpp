#include<iostream>
using namespace std;
float fn(float x,float y)
{
float ans;
ans=2*x;
return(ans);
}
int main(void)
{
float x0,y0,x,y,h,f1,f2;
int i,n;
cout<<"give me initial condition say x0 ";cin>>x0;
cout<<"give me initial condition say y0 ";cin>>y0;
cout<<"give the spacing between two points step size(h) = ";cin>>h;
cout<<"give the calculation point x ";cin>>x;
n=(x-x0)/h;
for(i=0;i<n;++i)
{
f1=x0+(h/2);
f2=y0+(h/2)*fn(x0,y0);
y=y0+h*fn(f1,f2);
y0=y;
x0=x0+h;
}
cout<<"the value of the function at x= "<<x<<" is "<<y<<endl;
return 0;
}
