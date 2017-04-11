from socket import *
from subprocess import call
from messagePrinter import printMessage
import sys
import os

class TextMessage:

	def __init__(self):
		try:
			self.directory = os.path.abspath(__file__).rsplit('\\',1)[0] + '/'
			self.file_name = self.directory + 'notifscript.ps1'
			if len(sys.argv) == 2:
				# self.UDPBroadcastReceivePort = 4090

				self.UDPBroadcastReceivePort = int(sys.argv[1])
				self.UDPBroadcastReceiver()
			else:
				printMessage('ERROR args','python ' + __file__ + ' UDPBroadcastReceivePort')
				call(['powershell','-ExecutionPolicy','Bypass','-File',self.file_name,'-name','Error','Error args'])
		except Exception as e:
			call(['powershell','-ExecutionPolicy','Bypass','-File',self.file_name,'-name','Error',str(e)])


	def UDPBroadcastReceiver(self):
		self.sock = socket(AF_INET, SOCK_DGRAM)
		self.sock.bind(('',self.UDPBroadcastReceivePort))

		call(['powershell','-ExecutionPolicy','Bypass','-File',self.file_name,'-name','Enabled','TextMessage notify enabled on port '+str(self.UDPBroadcastReceivePort)])

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
		call(['powershell','-ExecutionPolicy','Bypass','-File',self.file_name,'-name',sender,message])
	
	def getInputUDP(self):
		data, address = self.sock.recvfrom(4096)
		if len(data) < 1: 
			return None
		data = data.replace("\r\n","")
		return {'msg':data,'address':address}

if __name__ == "__main__":
	TextMessage()





