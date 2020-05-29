def spam():
    global eggs
    eggs = 'spam' # This is global.

def bacon():
    eggs = 'bacon' # This is local.

def ham():
    print(eggs) # This prints the global variable.

def sausage():
    eggs = 'sausage'
    print(eggs)

eggs = 42 # This is global.

spam()
print(eggs)
ham()
sausage()

