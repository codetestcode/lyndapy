#!/usr/bin/python


def main():
	a = 1
	b= 'one'
	c = 3.45
	multi_assign = [1, 2, 3]
	one, two, three = multi_assign
	print(type(a),id(a))
	print(type(b),id(b))
	print(type(c),id(c))
	print(one,two,three)

if __name__ == '__main__':
	main()