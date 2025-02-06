import random
print('Hello PLAYER! Welcome to my \'Guess The Number\' Game')

while True:
    print('So do you want to hear the RULES?(YES|NO) : ')
    x = input().upper()
    if x == 'YES' or x == 'Y' or x == 'YEA' or x == 'YEAH':
        print('Ok Here : \n 1)I will choose a random number between 0-100 and you have to guess it \n 2)You have just 5 attempts \n 3)Every time you guess wrong i will give you a hint \n 4)If you guess wrong 3 times you lost and i win \n 5)ENJOY')
        break
    elif x == 'NO' or x == 'NAH' or x == 'NO NEED' or x == 'N':
        print('Oh! so you are an old player.Awsome')
        break
    else:
        print('Answer my question')
print('Then lets start the game')


num = random.randint(0 , 100)
wrong = 1

while wrong <6 :
    HP = 6 - wrong
    guess = int(input(f'Guess the number|HP {HP}|:'))
    if guess > num:
        print('Your guess is high')
        wrong += 1
        if HP == 3:
            if num % 2:
                print('The number is even number')
            else:
                print('The number is odd number')
        elif HP == 2:
            print(f'You are far from the answer with {guess - num}')
    elif guess < num:
        print('Your guess is low')
        wrong += 1
        if HP == 3:
            if num % 2:
                print('The number is even number')
            else:
                print('The number is odd number')
        elif HP == 2:
            print(f'You are far from the answer with {num - guess}')
    else :
        print('Thats corect you WIN')
        break
