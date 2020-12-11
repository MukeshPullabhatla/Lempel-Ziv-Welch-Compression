Author: MUKESH KUMAR PULLABHATLA
	
PROGRAMMING LANGUAGE: PYTHON 3.6
ALGORITHM: LEMPEL ZIV WELCH ALGORITHM
FILES: README.txt
	encode.txt
	decode.txt

The programming code requires input as input1.txt and bit length which can be given in command line.

Procedure to execute encoding/compressing algorithm in python:
The input1.txt is encoded/compressed using encode.py python file.
The table size is 256 which will be initialized
All the characters and values will be in <key,value> pairs which are ascii values.
The lzw algorithm is applied.
We get the compressed data.
The compressed data will be stored in .lzw format which will be of 2 bytes.
To run the program
open cmd prompt window -- go to current working directory -- 
enter---
python encode.py input1.txt "number of bits"(where i have used 12)

Procedure to execute decoding/decompressing algorithm in python:
The input file will be the output of encode.py which I have assigned as output1.lzw
The table size is same as 256 which will be initialized
The lzw algorithm decompression is applied.
We get the decompressed data in newstring object which will be stored in .txt format.
To run the program:
open cmd prompt window the same where encode.py is executed
enter--
python decode.py output1.lzw "number of bits"(where i have used 12).

You can give any input in input1.txt for example
abbbab
abcabcabcabcabcabcabc
abcdabcdabcdabcdabcdabcdabcdabcd
or any other input.
 
	