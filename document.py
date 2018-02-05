Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 1==1 and 2==2
True
>>> 1==2 and 3==4
False
>>> 1/=4 or 1==1
SyntaxError: can't assign to literal
>>> 1/1 or 2/0
1.0
>>> 1==0 or 0==1
False
>>> 1==0 not 0==1
SyntaxError: invalid syntax
>>> 1==0 not 1==1
SyntaxError: invalid syntax
>>> not 1==0
True
>>> 
=================== RESTART: /home/ec2017b219/document.py ===================
True
>>> 2=3*4-6
SyntaxError: can't assign to literal
>>> 3+2==2+3
True
>>> 0/1
0.0
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> true and true
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> 1==1 or 0==0
True
>>> True
