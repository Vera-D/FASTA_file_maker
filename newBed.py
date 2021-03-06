import webbrowser
import requests
import re
import numpy
import xml.etree.ElementTree as ET
from xml.dom import minidom 
from datetime import datetime

startTime = datetime.now()

# This script will create a FASTA file from the coordinates in a bed file
# by querying UCSC web API, this script has hardcoded hg38 assembly sequence
# ToDo: Make Directories dynamic

# import bed file
BEDfile = open('C:\\Users\\vdiaz\\Documents\\FASTA_File_Maker\\input\\n30.bed', 'r')
#get the 1st line
lookup = 'track'
#this code finds whatever is in lookup

firstline = True
newBEDFile= open("newBed.bed","w+")
#Config
delim = ":"
nucAcid="DNA"
strand="+"
		
for line in BEDfile:
#this code splits the line
	if firstline: #skip
		firstline = False
	else:
		bedLine = re.split(r'\t+',line)
		#Use the line below only if you have to replace whitespace in the description
		bedLineDesc=bedLine[-1].replace(" ","_")
		#Remove trailing character with new line and extra underscore
		bedLineDesc=bedLineDesc[:-2]
		bedLineRegion = bedLine[0:3]
		newBedLine=bedLineRegion+bedLineDesc.split()
		print(newBedLine)
		newLine='\t'.join(str(x) for x in(newBedLine))
		newBEDFile.write(newLine)
		newBEDFile.write('\n')
		
newBEDFile.close()
BEDfile.close()

runtime = datetime.now() - startTime
print (runtime )