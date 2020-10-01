inaldi={}
for x in range(3):
	name=input('student name: ')
	m=(int(input("Enter Math Marks: ")))
	p=(int(input("Enter Physics Marks : ")))
	c=(int(input("Enter Chemistry Marks: ")))
	marks={'Maths':m,'phy':p,'Chemistry':c}
	finaldi[name]=marks
print(finaldi)
for x,y in finaldi.items():
	total=0
	per=0
	slist=[]
	print("Name of Student :",x)
	for i,j in y.items():
		total+=j
		per=total/3
		print(i,'\t',j)
	if per>60:
		print('Division : First')
	elif per>=45 and per<60:
		print("Division : Second")
	else:
		print('Division: Fail')
