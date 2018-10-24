import sys
import nltk
import re
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
    return (s.find("[Page ") >= 0 or (s.find("RFC 1035") >= 0 and s.find("November 1987") >= 0) or s.find("^")  >= 0)

text = ''
for line in sys.stdin:
    line = line.lstrip().rstrip().strip('\n')
    if len(line) == 0 or is_ascii(line) == False or is_email(line) == True or filter_log(line) == True:
       continue
    print "paaaa: " + line, len(line)
    text += (' ' + line)

sent_text = nltk.sent_tokenize(text)

fil_sent = []
for sentence in sent_text:
   nlp = StanfordCoreNLP('/z/david/stanford-corenlp-full-2018-10-05')
   sentence = re.sub(r'[\||+|:|=|<|>|[|\]|{|}|\|/"]', '', sentence)
   sentence = sentence.replace("  ", "")
   sentence = sentence.replace("--", "")
   str = nlp.parse(sentence)
   if str.find("VBZ") > 0 or str.find("DT") > 0:
      print sentence
      fil_sent.append(sentence)
   nlp.close()
