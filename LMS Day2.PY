#Write a program for arithmatic operators
# Addition+,Subtraction-,Multiplication*,Division/,Modulus%,Exponentiation**
a=5
b=2
print(a,b)
print(a+b) #Addition+
print(a-b) #Subtraction-
print(a*b) #Multiplication*
print(b/a) #Division/
print(a%b) #Modulus%
print(a**b) #Exponentiation**


#Q.Write a program for assignment operators
x = 10
print("Initial value:", x)
x += 5  # x = x + 5# Addition Assignment
print("After x+5=", x)
x -= 5 # x=x-5 #Subtraction Assignment
print(x)
x *= 5 #Multiplication Assignment
print(x)
x /= 5 #Division Assignment
print(x)
#x %= 3 # Modulus Assignment
#print(x)
x **= 5 # Exponentiation Assignment
print(x)
x //= 5 # Floor Division Assignment
print(x)


#Write a program for Bitwise operators
x=10
y=8
print(bin(x))
print(bin(y))
print(bin(x&y),x&y) # print Bitwise AND
print(bin(x|y),x|y) #print Bitwise OR
print(bin(x^y),x^y) #print Bitwise XOR

#Write a program to calculate greatest of three numbers
# Define three numbers
a = 10
b = 20
c = 15
print(max(a, b, c)) # Print the greatest number

# Write a program to calculate greatest of three numbers
# Define three numbers
a = 10
b = 20
c = 15

# greatest of the three numbers
if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

# Print the result
print("The greatest number is:", greatest)


#Calculate the area of a circle
#input---> radius
# PI=3.143.14*r*r
r=float(input("Enter radius: ")) # 3
area=3.14*r*r # 3.14*3*3 = 28.25
print('Area of Circle: ',area)


#Calculate the area of a triangle
#input---> a,b,c
# s=(a+b+c)/2
# area=(s*(s-a)(s-b)(s-c))**0.5
a=int(input('Enter 1st side: '))# 5
b=int(input('Enter 2nd side: '))# 6
c=int(input('Enter 3rd side: '))# 7
s=(a+b+c)/2 # s=9
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('Area of triangle: ', area)


#Calculate the area of a rectangle
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
area=1*b
print("Area of rectangle: ", area)


#Calculate the area of a square.
#area= side*side
side=int(input('Enter side: '))# 5
area=side*side # 25
print('Area of Square: ',area)