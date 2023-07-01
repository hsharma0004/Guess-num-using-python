'''
n=18
chances = 5
for i in range(1,chances+1):
    inp = int(input('Enter any number to guess: '))
    chances_left = chances - i

    if inp>n:
        print('You have entered a greater number please enter a smaller one')
        print(f"You are left with {chances_left} chances")
        continue
    elif inp<n:
        print('You have enterd a smaller number please enter bigger')
        print(f"You are left with {chances_left} chances")
        continue
    elif inp==n:
        print('Congrats you have one the game in ',i ,'chances')
        break
'''
import random
n1 = int(input('Enter the starting range : '))
n2 = int(input('Enter the ending range: '))
n3 = random.randint(n1,n2)
chances = 7
for i in range(1,8):
    chances_left = chances-i
    guess_int = int(input('Guess the number : '))
    if n3==guess_int:
     print(f"You have finished the game in {i} chances")
     break
    elif n3<guess_int:
         print('You have entererd a larger number\nNow you are left with',chances_left,'chances')
    elif n3>guess_int:
         print('You have entererd a Smaller number\nNow you are left with',chances_left,'chances')
    elif chances_left==0:
         print('Game over!!')