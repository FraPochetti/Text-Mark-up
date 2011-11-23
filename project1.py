#!/usr/bin/python -tt
# -*- coding: latin-1 -*-

import sys
import re

#WHAT DOES THIS PROGRAM DO? It receives a plain text, in the .txt extension, and returns a .html file (with the same name as the .txt file),
#created and saved in the same directory in which the .txt file and the .py script are stored.


#N.B.: ALL THE COMMENTS PRECEDED BY AN HASH KEY MUST BE INTENDED AS REFERRED TO THE ROWS FOLLOWING THE COMMENT ITSELF.


class MarkUp:
    
    def __init__(self,filename):
         self.text = open(filename, 'rU').readlines()


    def h1(self):
         """
         If the second text's row is blank (which also stands for: "if the first text'row is the title"), the method markups the first row 
         with <h1>. Otherwise, if the second row is not blank, passes directly to the second method (block_division), as this means that, in the 
         user's intentions, the first row could be considered as the first of a following titleless paragraph.
         """
         if self.text[1] == '\n':
            self.text[0] = '<h1>' + self.text[0] + '</h1>\n'
         else:
            pass

    def blocks_division(self,n):
         """
         The main idea is to divide the whole text in paragraphs in the following way: the text (in the __init__) is splitted into a list of strings,         in which each string corresponds to a text's line. The expected result of the method is a list of lists in which each one of them stands for         a paragraph (clearly as paragraph I mean a list of the text's lines (strings) which constitute it).
         The method starts initiating an empty list (self.list_blocks), to which the first element is appended (an empty list too!), and the i index          to 0. Then the program starts looping into the text (which, I underline being a list of lines) and, if the line is NOT blank it appends
         it the i-th element of self.list_blocks, otherwise, it skips the if statement, enters the else one, and carries out two successive actions:          adds 1 to the i index and appends an other empty list to the final list of paragraphs. IMPORTANT: it is worth to point out that the for
         statement loops from the n-th text line till the end; n may be 2 or 0 as explained in the following mark-up method.
         """
         self.list_blocks = []
         i = 0
         self.list_blocks.append([])
         for line in self.text[n:]:
             if line != '\n':
                  self.list_blocks[i].append(line)
             else:
               i += 1
               self.list_blocks.append([])
              # self.list_blocks[i] = []


    def h2(self):    
      """
      If the second text's line is blank, clearly the first one is the title and the paragraph division process must start from the third
      line (which in python is number 2, as it starts counting from 0). On the contrary, if the second row is not empty, the plain text is titleless
      and the parsing must begin from the first line (the 0-th one).
      """
      if self.text[1] == '\n':
          self.blocks_division(2)
          self.list_blocks.insert(0, [self.text[0]])
      else:
          self.blocks_division(0)
      
     #The intent is to remove empty blocks(paragraphs) from the main list. As there are problems to delete items from a list in a recursive way
     #(due to autoreindexing of the list items),the idea is to loop into the main list with the enumerate method in order to obtain the indexes
     # of empty blocks and store them in a new list named self.empty_list.     
      self.empty_list = []
      for index, block in enumerate(self.list_blocks):
              if block == []:
                  self.empty_list.append(index)

      #Deletes the first blank main list block. 
      del self.list_blocks[self.empty_list[0]] 
  
      #Due to the reindexing of the list items after an item delection (example: if I remove list[2], list[3] becomes list[2] and each item scales
      #by one unit), I cannot delete list elements in a recursive way. So, it is necessary to loop into the list subctracting one unit to the index
      #each time the program enters the for statement.   
      for int in self.empty_list[1:]:
          int -= 1
          del self.list_blocks[int]       

      #Marks up paragraphs titles; in order to understand which blocks are to be intended as paragraphs titles, I implemented the following 3 
      #conditions: the block MUST NOT contain a single line (which means that it is not a paragraph but a title or something like that), the second 
      #"letter" of the string (remember that a block is a list of text lines, which are strings) MUST NOT be a minus ('-'), which is the condition
      #for the line to be an element of an unordered list, and finally it MUST NOT have been previously marked up by other stuff (which means that
      #it mustn't begin with a <). If these three conditions are SIMULTANEOUSLY respected, it means that the line CAN ONLY be a paragraph title.    
      for block in self.list_blocks:
             if len(block) == 1 and block[0][1] != '-' and block[0][0] != '<':
                 block[0] = '<h2>' + block[0] + '</h2>\n'
         
    def par(self):
          """
          If the lenght of the block (which is a paragraph) is more than one, this method considers it a paragraph (and not a title,
          an element of a 'ul' or a 'ol', ecc..) and marks up the first element of the block (which is very important to remember being a list)
          with <p> and the last with </p>.
          """
          for block in self.list_blocks:
              if len(block) != 1:
                 block[0] = '<p>' + block[0]
                 block[-1] = block[-1] + '</p>\n'   
          

    def mail(self):
          for block in self.list_blocks:
               for i in range(len(block)):
                    block[i] = re.sub(r'([\w\-\._]+@[\w\-\._]+)', r'<u>\1</u>', block[i])
                    

    def number(self): 
          for block in self.list_blocks:
               for i in range(len(block)):
                   block[i] = re.sub(r'(\d+-\d+)', r'<em>\1</em>', block[i])


    def listing(self):                   
          for block in self.list_blocks:
               if block[0][1] == '-':
                    block[0] = '<ul>' + block[0] + '</ul>\n'        


    def wrap(self):
          self.list_blocks.insert(0, ['<html><body>\n'])
          self.list_blocks.append(['\n</html></body>'])
         

    def translate(self,filename):
         """
         Calls all the other methods definied before and then open and writes a new file (named filename.html) printing all the lines of the
         marked-up plain text.
         """
         self.h1()
         self.h2()
         self.par()
         self.mail()
         self.number()
         self.listing()
         self.wrap()

         self.match = re.search(r'([\w]+)\.', filename)

         self.f = open(self.match.group(1)+'.html', 'w')         

         for block in self.list_blocks:
           for line in block:
               self.f.write(line)


if __name__ == '__main__':

    file_name = 'test_input.txt'
    x = MarkUp(file_name)
    x.translate(file_name)

