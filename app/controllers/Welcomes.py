from system.core.controller import *
import random
import datetime

class Welcomes(Controller):
    def __init__(self, action):
        super(Welcomes, self).__init__(action)

    def index(self):
    	if not 'gold' in session:
    		session['gold'] = 0
    	if not 'log' in session:
    		session['log'] = ''
    	data = {}
    	data['gold'] = session['gold']
    	data['log'] = session['log']
        print session.items()
    	return self.load_view('index.html', data=data)

    def process(self):
        print 'amin1'
    	loc = request.form['location']
        print 'amin'

    	if loc == 'Farm':
    		rand = random.randrange(10, 21)
    		message = "<div class='won'>Entered the farm and earned " + str(rand) + " gold!</div>"
    	elif loc == 'Cave':
    		rand = random.randrange(5, 11)
    		message = "<div class='won'>Entered the cave and earned " + str(rand) + " gold!</div>"
    	elif loc == 'House':
    		rand = random.randrange(2, 6)
    		message = "<div class='won'>Entered the house and earned " + str(rand) + " gold!</div>"
    	elif loc == 'Casino':
    		rand = random.randrange(-50, 51)
    		if rand < 0:
    			win_or_lose = 'lost'
    		else:
    			win_or_lose = 'won'
    		message = "<div class='" + win_or_lose + "'>Entered the casino and " + win_or_lose + " " + str(rand) + " gold!</div>"


    	log = session['log']
    	session['log'] = message + log
    	session['gold'] += rand
    	print session['log']
    	return redirect('/')

    def reset(self):
    	session['gold'] = 0
    	session['log'] = ''
    	return redirect('/')
