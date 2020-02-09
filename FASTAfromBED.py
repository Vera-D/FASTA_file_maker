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
BEDfile = open('C:\\Users\\vdiaz\\Documents\\FASTA_File_Maker\\input\\n350.bed', 'r')
#get the 1st line
lookup = 'track'
#this code finds whatever is in lookup

firstline = True
fastaFile= open("newFASTA.fa","w+")
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
		
	#string to search in UCSC
		UCSCsearch='http://genome.ucsc.edu/cgi-bin/das/hg38/dna?segment='+newBedLine[0]+':'+newBedLine[1]+','+newBedLine[2]
		print(UCSCsearch)
	#search on ucsc and save 
		response = requests.get(UCSCsearch)
	#temporarily save the xml file to extract the sequence info
		with open('feed.xml', 'wb') as file:
			file.write(response.content)
		xmldoc = minidom.parse('feed.xml')
	#get the DNA sequence from the xml file
		itemlist = xmldoc.getElementsByTagName('DNA')
		FASTAdesc = ">"+bedLineDesc+delim+bedLineRegion[0]+delim+bedLineRegion[1]+delim+bedLineRegion[2]+delim+"hg38"+delim+strand+":"+nucAcid
		sequence=itemlist[0].firstChild.nodeValue
		print(FASTAdesc)
	#Write the FASTA description line and sequence to the new FASTA file
		fastaFile.write(FASTAdesc)
		fastaFile.write(sequence)
		
fastaFile.close()
file.close()

runtime = datetime.now() - startTime
print (runtime )