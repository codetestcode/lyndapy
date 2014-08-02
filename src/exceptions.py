

try:
	with open('testfile.txt') as f:
		for line in f.readlines():
			print(line)

except IOError as e:
	print('something bad happened({})'.format(e))