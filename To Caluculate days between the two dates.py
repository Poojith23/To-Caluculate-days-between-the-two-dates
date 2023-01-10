year1=int(input("Enter a year 1: "))
month1=int(input("Enter a Month 1: "))
date1=int(input("Enter a Day1: "))
if month1==1 or month1==3 or month1==5 or month1==7 or month1==8 or month1==10:
	maximumdays=31
elif month1==4 or month1==6 or month1==9 or month1==11:
	maximumdays=30
elif year1%4==0 and year1%100!=0 or year1%400==0:
	maximumdays=29
else:
	maximumdays=28

if month1<1 or month1>12:
	print("invalid")
elif date1<1 or date1>maximumdays:
	print("invalid")

year2=int(input("Enter a year 2: "))
month2=int(input("Enter a Month 2: "))
date2=int(input("Enter a Day2: "))
if month2==1 or month2==3 or month2==5 or month2==7 or month2==8 or month2==10:
	maximumdays=31
elif month2==4 or month2==6 or month2==9 or month2==11:
	maximumdays=30
elif year2%4==0 and year2%100!=0 or year2%400==0:
	maximumdays=29
else:
	maximumdays=28

if month2<1 or month2>12:
	print("invalid")
elif date2<1 or date2>maximumdays:
	print("invalid")
c=((year1-1)*365 + (year1-1)//4 - (year1-1)//100 + (year1-1)//400
         + [ 0,31,59,90,120,151,181,212,243,273,304,334][month1 - 1]
         + date1
         + int(((year1%4==0 and year1%100!=0) or year1%400==0) and month1> 2))
d=((year2-1)*365 + (year2-1)//4 - (year2-1)//100 + (year2-1)//400
         + [ 0,31,59,90,120,151,181,212,243,273,304,334][month2 - 1]
         + date2
         + int(((year2%4==0 and year2%100!=0) or year2%400==0) and month2> 2))
f=d-c
print(f)
