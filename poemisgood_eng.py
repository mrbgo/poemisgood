from sys import argv, exit
from PyQt6 import QtCore, QtGui, QtWidgets
from urllib.request import Request, urlopen
from json import loads

url = 'https://v1.jinrishici.com/all.json'


def read():
    req = Request(url=url)
    res = urlopen(req)
    v = res.read().decode('utf-8')
    return loads(v.replace("'", '"'))


def extr():
    try:
        v = read()
        c = v['content'].split('，')
        c = [(c[0] + '，').replace("。，", "。"),
             '，'.join(c[1:]).replace("。，", "。")]
        t = v['origin']
        a = v['author']
        if a == "佚名":
            a = "Unknown"
        lb = v['category']
        return (c, f"NAME:《{t}》 AUTHOR:{a}", f"POEM TYPE:{lb}")
    except:
        c = ["BAD REQUESTS，", "RETRY LATER..."]
        return (c, "SOMETHING HAPPENED┗|`O'|┛", ":( :( :( :( :( :( ")


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 245)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\poemisgood\\favicon.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\poemisgood\\favicon.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\poemisgood\\favicon.png"),
                       QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\poemisgood\\favicon.png"),
                       QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.On)
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\poemisgood\\favicon.png"),
                       QtGui.QIcon.Mode.Active, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\poemisgood\\favicon.png"),
                       QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\poemisgood\\favicon.png"),
                       QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\poemisgood\\favicon.png"),
                       QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 461, 151))
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 50, 131, 151))
        self.pushButton.setStyleSheet("font: 290 18pt \"Microsoft YaHei UI\";")
        self.pushButton.setObjectName("pushButton")
        (c1, c2), i1, i2 = extr()
        self.pushButton.clicked.connect(
            lambda: self.refreshtxtbs(c1, c2, i1, i2))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 601, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self._translate = QtCore.QCoreApplication.translate
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        (c1, c2), i1, i2 = extr()
        self.refreshtxtbs(c1, c2, i1, i2)
        MainWindow.setWindowTitle(
            self._translate("MainWindow", "PoemIsGood V0.1"))
        self.pushButton.setText(
            self._translate("MainWindow", "One more\nsentence"))
        self.label.setText(
            self._translate(
                "MainWindow",
                "Welcome to PoemIsGood! Author: Mr. Brain  Email: coder-brain@outlook.com   Idea from: Miss Chen"
            ))

    def refreshtxtbs(self, c1=None, c2=None, i1=None, i2=None):
        if not c1 or c2 or i1 or i2:
            (c1, c2), i1, i2 = extr()
        self.textBrowser.setHtml(
            self._translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \""
                "-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8"
                "\" /><style type=\"text/css\"> p, li { white-space: pre-wrap; }hr { height"
                ": 1px; border-width: 0; }</style></head><body style=\" font-family:\'Micro"
                "soft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\"><p s"
                "tyle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\""
                ">%s</span></p><p style=\" margin-top:0px; margin-bottom:0px; margin-left"
                ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style"
                "=\" font-size:24pt;\">%s</span></p><p style=\"-qt-paragraph-type:empty; "
                "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-"
                "block-indent:0; text-indent:0px;\"><br /></p><p style=\" margin-top:0px; m"
                "argin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                "ext-indent:0px;\">%s</p><p style=\" margin-top:0px; margin-botto"
                "m:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                "0px;\">%s</p></body></html>") % (c1, c2, i1, i2))


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(app.exec())
