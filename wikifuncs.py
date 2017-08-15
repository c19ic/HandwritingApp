import wikipedia
import codecs
import re

wikipedia.set_rate_limiting(True)
myflash={}
pageerror=[]

def inread(filename):
	with codecs.open(filename, 'r', encoding="utf-8") as f:
		for line in f:
			line=re.sub('[^\s\w]','',line)
			try:
				term=str(wikipedia.page(line,auto_suggest=False)).encode('utf-8')
				term=term[16:-2]
				definition=str((wikipedia.summary(term)).encode('utf-8')).split('\n')
				definition=definition[0]
				if definition=='':
					pageerror.append(line)
				else:
					myflash[term]=definition
			except wikipedia.exceptions.PageError:
				pageerror.append(line)
			except wikipedia.exceptions.DisambiguationError as e:
				term='DisambiguationError: %s' % str(line)
				definition=''
				for thing in e.options:
					definition+=(str(thing)+(' | '))
				definition=definition.strip(' | ')
				myflash[term]=definition
	return (myflash)

def out():
	filler=''
	for idx,term in enumerate(myflash):
		filler+=('-'*30+'\n'+term+'\n'+myflash[term]+'\n')
	if len(pageerror)>0:
		if len(myflash)>0:
			filler+=('\n')
		filler+=('~'*30+'\n'*2)
		for thing in pageerror:
			filler+=(thing+'\n')
	myflash.clear()
	return (filler)
