#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import re
import os
from state_parser import MarkUp

class GuiMarkup(wx.Frame):

       def __init__(self, parent=None, id=-1, title='MyGUI', size=(1000, 500)):
            super(GuiMarkup, self).__init__(parent, id, title, size=size)
 
            self.InitUI()
   
       def InitUI(self):
            #creating menubar
            menubar = wx.MenuBar()
            
            #creating menus to append to menubar
            fileMenu = wx.Menu()
            editMenu = wx.Menu()
            helpMenu = wx.Menu()

            fileMenu.Append(wx.ID_NEW, '&New', 'New file')
            
            #creating menuitems, appending them to their own menus and binding events. Event-functions are definied below.
            #working on fileMenu
            opn = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Open', 'Open stored file')
            fileMenu.AppendItem(opn)
            self.Bind(wx.EVT_MENU, self.OpenFile, opn)

            svou = wx.MenuItem(fileMenu, wx.ID_ANY, 'Save Output', 'Save converted text')
            fileMenu.AppendItem(svou)
            self.Bind(wx.EVT_MENU, self.Saveoutput, svou)

            svin = wx.MenuItem(fileMenu, wx.ID_ANY, 'Save Input', 'Save handtyped text or loaded file')
            fileMenu.AppendItem(svin)
            self.Bind(wx.EVT_MENU, self.Saveoutput, svin)
            
            fileMenu.AppendSeparator()

            qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
            fileMenu.AppendItem(qmi)
            self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

            menubar.Append(fileMenu, '&File')

            #working on editMenu
            cut = wx.MenuItem(editMenu, wx.ID_CUT, '&Cut', 'Deletes selected text')
            editMenu.AppendItem(cut)
 
            copy = wx.MenuItem(editMenu, wx.ID_COPY, 'C&opy', 'Copy selected text')
            editMenu.AppendItem(copy)

            paste = wx.MenuItem(editMenu, wx.ID_PASTE, '&Paste', 'Paste selected text')
            editMenu.AppendItem(paste)
      
            editMenu.AppendSeparator()

            select = wx.MenuItem(editMenu, wx.ID_SELECTALL, '&Select All', 'Select whole text')
            editMenu.AppendItem(select)
            
            menubar.Append(editMenu, '&Edit')

            #working on helpMenu
            about = wx.MenuItem(helpMenu, wx.ID_ABOUT, '&About', 'General info about the program')
            helpMenu.AppendItem(about)
            self.Bind(wx.EVT_MENU, self.OnAbout, about)           

            manual = wx.MenuItem(helpMenu, wx.ID_ANY, '&Little Manual...', 'Important editing rules')
            helpMenu.AppendItem(manual)
            self.Bind(wx.EVT_MENU, self.OnManual, manual)

            menubar.Append(helpMenu, '&Help')

            #setting menubar
            self.SetMenuBar(menubar)

            #setting statusbar
            self.statusbar = self.CreateStatusBar()
            self.statusbar.SetStatusText('Ready')
            
            self.SetTitle('MarkParser (OpenSource Editor/Converter)')
            self.Centre()
            self.Show(True)
 
            #setting font
            font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
            font.SetPointSize(11)

            #setting layout
            background = wx.BoxSizer(wx.HORIZONTAL)
            central = wx.BoxSizer(wx.VERTICAL)

            self.inp = wx.TextCtrl(self, style=wx.TE_MULTILINE)
            self.out = wx.TextCtrl(self, style=wx.TE_MULTILINE)

            languages = ['Convert into HTML', 'Convert into LaTex']
            self.combo = wx.ComboBox(self, -1, value='Convert into', choices=languages, style=wx.CB_DROPDOWN)
            self.Bind(wx.EVT_BUTTON, self.OnSelect, self.combo)

            self.button = wx.Button(self, -1, label='Convert -->')
            self.Bind(wx.EVT_BUTTON, self.Convert, self.button)

            central.Add(self.combo, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
            central.Add(self.button, proportion=2, flag=wx.ALL|wx.EXPAND, border=10)

            background.Add(self.inp, proportion=3, flag=wx.ALL|wx.EXPAND, border=10)
            background.Add(central, proportion=1, flag=wx.ALIGN_CENTER)
            background.Add(self.out, proportion=3, flag=wx.ALL|wx.EXPAND, border=10)

            self.SetSizer(background)

       def OnAbout(self, e):
        """Creates an About window in which the most important
           info about the program are dispayed
        """
        about = wx.AboutDialogInfo()

        about.SetDescription('This program manages a plain text and returns\n'+
                              'a marked-up one, implementing specific rules\n'+
                              'of the programming language chosen by the user.')
        about.SetDevelopers(['Francesco Pochetti'])
        about.SetName('MarkParser')

        wx.AboutBox(about)        

       def OnManual(self, e):
         """Creates a window with a static text in which
            some important editing rules are explained. A brief manual.
         """
         wx.MessageBox('FIRST DRAFT STILL TO BE WRITTEN', 'Editing Rules', 
            wx.OK | wx.ICON_INFORMATION)

       def Saveoutput(self, e):
         """Let's the user save files (input or output ones); it displays a pop window which let
            the user browse the file-system and choose a directory and a filename.
         """
         browse = wx.FileDialog(self, defaultDir=os.getcwd(), defaultFile="", style=wx.SAVE|wx.FD_OVERWRITE_PROMPT)
         if browse.ShowModal() == wx.ID_OK:
           filename = browse.GetFilename()
           self.out.SaveFile(filename)
  
       def OpenFile(self, e):
         """Let's the user open files; it displays a pop window which let
            the user browse the file-system and choose a directory and a filename in order to select and open it.
         """
         browse = wx.FileDialog(self, message='Open a plain text', defaultDir=os.getcwd(), defaultFile="", style=wx.OPEN)
         if browse.ShowModal() == wx.ID_OK:
           self.filename = browse.GetPath()
           self.inp.LoadFile(self.filename) 

       def OnSelect(self, e):
         """Manages item selection in combobox.
         """
         item = e.GetSelection()

       def Convert(self, e):
         """Calls the MarkUp class. This class has been modified in order to take a filename
            and return the markedup text.
         """
         to_convert = MarkUp(self.filename)
         html = to_convert.translate()
         self.out.AppendText(html)
        # self.match = re.search(r'([\w]+)\.', self.filename)
        # self.out.LoadFile(self.match.group(1)+'.html')

        
       def OnQuit(self, e):
          """Creates a quit window which bothers the user asking to
             confirm to quitting the program.
          """
          dial = wx.MessageDialog(None, 'Are you sure to quit?', 'OpenSource Editor/Converter',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
          ret = dial.ShowModal()
          if ret == wx.ID_YES:
            self.Destroy()
          else:
            e.Veto()

def main():
    ex = wx.App()
    GuiMarkup(None, title ='Border')
    ex.MainLoop()

if __name__ == '__main__':
    main()

