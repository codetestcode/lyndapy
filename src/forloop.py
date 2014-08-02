#!/usr/bin/env python


with open('../data/lines.txt','r') as fileout:
	for line in fileout.readlines():
		print(line)