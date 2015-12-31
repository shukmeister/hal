import sqlite3
import os
import sys

db_directory = '/usr/local/Library/Hal'
db_path = '/usr/local/Library/Hal/haldb'


def firstStartupCheck():
	# if the database file exists
	if os.path.exists(db_path):
		# it is not the first time running koto
		return False
	else:
		return True

def initializeDB():
	print ('Initializing database in ' + db_path)
	if not os.path.exists(db_directory):
		os.makedirs(db_directory)
		print ('Database directory created')
	conn = sqlite3.connect(db_path)
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS tasks(name text, time text, priority integer, UNIQUE(name))")
	print('Database created')
	conn.close()

def addTask(name, time):
	print ('Inserting ' + name + ' @ ' + time + ' into database ' + db_path + '...')
	conn = sqlite3.connect(db_path)
	c = conn.cursor()
	# c.execute("CREATE TABLE IF NOT EXISTS people(name, time, UNIQUE(name, time))")
	c.executemany("INSERT OR IGNORE INTO tasks(name, time) VALUES (?, ?)", [(name, time)])
	if (c.rowcount != 0):
		print ('Successfully added ' + name + ' @ ' + time)
	else:
		print ('Failed to add ' + name + ' @ ' + time)
		#insert already exists if statement error message
	conn.commit()
	conn.close()

def readTasks():
	conn = sqlite3.connect(db_path)
	c = conn.cursor()
	c.execute("SELECT name, time FROM tasks")
	return c.fetchall()
	conn.close()


def exit():
	sys.exit()

