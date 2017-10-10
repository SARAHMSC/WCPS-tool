
#/*
#* This file is subject to the terms and conditions defined in
#* file 'LICENSE.txt', which is part of this source code package.
#*/

#/*************************************************************************
# * 
# * ADOBE CONFIDENTIAL
# * __________________
# * 
# *  [2016] - [2017] WC Systems 
# *  All Rights Reserved.
# * 
# * NOTICE:  All information contained herein is, and remains
# * the property of WC systems  and its suppliers,
# * if any.  The intellectual and technical concepts contained
# * herein are proprietary to author and owner or writer of code.
# * and its suppliers and may be covered by U.S. and Foreign Patents,
# * patents in process, and are protected by trade secret or copyright law.
# * Dissemination of this information or reproduction of this material
# * is strictly forbidden unless prior written permission is obtained
# * from owner or writer of code.
# */



flages = []
files = []
flag_have_l = 0
flag_have_w = 0
flag_have_c = 0
source="file"
count_files = 0
import sys

#check and open file then read the file
def filerw(filename, source):
	# check file name too big 
	if source == "-": #if source from stdin
	   text= filename
	elif len(filename) > 250:
		 print "wc: %s: File name too long" %filename
		 text = "-1"# file name  too big 
	else:
		try:
			fin = open(filename, 'r')
			text = fin.read() 
			#print "in readw method"+text
			fin.close()
		except IOError:
			print "wc: %s: open: No such file or directory" %filename
			text = "-1"# incorrect file name 
			#raise SystemExit
	return text

# count number of lines, words and chars
def wccount(text):
    lwc = []
    # all characters
    number_of_characters = len(text)
    lwc.append(number_of_characters)
    # assumes lines end with '\n'
    number_of_lines = text.count('\n') + 1
    number_of_lines = number_of_lines -1
    # or    number_of_lines = text.count('\n')
    lwc.append(number_of_lines)
    # assumes words are separated by whitespace
    wordlist = text.split(None)
    number_of_words = len(wordlist)
    lwc.append(number_of_words)
    
    return lwc


#count number of lines only 
def charscount(text):
    number_of_characters = len(text)
    return number_of_characters

#count number of words only 
def wordscount(text):

    # assumes words are separated by whitespace
    wordlist = text.split(None)
    number_of_words = len(wordlist)
    return number_of_words  

    
#count number of chars only 
def linescount(text):
   
    number_of_lines = text.count('\n')
    return number_of_lines


# Get sys.argv list and find flages, files, and incorrect inputs 
# Get stdin if sys.argv list length is not grater than 1 
def processargv():

	global flages
	global files
	global flag_have_l
	global flag_have_w
	global flag_have_c
	global count_files
	global source

	if len(sys.argv) > 1:
	# sys.argv[0] is the program filename, slice it off
		for flagorfile in sys.argv[1:]:
			ff= str(flagorfile)
			# add .lower() because WC program is not case seanstive 
			if ff.lower() == '-l' or ff.lower() =='-w' or ff.lower()=='-c':
				flages.append(ff) # add flag to flages list 
			# check if the expression starts with -flag and if flage have a correct combination and correct letters otherwise show an error message 
			elif ff.startswith("-"):
				flag = ff
				# start form 1 as index 0 is "-" to check the flag
				for i in range(1, len(flag)):
				# add .lower() because WC program is not case seanstive 
				# if flag have any letter other than w or l or c show an error message 
					if (flag[i].lower() != "l") and (flag[i].lower() != "w") and (flag[i].lower() != "c"):
						 print "wc: invalid option --%s" %flag[i]
						 print "Try 'wc --help' for more information."
						 raise SystemExit
					elif flag[i].lower() == "l":
						flag_have_l= flag_have_l+1
					elif flag[i].lower() == "w":
						flag_have_w= flag_have_w+1
					elif flag[i].lower() == "c":
						flag_have_c= flag_have_c+1
				flages.append(flag)
			else:
				files.append(ff)
				count_files = count_files+1
				
	else:
	#if sys.argv list length is not grater than 1 the get input from stdin
	#stdin (no flages)
		source="-"
		text = sys.stdin.read()
		files.append(text)

	#stdin with flages 
	if len(files) == 0:
		if '-l' in flages or '-w' in flages or '-c' in flages or flag_have_l > 0 or  flag_have_w > 0 or flag_have_c > 0:
			source="-"
			text = sys.stdin.read()
			files.append(text)
	return flages, files 
	
#the defualt option :if there is no flag is chosen and files not equal 0 	
def call_defualt_lwc(files):
		
		count_lwc= []
		count_lines = count_words = count_chars = 0
		if len(files) > 0:  #len(files) > 0 and
			for x in files[0:]:
				file = filerw(x, source)
				if file == "-1":# file is not correct 
					continue
				count_lwc= wccount(file)
				count_lines= count_lines+count_lwc[1]# lines index 1
				count_words= count_words+count_lwc[2]# words index 2
				count_chars= count_chars+count_lwc[0]# chars index 0
				if source == "-":
					x = ""
				print " %d %d %d %s" % (count_lwc[1], count_lwc[2], count_lwc[0], x)
			if  len(files) >  1: # if number of files is more than one print total
				print " %d %d %d %s" % (count_lines, count_words, count_chars, "total")

		else: #stdin
			x = files[0]
			count_lwc= wccount(x)
			if source == "-":
				x = ""
			print " %d %d %d %s" % (count_lwc[1], count_lwc[2], count_lwc[0], x)
#===================================================

#all flages chosen  in any combination
def call_lwc(files):
			#print "lwc2"
			count_lwc= []
			count_lines = count_words = count_chars = 0
			if len(files) > 0:
				for x in files[0:]:
					file = filerw(x, source)
					if file == "-1":
						continue
					count_lwc= wccount(file)
					count_lines= count_lines+count_lwc[1]# lines index 1
					count_words= count_words+count_lwc[2]# words index 2
					count_chars= count_chars+count_lwc[0]# chars index 0
					if source == "-":
						x = ""
					print " %d %d %d %s" % (count_lwc[1], count_lwc[2], count_lwc[0], x)
				if  len(files) >  1:
					print " %d %d %d %s" % (count_lines, count_words, count_chars, "total")
			else: #stdin
				x = files[0]
				count_lwc= wccount(x)
				if source == "-":
					x = ""
				print " %d %d %d %s" % (count_lwc[1], count_lwc[2], count_lwc[0], x)
#=====================================================

#if chosen flag is -l
def call_l(files):
			
			#print "call-l"
			count_lines = num_of_lines = 0
			if len(files) > 0:
				for x in files[0:]:
					file = filerw(x, source)
					if file == "-1":
						continue
					num_of_lines=linescount(file)
					count_lines= count_lines+num_of_lines 
					if source == "-": # if source from stdin
						x = ""
					print "%d%s%s %s" % (num_of_lines, "", "", x)
				if  len(files) >  1:
					print "%d%s%s %s" % (count_lines, "", "", "total")
			else: #stdin
				x = files[0]
				#num_of_lines = linescount(x, source)
				num_of_lines = linescount(x)
				if source == "-":
					x = ""
				print "%d%s%s %s" % (num_of_lines, "", "", x)				
#=====================================================

#if chosen flag is -w
def call_w(files):
			#print "call-w"
			count_words = 0
			if len(files) > 0:
				for x in files[0:]:
					file = filerw(x, source)
					if file == "-1":
						continue
					num_of_words = wordscount(file)
					count_words= count_words+num_of_words 
					if source == "-":# if source from stdin
						x = ""
					print"%s%d%s %s" % ("", num_of_words, "", x)
				if  len(files) >  1:
					print"%s%d%s %s" % ("", count_words, "", "total")
			else:#stdin
				x = files[0]
				num_of_words = wordscount(x)
				if source == "-":
					x = ""
				print"%s%d%s %s" % ("", num_of_words, "", x)
#=====================================================

#if chosen flag is -c
def call_c(files):
			#print "call-c"
			count_chars = 0
			if len(files) > 0:
				for x in files[0:]:
					file = filerw(x, source)
					if file == "-1":
						continue
					#num_of_chars= charscount(file, source)
					num_of_chars= charscount(file)
					count_chars= count_chars+num_of_chars 
					if source == "-":
						x = ""
					print "%s%s%d %s" % ("", "", num_of_chars, x)
				if  len(files) >  1:
					print "%s%s%d %s" % ("", "", count_chars, "total")
			else:#stdin
				x = files[0]
				#num_of_chars= charscount(x, source)
				num_of_chars= charscount(x)
				if source == "-":
					x = ""
				print "%s%s%d %s" % ("", "", num_of_chars, x)
#=====================================================
#if chosen flages are -l and -w in any combination
def call_lw(files):
			
			count_l = 0
			count_w = 0
			if len(files) > 0:
				for x in files[0:]:
					file = filerw(x, source)
					if file == "-1":
						continue
					num_of_lines=linescount(file)
					num_of_words=wordscount(file)
					count_l= count_l+num_of_lines 
					count_w= count_w+num_of_words 
					if source == "-":
						x = ""
					print " %d %d%s %s" % (num_of_lines, num_of_words, "", x)
				if  len(files) >  1:
					print " %d %d%s %s" % (count_l, count_w, "", "total")
			else:#stdin
				x = files[0]
				num_of_lines=linescount(x)
				num_of_words=wordscount(x)
				if source == "-":
					x = ""
				print " %d %d%s %s" % (num_of_lines, num_of_words, "", x)
#=====================================================

# if chosen flages are -l and -c in any combination				
def call_lc(files):
			#print "call-lc"
			count_l = 0
			count_c = 0
			if len(files) > 0:
				for x in files[0:]:
					file = filerw(x, source)
					if file == "-1":
						continue
					num_of_lines=linescount(file)
					num_of_chars= charscount(file)
					count_l= count_l+num_of_lines 
					count_c= count_c+num_of_chars 
					if source == "-":
						x = ""
					print " %d%s %d %s" % (num_of_lines, "", num_of_chars, x)
				if  len(files) >  1:
					print " %d%s %d %s" % (count_l, "", count_c, "total")

			else:#stdin
				x = files[0]
				num_of_lines=linescount(x)
				num_of_chars= charscount(x)
				if source == "-":
					x = ""
				print " %d%s %d %s" % (num_of_lines, "", num_of_chars, x)	
#=====================================================	

# if chosen flages are -w and -c in any combination			
def call_wc(files):
			count_w = 0
			count_c = 0
			if len(files) > 0:
				for x in files[0:]:
					file = filerw(x, source)
					if file == "-1":
						continue
					num_of_words=wordscount(file)
					num_of_chars= charscount(file)
					count_w= count_w+num_of_words 
					count_c= count_c+num_of_chars 
					if source == "-":
					   x = ""
					print "%s %d %d %s" % ("", num_of_words, num_of_chars, x)
				if  len(files) >  1:
					print "%s %d %d %s" % ("", count_w, count_c, "total")
			else:#stdin
				x = files[0]
				num_of_words=wordscount(x)
				num_of_chars= charscount(x)
				if source == "-":
					x = ""
				print "%s %d %d %s" % ("", num_of_words, num_of_chars, x)				
							
# ---------------------------main -----------------------------------------
if __name__ == '__main__':
	
	#global flages
	#global files
	#global sys.argv


	flages, files = processargv()

#===============================================================
# Possibilities
#================================================================
# 1- the defualt option :if there is no flag is chosen
#================================================================

	if (len(flages) == 0) and (len(files)) != 0:
		call_defualt_lwc(files)
	
#================================================================
# 2- all flages in any combination
#================================================================

	elif ('-l' in flages and '-w' in flages and '-c' in flages) or (flag_have_l > 0 and  flag_have_w > 0 and flag_have_c > 0):
			call_lwc(files)
			
#================================================================           
# 3- if chosen flag is -l
#================================================================
	elif  ('-l' in flages and '-w' not in flages and '-c' not in flages) or (flag_have_l > 0 and  flag_have_w == 0 and flag_have_c == 0):
			call_l(files)
			
#================================================================           
# 4- if chosen flag is -w
#================================================================
	elif  ('-w' in flages and '-l' not in flages and '-c' not in flages) or (flag_have_l == 0 and  flag_have_w >0 and flag_have_c == 0):
			call_w(files)
			
#================================================================
# 5- if chosen flag is -c
#================================================================
	elif  ('-c' in flages and '-l' not in flages and '-w' not in flages) or (flag_have_l == 0 and  flag_have_w == 0 and flag_have_c >0):
			 call_c(files)
			
#================================================================
# 6- if chosen flages are -l and -w in any combination
#================================================================
	elif  ('-l' in flages and '-w'in flages and '-c' not in flages) or (flag_have_l > 0 and  flag_have_w > 0 and flag_have_c == 0):
			call_lw(files)
			
#================================================================           
# 7- if chosen flages are -l and -c in any combination
#================================================================
	elif  ('-l' in flages and '-c'in flages and '-w' not in flages) or (flag_have_l > 0 and  flag_have_w == 0 and flag_have_c >0):
		  call_lc(files)
			
#================================================================           
# 8 if chosen flages are -w and -c in any combination
#================================================================
	elif  ('-w' in flages and '-c'in flages and '-l' not in flages) or (flag_have_l == 0 and  flag_have_w >0 and flag_have_c >0):
			call_wc( files)
			
#=============================END========================================

