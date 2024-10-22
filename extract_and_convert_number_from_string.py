# This script extracts the numeric portion of the string 'X-DSPAM-Confidence: 0.8475'.
# It uses the find() method to locate the position of the colon (':') in the string.
# Then, it extracts the portion of the string after the colon, converts it to a float, and prints the result.

string = 'X-DSPAM-Confidence: 0.8475'

pos = string.find(':')                 
number = string[pos + 1:]               
portion = float(number)                  
print(portion)
