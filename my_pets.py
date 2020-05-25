my_pets = ['Mino', 'Carlo', 'Shiloh', 'Alfie', 'Jeanie']

print('Enter a pet name.')
name = input()
if name not in my_pets:
    print("I don't have a pet named %s." % name)
else:
    print('%s is my favourite pet.' % name)
