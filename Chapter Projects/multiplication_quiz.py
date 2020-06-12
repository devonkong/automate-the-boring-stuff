import pyinputplus as pyip
import random, time


number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    # Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    prompt = f"Question {question_number + 1}: {num1} x {num2}"
    
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes = [f"^{num1 * num2}$"], blockRegexes = [('.*', 'That is incorrect.')], timeout = 8, limit = 3)
        
    except pyip.TimeoutException:
        print("Time's up!")
    
    except pyip.RetryLimitException:
        print("You've tried too many times.")
        
    else:
        # This block runs if no exceptions were raised in the try block.
        print(f"{num1 * num2} is correct!")
        correct_answers += 1
        
    time.sleep(1) # A brief pause to let user see the result.
    print(f"Your score is {correct_answers} / {number_of_questions}.")
    time.sleep(1) # A brief pause to let user see the result.