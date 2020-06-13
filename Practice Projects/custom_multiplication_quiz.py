# Chapter 8: Custom Multiplication Quiz
# Recreate the muliplication quiz project without importing PyInputPlus.

import random, time


number_of_questions = 10
time_limit = 8
correct_answers = 0


# Main program loop that asks questions
for question_number in range(number_of_questions):
    # Setup two random numbers between 0 and 9
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    solution = num1 * num2
    
    # Prints question and receives user input
    print(f"\nQ{question_number + 1}: {num1} x {num2} = ")

    # Give user a second to read question before starting timer
    time.sleep(1)
    start_time = time.time()
    
    # Gives user 3 tries to give the correct answer
    number_of_tries = 0
    while number_of_tries < 3:
         # Checks if 8 seconds has passed since timer started
        if time.time() > start_time + time_limit:
            print("Time's up!")
            break
            
        number_of_tries += 1
        user_answer = input()
        
        # Checks if user_answer is an integer
        try:
            user_answer = int(user_answer)
            # Checks if answer was correct
            if user_answer == solution:
                # Checks if 8 seconds has passed since timer started
                if time.time() > start_time + 8:
                    print(f'Your answer is correct, but you took longer than {time_limit} seconds.')
                    
                else:
                    print('That is correct!')
                    correct_answers += 1
                    
                break  # Breaks the loop and goes on to the next question

            else:
                print('That is incorrect.')
                continue
            
        except:  # Restarts if input was not an integer
            print(f'{user_answer} is not an integer.')
            continue
            
    else:
        print(f"You've used up all {number_of_tries} attempts.")
    

# Show results
print(f"\nYou answered {correct_answers} of {number_of_questions} questions correctly.")
    