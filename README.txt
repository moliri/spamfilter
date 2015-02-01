These are the libraries I imported/installed:

import csv
import os.path
import sys
import nltk
nltk.download('punkt')
from bs4 import BeautifulSoup
from collections import OrderedDict
import numpy as num
import io

If you would like to change the SPAM and HAM directories to point to different examples, you can do that in the main function at the bottom of spellchecker.py:

if __name__ == '__main__':
	
	#change folder names here
	spam = "/spam"
	ham = "/easy_ham"
	mail = "/mail"
	dictionary = "dictionary.txt"
	priorProb = "blah"

	makedictionary(spam, ham, dictionary)
	spamsort(mail, spam, ham, dictionary, priorProb)