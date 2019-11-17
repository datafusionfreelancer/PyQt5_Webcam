

# Webcam Control


from gui import appGUI
import sys



from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = appGUI()
    w.show()

    sys.exit(app.exec_())

