#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Jun 16 14:18:52 2010

import wx
import MySQLdb
# begin wxGlade: extracode
# end wxGlade



class Socios(wx.Frame):
    def __init__(self, id, *args, **kwds):
        # begin wxGlade: Socios.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.db = MySQLdb.connect('localhost', 'cintia', 'cintia', 'cintia', charset='UTF8')
        self.id = id
        c = self.db.cursor()
        c.execute('''SELECT * FROM Socios WHERE ID_socios = %s''', (self.id))
        q = c.fetchone()
        print q
        c.close() 
        self.panel_ = wx.Panel(self, -1)
        self.apellido_ = wx.StaticText(self.panel_, -1, "Apellido :")
        self.textape = wx.TextCtrl(self.panel_, -1, q[1])
        self.nombre_ = wx.StaticText(self.panel_, -1, "Nombre : ")
        self.te_nom = wx.TextCtrl(self.panel_, -1, q[2])
        self.dni_ = wx.StaticText(self.panel_, -1, "D.N.I : ")
        self.text_dni = wx.TextCtrl(self.panel_, -1, q[3])
        self.tel_ = wx.StaticText(self.panel_, -1, "Telefono : ")
        self.text_tel = wx.TextCtrl(self.panel_, -1, q[9])
        self.calle_ = wx.StaticText(self.panel_, -1, "Calle : ")
        self.text_calle = wx.TextCtrl(self.panel_, -1, q[4])
        self.numero_ = wx.StaticText(self.panel_, -1, "Numero : ")
        self.text_num = wx.TextCtrl(self.panel_, -1, q[5])
        self.piso_ = wx.StaticText(self.panel_, -1, "Piso : ")
        self.text_piso = wx.TextCtrl(self.panel_, -1, q[7])
        self.dpto_ = wx.StaticText(self.panel_, -1, "Dpto : ")
        self.text_dpto = wx.TextCtrl(self.panel_, -1, q[6])
        self.cp_ = wx.StaticText(self.panel_, -1, "CP : ")
        self.text_cp = wx.TextCtrl(self.panel_, -1, q[10])
        self.localidad_ = wx.StaticText(self.panel_, -1, "Localidad : ")
        self.text_local = wx.TextCtrl(self.panel_, -1, q[8])
        self.email_ = wx.StaticText(self.panel_, -1, "email :")
        self.text_correo = wx.TextCtrl(self.panel_, -1, q[11])
        self.Aceptar_ = wx.Button(self.panel_, -1, "Aceptar ")
        self.button_1 = wx.Button(self.panel_, -1, "Cancelar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnAceptar, self.Aceptar_)
        self.Bind(wx.EVT_BUTTON, self.OnCancelar, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Socios.__set_properties
        self.SetTitle("SociosClub")
        self.SetSize((584, 628))
        self.textape.SetMinSize((120, 27))
        self.te_nom.SetMinSize((120, 27))
        self.text_dni.SetMinSize((120, 27))
        self.text_tel.SetMinSize((120, 27))
        self.text_local.SetMinSize((120, 27))
        self.text_correo.SetMinSize((120, 27))
        self.panel_.SetMinSize((120, 623))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Socios.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_5 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_4 = wx.GridSizer(2, 2, 0, 0)
        grid_sizer_6 = wx.GridSizer(2, 6, 0, 0)
        grid_sizer_2 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_2.Add(self.apellido_, 0, 0, 0)
        grid_sizer_2.Add(self.textape, 0, 0, 0)
        grid_sizer_2.Add(self.nombre_, 0, 0, 0)
        grid_sizer_2.Add(self.te_nom, 0, 0, 0)
        grid_sizer_2.Add(self.dni_, 0, 0, 0)
        grid_sizer_2.Add(self.text_dni, 0, 0, 0)
        grid_sizer_2.Add(self.tel_, 0, 0, 0)
        grid_sizer_2.Add(self.text_tel, 0, 0, 0)
        sizer_3.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(self.calle_, 0, 0, 0)
        grid_sizer_6.Add(self.text_calle, 0, 0, 0)
        grid_sizer_6.Add(self.numero_, 0, 0, 0)
        grid_sizer_6.Add(self.text_num, 0, 0, 0)
        grid_sizer_6.Add(self.piso_, 0, 0, 0)
        grid_sizer_6.Add(self.text_piso, 0, 0, 0)
        grid_sizer_6.Add(self.dpto_, 0, 0, 0)
        grid_sizer_6.Add(self.text_dpto, 0, 0, 0)
        grid_sizer_6.Add(self.cp_, 0, 0, 0)
        grid_sizer_6.Add(self.text_cp, 0, 0, 0)
        sizer_3.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.localidad_, 0, 0, 0)
        grid_sizer_4.Add(self.text_local, 0, 0, 0)
        grid_sizer_4.Add(self.email_, 0, 0, 0)
        grid_sizer_4.Add(self.text_correo, 0, 0, 0)
        sizer_3.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(self.Aceptar_, 0, 0, 0)
        grid_sizer_5.Add(self.button_1, 0, 0, 0)
        sizer_4.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        self.panel_.SetSizer(sizer_3)
        sizer_1.Add(self.panel_, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def OnAceptar(self, event): # wxGlade: Socios.<event_handler>
        Apellido = self.textape.GetValue()
        Nombres = self.te_nom.GetValue()
        dni = self.text_dni.GetValue()
        dni = str(dni)
        Calle = self.text_calle.GetValue()
        Numero = self.text_num.GetValue()
        Numero = str(Numero)
        Dpto = self.text_dpto.GetValue()
        Dpto = str(Dpto) 
        Piso = self.text_piso.GetValue()
        Piso = str(Piso) 
        Localidad = self.text_local.GetValue()
        Telefono =self.text_tel.GetValue()
        Telefono = str(Telefono)
        CodigoPostal = self.text_cp.GetValue()
        CodigoPostal = str(CodigoPostal)
        email = self.text_correo.GetValue()
       
        c = self.db.cursor()
        c.execute('''UPDATE Socios SET  Apellido = %s , Nombres = %s , dni =% s , Calle = %s , Numero = %s, Dpto = %s, Piso = %s , Localidad = %s, Telefono = %s, CodigoPostal = %s, email = %s WHERE id_socios = %s''',( Apellido, Nombres, dni, Calle, Numero, Dpto, Piso, Localidad, Telefono,CodigoPostal, email ,self.id  ))
        c.close() 
        
        wx.MessageBox(u'Se ha asociado exitosamente', u'Aceptado', wx.OK|wx.ICON_INFORMATION, None)
        

    def OnCancelar(self, event): 
        self.Close()

# end of class Socios


class socioclub(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        ClubFilm = Socios(None, -1, "")
        self.SetTopWindow(ClubFilm)
        ClubFilm.Show()
        return 1

# end of class socioclub

if __name__ == "__main__":
    app = socioclub(0)
    app.MainLoop()
