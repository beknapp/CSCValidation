#! /usr/bin/env python

import os
import sys
import fileinput
import string
import time
import subprocess
import pickle


######################################
########### Configuration ############
######################################


# First argument is the maximum number of events processed -> -1 for all events
MAXEVENTS = sys.argv[1]

 

# Second argument is the run number
RUNNUMBER = sys.argv[2]



# Third argument is the filepath
FILEPATH = sys.argv[3]




######################################
########### Retrieve Run Files #######
######################################

allruns = os.listdir(FILEPATH)

#print allruns

RUI = []

TEMPLATE = open('raw_template.py')

outlines = TEMPLATE.readlines()

TEMPLATE.close()

# This is the line before which the RUIs and their files are declared in the config file.
# Note that the first index is one

IN = 25

monitor = '000'

for rui in allruns:
	ruinum = rui[16:21]

	if '000' in rui:
		outlines.insert(IN, ",        "+ruinum+" = cms.untracked.vstring('"+FILEPATH+"csc_00"+RUNNUMBER+"_Emu"+ruinum+"_Monitor_"+monitor+".raw')\n")
		IN = IN + 1
		RUI.append(ruinum)

#print outlines

#pickle.dump(outfile, "process_run"+RUNNUMBER)	


	
outfile = open("process_run_"+RUNNUMBER+".py", "w")

for line in outlines:
	if "maxevents" in line:
		line = line.replace("maxevents", MAXEVENTS)
	 
	if "runnumber" in line:
		line = line.replace("runnumber", RUNNUMBER)
	
	#print line

	outfile.write(line)

outfile.close()

print RUNNUMBER
print MAXEVENTS




#subprocess.Popen("echo Hello World", stdout=PIPE).stdout.read()

pipe = subprocess.PIPE

#subprocess.Popen("cmsRun process_run_"+RUNNUMBER+".py", stdout=pipe, shell=True)

#shell=True, stdout=pipe).communicate()[0]









