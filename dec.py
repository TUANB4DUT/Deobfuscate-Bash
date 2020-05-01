#!/usr/bin/python
#https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
import os
import sys
import fileinput

textToSearch = "eval"
textToReplace = "echo"

print ("Path of File to Deobfuscate:")
fileToSearch  = input( ">>> " )

tempFile = open( fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        print('success')
    else:
        print('eval not found')
    tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()
print ("run your file for see the magic")
input( '\n\n Press Enter to exit...' )

