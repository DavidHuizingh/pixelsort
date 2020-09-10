# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\GitHub\pixelsort\pixel_sorter_gui_param_clength_dummy.ui',
# licensing of 'f:\GitHub\pixelsort\pixel_sorter_gui_param_clength_dummy.ui' applies.
#
# Created: Wed Sep  9 17:58:11 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Param_Clength(object):
    def setupUi(self, Frame, param_name):
        Frame.setObjectName(f"f_param_{param_name}")
        Frame.setFrameShape(QtWidgets.QFrame.Panel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hl_param_clength_t = QtWidgets.QHBoxLayout()
        self.hl_param_clength_t.setSpacing(10)
        self.hl_param_clength_t.setObjectName(f"hl_param_{param_name}_t")
        self.t_param_clength = QtWidgets.QLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_param_clength.sizePolicy().hasHeightForWidth())
        self.t_param_clength.setSizePolicy(sizePolicy)
        self.t_param_clength.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.t_param_clength.setObjectName(f"t_param_{param_name}")
        self.hl_param_clength_t.addWidget(self.t_param_clength)
        self.t_param_clength_desc = QtWidgets.QLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_param_clength_desc.sizePolicy().hasHeightForWidth())
        self.t_param_clength_desc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.t_param_clength_desc.setFont(font)
        self.t_param_clength_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.t_param_clength_desc.setWordWrap(True)
        self.t_param_clength_desc.setObjectName(f"t_param_{param_name}_desc")
        self.hl_param_clength_t.addWidget(self.t_param_clength_desc)
        self.verticalLayout.addLayout(self.hl_param_clength_t)
        self.hl_param_clength_b = QtWidgets.QHBoxLayout()
        self.hl_param_clength_b.setObjectName(f"hl_param_{param_name}_b")
        self.t_param_clength_helper = QtWidgets.QLabel(Frame)
        self.t_param_clength_helper.setObjectName(f"t_param_{param_name}_helper")
        self.hl_param_clength_b.addWidget(self.t_param_clength_helper)
        self.tb_param_clength = QtWidgets.QLineEdit(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_param_clength.sizePolicy().hasHeightForWidth())
        self.tb_param_clength.setSizePolicy(sizePolicy)
        self.tb_param_clength.setMinimumSize(QtCore.QSize(20, 0))
        self.tb_param_clength.setMaximumSize(QtCore.QSize(35, 16777215))
        self.tb_param_clength.setText("")
        self.tb_param_clength.setObjectName(f"tb_param_{param_name}")
        self.hl_param_clength_b.addWidget(self.tb_param_clength)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_param_clength_b.addItem(spacerItem)
        self.verticalLayout.addLayout(self.hl_param_clength_b)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtWidgets.QApplication.translate("Frame", "Frame", None, -1))
        self.t_param_clength.setText(QtWidgets.QApplication.translate("Frame", "Char. length", None, -1))
        self.t_param_clength_desc.setText(QtWidgets.QApplication.translate("Frame", "Characteristic length for the random width generator. Used in mode random and waves.", None, -1))
        self.t_param_clength_helper.setText(QtWidgets.QApplication.translate("Frame", "(0 - inf)", None, -1))

