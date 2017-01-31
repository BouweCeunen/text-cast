from time import strftime
import sys

def printMessage(sender,msg):
	time = strftime("%Y-%m-%d %H:%M:%S")
	message = "[" + str(time) + "] " + sender + ": " +  msg
	print(message)
	sys.stdout.flush()
	return message
