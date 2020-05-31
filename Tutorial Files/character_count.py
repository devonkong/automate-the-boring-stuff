import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character.lower(), 0)
    count[character.lower()] += 1
    
pprint.pprint(count)