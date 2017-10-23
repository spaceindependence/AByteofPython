number = 23
guess = int(input('Enter the number:'))

if guess == number:
    print('Congratulations, you guessed it,')
    print('...although you did not win any prize!')
elif guess < number:
    print('No, the unknown number a little more than that.')
else:
    print('No, the unknown number a little less than that.')
print('Completed')
