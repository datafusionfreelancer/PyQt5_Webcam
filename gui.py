
# Webcam Control

from  cameraX import WebcamX


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QFrame
from PyQt5.QtCore import QSize, QRect, Qt, QThread, QTimer
from PyQt5.QtGui import QFont, QPixmap, QImage

import sys

class appGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.webcam = WebcamX()
        self.init_gui()

    def init_gui(self):
        
        # Height, Width for QMainWindow
        mw_height = 700
        mw_width = 1000
        # Resize for QMainWindow
        self.resize(mw_width,mw_height)
        # Fixed Size for QMainWindow
        self.setMinimumSize(QSize(mw_width,mw_height))
        self.setMaximumSize(QSize(mw_width,mw_height))
        # Title for QMainWindow
        self.setWindowTitle("PYTHON 3.6.8 - QT 5.13.1 - OPENCV 4.1.1-pre - WEBCAM - PROJECT by Umit Kacar")

        # Define QWidget
        self.centralWidget = QWidget(self)
        # Resize for QWidget  
        self.centralWidget.resize(mw_width,mw_height)

        # Define QFont
        self.font = QFont()
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)

        # Define QPushButtons
        self.pushButton_open_camera = QPushButton("Open Camera",self.centralWidget)
        self.pushButton_open_camera.setGeometry(QRect(260, 50, 151, 50))
        self.pushButton_open_camera.setFont(self.font)

        self.pushButton_close_camera = QPushButton("Close Camera",self.centralWidget)
        self.pushButton_close_camera.setGeometry(QRect(80, 50, 161, 51))
        self.pushButton_close_camera.setFont(self.font)

        # Define QLABEL for WEBCAM frame
        self.label_img = QLabel(self.centralWidget)
        self.label_img.setGeometry(QRect(50, 130, 640, 480))
        self.label_img.setFrameShape(QFrame.Box)
        self.label_img.setText("")

        # SIGNALS
        self.pushButton_open_camera.clicked.connect(self.on_pushButton_open_camera_clicked)
        self.pushButton_close_camera.clicked.connect(self.on_pushButton_close_camera_clicked)

        # Timer for update frame
        self.acquisition_timer = QTimer()
        self.acquisition_timer.timeout.connect(self.update_frame)

    def on_pushButton_open_camera_clicked(self):
        self.webcam.acquisition()
        self.acquisition_timer.start(1)
                                                       
    def on_pushButton_close_camera_clicked(self):
        self.webcam.close()
        self.acquisition_timer.stop()

    def update_frame(self):
        self.frame = self.webcam.get_frame()
        self.show_frame()

    def show_frame(self):  
        QImg = QImage(self.frame.data, self.frame.shape[1], self.frame.shape[0], QImage.Format_RGB888)
        pixMap = QPixmap.fromImage(QImg)
        #pixMap = pixMap.scaled(320,240, Qt.KeepAspectRatio)
        self.label_img.setPixmap(pixMap)
        
if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = appGUI()
    w.show()

    sys.exit(app.exec_())
