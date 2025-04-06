from Lexer import *
import sys

dir = ["good", "bad"][1]
name = "prog1"

if __name__ == '__main__':
	lexer = Lexer(f'test_cases/{dir}/{name}.txt')
	
	token = lexer.scan()
	while token.tag != Tag.EOF:
		print(str(token))
		token = lexer.scan()
	print("END")