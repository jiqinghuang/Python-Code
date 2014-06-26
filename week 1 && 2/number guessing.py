#print("Hi"),
#print("here")
#x = float(raw_input('Enter a decimal number between 0 and 1: '))
print('Please think of a number between 0 and 100!')
low = 0
high = 100
ans = (high + low)/2
print("is your secret number " + str(ans) + "?")
x = str(raw_input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.') )

while x != "c":
    if x == "l":
        low = ans
    elif x == "h":
        high = ans
    else:
        print("Sorry, I did not understand your input.")
    ans = (high + low)/2
    print("is your secret number " + str(ans) + "?")
    x = str(raw_input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.') )

print("Game over. Your secret number was: " + str(ans))   


