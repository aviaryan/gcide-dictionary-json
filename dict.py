import json
from sys import argv, exit

from colorama import init as colorinit
from colorama import Fore, Style

colorinit()
data = []
words = []
# data = open('dictionary.json', 'r', encoding = 'utf-8').read()
# data = json.loads(data)
# words = data.keys()

def loadAlphabetDict(alphabet = 'a'):
	global data
	global words
	data = open('json_files/gcide_' + alphabet + '.json', 'r', encoding = 'utf-8').read()
	data = json.loads(data)
	words = data.keys()

# idea
# one by one - left to right - double chars - skip

def run():
	if len(argv) == 1:
		print('Enter word > ', end='')
		word = input()
		print()
	else:
		word = argv[1]
	word = word.lower()
	loadAlphabetDict(word[:1])
	if word in words:
		defn = data[word]
	else:
		print(Fore.RED + 'Not found', Style.RESET_ALL)
		exit()

	c = 1
	for i in defn:
		print(Fore.RED + Style.BRIGHT + str(c), Style.RESET_ALL + i)
		print()
		c+=1

	input() # to not close terminal
	# print(Style.RESET_ALL + '')


if __name__ == '__main__':
	run()