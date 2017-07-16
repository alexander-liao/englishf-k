import sys

wordchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-'

def BFinterpret(commands):
	tape = [0]
	pointer = 0
	index = 0
	while index < len(commands):
		if commands[index] == 0:
			tape[pointer] += 1
		elif commands[index] == 1:
			tape[pointer] -= 1
		elif commands[index] == 2:
			tape[pointer] = sys.stdin.read(1)
		elif commands[index] == 3:
			print(chr(tape[pointer]), end = '')
		elif commands[index] == 4:
			pointer -= 1
			while pointer < 0:
				tape.insert(0, 0)
				pointer += 1
		elif commands[index] == 5:
			pointer += 1
			while pointer > len(tape):
				tape.append(0)
		elif commands[index] == 6 and not tape[pointer]:
			brackets = 1
			while brackets:
				index += 1
				if commands[index] == 6:
					brackets += 1
				elif commands[index] == 7:
					brackets -= 1
			index += 1
		elif commands[index] == 7 and tape[pointer]:
			brackets = 1
			while brackets:
				index -= 1
				if commands[index] == 6:
					brackets -= 1
				elif commands[index] == 7:
					brackets += 1
		index += 1
	print()
	print(tape)
	print()

def interpret(code):
	command = 0
	commands = []
	rotation = 0
	index = 0
	while index < len(code):
		if code[index] in '.!?,;:':
			commands.extend([(command + rotation) % 8] * (2 ** '.!?,;:'.index(code[index])))
			index += 1
		elif code[index] in wordchars:
			word = ''
			while code[index] in wordchars:
				word += code[index]
				index += 1
			rotation += (len(word) % 2) * 2 - 1
		else:
			index += 1
	BFinterpret(commands)

if sys.argv[1:]:
	with open(sys.argv[1], 'r') as f:
		interpret(f.read)
else:
	while True:
		interpret(input())
