#imports:
#wikipedia is a python library that gives access to Wikipedia pages
#use the link to download: https://pypi.python.org/pypi/wikipedia/
import wikipedia
import sys

#---------------------------------------------

#variable setup:
#termlist and deflist will contain the terms and definitions inputed
termlist=[]
deflist=[]
#myflash is the dictionary that stores all the flashcards
myflash = {}

#---------------------------------------------

#function setup:
#asks the user for which the terms to search and imports info from Wikipeida
def fillflash(title,sentences):
	addnew=True
	newcount=0
	searchcount=0
	while (addnew==True):
		if newcount!=0:
			title=input('Choose a Topic: ')
		searchcount+=1
		term=str(wikipedia.page(title))
		term=term[16:-2]
		termlist.append(term)
		definition=wikipedia.summary(title,sentences)
		deflist.append(definition)
		myflash[term]=definition
		if newcount==0:
			maybeadd=input("Click Enter to add a term. Type 'done' to finish. ").lower()
			newcount+=1
		else:
			maybeadd=input().lower()
		if maybeadd=='done':
			addnew=False

#runs the flashcard quiz
def runflash():
	keyword_list = list(myflash.keys())
	for keyword in keyword_list:
	    sf = '''\
{}'''
	    print('-'*30)
	    print(sf.format(keyword))
	    letter = input('')
	    print (myflash[keyword])
	    letter = input('')
	print('-'*30+'\n'+'-'*30+'\n'+'Complete')
	restart()

#allows runflash() to repeat until the user decides to stop
def restart():
	end=input("Hit Enter to restart or type 'exit' to stop. ").lower()
	if end=='exit':
		sys.exit()
	elif end=='':
		runflash()
	else:
		restart()

#---------------------------------------------

fillflash(input('Choose a Topic: '), 1)
runflash()