#! python3
# mclip.py - A multi-clipboard program.

text = {'bye': """Thank you for your patience. Have a nice week!""",
        
       'dispatch': """Your order has been shipped. Thank you for supporting my shop!""",
        
       'shipping':"""I'm sorry to hear that your order has not arrived. Deliveries from Australia to the United States can sometimes take up to 4 weeks.
Unfortunately, there's not much I can do once I've handed it over to the postal service.
I'm sorry I can't do more to speed up the delivery, but I hope it gets to you soon."""}

import sys, pyperclip



if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit
    

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}.")

