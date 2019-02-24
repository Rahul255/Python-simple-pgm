num=int(raw_input("Enter the NUmber: "))
fact=1
if(num<0):
	print("factorial does not exists negative number")
elif(num==0):
	print("0")
else:
	for i in range(1,num+1):
		fact=fact*i
	print(fact)
