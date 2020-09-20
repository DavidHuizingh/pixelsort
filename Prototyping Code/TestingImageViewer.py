import sys
from PIL import Image, ImageQt
from pathlib import Path
from time import sleep

from PySide2 import QtWidgets, QtGui, QtCore
from QtImageViewer_Pyside2 import QtImageViewer


from TestViewer import Ui_MainWindow





if __name__ == '__main__':

    # Create the application.
    app = QtWidgets.QApplication(sys.argv)

    # Create image viewer and load an image file to display.
    viewer = QtImageViewer()
    #viewer.loadImageFromFile()  # Pops up file dialog.
    debug_image_main = "images/DSC04688.JPG"

    debug_image_PIL = Image.open(debug_image_main)
    pix_map = debug_image_PIL.toqpixmap()
    viewer.setImage(pix_map)
    
    # Show viewer and run application.
    viewer.show()
    sys.exit(app.exec_())
