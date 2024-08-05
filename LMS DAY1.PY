#print hrllo world
print ('hello world')

#describe local variable and global variable code
#A variable declared outside of the function or scope of variable in global that this variable is called Global Variable.
#A variable declared inside of the function this variable is called Local Variable.
x = 5
def hello():
   x = 10
   print('local var=',x)

hello()
print('global var=',x)


#Indentation error
# if True:
# print("Indentation error!")


#write a code that describe local and global variable with same name.

#Ans. A variable declared outside of the function or scope of variable in global that this variable is called Global Variable.
#a Global variable is also use outside or inside of the function or class.

#A variable declared inside of the function this variable is called Local Variable.
#A Local variable is not use outside of the function or class.
x = 5
def hello():
    global var
    var='this is global variable'
    x = 10
    print(var)
    print('local var=',x)

hello()
print('global var=',x)
print(var)


#Write a code for string, int and float input.
#string:"raman"
#int:2,5,14
#float:10.2,26.85
a='ram'
print(type(a))

b=10
print(type(b))

c=12.20
print(type(c))

#string:"raman",
a='raman'
print(type(a))

#int:2,5,14
b=2
print(type(b))

#float:10.2,26.85
c=10.2
print(type(c))

