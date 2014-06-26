s = 'zzcbobobegghakl'
# a clear logic way
# s = 'zyxw...'
# so inital must be z
# inital = 'z'
# for b in range(len(s)):
#    for e in range(b+1,len(s)):
#        if s[e-1] <= s[e]:
#            if len(s[b:e+1]) > len(inital):
#                inital = s[b:e+1]
#        else:
#            break
# print('Longest substring in alphabetical order is: '+str(inital))


# a more powerful way
cut = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= cut[-1]:
        cut += s[i]
        if len(cut) > len(longest):
            longest = cut
    else:
        cut = s[i]
print('Longest substring in alphabetical order is: '+ str(longest))
    


