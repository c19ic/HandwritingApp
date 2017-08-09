import wikipedia
import codecs
import re

wikipedia.set_rate_limiting(True)
myflash={}
pageerror=[]

def inread():
	with codecs.open('insource.txt', 'r', encoding="utf-8") as f:
		for line in f:
			line=re.sub('[\W]','',line)
			try:
				term=str(wikipedia.page(line,auto_suggest=False)).encode('utf-8')
				term=term[16:-2]
				definition=str((wikipedia.summary(line)).encode('utf-8')).split('\n')
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

def out():
	filler=''
	for idx,term in enumerate(myflash):
		filler+=('-'*30+'<br>'+term+'<br>'*2+myflash[term]+'<br>')
	if len(pageerror)>0:
		if len(myflash)>0:
			filler+=('<br>')
		filler+=('~'*30+'<br>'*2)
		for thing in pageerror:
			filler+=(thing+'<br>')
	return (filler)