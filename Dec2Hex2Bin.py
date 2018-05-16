#!/usr/bin/env python3


def convert():
    try:
        x = input("Input the number you want  to convert: ")
        print('{:*>48}'.format('*'))
	print('{0:^12} {1:^16} {2:^12}'.format('Decimal', 'Hexadecimal', 'Binary'))
	print('{0:^12,d} {0:^#16x} {0:^12b} '.format(int(x)))
	print("++++++++++++++++++++++++++++++++++++++++++++++++")
    except ValueError:
	print("Oops!  Make sure you enter an integer.  Try again...")
	print("++++++++++++++++++++++++++++++++++++++++++++++++")

if __name__ == '__main__':
    
     convert()	
