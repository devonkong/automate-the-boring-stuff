## Chapter 5

1. `empty_dict = {}`

2. `dict_2 = {'foo': 42}`

3. Dictionaries are unordered and contain key value pairs, and can be accessed using strings, floats, tuples or integers. Lists are ordered and can be assessed using an index integer.

4. `spam = {'bar': 100}`  
`spam['foo']` will result in a `KeyError`.

5. `'cat' in spam == 'cat' in spam.keys()`  
Both lines of code will look for the string `'cat'` as a `key` within the `spam` dictionary.

6. `'cat' in spam != 'cat' in spam.values()`  
`'cat' in spam` will search for the string `'cat'` as a `key` in the `spam` dictionary, while `'cat'` in `spam.values()` will search for the string `'cat'` as a `value` in the `spam` dictionary.

7. `spam.setdefault('color', 'black')`

8. `import pprint  
pprint.pprint(dict)`