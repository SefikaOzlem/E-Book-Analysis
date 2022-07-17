# E-Book-Analysis

EXAMPLES OF REQUESTED OUTPUT

For this example, we will consider (Wikibooks contributors, 2020b) and (Wikibooks contributors, 2020a) e-books. To calculate their word frequencies, we will use (Online Word Counter, n.d.) website, an online service for text analysis. You can use this tool to compare your results and check their accuracy. Assume that when the user selected the e-book “Non-Programmer's Tutorial for Python 2.6”, the console output is expected to be similar to the table below (try to make your console output as orderly as possible, learn about advanced python console output and string manipulation for this purpose):

BOOK 1: Programmer's Tutorial for Python 2.6

NO WORD FREQ_1

1 print 520

2 number 268

3 program 179

4 python 158

5 +  151

6 input 141

7 list 137

8 function 131

9 menu 100

10 true 96

11 type 92

12 item 91

13 string 87

14 license 82

15 numbers 82

16 document 75

17 file 75

18 text 72

19 return 68

20 false 67

If the user selected only one e-book, this will be the end of the program. However, if the user selected two e-books, the output should be similar to the table given below:

BOOK 1: Programmer's Tutorial for Python 2.6Programmer's Tutorial for Python 2.6

BOOK 2: Programmer's Programmer's Tutorial for Python 3Tutorial for Python 3

COMMON WORDS       

NO WORD    FREQ_1     FREQ_2   FREQ_SUM

1 print     520         529      1049 

2 number    268         288      556

3 program   179         177      356

4 python    158         198      356

5 list      137         157      294


BOOK 1:Programmer's Tutorial for Python 2.6Programmer's Tutorial for Python 2.6

DISTINCT WORDS

NO  WORD      FREQ_1

1  document    75 

2   raw        66 

3  sections    31

4   title      28

5   invariant  23  

BOOK 2: Programmer's Tutorial for Python 3Programmer's Tutorial for Python 3

DISTINCT WORDS

NO  WORD      FREQ_2

1   path       11

2   python3    11

3  subprocess  10

4    click      8

5  environment  8

Assignment Definition

You are asked to design a Python program (in a single script file) to download e-books from
(Wikibooks or Wikisource) and save them to a text file. The name of the book will be taken as user
input. For this, you can use Web scraping libraries in Python to get requested books.
Assuming that you have downloaded the requested e-book from Wikibooks to a text file in
your computer (should be in the same directory as your source code, do not use full file paths like

“C:\Users\User\Desktop\…”, just use file names)

After correctly saving the e-book to a text file, your program should be able to read it and
create word frequencies of that book, meaning counting the number of times words has been used
in that e-book. During this operation, you should also remove stop words (the, a, he, she, it, etc.),
words that are meaningless by themselves but usually have the highest frequency of available words.
You are required to use Python programming language and if you wish, you can use standard Python
libraries. However, you are required to explain how you used it and what it actually does, in your
source code comments. Any tool that takes only inputs from you, without any effort on your part to
use it in Python, will not be accepted.

Another functionality you are expected to implement is the comparison of two e-books and
their word frequencies. You will calculate word frequencies of two e-books and show the sum of
frequencies of common words (words that appear on the both e-books) and show the frequencies of
distinct words (words that only appear on only one of the e-books). The format you are required to
follow with these requested outputs will be given later in this document.
Your program should ask the user, how many word frequencies they wish to see (in this
document, as you can see, 20 words per list has been shown). You can take 20 as your default number
if the user does not enter a specific number they wish to use.
Make sure that your program works on command console, rather than requiring an IDE to
work (you can still use any IDE you wish to develop your assignment but you need to run your
program on console after your development). We will evaluate your assignments by executing them
on command console, as it has been done in our lab sessions.

