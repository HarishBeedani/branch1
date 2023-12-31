import sys
def add(num1, num2):
    n = num1 + num2
    return n
num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    s = num1 + num2
    print(s)

# we can use the command in cli " python test.py 4 add 5"
