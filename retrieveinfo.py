from flask import Flask
from datetime import datetime
from wikifuncs import *

#---------------------------------------------

application = Flask(__name__)

#---------------------------------------------
start=datetime.now()

header_text = '''
    <html>\n<head> <title>Flash Cards</title> </head>\n<body>'''

inread()

@application.route('/')
def main():
	return out()

if __name__ == "__main__":
    application.debug = True
    application.run()

end=datetime.now()

deltat=end-start

avgt=deltat/(len(myflash))