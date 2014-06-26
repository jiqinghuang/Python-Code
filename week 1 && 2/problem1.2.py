s = 'azcbobobegghakl'
count = 0
for n in range(len(s) - len("bob") + 1):
    if s[n:n+len('bob')] == 'bob':
        count = count + 1 

print('Number of times bob occurs is: ' + str(count)) 

