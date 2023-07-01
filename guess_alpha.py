import random
name = input("What's Your Name ? ")
print(f"Goodluck ! {name}")
words = ['computer','rainbow','light','fan','tv','radio','sand','pot','drone','pitch','bread','butter','mug','milk']
print('Hint:\nFirst alphabet may be:\na,c,f,t,s,d,p,b,m,r,n,l')
print('You have only 12 chances to predict the word')
word = random.choice(words)
s= list(word)
chances = 12
for i in range(1,12):
 chances_left=chances-i
 guess_word = input('Guess the first alphabet: ').lower()
 if s[0]!=guess_word:
  print('Incorrect guess try again')
  print(f"You are left with {chances_left} chances")
 elif s[0] in guess_word:
  #if s[0] == guess_word:
   print(s[0])
   print(f"You are left with {chances_left} chances")
   print(f"The third alphabet is {s[2]}")
   break
for x in range(1,12):
    chances=chances_left
    chances_left=chances-x
    guess_word1 = input('Guess the second alphabet: ').lower()
    if s[1] == guess_word1:
     print(f"You guessed the second word right it is {(s)}")
     print(f"You have won the game in {i+x} chances")
     break
    elif s[1]!=guess_word1:
     print(f"You are left with {chances_left} chances")