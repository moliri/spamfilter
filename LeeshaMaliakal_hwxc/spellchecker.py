import csv
import os.path
import sys
import nltk
nltk.download('punkt')
from bs4 import BeautifulSoup
from collections import OrderedDict
import numpy as num
import io

# makedictionary
# build a dictionary of words from a set of spam and ham files, including probability of the occurence of each word
#
# spam_directory - a character string containing the path to the directory containing ONLY spam files.  Every file in directory should be an ASCII text file that is spam
# ham_directory - a character string containing the path to the directory containing ONLY ham files.  Every file in directory should be an ASCII text file that is ham
# dictionary_filename - save results of dictionary to this file, which should be located in the CURRENT directory
#
# for each word in the dictionary, determine the probability of observing that word in a spam document and the probability of observing it in a ham document:
# [word] [P(word|spam)] [P(word|ham)]
# calculate the probability as follows:
# (# of documents containing the word / total # of documents)
def makedictionary( spam_directory, ham_directory, dictionary_filename):
	print "makedictionary: Implement me! "
	dictionary = {}

	spamFiles = os.listdir(os.getcwd()+spam_directory)
	hamFiles = os.listdir(os.getcwd()+ham_directory)
	spamCount = 0.1
	hamCount = 0.1

	#iterate through files in the SPAM directory
	for filename in spamFiles[1:]:
		isSpam = 1
		spamCount += 1
		openFile = open(os.getcwd()+spam_directory+'/'+filename, "r") #open each file
		fileString = openFile.read() #turn contents into a string
		soup = BeautifulSoup(fileString) #clean up string with BeautifulSoup
		removedHTML = soup.get_text()
		tokenizedSoup = nltk.word_tokenize(removedHTML) #tokenize string
		removedDupTokens = set(tokenizedSoup) #filter out duplicate tokens

		#add tokens to dictionary
		dictionary = addToDictionary(removedDupTokens, dictionary, isSpam, spamCount, hamCount)

	#iterate through files in the HAM directory
	for filename in hamFiles[1:]:
		isSpam = 0
		hamCount += 1
		openFile = open(os.getcwd()+ham_directory+'/'+filename, "r") #open each file
		fileString = openFile.read() #turn contents into a string
		soup = BeautifulSoup(fileString) #clean up string with BeautifulSoup
		removedHTML = soup.get_text()
		tokenizedSoup = nltk.word_tokenize(removedHTML) #tokenize string
		removedDupTokens = set(tokenizedSoup) #filter out duplicate tokens
		
		#add tokens to dictionary
		dictionary = addToDictionary(removedDupTokens, dictionary, isSpam, spamCount, hamCount)

	#sort and output dictionary
	with io.open(dictionary_filename, "w", encoding='utf8') as text_file:
		for key, val in sorted(dictionary.items()):
			probabilities = dictionary.get(key)
			text_file.write(u"{0} {1} {2}".format(key, probabilities[0], probabilities[1]))
			text_file.write(unicode("\n"))

	#print dictionary
		

# addToDictionary
# adds a list of tokens to the dictionary and calculates probabilities
def addToDictionary(tokens, dictionary, isSpam, totalSpamCount, totalHamCount):
	#if spam document 
		#for each token
			#if in dictionary
				#increment spam frequency of token
				#update token's p(spam)
			#else 
				#add token to dictionary - [token, (spam freq/spam count), (ham freq/ham count)]
	#repeat for if ham document
	

	if isSpam == 1:
		print "I AM SPAM"
		for token in tokens:

			if (token in dictionary) == True:
				#get current SpamFrequency
				probabilities = dictionary.get(token)
				currentTokenFrequency = (totalSpamCount-1)*probabilities[0] 
				#increase SpamFrequency
				currentTokenFrequency += 1
				#update dictionary values
				#dictionary[token] = [tokenSpamFrequency/totalSpamCount, tokenHamFrequency/totalHamCount]
				dictionary[token] = [currentTokenFrequency/totalSpamCount, probabilities[1]]
				print "UPDATED DICTIONARY"

			else:
				tokenHamFrequency = 0
				tokenSpamFrequency = 0
				tokenSpamFrequency += 1
				dictionary[token] = [tokenSpamFrequency/totalSpamCount, 0]
				print "ADDED TO DICTIONARY"
				
	else: 
		print "I AM HAM"
		for token in tokens:

			if (token in dictionary) == True:
				#get current HamFrequency
				probabilities = dictionary.get(token)
				currentTokenFrequency = (totalHamCount-1)*probabilities[1] 
				#increase HamFrequency
				currentTokenFrequency += 1
				#update dictionary values
				#dictionary[token] = [tokenSpamFrequency/totalSpamCount, tokenHamFrequency/totalHamCount]
				dictionary[token] = [probabilities[0], currentTokenFrequency/totalHamCount]
				print "UPDATED DICTIONARY"
			else:
				tokenSpamFrequency = 0
				tokenHamFrequency = 0
				tokenHamFrequency += 1
				dictionary[token] = [0, tokenHamFrequency/totalHamCount]
				print "ADDED TO DICTIONARY"
				

	return dictionary

# spamsort
# classifies each document in a directory containing ASCII text documents as either spam or ham
#
# mail_directory - specifies the path to a directory where every file is an ASCII text file to be classified as spam or not
# spam_directory - a character string containing the path to the directory containing ONLY spam files.  Every file in directory should be an ASCII text file that is spam
# ham_directory - a character string containing the path to the directory containing ONLY ham files.  Every file in directory should be an ASCII text file that is ham
# dictionary_filename - save results of dictionary to this file, which should be located in the CURRENT directory
#spam_prior_probability - specifies the base probability that any given document is spam
#
#classify each document in the mail directory as spam/ham.  Then, move it to spam_directory if it is spam and the ham_directory if it is ham.  At the end, mail_directory should be empty

def spamsort( mail_directory, spam_directory, ham_directory, dictionary_filename, spam_prior_probability):
	print "spamsort: Check spellchecker.py for commented pseudocode! "
	#for each document in ham and spam
		#and for each token in that document
			#pSpam *= P(token|spam)
			#pHam *= P(token|ham)
		#for each token not in the document but in the dictionary
			#pSpam *= [1-P(token|spam)]
			#pHam *= [1-P(token|ham)]
		#spamScore = ceiling(log(pSpam))
		#hamScore = ceiling(log(pHam))
			#if spamScore >= hamScore
				#move document to spam directory
			#if hamScore >= spamScore
				#move document to ham directory

if __name__ == '__main__':
	#change folder names here
	spam = "/spam"
	ham = "/easy_ham"
	mail = "/mail"
	dictionary = "dictionary.txt"
	priorProb = "blah"

	makedictionary(spam, ham, dictionary)
	spamsort(mail, spam, ham, dictionary, priorProb)
