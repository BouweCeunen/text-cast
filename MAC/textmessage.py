from socket import *
from subprocess import call
from messagePrinter import printMessage
import sys
import os
import getpass

class TextMessage:

	def __init__(self):
		self.directory = os.path.abspath(__file__).rsplit('/',1)[0] + '/' 
		self.iconpath = ''
		try:
			if len(sys.argv) == 2:
				# self.UDPBroadcastReceivePort = 4090
				# self.UDPBroadcastReceiver()

				self.UDPBroadcastReceivePort = int(sys.argv[1])
				self.UDPBroadcastReceiver()
			else:
				printMessage('ERROR args','python ' + __file__ + ' UDPBroadcastReceivePort')
				call(['osascript','-e','display notification "Error" with title "ERROR args"'])
		except Exception as e:
				call(['osascript','-e','display notification "Error" with title "' + str(e) + '"'])


	def UDPBroadcastReceiver(self):
		self.sock = socket(AF_INET, SOCK_DGRAM)
		self.sock.bind(('',self.UDPBroadcastReceivePort))

		messg = 'Textcast enabled on port ' + str(self.UDPBroadcastReceivePort)
		call(['osascript','-e','display notification "Enabled" with title "' + messg + '"'])

		while True:
			msg = self.getInputUDP()
			if (msg is None):
				continue
				
			message = msg['msg']
			sender = msg['address']
			senderIP = sender[0]
			senderPort = sender[1]
		
			printMessage(senderIP,message)

			self.sendMessage(message)

	def sendMessage(self,msg):
		splitmsg = msg.split(':',1)
		sender = splitmsg[0]
		message = splitmsg[1]
		
		#print(self.directory)
		call(['osascript','-e','display notification "' + str(message) + '" with title "' + str(sender) +'"'])
	
	def getInputUDP(self):
		data, address = self.sock.recvfrom(4096)
		if len(data) < 1: 
			return None
		data = data.replace("\r\n","").strip()
		return {'msg':data,'address':address}

if __name__ == "__main__":
	TextMessage()





