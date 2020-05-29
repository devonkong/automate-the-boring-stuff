def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print("Error: You can't divide by zero.")

def eggs(divide_by):
    return 42 / divide_by

print(spam(2))
print(spam(3))
print(spam(0))
print(spam(4))

print()

try:
    print(eggs(2))
    print(eggs(1))
    print(eggs(0))
    print(eggs(-1))
    print(eggs(-2))
except:
    print("Please don't try to divide by zero again.")
