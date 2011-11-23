#!/usr/bin/python -tt
# -*- coding: latin-1 -*-

import sys
import re

def markup(filename):
   text = open(filename, 'rU').readlines()
   html = ''
   
   status = 'START'

   for line in text:

    match = re.search(r'\s+\d+\)', line)

    if status == 'START':
        if line != '\n':
          html +=  '<h1>' + line[:-1] + '</h1>\n'
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
        elif line != '\n':
           html += '<ul>\n%s</ul>\n' % ''.join('<li>%s</li>\n' % line[2:-1] for line in unordered)
           status = 'READING'
 
    elif status == 'OLIST':
        if match:
           ordered.append(line)
           status = 'OLIST'
        elif line != '\n':
           html += '<ol>\n%s</ol>\n' % ''.join('<li>%s</li>\n' % line[3:-1] for line in ordered)

    elif status == 'FIRST_LINE':
        if line == '\n':
           html += '<h2>%s</h2>\n' % paragraph[0][:-1]
           status = 'READING'
        elif not line.startswith(' -'):
           paragraph.append(line)
           status = 'PARAGRAPH'
    
    elif status == 'PARAGRAPH':
        if line == '\n':
           status = 'READING'
        elif not line.startswith(' -'):
           html += '<p>%s</p>\n' % ''.join('%s\n' % line[:-1] for line in paragraph)
           status = 'READING'
           
   html = re.sub(r'(\d+-\d+)', r'<em>\1</em>', html)
   html = re.sub(r'([\w\-\._]+@[\w\-\._]+)', r'<u>\1</u>', html)
   html = '<body><html>\n' + html + '</body></html>'
        
   print html       
           
           
def main():
  if len(sys.argv)==2:
     markup(sys.argv[1])
  else:
     print 'No filename specified!'


if __name__ == '__main__':
   main()
