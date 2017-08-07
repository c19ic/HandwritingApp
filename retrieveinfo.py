import wikipedia
from PyDictionary import PyDictionary
import codecs
import re
from datetime import datetime

#---------------------------------------------

myflash={}
pageerror=[]
wikipedia.set_rate_limiting(True)
linecount=0

#---------------------------------------------
start = datetime.now()

with codecs.open('insource.txt', 'r', encoding="utf-8") as f:
	for line in f:
		linecount+=1
		line=re.sub('^[^a-zA-z]*|[^a-zA-Z]*$','',line)
		try:
			term=str(wikipedia.page(line,auto_suggest=False))
			term=term[16:-2]
			definition=str(wikipedia.WikipediaPage(line).content).split('\n')
			definition=definition[0]
			if definition=='':
				pageerror.append(line)
			else:
				myflash[term]=definition
		except wikipedia.exceptions.PageError:
			pageerror.append(line)
		except wikipedia.exceptions.DisambiguationError as e:
			dis=[]
			for item in e.options:
				dis.append(item)
			term='DisambiguationError: %s' % str(line)
			definition=''
			for thing in dis:
				definition+=(str(thing)+(' | '))
			definition=definition.strip(' | ')
			myflash[term]=definition
with codecs.open('outsource.txt', 'w', encoding="utf-8") as g:
	for term in myflash:
		g.write('-'*30+'\n'+term+'\n'*2+myflash[term]+'\n')
	if len(pageerror)>0:
		if len(myflash)>0:
			g.write('\n')
		g.write('~'*30+'\n'*2)
		for thing in pageerror:
			g.write(thing+'\n')

end = datetime.now()

deltat = end - start

avgt = deltat / linecount
