s = '(()())(())()'
open_count = 0
close_count = 0
start = 0
result = ''

for i,c in enumerate(s):
    if c == '(':
        open_count += 1
    else:
        close_count += 1

    if open_count == close_count:
        result += s[start:i+1]
        start = i+1
print('hello')
print(result)
        
        