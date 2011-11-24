#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class GuiMarkup(wx.Frame):

       def __init__(self, parent, title, *args, **kwargs):
            super(GuiMarkup, self).__init__(parent, title = title, size=(500, 400), *args, **kwargs)
 
            self.InitUI()
   
       def InitUI(self):
            menubar = wx.MenuBar()

            fileMenu = wx.Menu()
            editMenu = wx.Menu()
           # viewMenu = wx.Menu()
            helpMenu = wx.Menu()

           # self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar', 'Show Statusbar', kind=wx.ITEM_CHECK)
           # self.sht1 = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 'Show Toolbar', kind=wx.ITEM_CHECK)
           # viewMenu.Check(self.shst.GetId(), True)
           # viewMenu.Check(self.sht1.GetId(), True)

            fileMenu.Append(wx.ID_NEW, '&New')
            fileMenu.Append(wx.ID_OPEN, '&Open')
            fileMenu.Append(wx.ID_ANY, 'Save Input')
            fileMenu.Append(wx.ID_ANY, 'Save Output')
            fileMenu.AppendSeparator()

            qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
            fileMenu.AppendItem(qmi)

            self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
           # self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
           # self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.sht1)

            menubar.Append(fileMenu, '&File')
            menubar.Append(editMenu, '&Edit')
            menubar.Append(helpMenu, '&Help')
           # menubar.Append(viewMenu, '&View')
            self.SetMenuBar(menubar)

           # self.toolbar = self.CreateToolBar()
           # self.toolbar.AddLabelTool(1, '', wx.Bitmap('images.jpg'))
           # self.toolbar.Realize()

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
            
           # hbox1 = wx.BoxSizer(wx.HORIZONTAL)
           # st1 = wx.StaticText(panel, label='Input/Loaded text')
           # st1.SetFont(font)
           # hbox1.Add(st1, flag=wx.RIGHT|wx.RIGHT|wx.EXPAND, border=30)
           # st2 = wx.StaticText(panel, label='Converted text')
           # st2.SetFont(font)
           # hbox1.Add(st2, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=30)
           # vbox1.Add(hbox1, flag=wx.EXPAND, border=10)

           # vbox1.Add((-1, 10))

            hbox2 = wx.BoxSizer(wx.HORIZONTAL)
            tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
            hbox2.Add(tc2, proportion=1, flag=wx.RIGHT|wx.EXPAND, border=10)
            btn1 = wx.Button(panel, label='Convert into -->', size=(30, 30))
            hbox2.Add(btn1, proportion=1, flag=wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER, border=5)
            tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
            hbox2.Add(tc3, proportion=1, flag=wx.LEFT|wx.EXPAND, border=10)
            vbox1.Add(hbox2, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM|wx.EXPAND, border = 10)
           
           # vbox1.Add((-1, 10)) 
            
                        

            panel.SetSizer(vbox1)

           # vbox2 = wx.BoxSizer(wx.VERTICAL)

           # hbox3 = wx.BoxSizer(wx.HORIZONTAL)
           # st3 = wx.StaticText(panel, label='Converted text')
           # st3.SetFont(font)
           # hbox3.Add(st3, flag=wx.ALIGN_RIGHT, border=8)
           # vbox2.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

           # vbox2.Add((-1, 10))
             
           # hbox4 = wx.BoxSizer(wx.HORIZONTAL)
           # tc4 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
           # hbox4.Add(tc4, proportion=1, flag=wx.EXPAND)
           # vbox2.Add(hbox4, proportion=1, flag=wx.RIGHT|wx.BOTTOM|wx.TOP, border = 10)
#
           # vbox2.Add((-1, 10))

           # panel.SetSizer(vbox2)
            

            
#            hbox3 = wx.BoxSizer(wx.HORIZONTAL)
#            st3 = wx.StaticText(panel, label='Converted text')
#            st3.SetFont(font)
#            hbox3.Add(st3, flag=wx.RIGHT, border=8)
#            vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

#            vbox.Add((-1, 10))

#            panel.SetBackgroundColour('#4f5049')
#            vbox = wx.BoxSizer(wx.VERTICAL)

#            midPan = wx.Panel(panel)
#            midPan.SetBackgroundColour('#ededed')

#            vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
       
#            wx.TextCtrl(panel)

#       def ToggleStatusBar(self, e):
        
#             if self.shst.IsChecked():
#                 self.statusbar.Show()
#             else:
#                 self.statusbar.Hide()

#       def ToggleToolBar(self, e):

#             if self.sht1.IsChecked():
#                 self.toolbar.Show()
#             else:
#                 self.toolbar.Hide()
        
       def OnQuit(self, e):
         self.Close()

def main():
    ex = wx.App()
    GuiMarkup(None, title ='Border')
    ex.MainLoop()

if __name__ == '__main__':
    main()

