# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:19:03 2017

@author: saurabh.s1
"""
import wx

########################################################################
class MyFileDropTarget(wx.FileDropTarget):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, window):
        """Constructor"""
        wx.FileDropTarget.__init__(self)
        self.window = window
 
    def OnDropFiles(self, x, y, filenames):
        """When files are dropped, updates file paths on the text control"""
        self.window.SetInsertionPointEnd()
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
        self.fileTextCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.VSCROLL|wx.TE_READONLY)
        """Associates a drop target with this window.  If the window already has a drop target, it is deleted."""
        self.fileTextCtrl.SetDropTarget(file_drop_target)
        
        """add label and filetextctrl to boxsiser object with positioioning parameters"""
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(self.fileTextCtrl, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def SetInsertionPointEnd(self):
        """Put insertion point at end of text control to prevent overwriting"""
        self.fileTextCtrl.SetInsertionPointEnd()
 
    #----------------------------------------------------------------------
    def updateText(self, text):
        """Write text to the text control"""
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
    app = wx.App()
    frame = DnDFrame()
    app.MainLoop()  

 
