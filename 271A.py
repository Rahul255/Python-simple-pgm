n=int(raw_input())
while(True):
    n=n+1
    a=n/1000
    b=n/100%10
    c=n/10%10
    d=n%10
    if(a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
        break;
        
print n
