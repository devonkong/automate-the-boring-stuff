birthdays = {'Devon': '4 February', 'Wolf': '6 May', 'Vivien': '24 February'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
        
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}.")
        
    else:
        print(f"I don't have {name}'s birthday. What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
