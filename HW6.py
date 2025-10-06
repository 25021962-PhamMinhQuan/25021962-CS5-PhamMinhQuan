a=int(input())
b=int(input())
c=int(input())
if a+b>c or a+c>b or b+c>a:
	perimeter=(a+b+c)/2
	acreage=(perimeter*(perimeter-a)*(perimeter-b)*(perimeter-c))**(1/2)
	print(f"{acreage:.1f}")
else:
	print("khong phai la tam giac")