'''
Hal - Command line daily scheduler
Created by Ben Shukman

Usage:
	hal [-h | --help | --version]
	hal add <taskname> <time>
	hal init

Optional arguments:
	-h, --help   	Show help dialog
	--version    	Show version number

Hal commands:
	(no argument) 	Show today's schedule
	add				Add a task
	init			Run setup

'''

# modules:
# sublime to do grabber
# todoist grabber
# calendar grabber
# koto grabber
# food
# exercise
# walk dog

import db_methods as db
from docopt import docopt
import datetime

versionNumber = '0.0.2'


class Task(object):
	time = ''  # set up time object
	name = ''

def main():
	arguments = docopt(__doc__, version=versionNumber)

	if db.firstStartupCheck():
		if arguments['init']:
			pass
		else:
			print("This looks like your first time using hal.  Run 'hal init' to initialize setup.")
			db.exit()

	if arguments['init']:
		print('\nInitializing hal setup\n')

		# database creation
		db.initializeDB()

		# settings file creation
		# db.initializeSettings()
		# with open('/usr/local/Library/Koto/koto_settings.txt', 'w') as outfile:
		# 	json.dump({'updateTime': '', 'responseTime': '',}, outfile)

		print("\nWelcome to hal!  Use '--help' to learn more")
		db.exit()

	elif arguments['add']:
		db.addTask(arguments['<taskname>'], arguments['<taskname>'])

	else:
		print('Schedule')
		print('========')
		now = datetime.datetime.now().strftime('%H:%M')

		print('Current time: ' + now)
		print(db.readTasks())

		# display times of all tasks

		# ex: 10:30am - walk belka
		# highlight current task orange

		# walk belka
		# drink water
		# kgl
		# answer emails / koto support

		# integration with mac notifications

if __name__ == '__main__':
	main()
