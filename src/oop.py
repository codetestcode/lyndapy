#!/usr/bin/env

class AnimalActions:
	
	def quack(self):
		 return self.strings['quack']

	def feathers(self):
		return self.strings['feathers']

	def bark(self):
		return self.strings['bark']

	def fur(self):
		return self.strings['fur']

	def doAction(self,action):
		if action in self.strings:
			return self.strings[action]

class Duck(AnimalActions):
	"""Duck Class"""
	def __init__(self):
		pass

	strings = dict(
		quack = "quack",
		feathers = "The duck has grey and white feathers.",
		bark = "The duck cannot bark."
		fur = "The Duck has no fur"
		)
		