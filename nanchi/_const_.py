# -*- coding: utf-8 -*-
import os.path as path
import site
import matplotlib
from itertools import cycle

VERSION = "0.1.0-dev"
NANCHI_MAIN_CAPTION = "NanchiPlot %s"%(VERSION)

# Colors
PANEL_BG_COLOR = "#ababab"
FRAME_BG_COLOR = "#aaf0f0"
AXES_BG_COLOR = "#efefef"
FIGURE_BG_COLOR = "#fafafa"

LINE_COLOR = "#000000"
GRID_COLOR = "#080808"
XTICK_COLOR = "#101635"
YTICK_COLOR = "#101635"

BAR_COLOR_CYCLE = ['#E24A33', '#348ABD', '#988ED5', '#777777', '#FBC15E', '#8EBA42', '#FFB5B8']

#~ BAR_COLOR_CYCLE = ["#348ABD",
                   #~ "#DF6B59", 
                   #~ "#66B560", 
                   #~ "#988ED5", 
                   #~ "#FBC15E", 
                   #~ "#FBC959", 
                   #~ "#FFB5B8"]

# Font sizes
TICK_LABEL_SIZE = 10


# Captions
DEFAULT_DIALOG_CAPTION = NANCHI_MAIN_CAPTION


# Graphics properties
LINE_STYLES = "'-' | '--' | '-.' | ':' | 'None' ".split("|")


# Icons & Images dirs
cdir, _  = path.split(path.abspath(__file__))


IMGS_PATH = path.join(cdir, u"img")
PATH_NANCHI_LOGO = path.join(IMGS_PATH,"nanchi_logo.png")
PATH_IMPORT_ICON = path.join(IMGS_PATH, "import_icon_32x32.png")
PATH_LOAD_IMAGE_ICON = path.join(IMGS_PATH, "load_image_icon_32x32.png")
PATH_FUNCTION_ICON = path.join(IMGS_PATH, "function_icon_32x32.png")
PATH_BIVARIABLE_FUNCTION_ICON = path.join(IMGS_PATH, "bivariable_function_icon_32x32.png")
PATH_PLOT_ICON = path.join(IMGS_PATH, "plot_icon_32x32.png")
PATH_POLAR_ICON = path.join(IMGS_PATH, "polar_icon_32x32.png")
PATH_BAR_ICON = path.join(IMGS_PATH, "bar_icon_32x32.png")
PATH_SCATTER_ICON = path.join(IMGS_PATH, "scatter_icon_32x32.png")
PATH_PIE_ICON = path.join(IMGS_PATH, "pie_icon_32x32.png")
PATH_IMAGE_ICON = path.join(IMGS_PATH, "image_icon_32x32.png")
PATH_CONTOUR_ICON = path.join(IMGS_PATH, "contour_icon_32x32.png")
PATH_CONTOURF_ICON = path.join(IMGS_PATH, "contourf_icon_32x32.png")


PATH_ZOOM_BOX_ICON = path.join(IMGS_PATH, "zoom_box_icon_24x24.png")
PATH_RESET_VIEW_ICON = path.join(IMGS_PATH, "reset_view_icon_24x24.png")
PATH_AXES_COLOR_ICON = path.join(IMGS_PATH, "axes_color_icon_24x24.png")
PATH_GRID_STYLE_ICON = path.join(IMGS_PATH, "grid_style_icon_24x24.png")
PATH_GRID_COLOR_ICON = path.join(IMGS_PATH, "grid_color_icon_24x24.png")
PATH_LINE_STYLE_ICON = path.join(IMGS_PATH, "line_style_icon_24x24.png")
PATH_LINE_COLOR_ICON = path.join(IMGS_PATH, "line_color_icon_24x24.png")
PATH_LINE_WIDTH_ICON = path.join(IMGS_PATH, "line_width_icon_24x24.png")
PATH_LINE_LABEL_ICON = path.join(IMGS_PATH, "line_label_icon_24x24.png")
PATH_SHOW_LEGEND_ICON = path.join(IMGS_PATH, "show_legend_icon_24x24.png")
PATH_TEXT_ICON = path.join(IMGS_PATH, "text_icon_24x24.png")

PATH_XLABEL_ICON = path.join(IMGS_PATH, "xlabel_icon_24x24.png")
PATH_YLABEL_ICON = path.join(IMGS_PATH, "ylabel_icon_24x24.png")
PATH_XTICKS_ICON = path.join(IMGS_PATH, "xticks_icon_24x24.png")
PATH_YTICKS_ICON = path.join(IMGS_PATH, "yticks_icon_24x24.png")
PATH_PIE_LABELS_ICON = path.join(IMGS_PATH, "pie_labels_icon_24x24.png")

PATH_MOVE_TEXT_ICON = path.join(IMGS_PATH, "move_text_icon_24x24.png")
PATH_MOVE_LINE_ICON = path.join(IMGS_PATH, "move_line_icon_24x24.png")


# Documentation path
PATH_DOCUMENTATION_HTML = r"help/index.html"
PATH_ABOUT_HTML = r"help/about.html"

# Status for "Status bar"
SB_ON_INIT = "Import or insert data to start..."
SB_ON_IMPORT_IMAGE = "Image imported from %s"
SB_ON_IMPORT_IMAGE_CANCEL = "Unimported image"
SB_ON_IMPORT_DATA = "Data imported from %s"
SB_ON_IMPORT_DATA_FAIL = "Error on load file %s"
SB_ON_CREATE_DATA_FUNCTION = "Data from f(x)"
SB_ON_CREATE_DATA_BIVARIABLE_FUNCTION = "Data from f(x,y)"
SB_ERROR_ON_CREATE_DATA = "Please check inputs, some values are wrong"


#Import dialog
IMPORT_DIALOG_WILDCARD = "All files (*.*)|*.*|TXT Files (*.txt)|*.txt|DAT Files (*.dat)|*.dat"


# MPL-Stylesheets
WHITE_STYLE = path.join(cdir, u'styles','white.mplstyle')
DARK_STYLE = path.join(cdir, u'styles','dark.mplstyle')
BLUE_STYLE = path.join(cdir, u'styles','blue.mplstyle')






