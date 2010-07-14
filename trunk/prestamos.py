#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Jun 23 13:55:04 2010

import wx
import MySQLdb
# begin wxGlade: extracode
# end wxGlade

peli = []
clientes = []

class Prestamos(wx.Frame):
    def __init__(self, *args, **kwds):
        self.db = MySQLdb.connect('localhost', 'cintia', 'cintia', 'cintia', charset='UTF8')
        c = self.db.cursor()
        c.execute('''SELECT id_socios, Apellido, Nombres FROM Socios''')
        q = c.fetchall()
        a = []
        for persona in q:
            a.append(str(persona[0])+'-'+persona[2]+'-'+persona[1])
       
        c.close()
            
        # begin wxGlade: Prestamos.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.socio_ = wx.StaticText(self.panel_1, -1, "Socios : ")
        self.text_socios = wx.TextCtrl(self.panel_1, -1, "")
        self.pelicula_ = wx.StaticText(self.panel_1, -1, "Pelicula : ")
        c = self.db.cursor()
        c.execute('''SELECT id_film,pelicula FROM Videoclub''')
        q = c.fetchall()
        film = []
        for video in q :
            film.append(str(video[0]) + '-' + video[1])
        c.close()
            
        self.combo_peli = wx.ComboBox(self.panel_1, -1, choices=["Terror ", "Romantica", "Drama", "Ficcion", "Infantil", "Comedia"], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        
        
        
        self.label_retiro = wx.StaticText(self.panel_1, -1, "Dia retiro :")
        self.fecha_retiro = wx.DatePickerCtrl(self.panel_1, -1)
        self.reitegro_ = wx.StaticText(self.panel_1, -1, "Dia reitegro:")
        self.fecha_reitegro = wx.DatePickerCtrl(self.panel_1, -1)
        self.ingresar_ = wx.Button(self.panel_1, -1, "Ingresar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnIngresar, self.ingresar_)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Prestamos.__set_properties
        self.SetTitle("Prestamos")
        self.text_socios.SetMinSize((120, 27))
        self.combo_peli.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Prestamos.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(7, 2, 0, 0)
        grid_sizer_1.Add(self.socio_, 0, 0, 0)
        grid_sizer_1.Add(self.text_socios, 0, 0, 0)
        grid_sizer_1.Add(self.pelicula_, 0, 0, 0)
        grid_sizer_1.Add(self.combo_peli, 0, 0, 0)
        grid_sizer_1.Add(self.label_retiro, 0, 0, 0)
        grid_sizer_1.Add(self.fecha_retiro, 0, 0, 0)
        grid_sizer_1.Add(self.reitegro_, 0, 0, 0)
        grid_sizer_1.Add(self.fecha_reitegro, 0, 0, 0)
        grid_sizer_1.Add(self.ingresar_, 0, 0, 0)
        self.panel_1.SetSizer(grid_sizer_1)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnIngresar(self, event): # wxGlade: Prestamos.<event_handler>
       socios = self.text_socios.GetValue()
       clientes.append(socios)
       
       for personas in clientes :
           a = personas.strip()
           gente = str(a[0])
           ordenar = a.split('-')
           print gente
        
       titulo = self.combo_peli.GetValue()
       peli.append(titulo) 
       
       for algo in peli :
           a = algo.strip()
           ordenar = a.split('-')
           video = str(ordenar[0])
       print video 
       retiro = self.fecha_retiro.GetValue()
       retiro = ('%04d/%02d/%02d '% (retiro.GetYear(),retiro.GetMonth()+1,retiro.GetDay()))
       reitegro = self.fecha_reitegro.GetValue()
       reitegro =('%04d/%02d/%02d '% (reitegro.GetYear(),reitegro.GetMonth()+1,reitegro.GetDay()))
       c = self.db.cursor()
       print retiro, reitegro
       c.execute ('''INSERT INTO Prestamos (Dia_retiro, Dia_reitegro, id_film, id_socios) VALUES (%s, %s, %s , %s)''',(retiro, reitegro, video, gente))
       c.close() 
         
       wx.MessageBox('El alquiler se ha hecho correctamente',u'OK',
       wx.OK | wx.ICON_INFORMATION, None)
         
       self.Close()                               
              
# end of class Prestamos


class App(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        PrestFrame = Prestamos(None, -1, "")
        self.SetTopWindow(PrestFrame)
        PrestFrame.Show()
        return 1

# end of class App

if __name__ == "__main__":
    Prest = App(0)
    Prest.MainLoop()