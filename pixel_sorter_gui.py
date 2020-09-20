# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pixel_sorter_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CustomWidgets.Drag_Drop import FileDragDrop


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 1000)
        MainWindow.setMaximumSize(QSize(1500, 1000))
        self.actionhi = QAction(MainWindow)
        self.actionhi.setObjectName(u"actionhi")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.f_settings_panel = QFrame(self.centralwidget)
        self.f_settings_panel.setObjectName(u"f_settings_panel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_settings_panel.sizePolicy().hasHeightForWidth())
        self.f_settings_panel.setSizePolicy(sizePolicy)
        self.f_settings_panel.setMinimumSize(QSize(460, 460))
        self.f_settings_panel.setMaximumSize(QSize(500, 16777215))
        self.f_settings_panel.setFrameShape(QFrame.NoFrame)
        self.f_settings_panel.setFrameShadow(QFrame.Sunken)
        self.f_settings_panel.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.f_settings_panel)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 0, 2)
        self.scroll_area_settings = QScrollArea(self.f_settings_panel)
        self.scroll_area_settings.setObjectName(u"scroll_area_settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scroll_area_settings.sizePolicy().hasHeightForWidth())
        self.scroll_area_settings.setSizePolicy(sizePolicy1)
        self.scroll_area_settings.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area_settings.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area_settings.setWidgetResizable(True)
        self.scroll_area_settings.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scroll_area_settings_content = QWidget()
        self.scroll_area_settings_content.setObjectName(u"scroll_area_settings_content")
        self.scroll_area_settings_content.setGeometry(QRect(0, 0, 479, 970))
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scroll_area_settings_content.sizePolicy().hasHeightForWidth())
        self.scroll_area_settings_content.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.scroll_area_settings_content)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 5, 10, 5)
        self.line_major_5 = QFrame(self.scroll_area_settings_content)
        self.line_major_5.setObjectName(u"line_major_5")
        self.line_major_5.setWindowModality(Qt.NonModal)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_major_5.sizePolicy().hasHeightForWidth())
        self.line_major_5.setSizePolicy(sizePolicy3)
        self.line_major_5.setFrameShadow(QFrame.Plain)
        self.line_major_5.setLineWidth(2)
        self.line_major_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.line_major_5)

        self.vl_image = QVBoxLayout()
        self.vl_image.setObjectName(u"vl_image")
        self.vl_image.setContentsMargins(2, 2, 2, 2)
        self.hl_header_image = QHBoxLayout()
        self.hl_header_image.setSpacing(20)
        self.hl_header_image.setObjectName(u"hl_header_image")
        self.hl_header_image.setContentsMargins(-1, 0, -1, -1)
        self.t_image = QLabel(self.scroll_area_settings_content)
        self.t_image.setObjectName(u"t_image")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.t_image.sizePolicy().hasHeightForWidth())
        self.t_image.setSizePolicy(sizePolicy4)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.t_image.setFont(font)
        self.t_image.setLayoutDirection(Qt.LeftToRight)
        self.t_image.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.hl_header_image.addWidget(self.t_image)

        self.t_image_desc = QLabel(self.scroll_area_settings_content)
        self.t_image_desc.setObjectName(u"t_image_desc")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.t_image_desc.sizePolicy().hasHeightForWidth())
        self.t_image_desc.setSizePolicy(sizePolicy5)
        font1 = QFont()
        font1.setItalic(True)
        self.t_image_desc.setFont(font1)
        self.t_image_desc.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.t_image_desc.setWordWrap(True)

        self.hl_header_image.addWidget(self.t_image_desc)


        self.vl_image.addLayout(self.hl_header_image)

        self.hl_Image = QHBoxLayout()
        self.hl_Image.setObjectName(u"hl_Image")
        self.hl_Image.setContentsMargins(0, 2, 0, 2)
        self.vl_left = QVBoxLayout()
        self.vl_left.setObjectName(u"vl_left")
        self.vl_left.setContentsMargins(1, 1, 1, 1)
        self.b_choose_image = QPushButton(self.scroll_area_settings_content)
        self.b_choose_image.setObjectName(u"b_choose_image")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.b_choose_image.sizePolicy().hasHeightForWidth())
        self.b_choose_image.setSizePolicy(sizePolicy6)
        self.b_choose_image.setMinimumSize(QSize(100, 30))

        self.vl_left.addWidget(self.b_choose_image)

        self.b_load_current = QPushButton(self.scroll_area_settings_content)
        self.b_load_current.setObjectName(u"b_load_current")
        sizePolicy6.setHeightForWidth(self.b_load_current.sizePolicy().hasHeightForWidth())
        self.b_load_current.setSizePolicy(sizePolicy6)
        self.b_load_current.setMinimumSize(QSize(100, 30))

        self.vl_left.addWidget(self.b_load_current)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_left.addItem(self.verticalSpacer_2)


        self.hl_Image.addLayout(self.vl_left)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_Image.addItem(self.horizontalSpacer_4)

        self.vl_right = QVBoxLayout()
        self.vl_right.setObjectName(u"vl_right")
        self.vl_right.setContentsMargins(2, 2, 2, 2)

        self.hl_Image.addLayout(self.vl_right)

        self.l_loaded_image_preview = FileDragDrop(self.scroll_area_settings_content)
        self.l_loaded_image_preview.setObjectName(u"l_loaded_image_preview")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.l_loaded_image_preview.sizePolicy().hasHeightForWidth())
        self.l_loaded_image_preview.setSizePolicy(sizePolicy7)
        self.l_loaded_image_preview.setMinimumSize(QSize(75, 75))
        self.l_loaded_image_preview.setMaximumSize(QSize(200, 200))
        self.l_loaded_image_preview.setFont(font1)
        self.l_loaded_image_preview.setFrameShape(QFrame.Box)
        self.l_loaded_image_preview.setScaledContents(True)
        self.l_loaded_image_preview.setAlignment(Qt.AlignCenter)

        self.hl_Image.addWidget(self.l_loaded_image_preview)


        self.vl_image.addLayout(self.hl_Image)


        self.verticalLayout_5.addLayout(self.vl_image)

        self.line_major_1 = QFrame(self.scroll_area_settings_content)
        self.line_major_1.setObjectName(u"line_major_1")
        self.line_major_1.setWindowModality(Qt.NonModal)
        sizePolicy3.setHeightForWidth(self.line_major_1.sizePolicy().hasHeightForWidth())
        self.line_major_1.setSizePolicy(sizePolicy3)
        self.line_major_1.setFrameShadow(QFrame.Plain)
        self.line_major_1.setLineWidth(2)
        self.line_major_1.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.line_major_1)

        self.vl_image_mask = QVBoxLayout()
        self.vl_image_mask.setSpacing(2)
        self.vl_image_mask.setObjectName(u"vl_image_mask")
        self.vl_image_mask.setContentsMargins(2, 2, 2, 2)
        self.hl_header_image_mask = QHBoxLayout()
        self.hl_header_image_mask.setSpacing(20)
        self.hl_header_image_mask.setObjectName(u"hl_header_image_mask")
        self.hl_header_image_mask.setContentsMargins(0, 0, -1, -1)
        self.t_image_mask = QLabel(self.scroll_area_settings_content)
        self.t_image_mask.setObjectName(u"t_image_mask")
        sizePolicy4.setHeightForWidth(self.t_image_mask.sizePolicy().hasHeightForWidth())
        self.t_image_mask.setSizePolicy(sizePolicy4)
        self.t_image_mask.setFont(font)
        self.t_image_mask.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.hl_header_image_mask.addWidget(self.t_image_mask)

        self.t_image_mask_desc = QLabel(self.scroll_area_settings_content)
        self.t_image_mask_desc.setObjectName(u"t_image_mask_desc")
        sizePolicy5.setHeightForWidth(self.t_image_mask_desc.sizePolicy().hasHeightForWidth())
        self.t_image_mask_desc.setSizePolicy(sizePolicy5)
        self.t_image_mask_desc.setFont(font1)
        self.t_image_mask_desc.setWordWrap(True)

        self.hl_header_image_mask.addWidget(self.t_image_mask_desc)


        self.vl_image_mask.addLayout(self.hl_header_image_mask)

        self.hl_mask_selection = QHBoxLayout()
        self.hl_mask_selection.setObjectName(u"hl_mask_selection")
        self.rb_mask_none = QRadioButton(self.scroll_area_settings_content)
        self.rb_mask_none.setObjectName(u"rb_mask_none")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.rb_mask_none.sizePolicy().hasHeightForWidth())
        self.rb_mask_none.setSizePolicy(sizePolicy8)

        self.hl_mask_selection.addWidget(self.rb_mask_none)

        self.rb_mask_single = QRadioButton(self.scroll_area_settings_content)
        self.rb_mask_single.setObjectName(u"rb_mask_single")
        sizePolicy8.setHeightForWidth(self.rb_mask_single.sizePolicy().hasHeightForWidth())
        self.rb_mask_single.setSizePolicy(sizePolicy8)
        self.rb_mask_single.setChecked(True)

        self.hl_mask_selection.addWidget(self.rb_mask_single)

        self.rb_mask_folder = QRadioButton(self.scroll_area_settings_content)
        self.rb_mask_folder.setObjectName(u"rb_mask_folder")
        sizePolicy8.setHeightForWidth(self.rb_mask_folder.sizePolicy().hasHeightForWidth())
        self.rb_mask_folder.setSizePolicy(sizePolicy8)

        self.hl_mask_selection.addWidget(self.rb_mask_folder)


        self.vl_image_mask.addLayout(self.hl_mask_selection)

        self.f_hl_mask_none = QFrame(self.scroll_area_settings_content)
        self.f_hl_mask_none.setObjectName(u"f_hl_mask_none")
        sizePolicy8.setHeightForWidth(self.f_hl_mask_none.sizePolicy().hasHeightForWidth())
        self.f_hl_mask_none.setSizePolicy(sizePolicy8)
        self.f_hl_mask_none.setFrameShape(QFrame.NoFrame)
        self.f_hl_mask_none.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.f_hl_mask_none)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.t_no_mask = QLabel(self.f_hl_mask_none)
        self.t_no_mask.setObjectName(u"t_no_mask")
        sizePolicy.setHeightForWidth(self.t_no_mask.sizePolicy().hasHeightForWidth())
        self.t_no_mask.setSizePolicy(sizePolicy)
        self.t_no_mask.setFont(font1)
        self.t_no_mask.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_11.addWidget(self.t_no_mask)


        self.vl_image_mask.addWidget(self.f_hl_mask_none)

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.vl_image_mask.addItem(self.verticalSpacer_6)

        self.f_hl_mask_single = QFrame(self.scroll_area_settings_content)
        self.f_hl_mask_single.setObjectName(u"f_hl_mask_single")
        self.f_hl_mask_single.setFrameShape(QFrame.NoFrame)
        self.f_hl_mask_single.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_12 = QHBoxLayout(self.f_hl_mask_single)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 2, 0, 2)
        self.vl_mask_single_left = QVBoxLayout()
        self.vl_mask_single_left.setObjectName(u"vl_mask_single_left")
        self.vl_mask_single_left.setContentsMargins(0, 0, 0, 0)
        self.b_choose_mask = QPushButton(self.f_hl_mask_single)
        self.b_choose_mask.setObjectName(u"b_choose_mask")
        sizePolicy6.setHeightForWidth(self.b_choose_mask.sizePolicy().hasHeightForWidth())
        self.b_choose_mask.setSizePolicy(sizePolicy6)
        self.b_choose_mask.setMinimumSize(QSize(100, 30))

        self.vl_mask_single_left.addWidget(self.b_choose_mask)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_mask_single_left.addItem(self.verticalSpacer_4)


        self.horizontalLayout_12.addLayout(self.vl_mask_single_left)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.vl_mask_single_right = QVBoxLayout()
        self.vl_mask_single_right.setObjectName(u"vl_mask_single_right")
        self.vl_mask_single_right.setContentsMargins(2, 2, 2, 2)

        self.horizontalLayout_12.addLayout(self.vl_mask_single_right)

        self.l_loaded_mask_preview = FileDragDrop(self.f_hl_mask_single)
        self.l_loaded_mask_preview.setObjectName(u"l_loaded_mask_preview")
        sizePolicy7.setHeightForWidth(self.l_loaded_mask_preview.sizePolicy().hasHeightForWidth())
        self.l_loaded_mask_preview.setSizePolicy(sizePolicy7)
        self.l_loaded_mask_preview.setMinimumSize(QSize(75, 75))
        self.l_loaded_mask_preview.setMaximumSize(QSize(200, 200))
        self.l_loaded_mask_preview.setFont(font1)
        self.l_loaded_mask_preview.setFrameShape(QFrame.Box)
        self.l_loaded_mask_preview.setScaledContents(True)
        self.l_loaded_mask_preview.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.l_loaded_mask_preview)


        self.vl_image_mask.addWidget(self.f_hl_mask_single)

        self.f_vl_mask_folder = QFrame(self.scroll_area_settings_content)
        self.f_vl_mask_folder.setObjectName(u"f_vl_mask_folder")
        self.f_vl_mask_folder.setFrameShape(QFrame.NoFrame)
        self.f_vl_mask_folder.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.f_vl_mask_folder)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 2, 0, 2)
        self.t_mask_folder_info_header = QLabel(self.f_vl_mask_folder)
        self.t_mask_folder_info_header.setObjectName(u"t_mask_folder_info_header")
        sizePolicy8.setHeightForWidth(self.t_mask_folder_info_header.sizePolicy().hasHeightForWidth())
        self.t_mask_folder_info_header.setSizePolicy(sizePolicy8)
        self.t_mask_folder_info_header.setFont(font1)
        self.t_mask_folder_info_header.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.t_mask_folder_info_header)

        self.hl_mask_folder = QHBoxLayout()
        self.hl_mask_folder.setObjectName(u"hl_mask_folder")
        self.hl_mask_folder.setContentsMargins(2, 2, 2, 2)
        self.vl_mask_folder_left = QVBoxLayout()
        self.vl_mask_folder_left.setObjectName(u"vl_mask_folder_left")
        self.vl_mask_folder_left.setContentsMargins(2, 2, 2, 2)
        self.b_choose_mask_folder = QPushButton(self.f_vl_mask_folder)
        self.b_choose_mask_folder.setObjectName(u"b_choose_mask_folder")
        sizePolicy6.setHeightForWidth(self.b_choose_mask_folder.sizePolicy().hasHeightForWidth())
        self.b_choose_mask_folder.setSizePolicy(sizePolicy6)
        self.b_choose_mask_folder.setMinimumSize(QSize(100, 30))

        self.vl_mask_folder_left.addWidget(self.b_choose_mask_folder)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vl_mask_folder_left.addItem(self.verticalSpacer_7)


        self.hl_mask_folder.addLayout(self.vl_mask_folder_left)

        self.vl_mask_folder_right = QVBoxLayout()
        self.vl_mask_folder_right.setObjectName(u"vl_mask_folder_right")
        self.vl_mask_folder_right.setContentsMargins(2, 2, 2, 2)
        self.t_found_masks = QLabel(self.f_vl_mask_folder)
        self.t_found_masks.setObjectName(u"t_found_masks")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.t_found_masks.sizePolicy().hasHeightForWidth())
        self.t_found_masks.setSizePolicy(sizePolicy9)
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(True)
        font2.setWeight(50)
        self.t_found_masks.setFont(font2)

        self.vl_mask_folder_right.addWidget(self.t_found_masks)

        self.scrollArea = QScrollArea(self.f_vl_mask_folder)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy10)
        self.scrollArea.setWidgetResizable(True)
        self.scroll_area_found_masks = QWidget()
        self.scroll_area_found_masks.setObjectName(u"scroll_area_found_masks")
        self.scroll_area_found_masks.setGeometry(QRect(0, 0, 335, 69))
        self.gridLayout = QGridLayout(self.scroll_area_found_masks)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.vl_found_masks = QVBoxLayout()
        self.vl_found_masks.setSpacing(2)
        self.vl_found_masks.setObjectName(u"vl_found_masks")
        self.verticalSpacer_found_mask_area = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.vl_found_masks.addItem(self.verticalSpacer_found_mask_area)


        self.gridLayout.addLayout(self.vl_found_masks, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scroll_area_found_masks)

        self.vl_mask_folder_right.addWidget(self.scrollArea)


        self.hl_mask_folder.addLayout(self.vl_mask_folder_right)


        self.verticalLayout_3.addLayout(self.hl_mask_folder)


        self.vl_image_mask.addWidget(self.f_vl_mask_folder)


        self.verticalLayout_5.addLayout(self.vl_image_mask)

        self.line_major_2 = QFrame(self.scroll_area_settings_content)
        self.line_major_2.setObjectName(u"line_major_2")
        self.line_major_2.setWindowModality(Qt.NonModal)
        sizePolicy3.setHeightForWidth(self.line_major_2.sizePolicy().hasHeightForWidth())
        self.line_major_2.setSizePolicy(sizePolicy3)
        self.line_major_2.setFrameShadow(QFrame.Plain)
        self.line_major_2.setLineWidth(2)
        self.line_major_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.line_major_2)

        self.vl_interval_function = QVBoxLayout()
        self.vl_interval_function.setObjectName(u"vl_interval_function")
        self.vl_interval_function.setContentsMargins(2, 2, 2, 2)
        self.hl_header_interval_sorting = QHBoxLayout()
        self.hl_header_interval_sorting.setSpacing(20)
        self.hl_header_interval_sorting.setObjectName(u"hl_header_interval_sorting")
        self.hl_header_interval_sorting.setContentsMargins(-1, 0, -1, -1)
        self.t_interval_sorting = QLabel(self.scroll_area_settings_content)
        self.t_interval_sorting.setObjectName(u"t_interval_sorting")
        sizePolicy4.setHeightForWidth(self.t_interval_sorting.sizePolicy().hasHeightForWidth())
        self.t_interval_sorting.setSizePolicy(sizePolicy4)
        self.t_interval_sorting.setFont(font)
        self.t_interval_sorting.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.hl_header_interval_sorting.addWidget(self.t_interval_sorting)

        self.t_interval_sorting_desc = QLabel(self.scroll_area_settings_content)
        self.t_interval_sorting_desc.setObjectName(u"t_interval_sorting_desc")
        sizePolicy5.setHeightForWidth(self.t_interval_sorting_desc.sizePolicy().hasHeightForWidth())
        self.t_interval_sorting_desc.setSizePolicy(sizePolicy5)
        self.t_interval_sorting_desc.setFont(font1)

        self.hl_header_interval_sorting.addWidget(self.t_interval_sorting_desc)


        self.vl_interval_function.addLayout(self.hl_header_interval_sorting)

        self.hl_interval_function = QHBoxLayout()
        self.hl_interval_function.setSpacing(20)
        self.hl_interval_function.setObjectName(u"hl_interval_function")
        self.hl_interval_function.setContentsMargins(-1, 0, -1, -1)
        self.cb_interval_function = QComboBox(self.scroll_area_settings_content)
        self.cb_interval_function.setObjectName(u"cb_interval_function")
        sizePolicy4.setHeightForWidth(self.cb_interval_function.sizePolicy().hasHeightForWidth())
        self.cb_interval_function.setSizePolicy(sizePolicy4)
        self.cb_interval_function.setMinimumSize(QSize(90, 0))
        self.cb_interval_function.setEditable(False)
        self.cb_interval_function.setFrame(True)

        self.hl_interval_function.addWidget(self.cb_interval_function)

        self.t_interval_function_desc = QLabel(self.scroll_area_settings_content)
        self.t_interval_function_desc.setObjectName(u"t_interval_function_desc")
        self.t_interval_function_desc.setFont(font1)
        self.t_interval_function_desc.setWordWrap(True)

        self.hl_interval_function.addWidget(self.t_interval_function_desc)


        self.vl_interval_function.addLayout(self.hl_interval_function)

        self.hl_parameters_indent = QHBoxLayout()
        self.hl_parameters_indent.setObjectName(u"hl_parameters_indent")
        self.hl_parameters_indent.setContentsMargins(0, 2, 0, 2)
        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.hl_parameters_indent.addItem(self.horizontalSpacer_2)

        self.line_3 = QFrame(self.scroll_area_settings_content)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QFrame.VLine)

        self.hl_parameters_indent.addWidget(self.line_3)

        self.vl_parameters_shell = QVBoxLayout()
        self.vl_parameters_shell.setSpacing(2)
        self.vl_parameters_shell.setObjectName(u"vl_parameters_shell")
        self.line = QFrame(self.scroll_area_settings_content)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.vl_parameters_shell.addWidget(self.line)

        self.hl_parameters_subtitle = QHBoxLayout()
        self.hl_parameters_subtitle.setObjectName(u"hl_parameters_subtitle")
        self.t_parameters_subtitle = QLabel(self.scroll_area_settings_content)
        self.t_parameters_subtitle.setObjectName(u"t_parameters_subtitle")
        sizePolicy.setHeightForWidth(self.t_parameters_subtitle.sizePolicy().hasHeightForWidth())
        self.t_parameters_subtitle.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setItalic(True)
        font3.setUnderline(False)
        self.t_parameters_subtitle.setFont(font3)
        self.t_parameters_subtitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.hl_parameters_subtitle.addWidget(self.t_parameters_subtitle)

        self.b_load_current_2 = QPushButton(self.scroll_area_settings_content)
        self.b_load_current_2.setObjectName(u"b_load_current_2")
        sizePolicy6.setHeightForWidth(self.b_load_current_2.sizePolicy().hasHeightForWidth())
        self.b_load_current_2.setSizePolicy(sizePolicy6)
        self.b_load_current_2.setMinimumSize(QSize(100, 30))

        self.hl_parameters_subtitle.addWidget(self.b_load_current_2)


        self.vl_parameters_shell.addLayout(self.hl_parameters_subtitle)

        self.vl_parameters = QVBoxLayout()
        self.vl_parameters.setObjectName(u"vl_parameters")
        self.vl_parameters.setContentsMargins(0, 2, 0, 2)

        self.vl_parameters_shell.addLayout(self.vl_parameters)


        self.hl_parameters_indent.addLayout(self.vl_parameters_shell)


        self.vl_interval_function.addLayout(self.hl_parameters_indent)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.vl_interval_function.addItem(self.verticalSpacer_5)


        self.verticalLayout_5.addLayout(self.vl_interval_function)

        self.line_major_3 = QFrame(self.scroll_area_settings_content)
        self.line_major_3.setObjectName(u"line_major_3")
        self.line_major_3.setWindowModality(Qt.NonModal)
        sizePolicy3.setHeightForWidth(self.line_major_3.sizePolicy().hasHeightForWidth())
        self.line_major_3.setSizePolicy(sizePolicy3)
        self.line_major_3.setFrameShadow(QFrame.Plain)
        self.line_major_3.setLineWidth(2)
        self.line_major_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.line_major_3)

        self.vl_pixel_ordering = QVBoxLayout()
        self.vl_pixel_ordering.setObjectName(u"vl_pixel_ordering")
        self.vl_pixel_ordering.setContentsMargins(2, 2, 2, 2)
        self.hl_header_pixel_ordering = QHBoxLayout()
        self.hl_header_pixel_ordering.setSpacing(20)
        self.hl_header_pixel_ordering.setObjectName(u"hl_header_pixel_ordering")
        self.t_pixel_ordering = QLabel(self.scroll_area_settings_content)
        self.t_pixel_ordering.setObjectName(u"t_pixel_ordering")
        sizePolicy4.setHeightForWidth(self.t_pixel_ordering.sizePolicy().hasHeightForWidth())
        self.t_pixel_ordering.setSizePolicy(sizePolicy4)
        self.t_pixel_ordering.setFont(font)
        self.t_pixel_ordering.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.hl_header_pixel_ordering.addWidget(self.t_pixel_ordering)

        self.t_pixel_ordering_desc = QLabel(self.scroll_area_settings_content)
        self.t_pixel_ordering_desc.setObjectName(u"t_pixel_ordering_desc")
        sizePolicy5.setHeightForWidth(self.t_pixel_ordering_desc.sizePolicy().hasHeightForWidth())
        self.t_pixel_ordering_desc.setSizePolicy(sizePolicy5)
        self.t_pixel_ordering_desc.setFont(font1)
        self.t_pixel_ordering_desc.setWordWrap(True)

        self.hl_header_pixel_ordering.addWidget(self.t_pixel_ordering_desc)


        self.vl_pixel_ordering.addLayout(self.hl_header_pixel_ordering)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.cb_pixel_ordering_option = QComboBox(self.scroll_area_settings_content)
        self.cb_pixel_ordering_option.setObjectName(u"cb_pixel_ordering_option")
        sizePolicy4.setHeightForWidth(self.cb_pixel_ordering_option.sizePolicy().hasHeightForWidth())
        self.cb_pixel_ordering_option.setSizePolicy(sizePolicy4)
        self.cb_pixel_ordering_option.setMinimumSize(QSize(80, 0))
        self.cb_pixel_ordering_option.setEditable(False)
        self.cb_pixel_ordering_option.setFrame(True)

        self.horizontalLayout_6.addWidget(self.cb_pixel_ordering_option)

        self.t_pixel_ordering_option_desc = QLabel(self.scroll_area_settings_content)
        self.t_pixel_ordering_option_desc.setObjectName(u"t_pixel_ordering_option_desc")
        sizePolicy5.setHeightForWidth(self.t_pixel_ordering_option_desc.sizePolicy().hasHeightForWidth())
        self.t_pixel_ordering_option_desc.setSizePolicy(sizePolicy5)
        self.t_pixel_ordering_option_desc.setFont(font1)
        self.t_pixel_ordering_option_desc.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.t_pixel_ordering_option_desc)


        self.vl_pixel_ordering.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addLayout(self.vl_pixel_ordering)

        self.line_major_4 = QFrame(self.scroll_area_settings_content)
        self.line_major_4.setObjectName(u"line_major_4")
        self.line_major_4.setWindowModality(Qt.NonModal)
        sizePolicy3.setHeightForWidth(self.line_major_4.sizePolicy().hasHeightForWidth())
        self.line_major_4.setSizePolicy(sizePolicy3)
        self.line_major_4.setFrameShadow(QFrame.Plain)
        self.line_major_4.setLineWidth(2)
        self.line_major_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.line_major_4)

        self.vl_save_location = QVBoxLayout()
        self.vl_save_location.setObjectName(u"vl_save_location")
        self.vl_save_location.setContentsMargins(2, 2, 2, 2)
        self.hl_header_image_output = QHBoxLayout()
        self.hl_header_image_output.setSpacing(20)
        self.hl_header_image_output.setObjectName(u"hl_header_image_output")
        self.t_image_output = QLabel(self.scroll_area_settings_content)
        self.t_image_output.setObjectName(u"t_image_output")
        sizePolicy4.setHeightForWidth(self.t_image_output.sizePolicy().hasHeightForWidth())
        self.t_image_output.setSizePolicy(sizePolicy4)
        self.t_image_output.setFont(font)
        self.t_image_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.hl_header_image_output.addWidget(self.t_image_output)

        self.t_save_location_desc = QLabel(self.scroll_area_settings_content)
        self.t_save_location_desc.setObjectName(u"t_save_location_desc")
        sizePolicy5.setHeightForWidth(self.t_save_location_desc.sizePolicy().hasHeightForWidth())
        self.t_save_location_desc.setSizePolicy(sizePolicy5)
        self.t_save_location_desc.setFont(font1)
        self.t_save_location_desc.setWordWrap(True)

        self.hl_header_image_output.addWidget(self.t_save_location_desc)


        self.vl_save_location.addLayout(self.hl_header_image_output)

        self.vl_generation = QVBoxLayout()
        self.vl_generation.setObjectName(u"vl_generation")
        self.vl_generation.setContentsMargins(2, 2, 2, 2)
        self.hl_generation_2 = QHBoxLayout()
        self.hl_generation_2.setObjectName(u"hl_generation_2")
        self.vl_sort_options = QVBoxLayout()
        self.vl_sort_options.setObjectName(u"vl_sort_options")
        self.t_sort_image_title = QLabel(self.scroll_area_settings_content)
        self.t_sort_image_title.setObjectName(u"t_sort_image_title")
        self.t_sort_image_title.setFont(font2)

        self.vl_sort_options.addWidget(self.t_sort_image_title)

        self.cb_sort_option_preview = QCheckBox(self.scroll_area_settings_content)
        self.cb_sort_option_preview.setObjectName(u"cb_sort_option_preview")

        self.vl_sort_options.addWidget(self.cb_sort_option_preview)

        self.cb_live_preview = QCheckBox(self.scroll_area_settings_content)
        self.cb_live_preview.setObjectName(u"cb_live_preview")
        sizePolicy11 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.cb_live_preview.sizePolicy().hasHeightForWidth())
        self.cb_live_preview.setSizePolicy(sizePolicy11)

        self.vl_sort_options.addWidget(self.cb_live_preview)


        self.hl_generation_2.addLayout(self.vl_sort_options)

        self.vl_post_sort_options = QVBoxLayout()
        self.vl_post_sort_options.setObjectName(u"vl_post_sort_options")
        self.t_post_sort_after_image_sort = QLabel(self.scroll_area_settings_content)
        self.t_post_sort_after_image_sort.setObjectName(u"t_post_sort_after_image_sort")
        self.t_post_sort_after_image_sort.setFont(font2)

        self.vl_post_sort_options.addWidget(self.t_post_sort_after_image_sort)

        self.cb_post_sort_option_save_on_create = QCheckBox(self.scroll_area_settings_content)
        self.cb_post_sort_option_save_on_create.setObjectName(u"cb_post_sort_option_save_on_create")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.cb_post_sort_option_save_on_create.sizePolicy().hasHeightForWidth())
        self.cb_post_sort_option_save_on_create.setSizePolicy(sizePolicy12)

        self.vl_post_sort_options.addWidget(self.cb_post_sort_option_save_on_create)

        self.cb_post_sort_option_picture_viewer = QCheckBox(self.scroll_area_settings_content)
        self.cb_post_sort_option_picture_viewer.setObjectName(u"cb_post_sort_option_picture_viewer")
        sizePolicy12.setHeightForWidth(self.cb_post_sort_option_picture_viewer.sizePolicy().hasHeightForWidth())
        self.cb_post_sort_option_picture_viewer.setSizePolicy(sizePolicy12)

        self.vl_post_sort_options.addWidget(self.cb_post_sort_option_picture_viewer)


        self.hl_generation_2.addLayout(self.vl_post_sort_options)


        self.vl_generation.addLayout(self.hl_generation_2)

        self.hl_generation = QHBoxLayout()
        self.hl_generation.setSpacing(6)
        self.hl_generation.setObjectName(u"hl_generation")
        self.b_generate_pixel_sort = QPushButton(self.scroll_area_settings_content)
        self.b_generate_pixel_sort.setObjectName(u"b_generate_pixel_sort")
        sizePolicy6.setHeightForWidth(self.b_generate_pixel_sort.sizePolicy().hasHeightForWidth())
        self.b_generate_pixel_sort.setSizePolicy(sizePolicy6)
        self.b_generate_pixel_sort.setMinimumSize(QSize(100, 30))

        self.hl_generation.addWidget(self.b_generate_pixel_sort)

        self.horizontalSpacer_7 = QSpacerItem(8, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.hl_generation.addItem(self.horizontalSpacer_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.t_image_size_note = QLabel(self.scroll_area_settings_content)
        self.t_image_size_note.setObjectName(u"t_image_size_note")
        sizePolicy2.setHeightForWidth(self.t_image_size_note.sizePolicy().hasHeightForWidth())
        self.t_image_size_note.setSizePolicy(sizePolicy2)
        self.t_image_size_note.setFont(font1)
        self.t_image_size_note.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.t_image_size_note)

        self.t_image_size_warning_dynamic = QLabel(self.scroll_area_settings_content)
        self.t_image_size_warning_dynamic.setObjectName(u"t_image_size_warning_dynamic")
        sizePolicy.setHeightForWidth(self.t_image_size_warning_dynamic.sizePolicy().hasHeightForWidth())
        self.t_image_size_warning_dynamic.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 127, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        brush2 = QBrush(QColor(255, 63, 63, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(127, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(170, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush5)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.t_image_size_warning_dynamic.setPalette(palette)
        self.t_image_size_warning_dynamic.setFont(font1)
        self.t_image_size_warning_dynamic.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.t_image_size_warning_dynamic)


        self.hl_generation.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_5 = QSpacerItem(14, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.hl_generation.addItem(self.horizontalSpacer_5)


        self.vl_generation.addLayout(self.hl_generation)

        self.line_4 = QFrame(self.scroll_area_settings_content)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.HLine)

        self.vl_generation.addWidget(self.line_4)

        self.hl_save_location = QHBoxLayout()
        self.hl_save_location.setSpacing(2)
        self.hl_save_location.setObjectName(u"hl_save_location")
        self.b_save_image = QPushButton(self.scroll_area_settings_content)
        self.b_save_image.setObjectName(u"b_save_image")
        sizePolicy6.setHeightForWidth(self.b_save_image.sizePolicy().hasHeightForWidth())
        self.b_save_image.setSizePolicy(sizePolicy6)
        self.b_save_image.setMinimumSize(QSize(100, 30))

        self.hl_save_location.addWidget(self.b_save_image)

        self.horizontalSpacer_8 = QSpacerItem(16, 13, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.hl_save_location.addItem(self.horizontalSpacer_8)

        self.t_save_location_current_static = QLabel(self.scroll_area_settings_content)
        self.t_save_location_current_static.setObjectName(u"t_save_location_current_static")
        sizePolicy.setHeightForWidth(self.t_save_location_current_static.sizePolicy().hasHeightForWidth())
        self.t_save_location_current_static.setSizePolicy(sizePolicy)
        self.t_save_location_current_static.setFont(font1)
        self.t_save_location_current_static.setWordWrap(True)

        self.hl_save_location.addWidget(self.t_save_location_current_static)

        self.t_save_location_current = QLabel(self.scroll_area_settings_content)
        self.t_save_location_current.setObjectName(u"t_save_location_current")
        sizePolicy2.setHeightForWidth(self.t_save_location_current.sizePolicy().hasHeightForWidth())
        self.t_save_location_current.setSizePolicy(sizePolicy2)
        self.t_save_location_current.setFont(font1)
        self.t_save_location_current.setWordWrap(True)

        self.hl_save_location.addWidget(self.t_save_location_current)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.hl_save_location.addItem(self.horizontalSpacer_9)

        self.b_choose_save_location = QToolButton(self.scroll_area_settings_content)
        self.b_choose_save_location.setObjectName(u"b_choose_save_location")

        self.hl_save_location.addWidget(self.b_choose_save_location)


        self.vl_generation.addLayout(self.hl_save_location)


        self.vl_save_location.addLayout(self.vl_generation)

        self.verticalSpacer_9 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.vl_save_location.addItem(self.verticalSpacer_9)


        self.verticalLayout_5.addLayout(self.vl_save_location)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.scroll_area_settings.setWidget(self.scroll_area_settings_content)

        self.verticalLayout.addWidget(self.scroll_area_settings)


        self.horizontalLayout.addWidget(self.f_settings_panel)

        self.f_preview_panel = QFrame(self.centralwidget)
        self.f_preview_panel.setObjectName(u"f_preview_panel")
        self.f_preview_panel.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.f_preview_panel.sizePolicy().hasHeightForWidth())
        self.f_preview_panel.setSizePolicy(sizePolicy2)
        self.f_preview_panel.setAutoFillBackground(False)
        self.f_preview_panel.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.f_preview_panel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.hl_image_preview_top = QHBoxLayout()
        self.hl_image_preview_top.setObjectName(u"hl_image_preview_top")
        self.hl_image_preview_top.setContentsMargins(-1, 0, -1, -1)
        self.t_image_preview_orig_name_dyn = QLabel(self.f_preview_panel)
        self.t_image_preview_orig_name_dyn.setObjectName(u"t_image_preview_orig_name_dyn")
        sizePolicy.setHeightForWidth(self.t_image_preview_orig_name_dyn.sizePolicy().hasHeightForWidth())
        self.t_image_preview_orig_name_dyn.setSizePolicy(sizePolicy)
        self.t_image_preview_orig_name_dyn.setMinimumSize(QSize(150, 0))
        self.t_image_preview_orig_name_dyn.setMaximumSize(QSize(16777215, 25))
        font4 = QFont()
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.t_image_preview_orig_name_dyn.setFont(font4)

        self.hl_image_preview_top.addWidget(self.t_image_preview_orig_name_dyn)

        self.t_image_preview_sizes_dyn = QLabel(self.f_preview_panel)
        self.t_image_preview_sizes_dyn.setObjectName(u"t_image_preview_sizes_dyn")
        sizePolicy.setHeightForWidth(self.t_image_preview_sizes_dyn.sizePolicy().hasHeightForWidth())
        self.t_image_preview_sizes_dyn.setSizePolicy(sizePolicy)
        self.t_image_preview_sizes_dyn.setMinimumSize(QSize(150, 0))
        self.t_image_preview_sizes_dyn.setMaximumSize(QSize(16777215, 25))
        self.t_image_preview_sizes_dyn.setFont(font4)

        self.hl_image_preview_top.addWidget(self.t_image_preview_sizes_dyn)

        self.t_image_preview_ratio_dyn = QLabel(self.f_preview_panel)
        self.t_image_preview_ratio_dyn.setObjectName(u"t_image_preview_ratio_dyn")
        self.t_image_preview_ratio_dyn.setMinimumSize(QSize(150, 0))
        self.t_image_preview_ratio_dyn.setMaximumSize(QSize(16777215, 25))
        self.t_image_preview_ratio_dyn.setFont(font4)

        self.hl_image_preview_top.addWidget(self.t_image_preview_ratio_dyn)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.hl_image_preview_top.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addLayout(self.hl_image_preview_top)

        self.line_2 = QFrame(self.f_preview_panel)
        self.line_2.setObjectName(u"line_2")
        sizePolicy13 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy13)
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_2)

        self.gv_image_display = QGraphicsView(self.f_preview_panel)
        self.gv_image_display.setObjectName(u"gv_image_display")
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.gv_image_display.sizePolicy().hasHeightForWidth())
        self.gv_image_display.setSizePolicy(sizePolicy14)
        self.gv_image_display.setMinimumSize(QSize(400, 200))
        self.gv_image_display.setMaximumSize(QSize(1500, 1000))
        self.gv_image_display.setFrameShape(QFrame.NoFrame)
        self.gv_image_display.setFrameShadow(QFrame.Plain)
        self.gv_image_display.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.gv_image_display)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalSpacer = QSpacerItem(1, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.hl_image_preview_bottom = QHBoxLayout()
        self.hl_image_preview_bottom.setObjectName(u"hl_image_preview_bottom")
        self.horizontalSpacer_3 = QSpacerItem(5, 5, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.hl_image_preview_bottom.addItem(self.horizontalSpacer_3)

        self.b_open_in_native_viewer = QPushButton(self.f_preview_panel)
        self.b_open_in_native_viewer.setObjectName(u"b_open_in_native_viewer")
        sizePolicy6.setHeightForWidth(self.b_open_in_native_viewer.sizePolicy().hasHeightForWidth())
        self.b_open_in_native_viewer.setSizePolicy(sizePolicy6)
        self.b_open_in_native_viewer.setMinimumSize(QSize(100, 30))

        self.hl_image_preview_bottom.addWidget(self.b_open_in_native_viewer)


        self.verticalLayout_2.addLayout(self.hl_image_preview_bottom)


        self.horizontalLayout.addWidget(self.f_preview_panel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionhi.setText(QCoreApplication.translate("MainWindow", u"hi", None))
        self.t_image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.t_image_desc.setText(QCoreApplication.translate("MainWindow", u"*Required* This is the image that will have pixel sorting applied to it. JPG, PNG, TIFF, etc.", None))
        self.b_choose_image.setText(QCoreApplication.translate("MainWindow", u"Choose Image", None))
        self.b_load_current.setText(QCoreApplication.translate("MainWindow", u"Load Current", None))
        self.l_loaded_image_preview.setText(QCoreApplication.translate("MainWindow", u"Loaded image will display here", None))
        self.t_image_mask.setText(QCoreApplication.translate("MainWindow", u"Image Mask", None))
        self.t_image_mask_desc.setText(QCoreApplication.translate("MainWindow", u"Image used for masking parts of the image. Must be black and white.", None))
        self.rb_mask_none.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.rb_mask_single.setText(QCoreApplication.translate("MainWindow", u"Single Mask", None))
        self.rb_mask_folder.setText(QCoreApplication.translate("MainWindow", u"Masks from Folder", None))
        self.t_no_mask.setText(QCoreApplication.translate("MainWindow", u"No mask image will be used.", None))
        self.b_choose_mask.setText(QCoreApplication.translate("MainWindow", u"Choose Image", None))
        self.l_loaded_mask_preview.setText(QCoreApplication.translate("MainWindow", u"Loaded mask will display here", None))
        self.t_mask_folder_info_header.setText(QCoreApplication.translate("MainWindow", u"Note: If the loaded image is in found in the mask folder it will be ignored.", None))
        self.b_choose_mask_folder.setText(QCoreApplication.translate("MainWindow", u"Choose Folder", None))
        self.t_found_masks.setText(QCoreApplication.translate("MainWindow", u"Found Masks:", None))
        self.t_interval_sorting.setText(QCoreApplication.translate("MainWindow", u"Interval Sorting", None))
        self.t_interval_sorting_desc.setText(QCoreApplication.translate("MainWindow", u"Controls how the intervals used for sorting are defined.", None))
        self.t_interval_function_desc.setText(QCoreApplication.translate("MainWindow", u"(description)", None))
        self.t_parameters_subtitle.setText(QCoreApplication.translate("MainWindow", u"Parameters:", None))
#if QT_CONFIG(tooltip)
        self.b_load_current_2.setToolTip(QCoreApplication.translate("MainWindow", u"Save the current settings as the default for next time.", None))
#endif // QT_CONFIG(tooltip)
        self.b_load_current_2.setText(QCoreApplication.translate("MainWindow", u"Save as Default", None))
        self.t_pixel_ordering.setText(QCoreApplication.translate("MainWindow", u"Pixel Ordering", None))
        self.t_pixel_ordering_desc.setText(QCoreApplication.translate("MainWindow", u"Way in which the pixels are ordered.", None))
        self.t_pixel_ordering_option_desc.setText(QCoreApplication.translate("MainWindow", u"(description)", None))
        self.t_image_output.setText(QCoreApplication.translate("MainWindow", u"Image Output", None))
        self.t_save_location_desc.setText(QCoreApplication.translate("MainWindow", u"The fun part!", None))
        self.t_sort_image_title.setText(QCoreApplication.translate("MainWindow", u"Image Settings", None))
#if QT_CONFIG(tooltip)
        self.cb_sort_option_preview.setToolTip(QCoreApplication.translate("MainWindow", u"Will save files as soon as they are created", None))
#endif // QT_CONFIG(tooltip)
        self.cb_sort_option_preview.setText(QCoreApplication.translate("MainWindow", u"Preview Mode (1000px)", None))
        self.cb_live_preview.setText(QCoreApplication.translate("MainWindow", u"Live Preview (auto-updating 200px)", None))
        self.t_post_sort_after_image_sort.setText(QCoreApplication.translate("MainWindow", u"After image(s) are sorted:", None))
#if QT_CONFIG(tooltip)
        self.cb_post_sort_option_save_on_create.setToolTip(QCoreApplication.translate("MainWindow", u"Will save files as soon as they are created", None))
#endif // QT_CONFIG(tooltip)
        self.cb_post_sort_option_save_on_create.setText(QCoreApplication.translate("MainWindow", u"Save image(s)", None))
#if QT_CONFIG(tooltip)
        self.cb_post_sort_option_picture_viewer.setToolTip(QCoreApplication.translate("MainWindow", u"Will save files as soon as they are created", None))
#endif // QT_CONFIG(tooltip)
        self.cb_post_sort_option_picture_viewer.setText(QCoreApplication.translate("MainWindow", u"Open in native picture viewer", None))
        self.b_generate_pixel_sort.setText(QCoreApplication.translate("MainWindow", u"Pixel Sort!", None))
        self.t_image_size_note.setText(QCoreApplication.translate("MainWindow", u"Note: Depending on the size of the image this could take a few seconds to several minutes.", None))
        self.t_image_size_warning_dynamic.setText(QCoreApplication.translate("MainWindow", u"(image size warning)", None))
        self.b_save_image.setText(QCoreApplication.translate("MainWindow", u"Save Sorted Image", None))
        self.t_save_location_current_static.setText(QCoreApplication.translate("MainWindow", u"Current Folder: ", None))
        self.t_save_location_current.setText(QCoreApplication.translate("MainWindow", u"(save location)", None))
        self.b_choose_save_location.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.t_image_preview_orig_name_dyn.setText(QCoreApplication.translate("MainWindow", u"(image name)", None))
        self.t_image_preview_sizes_dyn.setText(QCoreApplication.translate("MainWindow", u"(image size)", None))
        self.t_image_preview_ratio_dyn.setText(QCoreApplication.translate("MainWindow", u"(image ratio)", None))
        self.b_open_in_native_viewer.setText(QCoreApplication.translate("MainWindow", u"Open in Viewer", None))
    # retranslateUi

