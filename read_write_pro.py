Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> r=open("1.txt","w")
>>> r.write("hello class")
11
>>> r=open("1.txt","r")
>>> r.read()
'hello class'
>>> r=open("1.txt","a")
>>> r.write("im in cmru")
10
>>> r.read()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    r.read()
io.UnsupportedOperation: not readable
>>> r=open("1.txt","r")
>>> r.read()
'hello classim in cmru'
>>> wb
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    wb
NameError: name 'wb' is not defined
>>> dir(_builtins__)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dir(_builtins__)
NameError: name '_builtins__' is not defined
>>> dir(_'builtins'_)
SyntaxError: invalid syntax
>>> dir('_builtins_')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help-find
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    help-find
NameError: name 'find' is not defined
>>> help(find)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    help(find)
NameError: name 'find' is not defined
>>> help(help)
Help on _Helper in module _sitebuiltins object:

class _Helper(builtins.object)
 |  Define the builtin 'help'.
 |  
 |  This is a wrapper around pydoc.help that provides a helpful message
 |  when 'help' is typed at the Python interactive prompt.
 |  
 |  Calling help() at the Python prompt starts an interactive help session.
 |  Calling help(thing) prints help for the python object 'thing'.
 |  
 |  Methods defined here:
 |  
 |  __call__(self, *args, **kwds)
 |      Call self as a function.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> help('replace')
No Python documentation found for 'replace'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> dir(_builtins_)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dir(_builtins_)
NameError: name '_builtins_' is not defined
>>> 
