if __name__ == '__main__':
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets
    from Expert_System import Expert_System
    
    app = QtWidgets.QApplication(sys.argv)
    window = Expert_System()
    window.setWindowTitle('Expert System')
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec_())