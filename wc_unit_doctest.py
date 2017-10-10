
#/*
#* This file is subject to the terms and conditions defined in
#* file 'LICENSE.txt', which is part of this source code package.
#*/

# Everything is in a docstring!
#import sys
"""
#====================def filerw========================
#first check file then open and read the file 

#correct file 
>>> wc.filerw('testinputs/text1.txt', "file")
'l1\\nl2 l22\\nl3\\nl4\\nl5 \\nl6 l7 l8 \\nl9 '

#not exist file show the error message and return -1 
>>> wc.filerw('testinputs/t.txt', "file")
wc: testinputs/t.txt: open: No such file or directory
'-1'

#file name too big 
>>> wc.filerw('testinputs/1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt', "file")
wc: testinputs/1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long
'-1'

#=================def wccount=========================
# method wccount return lis of number of lines,words and chars - order: chars, lines, words
>>> with open('testinputs/text1.txt') as f: wc.wccount(f.read())
[33, 6, 10]
>>> with open('testinputs/empty.txt') as f: wc.wccount(f.read())
[0, 0, 0]
>>> with open('testinputs/long.txt') as f: wc.wccount(f.read())
[68489, 1739, 10695]


#=================def charscount=========================
# method charscount return  the number of chars

>>> with open('testinputs/text1.txt') as f: wc.charscount(f.read())
33
>>> with open('testinputs/empty.txt') as f: wc.charscount(f.read())
0
>>> with open('testinputs/long.txt') as f: wc.charscount(f.read())
68489

#=================def wordscount=========================
# method wordscount return  the number of words

>>> with open('testinputs/text1.txt') as f: wc.wordscount(f.read())
10
>>> with open('testinputs/empty.txt') as f: wc.wordscount(f.read())
0
>>> with open('testinputs/long.txt') as f: wc.wordscount(f.read())
10695


#=================def linescount=========================
# method linescount return  the number of lines

>>> with open('testinputs/text1.txt') as f: wc.linescount(f.read())
6
>>> with open('testinputs/empty.txt') as f: wc.linescount(f.read())
0
>>> with open('testinputs/long.txt') as f: wc.linescount(f.read())
1739


#=================def call_defualt_lwc=====================
# if no flges is chosen and number of files is more than zero 

>>> wc.call_defualt_lwc(['testinputs/long.txt'])
 1739 10695 68489 testinputs/long.txt
 
>>> wc.call_defualt_lwc(['testinputs/long.txt'])
 1739 10695 68489 testinputs/long.txt
 
>>> wc.call_defualt_lwc(['testinputs/long.txt', 'testinputs/text1.txt', 'testinputs/text.txt'])
 1739 10695 68489 testinputs/long.txt
 6 10 33 testinputs/text1.txt
 3 5 15 testinputs/text.txt
 1748 10710 68537 total
 
>>> wc.call_defualt_lwc(['testinputs/long.txt', 'testinputs/empty.txt', 'testinputs/text.txt'])
 1739 10695 68489 testinputs/long.txt
 0 0 0 testinputs/empty.txt
 3 5 15 testinputs/text.txt
 1742 10700 68504 total
 
>>> wc.call_defualt_lwc(['testinputs/long.txt', 'testinputs/te.txt', 'testinputs/text.txt'])
 1739 10695 68489 testinputs/long.txt
wc: testinputs/te.txt: open: No such file or directory
 3 5 15 testinputs/text.txt
 1742 10700 68504 total
 
>>> wc.call_defualt_lwc(['testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt'])
wc: testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long


#=================def call_lwc=====================
if all the flages are chosen in any combaination 

>>> wc.call_lwc(['testinputs/long.txt'])
 1739 10695 68489 testinputs/long.txt
 
>>> wc.call_lwc(['testinputs/long.txt'])
 1739 10695 68489 testinputs/long.txt
 
>>> wc.call_lwc(['testinputs/long.txt', 'testinputs/text1.txt', 'testinputs/text.txt'])
 1739 10695 68489 testinputs/long.txt
 6 10 33 testinputs/text1.txt
 3 5 15 testinputs/text.txt
 1748 10710 68537 total
 
>>> wc.call_lwc(['testinputs/long.txt', 'testinputs/te.txt', 'testinputs/text.txt'])
 1739 10695 68489 testinputs/long.txt
wc: testinputs/te.txt: open: No such file or directory
 3 5 15 testinputs/text.txt
 1742 10700 68504 total
 
>>> wc.call_lwc(['testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt'])
wc: testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long

#=================def call_l=====================

>>> wc.call_l(['testinputs/long.txt', 'testinputs/text1.txt', 'testinputs/empty.txt'])
1739 testinputs/long.txt
6 testinputs/text1.txt
0 testinputs/empty.txt
1745 total

>>> wc.call_l(['testinputs/long.txt', 'testinputs/te.txt', 'testinputs/empty.txt'])
1739 testinputs/long.txt
wc: testinputs/te.txt: open: No such file or directory
0 testinputs/empty.txt
1739 total

>>> wc.call_l(['testinputs/long.txt'])
1739 testinputs/long.txt

>>> wc.call_l(['testinputs/tex.txt'])
wc: testinputs/tex.txt: open: No such file or directory

>>> wc.call_l(['testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt'])
wc: testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long

#=================def call_w=====================

>>> wc.call_w(['testinputs/long.txt', 'testinputs/text1.txt', 'testinputs/empty.txt'])
10695 testinputs/long.txt
10 testinputs/text1.txt
0 testinputs/empty.txt
10705 total

>>> wc.call_w(['testinputs/long.txt', 'testinputs/te.txt', 'testinputs/empty.txt'])
10695 testinputs/long.txt
wc: testinputs/te.txt: open: No such file or directory
0 testinputs/empty.txt
10695 total

>>> wc.call_w(['testinputs/long.txt'])
10695 testinputs/long.txt

>>> wc.call_w(['testinputs/tex.txt'])
wc: testinputs/tex.txt: open: No such file or directory

>>> wc.call_w(['testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt'])
wc: testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long

#=================def call_c=====================

>>> wc.call_c(['testinputs/long.txt', 'testinputs/text1.txt', 'testinputs/empty.txt'])
68489 testinputs/long.txt
33 testinputs/text1.txt
0 testinputs/empty.txt
68522 total

>>> wc.call_c(['testinputs/long.txt', 'testinputs/te.txt', 'testinputs/empty.txt'])
68489 testinputs/long.txt
wc: testinputs/te.txt: open: No such file or directory
0 testinputs/empty.txt
68489 total

>>> wc.call_c(['testinputs/long.txt'])
68489 testinputs/long.txt

>>> wc.call_c(['testinputs/tex.txt'])
wc: testinputs/tex.txt: open: No such file or directory

>>> wc.call_c(['testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt'])
wc: testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long

#=================def call_lw=====================

>>> wc.call_lw(['testinputs/long.txt', 'testinputs/text1.txt', 'testinputs/empty.txt'])
 1739 10695 testinputs/long.txt
 6 10 testinputs/text1.txt
 0 0 testinputs/empty.txt
 1745 10705 total

>>> wc.call_lw(['testinputs/long.txt', 'testinputs/te.txt', 'testinputs/empty.txt'])
 1739 10695 testinputs/long.txt
wc: testinputs/te.txt: open: No such file or directory
 0 0 testinputs/empty.txt
 1739 10695 total

>>> wc.call_lw(['testinputs/long.txt'])
 1739 10695 testinputs/long.txt

>>> wc.call_lw(['testinputs/tex.txt'])
wc: testinputs/tex.txt: open: No such file or directory

>>> wc.call_lw(['testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt'])
wc: testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long

#=================def call_lc=====================

>>> wc.call_lc(['testinputs/long.txt', 'testinputs/text1.txt', 'testinputs/empty.txt'])
 1739 68489 testinputs/long.txt
 6 33 testinputs/text1.txt
 0 0 testinputs/empty.txt
 1745 68522 total
>>> wc.call_lc(['testinputs/long.txt', 'testinputs/te.txt', 'testinputs/empty.txt'])
 1739 68489 testinputs/long.txt
wc: testinputs/te.txt: open: No such file or directory
 0 0 testinputs/empty.txt
 1739 68489 total

>>> wc.call_lc(['testinputs/long.txt'])
 1739 68489 testinputs/long.txt

>>> wc.call_lc(['testinputs/tex.txt'])
wc: testinputs/tex.txt: open: No such file or directory

>>> wc.call_lc(['testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt'])
wc: testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long

#=================def call_wc=====================

>>> wc.call_wc(['testinputs/long.txt', 'testinputs/text1.txt', 'testinputs/empty.txt'])
 10695 68489 testinputs/long.txt
 10 33 testinputs/text1.txt
 0 0 testinputs/empty.txt
 10705 68522 total
     
>>> wc.call_wc(['testinputs/long.txt', 'testinputs/te.txt', 'testinputs/empty.txt'])
 10695 68489 testinputs/long.txt
wc: testinputs/te.txt: open: No such file or directory
 0 0 testinputs/empty.txt
 10695 68489 total

>>> wc.call_wc(['testinputs/long.txt'])
 10695 68489 testinputs/long.txt

>>> wc.call_wc(['testinputs/tex.txt'])
wc: testinputs/tex.txt: open: No such file or directory

>>> wc.call_wc(['testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt'])
wc: testinputs/1111111111111111gggggggggggggggggdddddddddddddddddjjjjjjjjjjjjjjjjjjeeeeeeeeeetttttttttttttttttttttttttttasdadasdasdasdasdasdasda111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.txt: File name too long


#=================def processargv()=====================
# take random input and return two lists 1)list of flages 2)list of files 
# should be tested in separate documents 


#>>> wc.sys.argv[1:] = ['-l','-wwwwlllccc', '-c','testinputs/text2.txt', '-w','testinputs/empty.txt']
#>>> wc.processargv()
#(['-l', '-wwwwlllccc', '-c', '-w'], ['testinputs/text2.txt', 'testinputs/empty.txt'])


#>>> sys.agrv = ['testinputs/text2.txt','-c']
#>>> wc.processargv()
#(['-c'], ['testinputs/text2.txt'])

#>>> sys.argv = ['-wwwwlllccc','testinputs/text2.txt','-c','testinputs/empty.txt']
#>>> wc.processargv()
#(['-wwwwlllccc', '-c'], ['testinputs/empty.txt', 'testinputs/empty.txt'])
 
#>>> sys.argv = ['-w','testinputs/text2.txt','-c']
#>>> wc.processargv()
#(['-w','-c'], ['testinputs/text2.txt'])

#>>> sys.argv = ['-ll','-wwwwlllccc','testinputs/text2.txt','-c', 'testinputs/text3.txt', '-w']
#>>> wc.processargv()
#(['-ll','-wwwwlllccc','-w','-c'], ['testinputs/text3.txt','testinputs/text2.txt'])

# check flages if user enter incorrect flages
#>>> sys.argv = ['-w', '-t','testinputs/empty.txt','-wwwwwllllccc','-lcw', 'testinputs/empty.txt', '-w', '-l']
#>>> wc.processargv()
#wc: invalid option --t
#    Try 'wc --help' for more information.

#check sdin with processargv()
#>>> import io
#>>> oldstdin = sys.stdin
#>>> sys.stdin = open('testinputs/text1.txt', 'r')
#>>> sys.stdin.flush()
#>>> wc.processargv()
#([], ['l1\\nl2 l22\\nl3\\nl4\\nl5 \\nl6 l7 l8 \\nl9 '])

#check sdin with processargv() and add flages 
#>>> import io
#>>> wc.flages = ['-l','-wlc']
#>>> oldstdin = sys.stdin
#>>> sys.stdin = open('testinputs/text1.txt', 'r')
#>>> sys.stdin.flush()
#>>> wc.processargv()
#(['-l', '-wlc'], ['l1\\nl2 l22\\nl3\\nl4\\nl5 \\nl6 l7 l8 \\nl9 '])

"""


 # We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
	import wc
	import doctest
	import sys
	# The following command extracts all testable docstrings from the current module.
	doctest.testmod()
