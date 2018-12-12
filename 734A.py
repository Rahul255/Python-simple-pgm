var=0
var1=0
n=int(raw_input(''))
m=str(raw_input(''))
for i in m:
    if(i == "A"):
        var=var+1
    if(i == "D"):
        var1=var1+1
if(var<var1):
    print 'Danik'
if(var>var1):
    print 'Anton'
if(var==var1):
    print 'Friendship'
