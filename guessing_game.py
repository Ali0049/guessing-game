from random import randint
guess = [0]
computer_choice = randint(1,100)
print("guessing game")
print("you can guess number in between 1 to 100")
print("if guess is within 10 number of number to be guessed ")
print('computers tell warm else cold')
print('closer to number computer wil tell warmer than prevoius if farer it tell colder')
print('on write guess you will won')
while True:
    user_input = int(input("enter number : "))
    if user_input<1 or user_input>100:
        print("out of bound")
        continue
    elif user_input == computer_choice:
        print(f'you won, takes attempts {len(guess)} and the number is {computer_choice}')
        break
    guess.append(user_input)
    if guess[-2]:   
        if abs(user_input-computer_choice)<abs(guess[-2]-computer_choice):
            print('warmer')
        else:
            print('colder')

    else:
        if abs(user_input-computer_choice)<=10:
            print('warm')
            
        else: 
            print('cold')
            

