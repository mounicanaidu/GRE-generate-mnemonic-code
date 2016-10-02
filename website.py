import urllib
import re
import csv

replace_word = "http://www.mnemonicdictionary.com/?word=%REPLACEWORD%"

regex = re.compile(r'[<]i class[=]\"icon-lightbulb\"[>][<]\/i[>]\s*.*')

output = csv.writer(open("mnemonic.csv", "wb"),delimiter='\t', quoting=csv.QUOTE_NONE, quotechar='"',escapechar=' ')

with open("wordlist.txt", "r") as file:
    for line in file:
    	global flag
    	flag = 0
        url = replace_word
        word = line
        word = word.strip(" ")
        word = word.strip("\n")
        print word
        url = url.replace("%REPLACEWORD%", word)
        url = url.replace(" ","+")
        url = url.replace("'","%27")
        response = urllib.urlopen(url)
        for line01 in response:
        	if flag == 0:
        		found = regex.search(line01)
	        	if found:
	        		print "inside found"
		        	g = re.search(r'([<]i class[=]\"icon-lightbulb\"[>][<]\/i[>])(\s*)(.*)',found.group())
		        	meaning = g.group(3)
		        	meaning = meaning.strip("\t")
		        	meaning = meaning.replace('\r\n',' ')
		        	meaning = meaning.replace('\n',' ')
		        	meaning = meaning.replace('\r',' ')
		        	output.writerow([word,"-----",meaning])
		        	flag = 1