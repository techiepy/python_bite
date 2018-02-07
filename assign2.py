
import random

g=0
print('Welcome to take a guess game\n')
number=random.randint(1,10)

while g<10:
	print('Guess a number between 1 & 10. \n ')
	guess = input()
	guess = int(guess)
	g=g+1
	if guess != number:
		print("Wrong. Try Again!")
	if guess == number :
		print("Correct!")
		break
	elif guess==0 :
	    break	
	    

	
	
	  

    
