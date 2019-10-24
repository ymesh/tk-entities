# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system. 
    
    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("Entities", app_instance, AppDialog)


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """
    
    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)
        
        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        
        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - An Sgtk API instance, via self._app.sgtk 
        self._app = sgtk.platform.current_bundle()

        ent_list_widget = self.ui.ent_listWidget
        fld_list_widget = self.ui.fld_listWidget
        # TODO 
        # setup this properties in .ui files
        single_selection = QtGui.QAbstractItemView.SingleSelection
        ent_list_widget.setSelectionMode(single_selection)
        fld_list_widget.setSelectionMode(single_selection)

        ent_list_widget.itemSelectionChanged.connect(self.disp_fields)
        
        self.disp_entities()
        self.disp_fields()

        # logging happens via a standard toolkit logger
        logger.info("Launching Entities Application...")
        return


    def disp_entities(self):
        '''
        Display entities
        '''
        sg = self._app.shotgun
        project = self._app.engine.context.project
        ent_list_widget = self.ui.ent_listWidget
        item_role = 'entity'

        # clear list
        ent_list_widget.clear()

        entities = sg.schema_entity_read(project)
        entity_names = entities.keys()

        for entity_name in sorted(entity_names):
            item = QtGui.QListWidgetItem(entity_name)
            item.setData(QtCore.Qt.UserRole, item_role)
            ent_list_widget.addItem(item)
            print("{} = {}".format(entity_name, entities[entity_name]))
        return

    def disp_fields(self):
        '''
        Display entities
        '''
        sg = self._app.shotgun
        project = self._app.engine.context.project
        fld_list_widget = self.ui.fld_listWidget
        ent_list_widget = self.ui.ent_listWidget
        item_role = 'field'

        # clear list
        fld_list_widget.clear()

        entity_item = ent_list_widget.currentItem()
        if not entity_item:
            return

        entity_name = entity_item.text()
        fields = sg.schema_field_read(entity_name, None, project)
        field_names = fields.keys()

        for field_name in sorted(field_names):
            item = QtGui.QListWidgetItem(field_name)
            item.setData(QtCore.Qt.UserRole, item_role)
            fld_list_widget.addItem(item)
            print("{} = {}".format(field_name, fields[field_name]))
        return

