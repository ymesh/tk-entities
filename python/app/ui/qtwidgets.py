# -*- coding: utf-8 -*-
'''
File    : qtwidgets.py
Project : ui
Author  : Yuri Meshalkin (yuri.meshalkin@gmail.com)

Created : Tuesday, 22nd October 2019 11:28:38 pm
Modified: Wednesday, 23rd October 2019 12:10:00 am

(c) Copyright 2018 - 2019 Yuri Meshalkin, MeshStudio

Description:

Importing widgets into your app
Each of the modules in this framework can be used inside your Toolkit Apps.
They are typically imported via Toolkit’s special import_framework() method, 
which handles automatic reload and resource management behind the scenes:

overlay_widget = sgtk.platform.import_framework("tk-framework-qtwidgets", "overlay_widget")

These imports work just like the normal import call in python and we recommend 
that they are placed at the top of the file.

Once you have imported the module, you can access the class or objects inside:

my_overlay = overlay_widget.ShotgunOverlayWidget(self)

Using widgets with QT Designer
If you are dropping the widgets into QT Designer directly, 
there isn’t an option to run the import_framework method. 
In this case, we recommend adding imports to a wrapper file and place 
that next to your other python files. 
You can for example call this file qtwidgets.py 
and then do the imports in this file:

import sgtk

note_input_widget = sgtk.platform.current_bundle().import_module("note_input_widget")
NoteInputWidget = note_input_widget.NoteInputWidget

version_label = sgtk.platform.current_bundle().import_module("version_label")
VersionLabel = version_label.VersionLabel

In your designer generated .ui files, you can now reference these widgets 
as if they were local to your project.
'''

import sgtk

search_widget = sgtk.platform.import_framework("tk-framework-qtwidgets", "search_widget")
# search_widget = sgtk.platform.current_bundle().import_module("search_widget")

SearchWidget = search_widget.SearchWidget
