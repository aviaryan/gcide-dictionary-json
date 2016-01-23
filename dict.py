import json
from sys import argv, exit

from colorama import init as colorinit
from colorama import Fore, Back, Style

colorinit()
data = open('dictionary.json', 'r', encoding = 'utf-8').read()
data = json.loads(data)
words = data.keys()

# idea
# one by one - left to right - double chars - skip


def run():
	if len(argv) == 1:
		print('> ', end='')
		word = input()
	else:
		word = argv[1]
	word = word.lower()
	if word in words:
		defn = data[word]
	else:
		exit()

	c = 1
	for i in defn:
		print(Fore.RED + Style.BRIGHT + str(c), Style.RESET_ALL + i)
		c+=1

	# print(Style.RESET_ALL + '')


if __name__ == '__main__':
	run()