import json
from bs4 import BeautifulSoup


indent = 0 # indent of output alphabet-wise json ; make it to None for single-line compressed output
indent_main = None # indent of dictionary.json
remove_as = False # remove example sentences from defn .. like 'as, a valuable item' . These give examples of how the word is used
remove_prefix = False # remove words that don't start with alphabet . e.g. suffixes (-ing in i, -s in s)
all_lowercase = True # make all words lowercase (not their definitions)
only_alpha = False # words consisting of only alphabets allowed. e.g. removes words having spaces or dashes etc.

fix_er = True # Fix entry reference,hyperlinks . convert (Bacteria : See Bacterium.) to (Bacteria : ___Bacterium)
remove_orphans = True # remove words without definition
ascii_output = False # if false, outputs unicode (recommended)

gen_minimal = True


def gcide_xml2json(xml, alphabet):
	fname = xml
	data = open(fname, 'r').read()
	soup = BeautifulSoup(data, 'lxml')
	dic = {}
	ent = ''
	ents = []

	for p in soup.find_all('p'):
		if p.find('ent') != None:
			delete_entry = max( remove_prefix and ent.lower().startswith(alphabet) == False and ent != '' ,
							remove_orphans and ent != '' and len(dic[ent]) == 0 ,
							only_alpha and ent != '' and ent.isalpha() == False )
			if delete_entry:
				for _ent in ents:
					if _ent in dic: del dic[_ent] # band age and Band Age .. same when lowercase

			ents = [i.get_text().lower() if all_lowercase else i.get_text() for i in p.find_all('ent')]
			ents = [i for i in ents[:-1] if i[0:1].isalpha()] + [ents[-1]] # remove suffixes from same words cuz they are not my job
			ent = ents[-1] # get the root word, last one
			for _ent in ents[:-1]: # init all same words
				dic[_ent] = ['___' + ent]
			if ent not in dic:
				dic[ent] = []
		if ent == '':
			continue
		defn = p.find('def')
		if defn != None:
			defnt = defn.get_text()
			if fix_er and defnt.find('See') * defnt.find('Same as') == 0 and defn.find('er') != None:
				er = defn.find('er').get_text()
				if all_lowercase:
					er = er.lower()
				dic[ent] += ['___' + er]
			else:
				if remove_as and defn.find('as') != None:
					defn.find('as').clear()
					defnt = defn.get_text()
				dic[ent] += [defnt.strip(' ;.')]

	return dic


if __name__ == '__main__':
	a2z = 'abcdefghijklmnopqrstuvwxyz'
	# a2z = 's'
	mdic = {}
	for _ in a2z:
		fname = 'xml_files/gcide_' + _ + '.xml'
		print('Doing :', _)
		mdic[_] = gcide_xml2json(fname, _)
		open('json_files/gcide_' + _ + '.json', 'w', encoding='utf-8').write(json.dumps(mdic[_], ensure_ascii=ascii_output, indent=indent, sort_keys=True))

	fdic = {}
	for _ in mdic:
		fdic.update(mdic[_])
	print('writing dictionary.json')
	open('dictionary.json', 'w', encoding='utf-8').write(json.dumps(fdic, indent = indent_main, ensure_ascii=ascii_output, sort_keys=True))

	if gen_minimal:
		for i in fdic:
			if len(fdic[i]) > 0:
				fdic[i] = fdic[i][0]
			else:
				fdic[i] = ''
		open('dictionary_minimal.json', 'w', encoding='utf-8').write(json.dumps(fdic, indent = indent_main, ensure_ascii=ascii_output, sort_keys=True))