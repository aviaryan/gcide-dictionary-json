# GCIDE Dictionary

GCIDE dictionary in json format. Note that this is not the complete dictionary, just words with their definitions.


### Using

The uncompressed, formatted dictionary json files arranged alphabetically are inside the [json_files](json_files/) folder. The compressed all-in-one file is [dictionary.json](dictionary.json).

The basic structure of this dictionary is - 

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

There are some variables in the [python script](gcide_parser.py) which can be configured. The comments should be sufficient to explain what each configuration is for.


### Notes

* The 'same as word' or 'see word' type of definitions in dictionary have been replaced by ___word (3 underscores). This is controlled by the `fix_er` variable.
```json
"grains": [
"___grain",
"Pigeon's dung used in tanning.  See Grainer. n., 1"
]
```


### Similar Projects

* [adambom/dictionary](https://github.com/adambom/dictionary)