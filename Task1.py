"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
call_list = []
for i in range(len(calls)):
    call_list.append(calls[0][0] + "," + calls[0][1])
print(call_list)

text_list = []
for i in range(len(texts)):
    text_list.append(texts[0][0] + "," + texts[0][1])
print(text_list)

total_call_nums = len(call_list * 2)
total_text_nums = len(text_list * 2)

print(total_call_nums + total_text_nums)
