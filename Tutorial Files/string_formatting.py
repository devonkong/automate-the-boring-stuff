name = 'Devon'
age = 25
number = 3.7756321
facts = ('likes animals', 'is an introvert', 'rides a bicycle')

print(name + ' is ' + str(age) + ' years old.')

print('%s is %d years old.' % (name, age))

print("%s is %s's name and %s is %d years old." %(name, name, name, age))

print("Today's daily news report follows %s, a %d year old who %s and his special number today is %f or %.2f." % (name, age, facts, number, number))

surname = 'Kong'
balance = 1287.95

print("Hello %s %s. Your current balance is $%.2f." % (name, surname, balance))

data = (name, surname, balance)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)

print(format_string % data + ' Nice!')
