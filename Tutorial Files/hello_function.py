def hello():
    print("Hello!")
    print("What's up!")
    print("Okay.")

def yo(name):
    print("Yo %s, what's up?" % name)
    print('Swiggity swag.')
    return 'Cool.' # This value is returned by the function, but not shown unless called by the print function.
    print('Fuck, man!') # This line is not executed, because it comes after the return statement.

def hey(name, age, gender):
    print('Hey, %s. You are a %d year old %s.' % (name, age, gender))

hello()

yo('Wolf')

hey('Devon', 25, 'male')

print(yo('Wolf'))
