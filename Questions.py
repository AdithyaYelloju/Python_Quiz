import time
score = 0

name = input("What's your name? ")
print("Welcome, "+name+" to the quiz!")

def scorePlus():
	global score
	score +=1
	print("Your score: ",score)

def scoreMinus():
	global score
	score -=1
	print("Your score: ",score)

def q1():
	global score
	print("\n1. Who is the developed python?")
	time.sleep(0.5)
	print("a.Guido van Rossum")
	print("b.James Gosling")
	print("c.Larry Page")
	print("d.Sundar Pichai\n")

	ans = input("What is the right answer: ")
	if(ans == 'a'):
		print("Well done, that's correct")
		scorePlus()
	else:
		print("Sorry, that was the wrong answer")
		scoreMinus()

	q2()


def q2():
	global score
	print("\n1. Who is the developed python?")
	time.sleep(0.5)
	print("a.Guido van Rossum")
	print("b.James Gosling")
	print("c.Larry Page")
	print("d.Sundar Pichai\n")

	ans = input("What is the right answer: ")

	if(ans == 'a'):
		print("Well done, that's correct")
		scorePlus()
	else:
		print("Sorry, that was the wrong answer")
		scoreMinus()

	q3()
	


def q3():
	global score
	print("\n1. Who is the developed python?")
	time.sleep(0.5)
	print("a.Guido van Rossum")
	print("b.James Gosling")
	print("c.Larry Page")
	print("d.Sundar Pichai\n")

	ans = input("What is the right answer:")

	if(ans == 'a'):
		print("Well done, that's correct")
		scorePlus()
	else:
		print("Sorry, that was the wrong answer")	
		scoreMinus()

q1()
