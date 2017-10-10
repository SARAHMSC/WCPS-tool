

#/*
#* This file is subject to the terms and conditions defined in
#* file 'LICENSE.txt', which is part of this source code package.
#*/

# Everything is in a docstring!
"""


>>> import subprocess
>>> subprocess.check_output('python wc.py -wwwwllllccccc -lllll  testinputs/text2.txt', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'

#wrong flag after file 
>>> import subprocess
>>> subprocess.check_output('python wc.py testinputs/text2.txt -tww', shell=True).rstrip()
"wc: invalid option --t\\nTry 'wc --help' for more information."

#wrong flag before file 
>>> import subprocess
>>> subprocess.check_output('python wc.py -k testinputs/text2.txt', shell=True).rstrip()
"wc: invalid option --k\\nTry 'wc --help' for more information."

#Too long file name 
>>> import subprocess
>>> subprocess.check_output('python wc.py -wlc testinputs/fdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsa.txt', shell=True).rstrip()
'wc: testinputs/fdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsafdfgvfvsfsdfsdfsdfsdfsdfsdfsdfsffffffffffff444444444444444fwfdfsdfsa.txt: File name too long'

#wrong files name, No such file or directory
>>> import subprocess
>>> subprocess.check_output('python wc.py  testinputs/text.txt testinputs/readd.txt testinput/text2.txt', shell=True).splitlines()
[' 3 5 15 testinputs/text.txt', 'wc: testinputs/readd.txt: open: No such file or directory', 'wc: testinput/text2.txt: open: No such file or directory', ' 3 5 15 total']

#  all files are wrong 
>>> import subprocess
>>> subprocess.check_output('python wc.py  testinputs/ffft.txt testinputs/readd.txt testinput/text2.txt', shell=True).splitlines()
['wc: testinputs/ffft.txt: open: No such file or directory', 'wc: testinputs/readd.txt: open: No such file or directory', 'wc: testinput/text2.txt: open: No such file or directory', ' 0 0 0 total']

#  empty file 
>>> import subprocess
>>> subprocess.check_output('python wc.py  testinputs/empty.txt', shell=True).rstrip()
' 0 0 0 testinputs/empty.txt'

#  empty files 
>>> import subprocess
>>> subprocess.check_output('python wc.py  testinputs/empty.txt testinputs/empty.txt testinputs/empty.txt testinputs/empty.txt', shell=True).rstrip()
' 0 0 0 testinputs/empty.txt\\n 0 0 0 testinputs/empty.txt\\n 0 0 0 testinputs/empty.txt\\n 0 0 0 testinputs/empty.txt\\n 0 0 0 total'


#  More than one file 
>>> import subprocess
>>> subprocess.check_output('python wc.py  testinputs/text.txt testinputs/text1.txt testinputs/empty.txt testinputs/text3.txt', shell=True).rstrip()
' 3 5 15 testinputs/text.txt\\n 6 10 33 testinputs/text1.txt\\n 0 0 0 testinputs/empty.txt\\n 1739 10695 68489 testinputs/text3.txt\\n 1748 10710 68537 total'


>>> import subprocess
>>> subprocess.check_output('python wc.py testinputs/text2.txt -llll -cccc -wwww', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'

>>> import subprocess
>>> subprocess.check_output('python wc.py -wlc testinputs/text2.txt -llll -cccc -wwww', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'


>>> import subprocess
>>> subprocess.check_output('python wc.py -wlc testinputs/text2.txt -lllwwwc testinputs/read.txt testinputs/empty.txt', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt\\n 115 713 4565 testinputs/read.txt\\n 0 0 0 testinputs/empty.txt\\n 116 716 4573 total'

>>> import subprocess
>>> subprocess.check_output('python wc.py -wlc -lllll testinputs/incorrect.txt -lllwwwc testinputs/read.txt testinputs/empty.txt', shell=True).rstrip()
'wc: testinputs/incorrect.txt: open: No such file or directory\\n 115 713 4565 testinputs/read.txt\\n 0 0 0 testinputs/empty.txt\\n 115 713 4565 total'


>>> import subprocess
>>> subprocess.check_output('python wc.py testinputs/text2.txt', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'


>>> import subprocess
>>> subprocess.check_output('python wc.py testinputs/read.txt', shell=True).rstrip()
' 115 713 4565 testinputs/read.txt'

>>> import subprocess
>>> subprocess.check_output('python wc.py -l testinputs/text2.txt', shell=True).rstrip()
'1 testinputs/text2.txt'

>>> import subprocess
>>> subprocess.check_output('python wc.py -w testinputs/text2.txt', shell=True).rstrip()
'3 testinputs/text2.txt'

>>> import subprocess
>>> subprocess.check_output('python wc.py -c testinputs/text2.txt', shell=True).rstrip()
'8 testinputs/text2.txt'

>>> import subprocess
>>> subprocess.check_output('python wc.py -l -w -c testinputs/text2.txt', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'

# Flages in any combination 
>>> import subprocess
>>> subprocess.check_output('python wc.py -c -l -w testinputs/text2.txt', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'

# flags in  any combination 
>>> import subprocess
>>> subprocess.check_output('python wc.py -w -l -c testinputs/text2.txt', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'

# flags in  any combination 
>>> import subprocess
>>> subprocess.check_output('python wc.py -w -l testinputs/text2.txt', shell=True).rstrip()
' 1 3 testinputs/text2.txt'

# flags in  any combination 
>>> import subprocess
>>> subprocess.check_output('python wc.py -c -w testinputs/text2.txt', shell=True).rstrip()
' 3 8 testinputs/text2.txt'

#Repeated flages
>>> import subprocess
>>> subprocess.check_output('python wc.py -c -c -c -c -l -l -l -w testinputs/text2.txt', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'


#Repeated flages
>>> import subprocess
>>> subprocess.check_output('python wc.py -w -w -l -c -c -c testinputs/text2.txt', shell=True).rstrip()
' 1 3 8 testinputs/text2.txt'

#Repeated flages
>>> import subprocess
>>> subprocess.check_output('python wc.py -c -c -c testinputs/text2.txt', shell=True).rstrip()
'8 testinputs/text2.txt'

#empty file
>>> import subprocess
>>> subprocess.check_output('python wc.py  testinputs/empty.txt', shell=True).rstrip()
' 0 0 0 testinputs/empty.txt'

#Enter the wrong file name or file which is not exist 
>>> import subprocess
>>> subprocess.check_output('python wc.py testinputs/ttt.txt', shell=True).rstrip()
'wc: testinputs/ttt.txt: open: No such file or directory'

#Enter the wrong file name or file which is not exist   
>>> import subprocess
>>> subprocess.check_output('python wc.py txtxtx', shell=True).rstrip()
'wc: txtxtx: open: No such file or directory'

#Enter the wrong file name or file which is not exist and flags
>>> import subprocess
>>> subprocess.check_output('python wc.py -l testinputs/txtxtx', shell=True).rstrip()
'wc: testinputs/txtxtx: open: No such file or directory'

#Enter the wrong file name or file which is not exist and flags
>>> import subprocess
>>> subprocess.check_output('python wc.py -w -l ttt.txt', shell=True).rstrip()
'wc: ttt.txt: open: No such file or directory'

# Test case with more than one file
>>> import subprocess
>>> subprocess.check_output('python wc.py testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 3 5 15 testinputs/text.txt', ' 115 713 4565 testinputs/read.txt', ' 118 718 4580 total']

# Another solution is to add '\' to '\n' in expected output
# Test case with more than one file
>>> import subprocess
>>> subprocess.check_output('python wc.py testinputs/text.txt testinputs/read.txt', shell=True)
' 3 5 15 testinputs/text.txt\\n 115 713 4565 testinputs/read.txt\\n 118 718 4580 total\\n'

# Test case with more than one file with all the flags
>>> import subprocess
>>> subprocess.check_output('python wc.py -l -w -c testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 3 5 15 testinputs/text.txt', ' 115 713 4565 testinputs/read.txt', ' 118 718 4580 total']

 #Test cases with more than one file with flags in any combination 
>>> import subprocess
>>> subprocess.check_output('python wc.py -c -l -w testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 3 5 15 testinputs/text.txt', ' 115 713 4565 testinputs/read.txt', ' 118 718 4580 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py -c -l testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 3 15 testinputs/text.txt', ' 115 4565 testinputs/read.txt', ' 118 4580 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py -l -c testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 3 15 testinputs/text.txt', ' 115 4565 testinputs/read.txt', ' 118 4580 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py -w -c testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 5 15 testinputs/text.txt', ' 713 4565 testinputs/read.txt', ' 718 4580 total']


>>> import subprocess
>>> subprocess.check_output('python wc.py -w -l -c -l -l -w -c testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 3 5 15 testinputs/text.txt', ' 115 713 4565 testinputs/read.txt', ' 118 718 4580 total']


>>> import subprocess
>>> subprocess.check_output('python wc.py -w -c -w -w -c -c -c testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 5 15 testinputs/text.txt', ' 713 4565 testinputs/read.txt', ' 718 4580 total']


>>> import subprocess
>>> subprocess.check_output('python wc.py  -l -l -l -l testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
['3 testinputs/text.txt', '115 testinputs/read.txt', '118 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py -w -l testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
[' 3 5 testinputs/text.txt', ' 115 713 testinputs/read.txt', ' 118 718 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py  testinputs/empty.txt testinputs/text3.txt', shell=True).splitlines()
[' 0 0 0 testinputs/empty.txt', ' 1739 10695 68489 testinputs/text3.txt', ' 1739 10695 68489 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py -c -c -c testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
['15 testinputs/text.txt', '4565 testinputs/read.txt', '4580 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py -w -w -w testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
['5 testinputs/text.txt', '713 testinputs/read.txt', '718 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py -l -l -l testinputs/text.txt testinputs/read.txt', shell=True).splitlines()
['3 testinputs/text.txt', '115 testinputs/read.txt', '118 total']

>>> import subprocess
>>> subprocess.check_output('python wc.py  testinputs/text.txt testinputs/readd.txt testinput/text2.txt', shell=True).splitlines()
[' 3 5 15 testinputs/text.txt', 'wc: testinputs/readd.txt: open: No such file or directory', 'wc: testinput/text2.txt: open: No such file or directory', ' 3 5 15 total']

#============================================================================================================================
# the output :
#$ python wc.py testinputs/text1.txt testinputs/text3.txt testinputs/tex.txt  
#6 10 33 testinputs/text1.txt
# 1739 10695 68489 testinputs/text3.txt
# wc: testinputs/tex.txt: open: No such file or directory
#1745 10705 68522 total

"""
#.rstrip()
#replace()
#.splitlines()
#.replace('\\n',<BLANKLINE>)


 # We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()
