import bs4 as bs
import urllib.request
import os
import re
import nltk
import requests
from bs4 import BeautifulSoup
from requests.utils import requote_uri

stopwords_list=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the","`","th","st","nd","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z","w"]  
punc2 = '''!¡|←↑→1234567890'\"'>>>`//\\[\\]=()-[]{};:'"\, <>./?¿‽¬@#¶$§%^&*_~°•’'\‘’“”'''
mystring_file=''     #string holding the content of the first book in file read operations
mystring_files=''    #In case of two books, the content of the second book is kept in the file reading process.
listw = []           #List of pure words after reading the file, free of punctuations and stop words
dicti={}             #a dictionary that keeps the word and frequency of the book in case of a single book.
listws = []          #When there are two books, our second list that keeps the pure words of the second book free of puntuation and stop words.
dicti_one={}         #When there are two books, a dictionary that holds the words and frequencies of the first book.
dicti_two={}         #When there are two books, a dictionary that holds the words and frequencies of the second book.
total={}             #When there are two books, the dictionary holding the common words of the first book and the second book and their value sum frequency
dicti1={}            #When there are two books, the dictionary that holds words and their frequencies that are in the first book that are not in the second
dict2={}             #when there are two books, a dictionary that keeps the words and frequencies of those in the second book but not in the first
temp_bookname1=''    #name of the first book
temp_bookname2=''    #name of the second book
selection=0          #the choice of action the user wants to do
def main():  #The main function that calls the necessary functions according to the user's choice, which gives information about the operations that can be done on the screen.
    print("Press the 1 key for only one book entry")
    print("Press the 2 key for two books entry")
    selection=int(input("Press 1 or 2 depending on what you want to do : "))
    if selection==1:  #if the user selects a single book,
        temp_bookname1=input("Enter a book name : " )
        readfile(temp_bookname1,mystring_file,listw)  
        oprt(temp_bookname1,listw,dicti)              
    elif selection==2: # if the user selects two books 
        temp_bookname1=input("Enter first book name : " )
        readfile(temp_bookname1,mystring_file,listw)
        temp_bookname2=input("Enter second book name : " )
        readfile(temp_bookname2,mystring_files,listws)     
        limit=int(input("how many word frequencies they wish to see? ") or 20) #It asks how many data will be available to the user. 
        common(limit,temp_bookname1,temp_bookname2,listw,listws,dicti_one,dicti_two) 
        distincts(limit,temp_bookname1,temp_bookname2,listw,listws,dicti1,dict2)     
        
def readfile(book_name,mystring_file,listw):   #The function that pulls data according to the url of the book, writes the received data to the text document and then reads.
    for i in book_name:
        if '#' in i:      #if there is a # in the book and if there is, I perform the replacement process.
            book_name=book_name.replace("#","_Sharp_").strip()    
    liste=''     #string variable holding embedded links of the entered book
    url=''       #string holding the URL of the link to the original processing of the book(with printable version)
    temp_url="https://en.wikibooks.org/wiki/"+book_name  #The string holding the url of the main page of the book taken from the user
    r = requests.get(temp_url)
    soup=BeautifulSoup(r.content,"html.parser")     #split the html tags in the source code of the page according to the url received.
    for college in soup.findAll('p'):
        for a in college.find_all('a'):
            liste=str((a.get('href')))   #I found the property belonging to 'href' under the '<p>' and '<a href:link>' tags and reached some embedded links and dropped each link to the list string variable.
            #print(liste)
            if '/wiki/' in liste: #If there is a link with /wiki/ on the link I get it
                wik=liste         # If there is a link with a wiki, it is checked if there is a link with a print version or a printable version.
                if "/print_version" in wik:
                    temp_url="https://en.wikibooks.org/"+wik
                elif "/Print_version" in wik:
                    temp_url="https://en.wikibooks.org/"+wik
                elif "/Print_Version" in wik:
                    temp_url="https://en.wikibooks.org/"+wik
                elif "/print_Version" in wik:
                    temp_url="https://en.wikibooks.org/"+wik
                elif "Printable_version" in wik:
                    temp_url="https://en.wikibooks.org/"+wik
                elif "Printable_Version" in wik:
                    temp_url="https://en.wikibooks.org/"+wik
                elif "printable_Version" in wik:
                    temp_url="https://en.wikibooks.org/"+wik
                elif "printable_version" in wik:
                    temp_url="https://en.wikibooks.org/"+wik
    url=temp_url # I throw the extension of the link containing print or printable version to the main url variable to do all the rest.
    #print(url)

    try:
        sauce=urllib.request.urlopen(requote_uri(url)).read()
        soup=bs.BeautifulSoup(sauce,"lxml")
        new_soup=bs.BeautifulSoup((str(soup)),"lxml")
        #print(str(new_soup.get_text()))
        mystring=str(new_soup.get_text())
        mystring=mystring.strip()
        result1 = int((str(mystring)).find("Jump to search")) # Index find process is in progress. To get the contents of the next string from the found index.
        result = int((str(mystring)).find('Retrieved from "https://en.wikibooks.org/w/')) #Finding the index. This index is our limit index.
        mystring=mystring[result1:result] #The contents of the string between the two indexes found are synchronized to my string.
        mystring=mystring.replace("Jump to search","")
        mystring=mystring.strip()
        f = open(book_name+".txt", "w", encoding='utf8') 
        f.write(str(mystring))  #prints the resulting last string to the text document.
        f.close()
        with open(book_name+".txt", 'r', encoding='utf-8') as inFile,open(book_name+'outfile.txt', 'w', encoding='utf-8') as outFile:
            for line in inFile:    # text document is read line by line, line is put into a new string(mystring_file)
                if not line in '\t' or not line in '\n':
                    if line.strip():
                        outFile.write(line) #When reading line by line, the blank line is deleted and a new text document('book_name+'outfile.txt') is printed for a smoother text document.
                        mystring_file+=line
        
        f.close()
        mystring_file = re.sub(' +',' ',mystring_file) #I replace variable spaces with only one character space.
        
        for ele in mystring_file:
            if ele in punc2: #If there are punctuation marks, they are replaced by the single space character.
                mystring_file=mystring_file.replace(ele," ")
        mystring_file = re.sub(' +',' ',mystring_file) # If extra spaces occur, they are replaced with a single space character again.
        mystring_file=mystring_file.lower()
        #print(mystring_file)        
        for b in mystring_file.split():  # string parsing into space.
            if not b in stopwords_list : #If the word resulting from shredding is not a stop word, it is added to the listw list.
                
                listw.append(b)
        
    except urllib.error.URLError:
        print("Due to the problem with the url of the book you entered, we cannot continue the process.")
        
def oprt(book_name,listw,dicti): #the function by which the frequencies of the words of the book are calculated and sorted.
    limit=int(input("how many word frequencies they wish to see? ") or 20)
    print('BOOK 1: ',book_name)
    print("-------------------------------------------------------------")
    print ('| %-17s | %-17s | %-17s |' % ('NO', 'WORD', 'FREQUENCY'))
    for k in listw:  # I scroll through the list of words and put the words into the dictionary with their frequencies.
        if k in dicti:
            dicti[k]+=1
        else:
            dicti[k]=1  
    time=1
    length=len(dicti)
    while time!=(limit+1):
        if time==length+1:
            break
        max=0
        for i in dicti.values(): # The dictionary is sorted by looking at the values ​​of the words.
            if max<i:
                max=i
        key=''
        for k,v in dicti.items():#The word that the obtained max value belongs to is checked.
            if v==max:
                key=k         
                print ('| %-17d | %-17s | %-17d |' % (time, key,max))         
                break
        del dicti[key]
        time+=1
    print("-------------------------------------------------------------")  

def common(limit,book_name1,book_name2,listw,listws,dicti_one,dicti_two): #The function that calculates the common word and total frequency of two books and then sorts.
    print("BOOK 1: ",book_name1)
    print("BOOK 2: ",book_name2)
    print("COMMON WORDS")
    print("-----------------------------------------------------------------------------------------------------")
    print ('| %-17s | %-17s | %-17s | %-17s | %-17s |' % ('NO', 'WORD', 'FREQ_1','FREQ_2','FREQ_SUM'))
    for k in listw:
        if k in dicti_one:
            dicti_one[k]+=1
        else:
            dicti_one[k]=1
    for k in listws:
        if k in dicti_two:
            dicti_two[k]+=1
        else:
            dicti_two[k]=1
    
    for k,v in dicti_one.items():  #If there are words in both books, I put them in the dictionary named 'total' with frequency sums.
        for x,y in dicti_two.items():
            if k==x:
                total[k]=v+y
                
    time=1
    length=len(total)
    while time!=(limit+1):
        if time==length+1:
            break
        max=0
        for i in total.values(): #The values ​​of the created total dictionary are listed in descending order.
           if max<i:
                max=i
        key=' '
        for k,v in total.items():
             if v==max:
                key=k
                print('| %-17d | %-17s | %-17d | %-17d | %-17d |' %(time,key,dicti_one.get(key),dicti_two.get(key),max,))
                break
        del total[key]
        time += 1 
    print("-----------------------------------------------------------------------------------------------------")        
    
def distincts(limit,book_name1,book_name2,listw,listws,dict1,dict2): #sorting functions that calculate the frequencies of the words in which the books are different.
    
    for k in listw:
        if k in dicti1:
            dicti1[k]+=1
        else:
            dicti1[k]=1
            
    for k in listws:
        if k in dict2:
            dict2[k]+=1
        else:
            dict2[k]=1

    dictinct1={} #dictionary that holds the distincts words of the first book.
    for key in dict1.keys(): 
        if not key in dict2: #words in the first book but not in the second book
            dictinct1[key]=dicti1.get(key)
            
    print("BOOK 1: ",book_name1)
    print("DISTINCT WORDS")
    print("-------------------------------------------------------------")
    print ('| %-17s | %-17s | %-17s |' % ('NO', 'WORD', 'FREQ_1'))
    time=1
    length=len(dictinct1)
    while time!=(limit+1):
        if time==length+1:
            break
        max=0
        for i in dictinct1.values(): #The values ​​of the created distinct1 dictionary are listed in descending order
            if max<i:
                max=i 
        key=' '
        for k,v in dictinct1.items():
            if v==max:
                key=k
                print('| %-17d | %-17s | %-17d |' % (time, key,max))
                break
        del dictinct1[key]
        time+=1
    print("-------------------------------------------------------------")
    
    dictinct2={} #dictionary that holds the distincts words of the second book.
    for key in dict2.keys(): 
        if not key in dict1: #words in the second book but not in the first book
            dictinct2[key]=dict2.get(key)
    
    print("BOOK 2: ",book_name2)
    print("DISTINCT WORDS")
    print("-------------------------------------------------------------")
    print ('| %-17s | %-17s | %-17s |' % ('NO', 'WORD', 'FREQ_2'))
    time=1
    length=len(dictinct2)
    while time!=(limit+1):
        if time==length+1:
            break
        max=0
        for i in dictinct2.values(): #The values ​​of the created distinct1 dictionary are listed in descending order
            if max<i:
                max=i
        key=' '
        for k,v in dictinct2.items():
            if v==max:
                key=k
                print('| %-17d | %-17s | %-17d |' % (time, key,max))
                break
        del dictinct2[key]
        time+=1
    print("-------------------------------------------------------------")
main()


