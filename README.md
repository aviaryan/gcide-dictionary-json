# GCIDE Dictionary

[GCIDE dictionary](https://www.ibiblio.org/webster/) in json format. Note that this is not a complete version of GCIDE dictionary, it only has words and their definitions.


### Using

The formatted dictionary json files, arranged alphabetically are inside the [json_files](json_files/) folder. 

The compressed all-in-one file is [dictionary.json](dictionary.json).

There is also a minimal form of dictionary.json which only has **one definition per word** (the first one). The file is [dictionary_minimal.json](dictionary_minimal.json).

The basic structure of these files looks like

```javascript
"word1": [
"definition 1",
"definition 2"
],
"word2": [
"definition 1"
],
"word3": [
"definition 1",
"definition 2",
"definition 3",
]
// etc
```

### Customizing

If you want to have control over the output json files, there are some variables in the [python script](gcide_parser.py) which can be configured. The comments should be sufficient to explain what each configuration is for.


### Notes

* The 'Same as word' or 'See word' type of definitions in dictionary have been replaced by ___word (3 underscores). This is controlled by the `fix_er` variable.
```json
"grains": [
"___grain",
"Pigeon's dung used in tanning.  See Grainer. n., 1"
]
```

* To cleanup generated dictionary, you can use variables like `only_alpha`, `remove_prefix` and `remove_as` from the [script](gcide_parser.py).


### Bonus

* You can use [dict.py](dict.py) as a command-line dictionary. It doesn't support word correction though.


### Similar Projects

* [adambom/dictionary](https://github.com/adambom/dictionary)
* [javierjulio/dictionary](https://github.com/javierjulio/dictionary)