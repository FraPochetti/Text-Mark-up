#!/usr/bin/python -tt
# -*- coding: latin-1 -*-

#VERY IMPORTANT!!!! This program works properly ONLY IF the plain text given ENDS WITH AN EMPTY LINE!!!!!!!! 

import sys
import re

class MarkUp:
 
   def __init__(self,filename):
     self.text = open(filename, 'rU').readlines()
     self.html = '' 

   def markparser(self):
   
     status = 'START'

     for line in self.text:

      match = re.search(r'\s+\d+\)', line)

      if status == 'START':
        if line != '\n':
          self.html +=  '<h1>' + line[:-1] + '</h1>\n'
          status = 'READING'
     
      elif status == 'READING':
        if line == '\n':
           pass
        elif match:
           ordered = [line]
           status = 'OLIST' 
        elif line.startswith(' -'):
           unordered = [line]
           status = 'ULIST'
        else:
           paragraph = [line]
           status = 'FIRST_LINE'
     
      elif status == 'ULIST':
        if line.startswith(' -'):
           unordered.append(line)
           status = 'ULIST'
        elif line!= '\n':
           paragraph = [line]
           self.html += '<ul>\n%s</ul>\n' % ''.join('<li>%s</li>\n' % line[2:-1] for line in unordered)
           status = 'FIRST_LINE'
 
      elif status == 'OLIST':
        if match:
           ordered.append(line)
           status = 'OLIST'
        elif line != '\n':
           paragraph = [line]
           self.html += '<ol>\n%s</ol>\n' % ''.join('<li>%s</li>\n' % line[3:-1] for line in ordered)
           status = 'FIRST_LINE'

      elif status == 'FIRST_LINE':
        if line == '\n':
           self.html += '<h2>%s</h2>\n' % paragraph[0][:-1]
           status = 'READING'
        elif not line.startswith(' -'):
           paragraph.append(line)
           status = 'PARAGRAPH'
    
      elif status == 'PARAGRAPH':
        if line == '\n':
           self.html += '<p>%s</p>\n' % ''.join('%s\n' % line[:-1] for line in paragraph)
           status = 'READING'
        elif not line.startswith(' -'):
           paragraph.append(line)
           status = 'PARAGRAPH'
           
     self.html = re.sub(r'(\d+-\d+)', r'<em>\1</em>', self.html)
     self.html = re.sub(r'([\w\-\._]+@[\w\-\._]+)', r'<u>\1</u>', self.html)
     self.html = '<body><html>\n' + self.html + '</body></html>'

   def translate(self): 
     self.markparser()      
     print self.html       


if __name__ == '__main__':

   file_name = sys.argv[1]
   x = MarkUp(file_name)
   x.translate()

