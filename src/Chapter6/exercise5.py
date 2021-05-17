str = 'X-DSPAM-Confidence: 0.8475'

start = str.find(':')
end = len(str)

#stores the string after the colon in the variable str into the variable number 
number = str[start+1:end]

#store the string from the variable number as a floating point number in the variable fpnumber 
fpnumber = float(number)


print(number)
print(fpnumber)
