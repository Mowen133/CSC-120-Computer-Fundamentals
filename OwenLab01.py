# input statements
# A = 2
# B = 3
# C = -2

x = int(input(" Please enter integer ..."))
y = int(input(" Please enter another integer ..."))
z = int(input(" Please enter the third integer ..."))

print(" the numbers entered are ", x," and", y, " and ", z)
s = x + y + z #2
m = max(x,y,z)  #4 MAX function similar function for min
mi = min(x,y,z) #5
p = x*y*z #3
avg = s/3 #6
s1 = s**mi #7
s2 = s/mi #8
s3 = s//m #9
avg2 = (m+mi)/2 #10

print(" values are SUM = ", s, " product = ", p,  " maximum = ",  m, "minimum =", mi, "average = ", avg)
print(" the sum raised to the power of the minimum integer = ", s1)
print(" the sum divided by the minimum integer = ", s2)
print(" The sum divided by the maximum integer = ", s3)
print(" average of the largest and smallest integers = ", avg2)
print(" the integers in sorted order: ", m, " ", s-(m+mi), " ", mi)
print(" Student Name: Marcus Owen \n Major: Graphic Design \n Reason for Taking CSC 120: to gain a better understanding of the fundamentals of computer science")
print(" Plan in 5 Years: Hopefully be employed as a graphic designer either as a freelancer or at a firm")
# this is a comment
# the following if...else structure is used to illustrate the syntax
# note the3 indentation
# the code below is to illustrate a if….else 
# for illustration only and not needed for the lab Please comment out 
# if (x > 0) :
#    x = A*x
#    x = B*x
# else:
#    y = C*y
#    y = A*y
#
# print("NEW value of x = ", x, " and ", " y ", y)
