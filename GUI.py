#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class GuiMarkup(wx.Frame):

       def __init__(self, parent, title, *args, **kwargs):
            super(GuiMarkup, self).__init__(parent, title = title, *args, **kwargs)
 
            self.InitUI()
   
       def InitUI(self):
            menubar = wx.MenuBar()

            fileMenu = wx.Menu()
            editMenu = wx.Menu()
            helpMenu = wx.Menu()

            fileMenu.Append(wx.ID_NEW, '&New', 'New file')
            fileMenu.Append(wx.ID_OPEN, '&Open', 'Open stored file')
            fileMenu.Append(wx.ID_ANY, 'Save Input', 'Save handtyped text')
            fileMenu.Append(wx.ID_ANY, 'Save Output', 'Save converted text')
            fileMenu.AppendSeparator()

            qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
            fileMenu.AppendItem(qmi)

            self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

            menubar.Append(fileMenu, '&File')
            menubar.Append(editMenu, '&Edit')
            menubar.Append(helpMenu, '&Help')
            self.SetMenuBar(menubar)

            self.statusbar = self.CreateStatusBar()
            self.statusbar.SetStatusText('Ready')
            
            self.SetSize((500, 500))
            self.SetTitle('OpenSource Editor/Converter')
            self.Centre()
            self.Show(True)

            panel = wx.Panel(self)
 
            font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
            font.SetPointSize(11)

            vbox1 = wx.BoxSizer(wx.VERTICAL)

            hbox2 = wx.BoxSizer(wx.HORIZONTAL)
            tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, name='Input/Loaded text')
            hbox2.Add(tc2, proportion=1, flag=wx.RIGHT|wx.EXPAND, border=10)

            languages = ['Convert into HTML', 'Convert into LaTex']
            cmb1 = wx.ComboBox(panel, -1, value='Convert into', size=wx.DefaultSize, choices=languages, style=wx.CB_DROPDOWN)
            self.Bind(wx.EVT_BUTTON, self.OnSelect, cmb1)
            hbox2.Add(cmb1, flag=wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER, border=5)

            tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, name='Marked-up text')
            hbox2.Add(tc3, proportion=1, flag=wx.LEFT|wx.EXPAND, border=10)

            vbox1.Add(hbox2, proportion=1, flag=wx.ALL|wx.EXPAND, border = 10)
            
            panel.SetSizer(vbox1)

       def OnSelect(self, e):
         item = event.GetSelection()
        
       def OnQuit(self, e):
         self.Close()

def main():
    ex = wx.App()
    GuiMarkup(None, title ='Border')
    ex.MainLoop()

if __name__ == '__main__':
    main()

