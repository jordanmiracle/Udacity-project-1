"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from timeit import Timer


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
call
Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
#telemarketers = set()
#for call in calls:
#    if call[0][:3] == '140':
#        telemarketers.add(call[0])
#print(sorted(telemarketers))
telemarketers = set()
for call in calls:
    telemarketers.add(call[0])

for call in calls:
    if call[1] in telemarketers:
        telemarketers.remove(call[1])

for text in texts:
    if text[0] in telemarketers:
        telemarketers.remove(text[0])
    if text[1] in telemarketers:
        telemarketers.remove(text[1])

telemarketer_sorted = sorted(telemarketers)
print(f"These numbers could be telemarketers: ")
for telemarketer in telemarketer_sorted:
    print(telemarketer)



if '__name__' == '__main__':
    t = Timer("test()", "from __main__ import test")
print(t.timeit())




