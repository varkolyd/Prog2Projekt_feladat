class Fmeccs:

    def __init__(self, id, hazai, dontetlen, vendeg, hszorzo, dszorzo, vszorzo):
        self.id = id
        self.hazai = hazai
        self.dontetlen = dontetlen
        self.vendeg = vendeg
        self.hszorzo = hszorzo
        self.dszorzo = dszorzo
        self.vszorzo = vszorzo

    def get_match(self):
        return f"{self.id()},{self.hazai()},{self.dontetlen()},{self.vendeg()},{self.hszorzo(), self.dszorzo, self.vszorzo}"

    def __str__(self):
        return f"{self.id()},{self.hazai()},{self.dontetlen()},{self.vendeg()},{self.hszorzo(), self.dszorzo, self.vszorzo}"

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

    def __ge__(self, other):
        return self.id >= other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id


############################################################################
############################################################################
import profile as p
import re
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    eredmenyls = []
    meccshalmaz = {}
    profilhalmaz = {}
    kreditossz = 0
    fogadott_csapatok = []
    nyert_csapatok = []
    megtett_tet = 0
    szorzo_osszeg = 1.0
    nyert_osszeg = 0

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1161, 893)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(490, 10, 161, 61))
        font = QFont()
        font.setFamily(u"Copperplate Gothic Bold")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet(
            u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.home = QPushButton(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        self.home.setGeometry(QRect(190, 260, 221, 41))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.home.setFont(font1)
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black\n"
            "\n"
            "\n"
            "")
        self.home.setAutoDefault(False)
        self.home.setFlat(False)
        self.away = QPushButton(self.centralwidget)
        self.away.setObjectName(u"away")
        self.away.setGeometry(QRect(730, 260, 211, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.away.setFont(font2)
        self.away.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black\n"
            "\n"
            "")
        self.matchlist = QListWidget(self.centralwidget)
        self.matchlist.setObjectName(u"matchlist")
        self.matchlist.setGeometry(QRect(190, 330, 411, 192))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.matchlist.setFont(font3)
        self.matchlist.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color: rgb(170, 0, 0);\n"
            "color:white;\n"
            "border-color:black")
        self.tie = QPushButton(self.centralwidget)
        self.tie.setObjectName(u"tie")
        self.tie.setGeometry(QRect(470, 260, 211, 41))
        self.tie.setFont(font2)
        self.tie.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black\n"
            "\n"
            "")
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1231, 841))
        self.background.setStyleSheet(u"background-color: rgb(53, 30, 99);")
        self.background.setPixmap(QPixmap(u"../../../Documents/ball.jpg"))
        self.background.setScaledContents(False)
        self.feltoltes = QPushButton(self.centralwidget)
        self.feltoltes.setObjectName(u"feltoltes")
        self.feltoltes.setGeometry(QRect(190, 720, 191, 41))
        self.feltoltes.setFlat(True)
        self.matchupload = QPushButton(self.centralwidget)
        self.matchupload.setObjectName(u"matchupload")
        self.matchupload.setGeometry(QRect(190, 530, 171, 28))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(False)
        font4.setKerning(False)
        self.matchupload.setFont(font4)
        self.matchupload.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black")
        self.results = QPushButton(self.centralwidget)
        self.results.setObjectName(u"results")
        self.results.setGeometry(QRect(400, 530, 201, 28))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(50)
        font5.setStrikeOut(False)
        font5.setKerning(False)
        self.results.setFont(font5)
        self.results.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black")
        self.kreditszam = QLabel(self.centralwidget)
        self.kreditszam.setObjectName(u"kreditszam")
        self.kreditszam.setGeometry(QRect(20, 30, 201, 41))
        font6 = QFont()
        font6.setPointSize(10)
        self.kreditszam.setFont(font6)
        self.kreditszam.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.483684, y1:0, x2:0.516, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black\n"
            "")
        self.bet = QLineEdit(self.centralwidget)
        self.bet.setObjectName(u"bet")
        self.bet.setGeometry(QRect(490, 200, 171, 41))
        self.bet.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black\n"
            "")
        self.tet_label = QLabel(self.centralwidget)
        self.tet_label.setObjectName(u"tet_label")
        self.tet_label.setGeometry(QRect(430, 200, 41, 31))
        font7 = QFont()
        font7.setPointSize(14)
        self.tet_label.setFont(font7)
        self.tet_label.setStyleSheet(u"color:white\n"
                                     "")
        self.regist = QPushButton(self.centralwidget)
        self.regist.setObjectName(u"regist")
        self.regist.setGeometry(QRect(940, 20, 181, 41))
        self.regist.setFont(font2)
        self.regist.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black\n"
            "\n"
            "")
        self.bethistory = QListWidget(self.centralwidget)
        self.bethistory.setObjectName(u"bethistory")
        self.bethistory.setGeometry(QRect(190, 630, 751, 192))
        self.bethistory.setFont(font3)
        self.bethistory.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color: rgb(170, 0, 0);\n"
            "color:white;\n"
            "border-color:black")
        self.history_title = QLabel(self.centralwidget)
        self.history_title.setObjectName(u"history_title")
        self.history_title.setGeometry(QRect(370, 580, 421, 41))
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setPointSize(22)
        font8.setBold(True)
        font8.setItalic(True)
        font8.setUnderline(False)
        font8.setWeight(75)
        self.history_title.setFont(font8)
        self.history_title.setStyleSheet(
            u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.profilok_list = QListWidget(self.centralwidget)
        self.profilok_list.setObjectName(u"profilok_list")
        self.profilok_list.setGeometry(QRect(630, 330, 351, 192))
        self.profilok_list.setFont(font3)
        self.profilok_list.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color: rgb(170, 0, 0);\n"
            "color:white;\n"
            "border-color:black")
        self.profilupload = QPushButton(self.centralwidget)
        self.profilupload.setObjectName(u"profilupload")
        self.profilupload.setGeometry(QRect(630, 530, 171, 28))
        self.profilupload.setFont(font4)
        self.profilupload.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black")
        self.profilchoose = QPushButton(self.centralwidget)
        self.profilchoose.setObjectName(u"profilchoose")
        self.profilchoose.setGeometry(QRect(810, 530, 171, 28))
        self.profilchoose.setFont(font4)
        self.profilchoose.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
            "color:white;\n"
            "border-style:outset;\n"
            "border-width:2px;\n"
            "border-radius:10px;\n"
            "border-color:black")
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.title.raise_()
        self.home.raise_()
        self.away.raise_()
        self.matchlist.raise_()
        self.tie.raise_()
        self.feltoltes.raise_()
        self.matchupload.raise_()
        self.results.raise_()
        self.kreditszam.raise_()
        self.bet.raise_()
        self.tet_label.raise_()
        self.regist.raise_()
        self.bethistory.raise_()
        self.history_title.raise_()
        self.profilok_list.raise_()
        self.profilupload.raise_()
        self.profilchoose.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1161, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.home.setDefault(False)
        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

        self.matchupload.clicked.connect(self.load_matches)
        self.regist.clicked.connect(self.open_window)
        self.home.clicked.connect(self.gyoztesre_fogadas)
        self.tie.clicked.connect(self.dontetlenre_fogadas)
        self.away.clicked.connect(self.vesztesre_fogadas)
        self.results.clicked.connect(self.eredmenyek)
        self.profilupload.clicked.connect(self.load_profiles)
        self.profilchoose.clicked.connect(self.profilvalasztas)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"IK-BETS", None))
        self.home.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.away.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.tie.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.background.setText("")
        self.feltoltes.setText("")
        self.matchupload.setText(QCoreApplication.translate("MainWindow", u"Meccsek bet\u00f6lt\u00e9se", None))
        self.results.setText(QCoreApplication.translate("MainWindow", u"Eredm\u00e9nyek bet\u00f6lt\u00e9se", None))
        self.kreditszam.setText(QCoreApplication.translate("MainWindow", u"Kreditek:", None))
        self.tet_label.setText(QCoreApplication.translate("MainWindow", u"T\u00e9t:", None))
        self.regist.setText(QCoreApplication.translate("MainWindow", u"REGISZTR\u00c1CI\u00d3", None))
        self.history_title.setText(
            QCoreApplication.translate("MainWindow", u"Fogad\u00e1si el\u0151zm\u00e9nyek", None))
        self.profilupload.setText(QCoreApplication.translate("MainWindow", u"Profilok bet\u00f6lt\u00e9se", None))
        self.profilchoose.setText(QCoreApplication.translate("MainWindow", u"Profil választása", None))

    def open_window(self):  ##regisztrációs fül megnyitása
        Ui_registration.window = QMainWindow()
        Ui_registration.ui = Ui_registration()
        Ui_registration.ui.setupUi(Ui_registration.window)
        Ui_registration.window.show()

    # fájlból betöltés függvény
    def load_matches(self):
        f = open("meccsek.txt", "r", encoding="utf8")
        for line in f:
            data = line.rstrip().split(";")
            m1 = Fmeccs(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            if m1.id not in self.meccshalmaz:
                self.matchlist.addItem(
                    m1.id + "," + m1.hazai + "," + m1.dontetlen + "," + m1.vendeg + "," + m1.hszorzo + "," + m1.dszorzo + "," + m1.vszorzo)
                self.meccshalmaz[m1.id] = m1

    # profilok betöltése
    def load_profiles(self):
        self.profilok_list.clear()
        self.profilhalmaz={}
        f = open("profilok.txt", "r", encoding="utf8")
        for line in f:
            data = line.rstrip().split(",")
            p2 = p.Profile(data[0], data[1], data[2], data[3])
            if p2.id not in self.profilhalmaz:
                self.profilok_list.addItem(p2.id + "," + p2.name + "," + p2.email + "," + p2.egyenleg)  # itt az egyenleg és az id valamiért fordítva működik
                self.profilhalmaz[p2.id] = p2
    cp=""
    def profilvalasztas(self):
        if not self.profilok_list.currentItem():
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Válasszon profilt!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        if self.profilok_list.currentItem():
            prof = self.profilok_list.currentItem().text()
            kredit = prof.split(",")[3]
            kredit = int(kredit)
            prof_id= prof.split(",")[0]
            self.cp=prof_id
        self.kreditossz = kredit
        self.kreditek_frissites()
        self.bethistory.clear()
        self.meccscounter=1
    def kreditek_frissites(self):
        self.kreditszam.setText("Kreditek: " + str(round(self.kreditossz)))
        f = open("profilok.txt", "r", encoding="utf8")
        for line in f:
            data = line.rstrip().split(",")
            id=data[0]
            if id==self.cp:
                data[2]=self.kreditossz


    def gyoztesre_fogadas(self):
        if not self.matchlist.currentItem():
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Válasszon a fogadni kívánt meccsre!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

        lement = False
        try:
            if int(self.bet.text()) <= self.kreditossz:
                try:
                    int(self.bet.text())
                    m = self.matchlist.currentItem().text()
                    id = m.split(",")[0]
                    me = m.split(",")[1]
                    id = int(id)
                    if id not in self.fogadott_csapatok:
                        self.fogadott_csapatok.append(int(id))
                        self.fogadott_csapatok.append(me)
                        self.megtett_tet += int(self.bet.text())
                        self.kreditossz -= int(self.bet.text())
                        self.kreditek_frissites()
                        lement = True

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Figyelem!")
                        msg.setText("Erre a meccsre már fogadott!")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec_()
                        lement = True
                except ValueError:
                    msg = QMessageBox()
                    msg.setWindowTitle("Figyelem!")
                    msg.setText("Tegye meg a tétjét!")
                    msg.setIcon(QMessageBox.Warning)
                    msg.exec_()
                    lement = True
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Tegye meg a tétjét!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            lement = True

        if lement is False:
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Tétje meghaladja a rendelkezésre álló összeget!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        print(self.fogadott_csapatok)

    def vesztesre_fogadas(self):
        if not self.matchlist.currentItem():
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Válasszon a fogadni kívánt meccsre!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

        lement = False
        try:
            if int(self.bet.text()) <= self.kreditossz:
                try:
                    int(self.bet.text())
                    m = self.matchlist.currentItem().text()
                    id = m.split(",")[0]
                    me = m.split(",")[3]
                    id = int(id)
                    if id not in self.fogadott_csapatok:
                        self.fogadott_csapatok.append(int(id))
                        self.fogadott_csapatok.append(me)
                        self.megtett_tet += int(self.bet.text())
                        self.kreditossz -= int(self.bet.text())
                        self.kreditek_frissites()
                        lement = True

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Figyelem!")
                        msg.setText("Erre a meccsre már fogadott!")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec_()
                        lement = True
                except ValueError:
                    msg = QMessageBox()
                    msg.setWindowTitle("Figyelem!")
                    msg.setText("Tegye meg a tétjét!")
                    msg.setIcon(QMessageBox.Warning)
                    msg.exec_()
                    lement = True
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Tegye meg a tétjét!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            lement = True

        if lement is False:
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Tétje meghaladja a rendelkezésre álló összeget!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        print(self.fogadott_csapatok)

    def dontetlenre_fogadas(self):
        if not self.matchlist.currentItem():
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Válasszon a fogadni kívánt meccsre!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

        lement = False
        try:
            if int(self.bet.text()) <= self.kreditossz:
                try:
                    int(self.bet.text())
                    m = self.matchlist.currentItem().text()
                    id = m.split(",")[0]
                    me = m.split(",")[2]
                    id = int(id)
                    if id not in self.fogadott_csapatok:
                        self.fogadott_csapatok.append(int(id))
                        self.fogadott_csapatok.append(me)
                        self.megtett_tet += int(self.bet.text())
                        self.kreditossz -= int(self.bet.text())
                        self.kreditek_frissites()
                        lement = True

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Figyelem!")
                        msg.setText("Erre a meccsre már fogadott!")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec_()
                        lement = True
                except ValueError:
                    msg = QMessageBox()
                    msg.setWindowTitle("Figyelem!")
                    msg.setText("Tegye meg a tétjét!")
                    msg.setIcon(QMessageBox.Warning)
                    msg.exec_()
                    lement = True
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Tegye meg a tétjét!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            lement = True

        if lement is False:
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Tétje meghaladja a rendelkezésre álló összeget!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        print(self.fogadott_csapatok)

    nyert=False
    def eredmenyek(self):
        import random
        fileopen = open("meccsek.txt", "r", encoding='utf8')
        count = 0
        if not self.fogadott_csapatok:
            msg = QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setText("Először tegye meg a tétjeit!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            for row in fileopen:
                row = row.strip().split(";")
                H = row[1]
                D = row[2]
                V = row[3]
                Hsz = float(row[4])
                Dsz = float(row[5])
                Vsz = float(row[6])

                lista = []
                for i in range(int(1000 / Hsz)):
                    lista.append(H)
                for i in range(int(1000 / Dsz)):
                    lista.append(D)
                for k in range(int(1000 / Vsz)):
                    lista.append(V)
                count += 1
                self.eredmenyls.append(count)
                self.eredmenyls.append(random.choice(lista))

            # print(self.fogadott_csapatok)
            print(self.eredmenyls)
            for i in range(0, len(self.fogadott_csapatok), 2):
                fogadott_index = self.fogadott_csapatok[i]
                fogadott_csapi = self.fogadott_csapatok[i + 1]
                # print(self.eredmenyls[((fogadott_index-1)*2)+1])
                if self.eredmenyls[((fogadott_index - 1) * 2) + 1] == fogadott_csapi:
                    self.nyert_csapatok.append(fogadott_index)
                    self.nyert_csapatok.append(fogadott_csapi)
            print(self.nyert_csapatok)
            # print(self.nyert_csapatok)
            print(self.fogadott_csapatok)

            ####FOGADÁS####
            if self.fogadott_csapatok == self.nyert_csapatok:

                self.szorzo_generalasa()
                self.kreditossz += (self.szorzo_osszeg * self.megtett_tet)
                msg = QMessageBox()
                msg.setWindowTitle("Gratulálunk!")
                msg.setText(f"Ön nyert {self.szorzo_osszeg * self.megtett_tet} kreditet!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.kreditek_frissites()
                self.nyert = True
                self.meccselozmenyek()
                self.fogadott_csapatok = []
                self.nyert_csapatok = []
                self.megtett_tet = 0
                self.eredmenyls = []
                self.szorzo_osszeg = 1.0


            else:
                msg = QMessageBox()
                msg.setWindowTitle("Sajnáljuk!")
                msg.setText("Ön veszített")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                self.nyert=False
                self.meccselozmenyek()
                self.fogadott_csapatok = []
                self.nyert_csapatok = []
                self.megtett_tet = 0
                self.eredmenyls = []
                self.szorzo_osszeg = 1.0
    def szorzo_generalasa(self):
        filenyer = open("meccsek.txt", "r", encoding='utf8')
        for i in range(len(self.nyert_csapatok)):
            for row in filenyer:
                row = row.strip().split(";")
                id = row[0]
                H = row[1]
                D = row[2]
                V = row[3]
                Hsz = float(row[4])
                Dsz = float(row[5])
                Vsz = float(row[6])
                if int(id) == self.nyert_csapatok[i]:
                    if str(self.nyert_csapatok[i + 1]) == str(H):
                        self.szorzo_osszeg *= Hsz

                    if str(self.nyert_csapatok[i + 1]) == str(D):
                        self.szorzo_osszeg *= Dsz

                    if str(self.nyert_csapatok[i + 1]) == str(V):
                        self.szorzo_osszeg *= Vsz

        return self.szorzo_osszeg

    meccscounter = 1

    def meccselozmenyek(self):
        if self.nyert is True:
            self.bethistory.addItem(f"{self.meccscounter}. fogadás | kimenetel: nyert | kredit változás: +{(self.szorzo_osszeg * self.megtett_tet)-self.megtett_tet}")
        if self.nyert is False:
            self.bethistory.addItem(f"{self.meccscounter}. fogadás | kimenetel: veszítettet | kredit változás: -{self.megtett_tet}")
        for i in range(0,len(self.fogadott_csapatok),2):
                self.bethistory.addItem(f"  {self.fogadott_csapatok[i]}. mérkőzés | Fogadás: {self.fogadott_csapatok[i+1]}")
        self.meccscounter += 1
        self.nyert=False


# alwindow nem kell vele foglakozni

class Ui_registration(object):
    profiles = []

    def setupUi(self, registration):
        if registration.objectName():
            registration.setObjectName(u"registration")
        registration.resize(720, 668)
        registration.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(registration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.name_in = QLineEdit(self.centralwidget)
        self.name_in.setObjectName(u"name_in")
        self.name_in.setGeometry(QRect(130, 80, 311, 31))
        self.name_ = QLabel(self.centralwidget)
        self.name_.setObjectName(u"name_")
        self.name_.setGeometry(QRect(20, 80, 51, 21))
        font = QFont()
        font.setFamily(u"Garamond")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.name_.setFont(font)
        self.regtitle = QLabel(self.centralwidget)
        self.regtitle.setObjectName(u"regtitle")
        self.regtitle.setGeometry(QRect(100, 10, 571, 51))
        font1 = QFont()
        font1.setFamily(u"Garamond")
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.regtitle.setFont(font1)
        self.email_in = QLineEdit(self.centralwidget)
        self.email_in.setObjectName(u"email_in")
        self.email_in.setGeometry(QRect(130, 120, 311, 31))
        self.email = QLabel(self.centralwidget)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(20, 110, 71, 41))
        self.email.setFont(font)
        self.id = QLabel(self.centralwidget)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(20, 150, 71, 41))
        self.id.setFont(font)
        self.id_in = QLineEdit(self.centralwidget)
        self.id_in.setObjectName(u"id_in")
        self.id_in.setGeometry(QRect(130, 160, 311, 31))
        self.add_but = QPushButton(self.centralwidget)
        self.add_but.setObjectName(u"add_but")
        self.add_but.setGeometry(QRect(40, 260, 91, 71))
        self.delete_but = QPushButton(self.centralwidget)
        self.delete_but.setObjectName(u"delete_but")
        self.delete_but.setGeometry(QRect(400, 260, 91, 71))
        self.edit_but = QPushButton(self.centralwidget)
        self.edit_but.setObjectName(u"edit_but")
        self.edit_but.setGeometry(QRect(160, 260, 91, 71))
        self.modify_but = QPushButton(self.centralwidget)
        self.modify_but.setObjectName(u"modify_but")
        self.modify_but.setGeometry(QRect(280, 260, 91, 71))
        self.list_of_p_list = QListWidget(self.centralwidget)
        self.list_of_p_list.setObjectName(u"list_of_p_list")
        self.list_of_p_list.setGeometry(QRect(30, 410, 531, 211))
        self.list_of_p = QLabel(self.centralwidget)
        self.list_of_p.setObjectName(u"list_of_p")
        self.list_of_p.setGeometry(QRect(30, 360, 161, 41))
        self.list_of_p.setFont(font)
        self.egyenleg = QLabel(self.centralwidget)
        self.egyenleg.setObjectName(u"egyenleg")
        self.egyenleg.setGeometry(QRect(20, 190, 111, 41))
        self.egyenleg.setFont(font)
        self.egyenleg_in = QLineEdit(self.centralwidget)
        self.egyenleg_in.setObjectName(u"egyenleg_in")
        self.egyenleg_in.setGeometry(QRect(130, 200, 311, 31))
        registration.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(registration)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 26))
        registration.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(registration)
        self.statusbar.setObjectName(u"statusbar")
        registration.setStatusBar(self.statusbar)

        self.retranslateUi(registration)

        QMetaObject.connectSlotsByName(registration)
    # setupUi

        QMetaObject.connectSlotsByName(registration)
        self.add_but.clicked.connect(self.add_or_modify_profile)
        self.edit_but.clicked.connect(self.edit_profile)
        self.modify_but.clicked.connect(self.add_or_modify_profile)
        self.delete_but.clicked.connect(self.delete_profile)

    # setupUi

    def delete_profile(self):
        if not self.list_of_p_list.currentItem():
            msg = QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setText("Please select a worker for delete!")
            msg.exec_()
        else:
            p = self.list_of_p_list.currentItem().text()
            id = p.split(",")[3]
            for profile in self.profiles:
                if id == profile.get_id():
                    self.profiles.remove(profile)
                    self.profiles.sort()
                    self.print_profiles()
                    self.save_to_file()
                    self.clear_form_items()

    def edit_profile(self):
        if not self.list_of_p_list.currentItem():
            msg = QMessageBox()
            msg.setWindowTitle("!")
            msg.setText("Please select a worker for edit!")
            msg.exec_()
        else:
            profile = self.list_of_p_list.currentItem().text()
            id = profile.split(",")[3]
            for profile in self.profiles:
                if profile.get_id() == id:
                    self.name_in.setText(profile.get_name())
                    self.email_in.setText(profile.get_email())
                    self.egyenleg_in.setText(profile.get_egyenleg())
                    self.id_in.setText(profile.get_id())
            self.id_in.setReadOnly(True)

    def print_profiles(self):
        self.list_of_p_list.clear()
        for profile in self.profiles:
            self.list_of_p_list.addItem(profile.__str__())

    def add_or_modify_profile(self):
        try:
           name = self.name_in.text()
           e_mail = self.email_in.text()
           egyenleg = self.egyenleg_in.text()
           id = self.id_in.text()
           if len(name) == 0:
               raise p.MissingDataException("Name")
           if len(e_mail) == 0:
               raise p.MissingDataException("E-mail")
           if len(egyenleg) == 0:
               raise p.MissingDataException("Address")
           if len(id) == 0:
               raise p.MissingDataException("ID")
           if not re.match('[0-9a-zA-Z_.-]+@[0-9a-zA-Z_.-]+(\.)[a-z]{2,4}$',e_mail):
               raise p.EmailAddressFormatException

        except p.MissingDataException as mde:
            msg = QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setText(mde.__str__())
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("E-mail warning!")
            msg.setText("Invalid e-mail format")
            msg.exec_()
        else:
            profile = p.Profile(self.name_in.text(),self.email_in.text(), self.egyenleg_in.text(), self.id_in.text())
            if not self.id_in.isReadOnly():
                if profile not in self.profiles:
                    self.profiles.append(profile)
                    self.profiles.sort()
                    self.print_profiles()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Warning!")
                    msg.setText("Worker already added with this ID!")
                    msg.exec_()
            else:
                for bet_person in self.profiles:
                    if bet_person == profile:
                        bet_person.set_name(profile.get_name())
                        bet_person.set_email(profile.get_email())
                        bet_person.set_egyenleg(profile.get_egyenleg())
                self.print_profiles()
                self.id_in.setReadOnly(False)
            self.save_to_file()
            self.clear_form_items()


    def save_to_file(self):
        f = open("profilok.txt","w")
        for profile in self.profiles:
            print(profile.__str__(), file=f)
        f.close()

    def load_data_from_file(self):
        try:
            f = open("profilok.txt","r")
            for line in f:
                data = line.rstrip().split(",")
                profile = p.Profile(data[0], data[1], data[2], data[3])
                self.profiles.append(profile)
            self.print_profiles()
            f.close()
        except:
            pass

    def clear_form_items(self):
        self.name_in.clear()
        self.email_in.clear()
        self.egyenleg_in.clear()
        self.id_in.clear()

    def retranslateUi(self, registration):
        registration.setWindowTitle(QCoreApplication.translate("registration", u"MainWindow", None))
        self.name_.setText(QCoreApplication.translate("registration", u"N\u00e9v:", None))
        self.regtitle.setText(QCoreApplication.translate("registration", u"REGISZTR\u00c1CI\u00d3S FEL\u00dcLET", None))
        self.email.setText(QCoreApplication.translate("registration", u"Email:", None))
        self.id.setText(QCoreApplication.translate("registration", u"ID", None))
        self.add_but.setText(QCoreApplication.translate("registration", u"Add", None))
        self.delete_but.setText(QCoreApplication.translate("registration", u"Delete", None))
        self.edit_but.setText(QCoreApplication.translate("registration", u"Edit", None))
        self.modify_but.setText(QCoreApplication.translate("registration", u"Modify", None))
        self.list_of_p.setText(QCoreApplication.translate("registration", u"List of persons:", None))
        self.egyenleg.setText(QCoreApplication.translate("registration", u"Egyenleg", None))

    # retranslateUi


import sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.kreditek_frissites()  ### Felhasználható krediteket rendel a profilhoz
MainWindow.show()
sys.exit(app.exec_())
