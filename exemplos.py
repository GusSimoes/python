Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
frase = 'o rato roeu a roupa do rei de Roma'
frase.split()
['o', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'Roma']
frase.split()[0]
'o'
frase.split()[1]
'rato'
frase.split()[2]
'roeu'
frase.split()[3]
'a'
frase.split()[4]
'roupa'
frase.split()[5]
'do'
frase.split(' ')
['o', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'Roma']
frase.split('r')
['o ', 'ato ', 'oeu a ', 'oupa do ', 'ei de Roma']
expressao = '10+5+8+3'
expressao.split('+')
['10', '5', '8', '3']

chr(65)
'A'
chr(66)
'B'
chr(67)
'C'
chr(68)
'D'
chr(48)
'0'
chr(49)
'1'
chr(50)
'2'
chr(51)
'3'
chr(10)
'\n'
chr(13)
'\r'
chr(1)
'\x01'

4%2
0
3%2
1
2%2
0
1%2
1
100%6
4
99%6
3
98%6
2
97%6
1
96%6
0
95%6
5
94%6
4
t
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t
NameError: name 't' is not defined
"macaco".title
<built-in method title of str object at 0x0000018FCA73AC70>


"macaco".title()
'Macaco'
1+2
3
1-3
-2
4/3
1.3333333333333333
5*5
25
4//3
1
9/2
4.5
9//2
4
9%2
1
2**3
8
math.pow(2*3)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    math.pow(2*3)
NameError: name 'math' is not defined
import math
math.pow(2*3)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    math.pow(2*3)
TypeError: pow expected 2 arguments, got 1
math.pow(2,3)
8.0
math.sqrt(9)
3.0
4==4
True
4!=5
True
5>4
True
4<5
True
5>=4
True
"uva" != "banana"
True
"uva" != "UVA"
True
#texto formatado
print("\n%s=%.2f\n%s = %d kg" % ("Preço banana", 1.99, "Quantidade",3))

Preço banana=1.99
Quantidade = 3 kg
