from controller_Project_2 import *


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.setStyle(QStyleFactory.create('Fusion'))
    app.exec_()


if __name__ == '__main__':
    main()
    