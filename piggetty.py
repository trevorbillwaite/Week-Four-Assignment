__author__ = 'trevorbillwaite'

# Week Four Assignment
# Introduction to Computer Science
# piggetty.py
# correlation with Nicole Ignasiak and Rebekah Orth 


# Define a function called piggy(string) that returns a string
vowels = "AEIOUaeiou"
def piggy(word):
	n=0
	endword=""
	for letter in word:
		# Is letter a vowel?
		if letter in vowels:
			if n==0:
				# true? done.
				pig = word + "yay"
				return pig
			else:
				# false. consonant.
				pig = word[n:] + endword + "ay"
				return pig
		else:
			endword = endword + word[n]
			n = n + 1

# Open the file *getty.txt* for reading.  
inFile = open("getty.txt" , "r")

# Open a new file *piggy.txt* for writing.  
outFile = open("piggy.txt" , "w")

# Read the getty.txt file into a string.  
addressString = inFile.read()

# Strip out bad characters (, - .). 
addressString = addressString.replace ("." , "")
addressString = addressString.replace ("," , "")	
addressString = addressString.replace ("-" , "")

# Split the string into a list of words.  
addressList = addressString.split()

# Create a new empty string.  
piggyString = ""

# Loop through the list of words, pigifying each one.  
for word in addressList:

# Add the pigified word (and a space) to the new string.  
	if len(word) > 0:
		piggyString = piggyString + str(piggy(word)) + " "

# Write the new string to piggy.txt.  

outFile.write(piggyString)

# close the files.
inFile.close()
outFile.close()

