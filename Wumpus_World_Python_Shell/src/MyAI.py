# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================
from collections import defaultdict
from Agent import Agent

class MyAI ( Agent ):

	def __init__ ( self ):
		# ======================================================================
		# YOUR CODE BEGINS
		# ======================================================================
		self.turn = 0
		self.current = [0,0]
		self.row = int()
		self.column = int()
		self.start = [0,0]
		self.moveList = [[0,0]]
		self.back = False
		self.steps = 0
		self.direction = 1
		self.myMap = defaultdict(list)
		# ======================================================================
		# YOUR CODE ENDS
		# ======================================================================

	def getAction( self, stench, breeze, glitter, bump, scream ):
		# ======================================================================
		# YOUR CODE BEGINS
		# ======================================================================
		#self.setCurrentSquare(stench, breeze, glitter, bump, scream)
		#The Minimal Version
		if self.back == True:
			if (set(self.current) == set([0,0])):
				return Agent.Action.CLIMB;

			return self.getBackToTheStart()
		
		else:
			if glitter:
				self.back = True
				return Agent.Action.GRAB
			
			elif not (stench or breeze or bump):
				self.steps += 1
				if (self.steps >= 3):
					self.back = True
				self.setCurrentSquare()
				self.moveList.append(self.current[:])
				return Agent.Action.FORWARD
	
			if bump or stench or breeze:
				self.back = True
				return self.getBackToTheStart()
		

#		if self.back == False:
#			if breeze or stench:
#				self.back = True
#				return self.getBackToTheStart()
#			elif glitter:
#				self.back = True
#				self.steps += 1
#				return Agent.Action.GRAB
#		else:
#			return self.getBackToTheStart()
		# ======================================================================
		# YOUR CODE ENDS
		# ======================================================================

	# ======================================================================
	# YOUR CODE BEGINS
	# ======================================================================
	def setMap( self, stench, breeze, glitter, bump, scream ):
		if stench:
			self.myMap[self.current].append(1)
		if breeze:
			self.myMap[self.current].append(2)
		if glitter:
			self.myMap[self.current].append(3)
		if bump:
			self.myMap[self.current].append(4)
		if scream:
			self.myMap[self.current].append(5)
	
	def setCurrentSquare(self):
		if self.direction == 1:
			self.current[1] += 1
		elif self.direction == 2:
			self.current[0] += 1
		elif self.direction == 3:
			self.current[1] -= 1
		elif self.direction == 4:
			self.current[0] -= 1
		
	def getBackToTheStart(self):
		if set(self.current) == set([0,0]):
			return Agent.Action.CLIMB;
		if (self.current[0] == self.moveList[-2][0]):
			if (self.current[1] > self.moveList[-2][1]):	
					
				if (self.direction == 3):
					self.steps += 1
					self.setCurrentSquare()
					self.moveList.pop()
					return Agent.Action.FORWARD
				else:
					return self.changeDirection(3)
			else:
				if (self.direction == 1):
					self.steps += 1
					self.setCurrentSquare()
					self.moveList.pop()
					return Agent.Action.FORWARD
				else:
					return self.changeDirection(1)
		else:
			if (self.current[0] > self.moveList[-2][0]):
				if (self.direction == 4):
					self.steps += 1
					self.setCurrentSquare()
					self.moveList.pop()
					return Agent.Action.FORWARD
				else:
					return self.changeDirection(4)
			else:
				if (self.direction == 2):
					self.steps += 1
					self.setCurrentSquare()
					self.moveList.pop()
					return Agent.Action.FORWARD	
				else:
					return self.changeDirection(2)

			
	def changeDirection(self, targetDirection):
		n = self.direction - targetDirection
		if (n == 3) or (n == -1):
			if self.direction == 4:
				self.direction = 1
			else:
				self.direction += 1
			return Agent.Action.TURN_LEFT
		elif (n == -3) or (n == 1):
			if self.direction == 1:
				self.direction = 4	
			else:
				self.direction -= 1
			return Agent.Action.TURN_RIGHT
		else:
			if self.direction == 4:
				self.direction = 1
			else:
				self.direction += 1
			return Agent.Action.TURN_LEFT
			
			


	# ======================================================================
	# YOUR CODE ENDS
	# ======================================================================
