#global variable which is defining outside of the functions 
a = 5
b = 6

def addition():
    print(a + b)

def sub():
    print(a - b)

addition()
sub()


#local variable

def addition():
    a = 4
    b =5
    print(a + b)

#below one throws the error if i remove the first and second variable on the top.
#def sub:
#    print(a - b)

addition()
#sub()  this is sample for the last function

def addition():
    c=7
    print(a+b+c)
#here a and b are the global variable and c is the local variable
addition()

full_name = "Harish Beedani"  # snake casing
fullName =  "Harish Beedani" #camel casing


