# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\GitHub\pixelsort\param_slider.ui',
# licensing of 'f:\GitHub\pixelsort\param_slider.ui' applies.
#
# Created: Tue Sep  8 18:41:15 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Param_Slider(object):
    def setupUi(self, Frame, param_name, is_value_display_tb=False):
        self.Frame = Frame
        Frame.setObjectName(f"f_param_{param_name}")
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName(f"vl_param_{param_name}")
        
        self.line = QtWidgets.QFrame(Frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setObjectName(f"line_{param_name}")
        self.verticalLayout.addWidget(self.line)
        
        self.hl_param_generic_t = QtWidgets.QHBoxLayout()
        self.hl_param_generic_t.setSpacing(10)
        self.hl_param_generic_t.setObjectName(f"hl_param_{param_name}_t")
        self.t_param_generic = QtWidgets.QLabel(Frame)
        self.t_param_generic.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.t_param_generic.setObjectName(f"t_param_{param_name}")
        self.hl_param_generic_t.addWidget(self.t_param_generic)
        self.t_param_generic_desc = QtWidgets.QLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_param_generic_desc.sizePolicy().hasHeightForWidth())
        self.t_param_generic_desc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.t_param_generic_desc.setFont(font)
        self.t_param_generic_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.t_param_generic_desc.setObjectName(f"t_param_{param_name}_desc")
        self.t_param_generic_desc.setWordWrap(True)
        self.hl_param_generic_t.addWidget(self.t_param_generic_desc)
        self.verticalLayout.addLayout(self.hl_param_generic_t)
        self.hl_param_generic_b = QtWidgets.QHBoxLayout()
        self.hl_param_generic_b.setObjectName(f"hl_param_{param_name}_b")
        
        if is_value_display_tb:
            self.tb_param_generic_value = QtWidgets.QLineEdit(Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.tb_param_generic_value.sizePolicy().hasHeightForWidth())
            self.tb_param_generic_value.setSizePolicy(sizePolicy)
            self.tb_param_generic_value.setMinimumSize(QtCore.QSize(20, 0))
            self.tb_param_generic_value.setMaximumSize(QtCore.QSize(35, 16777215))
            self.tb_param_generic_value.setText("")
            self.tb_param_generic_value.setObjectName(f"tb_param_{param_name}")
            self.hl_param_generic_b.addWidget(self.tb_param_generic_value)

        else:   # Using Label:
            self.t_param_generic_value = QtWidgets.QLabel(Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.t_param_generic_value.sizePolicy().hasHeightForWidth())
            self.t_param_generic_value.setSizePolicy(sizePolicy)
            self.t_param_generic_value.setMinimumSize(QtCore.QSize(40, 0))
            self.t_param_generic_value.setObjectName(f"t_param_{param_name}_value")
            self.hl_param_generic_b.addWidget(self.t_param_generic_value)

        self.slider_param_generic = QtWidgets.QSlider(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_param_generic.sizePolicy().hasHeightForWidth())
        self.slider_param_generic.setSizePolicy(sizePolicy)
        self.slider_param_generic.setMaximum(100)
        self.slider_param_generic.setProperty("value", 0)
        self.slider_param_generic.setOrientation(QtCore.Qt.Horizontal)
        self.slider_param_generic.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider_param_generic.setTickInterval(10)
        self.slider_param_generic.setObjectName(f"slider_param_{param_name}")
        self.hl_param_generic_b.addWidget(self.slider_param_generic)
        self.verticalLayout.addLayout(self.hl_param_generic_b)

        #self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtWidgets.QApplication.translate("Frame", "Frame", None, -1))
        self.t_param_generic.setText(QtWidgets.QApplication.translate("Frame", "param title", None, -1))
        self.t_param_generic_desc.setText(QtWidgets.QApplication.translate("Frame", "param description", None, -1))
        self.t_param_generic_value.setText(QtWidgets.QApplication.translate("Frame", "param val", None, -1))

