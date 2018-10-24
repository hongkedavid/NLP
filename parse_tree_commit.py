import sys
import nltk
from stanfordcorenlp import StanfordCoreNLP

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_email(s):
    for ss in s.split(' '):
        if len(ss) == 0:
           continue
        if ss[0] == '<' and ss[-1] == '>' and ss.find("@") > 0:
           return True
    return False

def filter_log(s):
    return (s[0:6] == "Thanks" or s[0:5] == "Merge" or s[0:9] == "import of")

text = ''
for line in sys.stdin:
    line = line.lstrip().rstrip().strip('\n')
    if len(line) == 0 or is_ascii(line) == False or is_email(line) == True or filter_log(line) == True:
       continue
    if line[-1] != '.':
       line += '.'
    text += (' ' + line)

sent_text = nltk.sent_tokenize(text)
print len(sent_text)

fil_sent = []
for sentence in sent_text:
   nlp = StanfordCoreNLP('/z/david/stanford-corenlp-full-2018-10-05')
   str = nlp.parse(sentence)
   if str.find("VBZ") > 0 or str.find("DT") > 0:
      print sentence
      fil_sent.append(sentence)
   nlp.close()

print len(fil_sent)
