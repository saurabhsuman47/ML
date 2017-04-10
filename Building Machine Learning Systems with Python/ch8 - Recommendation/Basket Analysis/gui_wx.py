#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 22:51:04 2017

@author: saurabh
"""

import wx 
 
#app = wx.App() 
#window = wx.Frame(None, title = "wxPython Frame", size = (300,200)) 
#panel = wx.Panel(window) 
#label = wx.StaticText(panel, label = "Hello World", pos = (100,50)) 
#window.Show(True) 
#app.MainLoop()


#app = wx.App()
#window = wx.Frame(None, title = "DnD", size = (200,200))
#panel = wx.Panel(window)
#window.Show(True) 
#app.MainLoop()

"""  
class MyTarget(wx.TextDropTarget): 
   def __init__(self, object): 
      wx.TextDropTarget.__init__(self) 
      self.object = object  
		
   def OnDropText(self, x, y, data): 
      self.object.InsertStringItem(0, data)  
		
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (-1,300))   
      panel = wx.Panel(self) 
      box = wx.BoxSizer(wx.HORIZONTAL)  
      languages = ['C', 'C++', 'Java', 'Python', 'Perl', 'JavaScript',
         'PHP', 'VB.NET','C#']
			
      self.lst1 = wx.ListCtrl(panel, -1, style = wx.LC_LIST) 
      self.lst2 = wx.ListCtrl(panel, -1, style = wx.LC_LIST) 
      for lang in languages: 
          self.lst1.InsertStringItem(0,lang) 
             
      dt = MyTarget(self.lst2) 
      self.lst2.SetDropTarget(dt) 
      wx.EVT_LIST_BEGIN_DRAG(self, self.lst1.GetId(), self.OnDragInit)
		
      box.Add(self.lst1,0,wx.EXPAND) 
      box.Add(self.lst2, 1, wx.EXPAND) 
		
      panel.SetSizer(box) 
      panel.Fit() 
      self.Centre() 
      self.Show(True)  
     
   def OnDragInit(self, event): 
      text = self.lst1.GetItemText(event.GetIndex()) 
      tobj = wx.PyTextDataObject(text) 
      src = wx.DropSource(self.lst1) 
      src.SetData(tobj) 
      src.DoDragDrop(True) 
      self.lst1.DeleteItem(event.GetIndex()) 
		
ex = wx.App() 
Mywin(None,'Drag&Drop Demo') 
ex.MainLoop()
"""

 
########################################################################
class MyFileDropTarget(wx.FileDropTarget):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, window):
        """Constructor"""
        wx.FileDropTarget.__init__(self)
        self.window = window
 
    #----------------------------------------------------------------------
    def OnDropFiles(self, x, y, filenames):
        """
        When files are dropped, write where they were dropped and then
        the file paths themselves
        """
        
        for filepath in filenames:
            self.window.updateText(filepath + '\n')    
 
########################################################################
class DnDPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
 
        file_drop_target = MyFileDropTarget(self)
        lbl = wx.StaticText(self, label="Drag some files here:")
        self.fileTextCtrl = wx.TextCtrl(self,
                                        style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
        self.fileTextCtrl.SetDropTarget(file_drop_target)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(self.fileTextCtrl, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def SetInsertionPointEnd(self):
        """
        Put insertion point at end of text control to prevent overwriting
        """
        self.fileTextCtrl.SetInsertionPointEnd()
 
    #----------------------------------------------------------------------
    def updateText(self, text):
        """
        Write text to the text control
        """
        self.fileTextCtrl.WriteText(text)
 
########################################################################
class DnDFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="DnD Tutorial")
        self.panel = DnDPanel(self)
        self.Show()
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = DnDFrame()
    app.MainLoop()  