import json
from bs4 import BeautifulSoup


fix_er = True # Fix entry reference,hyperlinks . convert (Bacteria : See Bacterium.) to (Bacteria : ___Bacterium)
indent = 0 # indent of ouput json ; make it to None for single-line compressed output
remove_as = False # remove example sentences from defn .. like 'as, a valuable item' . These give examples of how the word is used
strict = True # remove words that don't start with alphabet . e.g. suffixes (-ing in i, -s in s)


def gcide_xml2json(xml, alphabet):
	fname = xml
	data = open(fname, 'r').read()
	x = BeautifulSoup(data, 'lxml')
	dic = {}
	ent = ''

	for p in x.find_all('p'):
		if p.find('ent') != None:
			if strict and ent.lower().startswith(alphabet) == False and ent != '':
				del dic[ent]
			if ent != '' and len(dic[ent]) == 0: # word with no meanings
				del dic[ent]
			ent = p.find_all('ent')[-1].get_text() # get the root word, last one
			if ent not in dic:
				dic[ent] = []
		if ent == '':
			continue
		defn = p.find('def')
		if defn != None:
			defnt = defn.get_text()
			if fix_er and defnt.find('See') * defnt.find('Same as') == 0 and defn.find('er') != None:
				dic[ent] += ['___' + defn.find('er').get_text()]
			else:
				if remove_as and defn.find('as') != None:
					defn.find('as').clear()
					defnt = defn.get_text()
				dic[ent] += [defnt.strip(' ;.')]

	return dic


if __name__ == '__main__':
	a2z = 'abcdefghijklmnopqrstuvwxyz'
	a2z = 's'
	mdic = {}
	for _ in a2z:
		fname = 'xml_files/gcide_' + _ + '.xml'
		print('Doing :', _)
		mdic[_] = gcide_xml2json(fname, _)
		open('json_files/gcide_' + _ + '.json', 'w', encoding='utf-8').write(json.dumps(mdic[_], ensure_ascii=False, indent=indent, sort_keys=True))

	fdic = {}
	for _ in mdic:
		fdic.update(mdic[_])
	print('writing dictionary.json')
	open('dictionary.json', 'w', encoding = 'utf-8').write(json.dumps(fdic, ensure_ascii=False, sort_keys=True))