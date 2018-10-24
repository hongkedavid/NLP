import sys
import nltk
from stanfordcorenlp import StanfordCoreNLP

text = ''
for line in sys.stdin:
    line = line.strip('\n')
    if len(line) == 0:
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

