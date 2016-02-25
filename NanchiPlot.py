# -*- coding: utf-8 -*-
# 
# Author: Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Version: 0.1.0-dev
#

import wx
import os
import numpy as np
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.cm as cm
import nanchi.setplot as setplot
import nanchi.iodata as io
import nanchi.uibase as ui
import nanchi.uiaux as aux
import nanchi.image as image
from nanchi._const_ import *


class NanchiPlot(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title=NANCHI_MAIN_CAPTION,size=(800,600))
		self.initMenu()
		self.initCtrls()
		self.initToolBar()
		self.initSizers()
		self.initEvents()
		
		# Icon
		self.icon = wx.Icon(PATH_NANCHI_LOGO)
		self.SetIcon(self.icon)
		 
		# Status bar
		self.sb = aux.StatusBar(self,-1)
		self.SetStatusBar(self.sb)
		self.sb.SetStatusText(SB_ON_INIT)
		
		self.axes = self.notebook.graphs.axes
		self.figure = self.notebook.graphs.figure
		self.canvas = self.notebook.graphs.canvas
		self.data = self.notebook.data
		
		self.Centre(True)
		self.Show()
		
	def initMenu(self):
		"""
		Crear la barra de Menús
		"""
		m_archivo = wx.Menu()
		guardar = m_archivo.Append(-1, "Exportar imagen... \tCtrl+S")
		importar = m_archivo.Append(-1, "Importar datos... \tCtrl+I")
		salir = m_archivo.Append(-1, "Salir \tCtrl+Q")
		
		m_imagen = wx.Menu()
		filtros = wx.Menu()
		sobel = wx.MenuItem(filtros, -1, "Sobel")
		filtros.AppendItem(sobel)
		roberts = wx.MenuItem(filtros, -1, "Roberts")
		filtros.AppendItem(roberts)
		prewitt = wx.MenuItem(filtros, -1, "Prewitt")
		filtros.AppendItem(prewitt)
		m_imagen.AppendMenu(-1, "Filtros", filtros)
		binarizar = m_imagen.Append(-1, "Binarizar")
		
		
		m_ayuda = wx.Menu()
		ayuda = m_ayuda.Append(-1, "Ayuda")
		acerca_de = m_ayuda.Append(-1, "Acerca de...")
		
		
		menu_bar = wx.MenuBar()
		menu_bar.Append(m_archivo, "Archivo")
		menu_bar.Append(m_imagen, "Imagen")
		menu_bar.Append(m_ayuda, "Ayuda")
		self.SetMenuBar(menu_bar)
		
		self.Bind(wx.EVT_MENU, self.OnSave, guardar)
		self.Bind(wx.EVT_MENU, self.OnImport, importar)
		
		self.Bind(wx.EVT_MENU, self.OnSobel, sobel)
		self.Bind(wx.EVT_MENU, self.OnRoberts, roberts)
		self.Bind(wx.EVT_MENU, self.OnPrewitt, prewitt)
		self.Bind(wx.EVT_MENU, self.OnBinarize, binarizar)
		
		self.Bind(wx.EVT_MENU, self.OnAbout, acerca_de)
		self.Bind(wx.EVT_MENU, self.OnHelp, ayuda)
		self.Bind(wx.EVT_MENU, self.OnExit, salir)
		
	def initSizers(self):
		"""
		Inicializar los sizers
		"""
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.panelsz = wx.BoxSizer(wx.HORIZONTAL)
		self.mainsz.Add(self.toolbar, 0, wx.EXPAND)
		self.panelsz.Add(self.notebook, 4, wx.EXPAND|wx.ALL, 2)
		self.mainsz.Add(self.mainpanel, 1, wx.EXPAND)
		self.mainpanel.SetSizer(self.panelsz)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		"""
		Inicializar los controles básicos
		"""
		self.mainpanel = wx.Panel(self,-1)
		self.notebook = ui.NanchiNoteBook(self.mainpanel)
		
	def initToolBar(self):
		"""
		Inicializar la barra de herramientas
		"""
		self.toolbar = aux.CustomTB(self)
		self.toolbar.Realize()
		
	def initEvents(self):
		"""
		Inicializar (conexión de ) eventos
		"""
		self.Bind(wx.EVT_TOOL, self.OnImport, self.toolbar.import_tool)
		self.Bind(wx.EVT_TOOL, self.OnLoadImage, self.toolbar.load_image_tool)
		self.Bind(wx.EVT_TOOL, self.OnFunction, self.toolbar.function_tool)
		self.Bind(wx.EVT_TOOL, self.OnBivariableFunction, self.toolbar.bivariable_function_tool)
		self.Bind(wx.EVT_TOOL, self.OnPlot, self.toolbar.plot_tool)
		#self.Bind(wx.EVT_TOOL, self.OnPolar, self.toolbar.polar_tool)
		self.Bind(wx.EVT_TOOL, self.OnBar, self.toolbar.bar_tool)
		self.Bind(wx.EVT_TOOL, self.OnScatter, self.toolbar.scatter_tool)
		self.Bind(wx.EVT_TOOL, self.OnPie, self.toolbar.pie_tool)
		self.Bind(wx.EVT_TOOL, self.OnImage, self.toolbar.image_tool)
		self.Bind(wx.EVT_TOOL, self.OnContour, self.toolbar.contour_tool)
		self.Bind(wx.EVT_TOOL, self.OnContourf, self.toolbar.contourf_tool)
		self.Bind(wx.EVT_TOOL, self.OnZoomBox, self.toolbar.zoom_box_tool)
		self.Bind(wx.EVT_TOOL, self.OnResetView, self.toolbar.reset_view_tool)
		
	def OnExit(self,event):
		"""
		Archivo -> Salir -> (Atajo) Ctrl+Q 
		"""
		self.Close(True)
		
	def OnHelp(self,event):
		"""
		Ayuda -> Ayuda
		
		Abre la documentación en HTML
		"""
		os.startfile(PATH_HTML_DOCUMENTATION)
		
	def OnSave(self,event):
		"""
		Archivo -> Exportar imagen -> (Atajo) Ctrl + S
		"""
		wldc = "PNG (*.png)|*.png|PDF (*.pdf)|*.pdf|EPS (*.eps)|*.eps|JPG (*.jpg)|*jpg"
		dlg=wx.FileDialog(self, "Guardar", os.getcwd(), style=wx.SAVE, wildcard=wldc)
		if dlg.ShowModal() == wx.ID_OK:
			self.figure.savefig(dlg.GetPath())
		dlg.Destroy()
		
	def OnImport(self,event):
		"""
		Archivo -> Importar datos -> (Atajo) Ctrl + I
		Toolbar -> Importar datos
		
		Importa datos de un fichero de texto plano
		"""
		path = ""
		wildcard = "*.txt"
		dlg = wx.FileDialog(self, message="Seleccione un archivo",
		defaultDir=os.getcwd(), wildcard=wildcard, style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			busy_dlg = aux.BusyInfo("Espere un momento...", self)
			path = dlg.GetPath()
			data = io.read_txt(path)
			if data is None:
				self.sb.SetStatusText(SB_ON_IMPORT_DATA_FAIL%(path))
				del busy_dlg
			else:
				self.data.grid_data.SetArrayData(data)
				del busy_dlg
		dlg.Destroy()
		
			
	def OnLoadImage(self,event):
		path = ""
		wildcard = "*.png"
		dlg = wx.FileDialog(self, message="Seleccione una imagen",
		defaultDir=os.getcwd(), wildcard=wildcard, style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			busy_dlg = aux.BusyInfo("Espere un momento...", self)
			path = dlg.GetPath()
			data = io.imread(path)
			self.data.grid_data.SetArrayData(data)
			self.sb.SetStatusText(SB_ON_IMPORT_IMAGE%(path))
			del busy_dlg
		else:
			self.sb.SetStatusText(SB_ON_IMPORT_IMAGE_CANCEL)
		dlg.Destroy()
			
	def OnFunction(self,event):
		dialog = aux.FunctionDialog(None)
		if dialog.ShowModal() == wx.ID_OK:
			fx,a,b = dialog.GetData()
			x = np.linspace(float(a), float(b), 100)
			fx = eval(fx)
			self.data.grid_data.SetArrayData(np.array([x,fx]).transpose())
			self.data.grid_data.SetColLabelValue(0,"x")
			self.data.grid_data.SetColLabelValue(1,"f(x)")
			self.sb.SetStatusText(SB_ON_CREATE_DATA_FUNCTION)
		dialog.Destroy()
		
	def OnBivariableFunction(self,event):
		dialog = aux.BivariableFunctionDialog(None)
		if dialog.ShowModal() == wx.ID_OK:
			fxy,x,y = dialog.GetData()
			print fxy,x,y
			x1,x2 = [float(n) for n in x]
			y1,y2 = [float(n) for n in y]
			xx = np.linspace(x1, x2, 100)
			yy = np.linspace(y1, y2, 100)
			x,y = np.meshgrid(xx,yy)
			Z = eval(fxy)
			self.data.grid_data.SetArrayData(Z)
			self.sb.SetStatusText(SB_ON_CREATE_DATA_BIVARIABLE_FUNCTION)
		dialog.Destroy()
		
	def OnPlot(self,event):
		setplot.set_default_params(self.axes,self.figure)
		busy_dlg = aux.BusyInfo("Espere un momento...", self)
		X = self.data.grid_data.GetArrayData()
		rows,cols = X.shape
		if cols == 2: # Common case
			self.axes.plot(X[:,0],X[:,1], picker=True)
		elif cols == 1:
			self.axes.plot(X[:,0], picker=True)
		elif cols > 2:
			for col in range(cols):
				#clabel = self.data.grid_data.GetColLabelValue(col)
				self.axes.plot(X[:,col], picker=True)
		self.canvas.draw()
		del busy_dlg
		
	def OnPolar(self,event):
		"""
		Implementación pendiente...
		"""
		pass
		
	def OnBar(self,event):
		self.axes.cla()
		X = self.data.grid_data.GetArrayData()
		rows,cols = X.shape
		if cols == 1: # Common case
			x = range(len(X[:,0]))
			self.axes.bar(x,X[:,0])
		self.canvas.draw()
		
	def OnScatter(self,event):
		self.axes.cla()
		X = self.data.grid_data.GetArrayData()
		rows,cols = X.shape
		if cols == 2: # Common case
			self.axes.plot(X[:,0],X[:,1],"bo")
		elif cols == 1:
			self.axes.plot(X[:,0],"bo")
		self.canvas.draw()
		
	def OnPie(self,event):
		self.axes.cla()
		X = self.data.grid_data.GetArrayData()
		rows,cols = X.shape
		if cols == 1:
			self.axes.pie(X[:,0])
		else:
			pass
		self.canvas.draw()
		
	def OnImage(self,event):
		self.axes.cla()
		X = self.data.grid_data.GetArrayData()
		rows,cols = X.shape
		self.axes.imshow(X, cmap=cm.gray)
		self.canvas.draw()
		
	def OnContour(self,event):
		self.axes.cla()
		X = self.data.grid_data.GetArrayData()
		rows,cols = X.shape
		self.axes.contour(X)
		self.canvas.draw()
		
	def OnContourf(self,event):
		self.axes.cla()
		X = self.data.grid_data.GetArrayData()
		rows,cols = X.shape
		self.axes.contourf(X)
		self.canvas.draw()
		
	# Operaciones con imágenes ============================
	def OnSobel(self,event):
		cx = self.data.grid_data.GetArrayData()
		xmod = image.sobel(cx)
		self.data.grid_data.SetArrayData(xmod)
		
	def OnPrewitt(self,event):
		cx = self.data.grid_data.GetArrayData()
		xmod = image.prewitt(cx)
		self.data.grid_data.SetArrayData(xmod)
		
	def OnRoberts(self,event):
		cx = self.data.grid_data.GetArrayData()
		xmod = image.roberts(cx)
		self.data.grid_data.SetArrayData(xmod)
		
	def OnBinarize(self,event):
		cx = self.data.grid_data.GetArrayData()
		xmod = image.binarize(cx)
		self.data.grid_data.SetArrayData(xmod)
		
	def OnZoomBox(self,event):
		self.canvas.zoomit()
		
	def OnResetView(self,event):
		#self.axes.relim()
		self.axes.autoscale()
		self.axes.set_aspect("auto")
		self.canvas.disconnect_all()
		self.canvas.draw()
		
	def OnAbout(self,event):
		aux.AboutDialog(None)


if __name__=='__main__':
	app = wx.App()
	frame = NanchiPlot(None)
	app.MainLoop()
