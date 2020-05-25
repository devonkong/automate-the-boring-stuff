import time, sys
indent = 0 # How many spaces to indent.
indent_increasing = True # Whether the indentation is increasing or not.

try:
    while True: # This is the main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second.

        if indent_increasing:
            indent += 1 # This increases the number of spaces.
            if indent == 20:
                indent_increasing = False # This changes direction.

        else:
            indent -= 1 # This decreases the number of spaces.
            if indent == 0: # This changes direction.
                indent_increasing = True

except KeyboardInterrupt:
    print('Goodbye!')
    sys.exit()
