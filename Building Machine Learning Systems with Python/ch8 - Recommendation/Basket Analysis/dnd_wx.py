#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:05:45 2017

@author: saurabh
"""

import wx

class FileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
 
    def OnDropFiles(self, x, y, filenames):
        self.window.set_insertion_point_to_end()
        for filepath in filenames:
            self.window.update_text(filepath + '\n') 

class DnDPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        file_drop_target = FileDropTarget(self)
        lbl = wx.StaticText(self, label="Drag Transactions File here:")
        self.fileTextCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.VSCROLL|wx.TE_READONLY)
        self.fileTextCtrl.SetDropTarget(file_drop_target)
        button = wx.Button(self, label = "Process File")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 1, wx.ALL, 5)
        sizer.Add(self.fileTextCtrl, 10, wx.EXPAND|wx.ALL, 10)
        sizer.Add(button, 1, wx.ALIGN_CENTER, 5)
#        sizer.SetDimension(0, 0, 10, 100)
        self.SetSizer(sizer)
 
    def set_insertion_point_to_end(self):
        self.fileTextCtrl.SetInsertionPointEnd()
 
    def update_text(self, text):
        self.fileTextCtrl.WriteText(text)
        
    
class DnDFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Association Rule Mining")
        DnDPanel(self)
        self.Show()

if __name__ == '__main__':
	app = wx.App(redirect = False)
	DnDFrame()
	app.MainLoop()
