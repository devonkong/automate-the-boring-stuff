cat_names = []

while True:
    print('Enter the name of cat %d or enter nothing to stop.' % (len(cat_names) + 1))
    name = input()
    if name == '':
        break
    cat_names += [name]

print("My cat's names are:")

for name in cat_names:
    print(name)


