#Name: Mukesh Kumar Pullabhatla
#LEMPEL ZIV WELCH ALGORITHM
#--------------------------------------

#Encoding/compression program
#load the module named sys - to pass command line arguments
import sys
from sys import argv
#to interpret strings as binary we import struct
from struct import *
#load the input file and number of bits
input1, n = argv[1:]
#define MAX_TABLE_SIZE
MAX_TABLE_SIZE = pow(2,int(n)) #bit length is number of encoding bits
#open the input file
inputfile = open(input1)
#read the input file and store in a variable
var = inputfile.read()
#initialize table
tablesize = 256
table = {chr(i): i for i in range(tablesize)}
#string = null
string = ""
#define variable to store the compressed data
compressvar = []
#iterate the input symbols and use algorithm
#while(or for) there are still input symbols:
for symbol in var:
    #symbol = get input symbol
    stringandsymbol = string + symbol
    #if string + symbol is in table
    if stringandsymbol in table:
        string = stringandsymbol
    else:
        #output the code for string
        compressvar.append(table[string])
        #if table.size < MAX_TABLE_SIZE
        if(len(table) <= MAX_TABLE_SIZE):
            #add string+symbole to table
           table[stringandsymbol]= tablesize
           tablesize += 1
        string = symbol
#output the code for string
if string in table:
    compressvar.append(table[string])
print(compressvar)
#store the compressed string in output file
output = open("output1.lzw","w")
for var in compressvar:
    x = format(int(var),"016b")
    output.write(str(x))
    output.write(str('\t'))
    print(x)
output.close()
inputfile.close()
