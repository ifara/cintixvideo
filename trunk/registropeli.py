#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Jun 16 13:18:13 2010

import wx
import MySQLdb

# begin wxGlade: extracode
# end wxGlade



class Pelicula(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Pelicula.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.db = MySQLdb.connect('localhost', 'cintia', 'cintia', 'cintia', charset='UTF8')
        self.panel_1 = wx.Panel(self, -1)
        self.pelicula_ = wx.StaticText(self.panel_1, -1, "Pelicula : ")
        self.text_pelicula = wx.TextCtrl(self.panel_1, -1, "")
        self.genero_ = wx.StaticText(self.panel_1, -1, "Genero :")
        Listado = ['Drama','Terror','Ficcion' ,'Romantica','Infantil','Comedia']
        self.genero_t = wx.ComboBox(self.panel_1, -1, "", choices=Listado)
        self.duracion_ = wx.StaticText(self.panel_1, -1, "Duracion :")
        self.txt_duracion = wx.TextCtrl(self.panel_1, -1, "")
        self.protagonista_ = wx.StaticText(self.panel_1, -1, "Protagonista :")
        self.texto_prota = wx.TextCtrl(self.panel_1, -1, "")
        self.director_ = wx.StaticText(self.panel_1, -1, "Director :")
        self.t_director = wx.TextCtrl(self.panel_1, -1, "")
        self.origen_ = wx.StaticText(self.panel_1, -1, "Origen :")
        self.tt_origen = wx.TextCtrl(self.panel_1, -1, "")
        self.Aceptar_ = wx.Button(self.panel_1, -1, "Aceptar")
        self.Cancelar_ = wx.Button(self.panel_1, -1, "Cancelar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnAceptar, self.Aceptar_)
        self.Bind(wx.EVT_BUTTON, self.onCancelar, self.Cancelar_)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Pelicula.__set_properties
        self.SetTitle("Pelicula")
        self.text_pelicula.SetMinSize((200, 27))
        self.genero_t.SetMinSize((200, 27))
        self.tt_origen.SetMinSize((200, 27))
        self.panel_1.SetMinSize((400, 459))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Pelicula.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(7, 2, 0, 0)
        grid_sizer_1.Add(self.pelicula_, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.text_pelicula, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.genero_, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.genero_t, 0, 0, 0)
        grid_sizer_1.Add(self.duracion_, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.txt_duracion, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.protagonista_, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.texto_prota, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.director_, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.t_director, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.origen_, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.tt_origen, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.Aceptar_, 0, 0, 0)
        grid_sizer_1.Add(self.Cancelar_, 0, wx.RIGHT, 0)
        self.panel_1.SetSizer(grid_sizer_1)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def OnAceptar(self, event): # wxGlade: Pelicula.<event_handler>
        pelicula = self.text_pelicula.GetValue()
        genero = self.genero_t.GetValue()
        duracion = self.txt_duracion.GetValue()
        protagonista = self.texto_prota.GetValue()
        director = self.t_director.GetValue()
        origen = self.tt_origen.GetValue()
        c = self.db.cursor()
        c.execute('''INSERT INTO Videoclub (pelicula, genero, duracion, protagonista, director,
         origen) VALUES (%s, %s, %s, %s, %s, %s)''' ,(pelicula, genero, duracion, protagonista, director, origen))
        c.close() 
        wx.MessageBox(u'Se ha recibido la informacion',u'Aceptar', wx.OK|wx.ICON_INFORMATION, None)
        self.text_pelicula.SetValue('')
        self.genero_t.SetValue('')
        self.txt_duracion.SetValue('')
        self.texto_prota.SetValue('')
        self.t_director.SetValue('')
        self.tt_origen.SetValue('')
        
    def onCancelar(self, event):
        self.Close()

# end of class Pelicula


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Pelicula_ = Pelicula(None, -1, "")
    app.SetTopWindow(Pelicula_)
    Pelicula_.Show()
    app.MainLoop()