#Name: Mukesh Kumar Pullabhatla
#LEMPEL ZIV WELCH ALGORITHM
#--------------------------------------

#Decoding/decompression program

import sys
from sys import argv
import struct
from struct import *

# insert the compressed file input and the number of bits
output1, n = argv[1:]            
# defining the maximum table size
MAX_TABLE_SIZE = pow(2,int(n))
# opening the compressed file
outputfile = open(output1, "r")
# defining variables
compressvar = []

string = ""
bits=outputfile.read()
splitbits=bits.split('\t')
print(splitbits)
# Reading the compressed file.
for code in splitbits:
    if code!='':
        code=int(code,2)
        compressvar.append(code)
print(compressvar)
# Building and initializing the dictionary.
tablesize = 256
table ={}
for x in range(256):
    table[x]= chr(x)
#print(table)
# iterating the codes.
# LZW Decompression algorithm
print(compressvar)
string=table[compressvar[0]]
print(string)

out = open("decode.txt",'w')
out.write(string)
i=1
for code in compressvar:
    nextcode = compressvar[i]
    if nextcode not in table:
        newstring = string + string[0]
    else:
        newstring=table[nextcode]
    #print(newstring)
    if tablesize<MAX_TABLE_SIZE:
        table[tablesize]=string+newstring[0]
        tablesize = tablesize+1
    string=newstring
    i+=1
    if(i==len(compressvar)):
        break;
    print(newstring)
    out.write(newstring)
# storing the decompressed string into a file.
#print(table)
print(newstring)
out.write(newstring)
out.close()
outputfile.close()
