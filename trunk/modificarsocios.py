#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Jul  6 13:16:57 2010

import wx
import MySQLdb
# begin wxGlade: extracode
# end wxGlade



class Modificarsocio(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Modificarsocio.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        self.db = MySQLdb.connect('localhost', 'cintia', 'cintia', 'cintia', charset='UTF8')
        wx.Frame.__init__(self, *args, **kwds)
        self.frase2 = wx.StaticText(self, -1, "Ingrese el socio a Modificar")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.socio_ = wx.StaticText(self, -1, "Socio :")
        self.text_socio = wx.TextCtrl(self, -1, "")
        self.Cancelar_ = wx.Button(self, -1, "Cancelar")
        self.Aceptar_ = wx.Button(self, -1, "Aceptar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnCancelar, self.Cancelar_)
        self.Bind(wx.EVT_BUTTON, self.OnAceptar, self.Aceptar_)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Modificarsocio.__set_properties
        self.SetTitle("ModificarSocios")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("/home/tt06/videoclub/logodevideo.jpeg", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.text_socio.SetMinSize((160, 27))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Modificarsocio.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_1.Add(self.frase2, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.socio_, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.text_socio, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.Cancelar_, 0, wx.EXPAND|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.Aceptar_, 0, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def OnCancelar(self, event): # wxGlade: Modificarsocio.<event_handler>
        print "Event handler `OnCancelar' not implemented!"
        event.Skip()

    def OnAceptar(self, event): # wxGlade: Modificarsocio.<event_handler>
        self.text_socio.GetValue()
        self.text_socio.SetValue('')
        c = self.db.cursor()
        c.execute('''SELECT id_socios, Nombre, Apellido FROM Socios WHERE id_socios= %s''',(socio))
        q = c.fetchall()
        print q 
        c.close()
        lista = []
        for cosa 
        

# end of class Modificarsocio


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Modificar = Modificarsocio(None, -1, "")
    app.SetTopWindow(Modificar)
    Modificar.Show()
    app.MainLoop()