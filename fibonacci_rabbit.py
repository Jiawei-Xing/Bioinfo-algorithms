Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={}
>>> s['a']=1
>>> s['b']=0
>>> for n in range(2, 33):
	i = s['a']
	j = s['b']
	s['a'] = j*5
	s['b'] = i+j

>>> print(s)
{'a': 25822505482080, 'b': 14415648500221}
>>> sum(s.values())
40238153982301
>>> 