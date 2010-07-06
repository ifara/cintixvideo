#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon Jun 28 13:33:28 2010

import wx
import sys
import MySQLdb
# begin wxGlade: extracode
# end wxGlade



class MyLista(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyLista.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        self.db = MySQLdb.connect('localhost', 'cintia', 'cintia', 'cintia', charset='UTF8')
        wx.Frame.__init__(self, *args, **kwds)
        self.list_socios = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyLista.__set_properties
        self.SetTitle("listadodesocios")
        columnas = [u'Item a considerar', 'Apellido',  'Nombres','dni' , 'Calle' , 'Numero', 'Dpto', 'Piso', 'Localidad' , 'Telefono','CodigoPostal', 'email' ]
        for col, text in enumerate(columnas):
            self.list_socios.InsertColumn(col, text)
        self.list_socios.SetColumnWidth(0, 300)
        self.list_socios.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(4, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(5, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(6, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(7, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(8, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(9, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(10, wx.LIST_AUTOSIZE_USEHEADER)
        self.list_socios.SetColumnWidth(11, wx.LIST_AUTOSIZE_USEHEADER)
        
        c = self.db.cursor()
        c.execute('''SELECT* FROM Socios ''')
        q = c.fetchall()
        for lista in q:
            index = self.list_socios.InsertStringItem(sys.maxint, str(lista[0]))
            for colu, text in enumerate (lista[1:]):
                self.list_socios.SetStringItem(index, colu+1, str(text))
        c.close()
    def __do_layout(self):
        # begin wxGlade: MyLista.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.list_socios, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyLista


if __name__ == "__main__":
    lissocios = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyLista(None, -1, "")
    lissocios.SetTopWindow(frame_1)
    frame_1.Show()
    lissocios.MainLoop()
