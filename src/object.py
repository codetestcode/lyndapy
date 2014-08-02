#!/usr/bin/env python

class Egg:
	def __init__( self,kind = "fried"):
		self.kind = kind #object variable

	def what_kind(self):
		return self.kind

def main():
	
	myegg = Egg('scambled')
	print(myegg.what_kind())


if __name__ == '__main__':
	main()