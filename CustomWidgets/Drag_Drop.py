
# Solution for PyQt5 below:
# https://www.reddit.com/r/learnpython/comments/97z5dq/pyqt5_drag_and_drop_file_option/
# A PySide2 version, and modified version of the code is below:

import sys
import os
from PySide2 import QtWidgets, QtGui, QtCore


class FileDragDrop(QtWidgets.QLabel):
    def __init__(self, parent):
        super(FileDragDrop, self).__init__(parent)

        self.setAcceptDrops(True)

        self.sorter_image_type = None       # Set during main app's setup to either "main" or "mask"
        self.drop_callback = None           # Also set by main app's setup.

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()
    
    #QtWidgets.QLabel.event

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        #urls = data.urls()
        
        url_paths = [str(url.toLocalFile()) for url in data.urls()]
        
        # callback to method
        try:
            # def images_dropped(self, urls, sorter_image_type, label_wig)
            self.drop_callback(url_paths, self.sorter_image_type)
        except:
            print("drop_callback was not handled correctly.")
        #print(f"FILES DRAGGED IN: {urls}")
        

    def setDropEventCallback(self, method=None):
        '''Pass in a method that should be called when the drop event is triggered.'''

        self.drop_callback = method




        '''
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            # any file type here
            if filepath[-4:].upper() == ".txt":
                self.setText(filepath)
            else:
                dialog = QtWidgets.QMessageBox()
                dialog.setWindowTitle("Error: Invalid File")
                dialog.setText("Only .txt files are accepted")
                dialog.setIcon(QtWidgets.QMessageBox.Warning)
                dialog.exec_()

        '''









# Solution for Pyside 1 below:
# https://gist.github.com/benjaminirving/f45de3bbabbcacd3ca29

'''
class MainWindowWidget(QtGui.QWidget):
    """
    Subclass the widget and add a button to load images. 
    
    Alternatively set up dragging and dropping of image files onto the widget
    """

    def __init__(self):
        super(MainWindowWidget, self).__init__()

        # Button that allows loading of images
        self.load_button = QtGui.QPushButton("Load image")
        self.load_button.clicked.connect(self.load_image_but)

        # Image viewing region
        self.lbl = QtGui.QLabel(self)

        # A horizontal layout to include the button on the left
        layout_button = QtGui.QHBoxLayout()
        layout_button.addWidget(self.load_button)
        layout_button.addStretch()

        # A Vertical layout to include the button layout and then the image
        layout = QtGui.QVBoxLayout()
        layout.addLayout(layout_button)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

        # Enable dragging and dropping onto the GUI
        self.setAcceptDrops(True)

        self.show()

    def load_image_but(self):
        """
        Open a File dialog when the button is pressed
        :return:
        """
        
        #Get the file location
        self.fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        # Load the image from the location
        self.load_image()

    def load_image(self):
        """
        Set the image to the pixmap
        :return:
        """
        pixmap = QtGui.QPixmap(self.fname)
        pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.lbl.setPixmap(pixmap)

    # The following three methods set up dragging and dropping for the app
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        """
        Drop files directly onto the widget
        File locations are stored in fname
        :param e:
        :return:
        """
        if e.mimeData().hasUrls:
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
            # Workaround for OSx dragging and dropping
            for url in e.mimeData().urls():
                if op_sys == 'Darwin':
                    fname = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
                else:
                    fname = str(url.toLocalFile())

            self.fname = fname
            self.load_image()
        else:
            e.ignore()
'''