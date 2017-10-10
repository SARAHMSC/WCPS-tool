
#/*
#* This file is subject to the terms and conditions defined in
#* file 'LICENSE.txt', which is part of this source code package.
#*/
from subprocess import Popen, PIPE, STDOUT
import sys 
import os

def efficiency_teste():

	#Set up directory 
	if len(sys.argv)>1:
	# sys.argv[0] is the program filename
		directory = sys.argv[1]
	else:
	# Default Directory
		directory = 'testinputs'
	program = 'python wc.py'
	#print header 
	print('Testcase    RealTime    CPUTime')
	
	 
	# sys.argv[0] is the program filename
	for filename in os.listdir(directory):
		if filename.endswith(".txt") or filename.endswith(".py"): 

			cmd = 'time'+' '+program+' '+directory+'/filename'
			p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
			output1 = p.stdout.read()
			#Remove lines
			output_without_spaces = output1.replace('\n','')
			#Remove taps
			output_without_taps = output_without_spaces.replace('	','')
		
			#Get real time 
			index_of_real= output_without_taps.index('real')
			index_of_real_time = index_of_real + 4 
			end_index_of_real_time= index_of_real_time + 8
		
		
			#Get CPU\user time 
			index_of_user= output_without_taps.index('user')
			index_of_user_time = index_of_user + 4 
			end_index_of_user_time= index_of_user_time + 8
		
		
			#Get CPU\sys time 
			index_of_sys= output_without_taps.index('sys')
			index_of_sys_time = index_of_sys + 3 
			end_index_of_sys_time= index_of_sys_time + 8

		
			#Add CPU time user+sys
			#==============================================================================
			# 1- add secs 
			#Get user time mints
			user_end_mins = index_of_user_time + 1
			user_num_mins = output_without_taps[index_of_user_time: user_end_mins]
			user_num_mins_int = int(user_num_mins)
			# additional step convert mins to secs if it necessary 
			#user_mins_to_secs= user_num_mins_int* 60

			# Get sys time mints
			sys_end_mins = index_of_sys_time + 1
			sys_num_mins = output_without_taps[index_of_sys_time: sys_end_mins]
			sys_num_mins_int = int(sys_num_mins)
			# additional step convert mins to secs
			#sys_mins_to_secs= sys_num_mins_int* 60
					
			# add mins 
			#CPU mins = user and sys mins 
			CPU_mins = user_num_mins_int + sys_num_mins_int
			CPU_mins_str = str(CPU_mins)
			
			#OR CPU total mins in secs
			#CPU_mins_secs = user_mins_to_secs + sys_mins_to_secs
			#CPU_mins_secs_str = str(CPU_mins_secs)
			
			#==============================================================================
			# 2- add secs 
			#user time secs
			user_start_secs = user_end_mins + 1
			user_end_secs = output_without_taps.index('s', user_end_mins)
			user_num_secs = output_without_taps[user_start_secs: user_end_secs]
			user_num_secs_float = float(user_num_secs)
		
			#sys time secs
			sys_start_secs = sys_end_mins + 1
			sys_end_secs = output_without_taps.index('s', sys_end_mins)
			sys_num_secs = output_without_taps[sys_start_secs: sys_end_secs]
			sys_num_secs_float = float(sys_num_secs)

		
			#CPU secs = user and sys secs
			CPU_secs = user_num_secs_float + sys_num_secs_float
			CPU_secs_str = str(CPU_secs)
			
			#==============================================================================
			#CPUtime 
			CPU_Time = CPU_mins_str+"m"+CPU_secs_str +"s"
			
			#==============================================================================

			# print real time , CPU time 
			print (filename+'	'+output_without_taps[index_of_real_time: 	end_index_of_real_time]+'	'+CPU_Time)

			

	
if __name__ == "__main__":
	
    efficiency_teste()
    
 