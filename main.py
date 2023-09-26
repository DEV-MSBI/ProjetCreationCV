#-*- coding: utf-8 -*-
from PySide2 import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtGui, QtCore
from docxtpl import DocxTemplate
import time,os,sys,res_rc,json
from os import path
from main_ui import Ui_MainWindow

#ui,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))
count3 = 1
count4 = 1
count5 = 1
count6 = 1
count7 = 1
count8 = 1
indx_lang = 0
add_comp1 = 0
index_exp = 0
index_form = 0
indx_lois = 0
add_comp2 = 0
doc1 = ""
Nb_Forma = ""
Nb_comp = ""
Nb_comp_1 = ""
Nb_Exp = ""
Nb_lang = ""
Nb_lois = ""
L = []
L2 = []
L3 = []
D1 = dict()
L4 = []
class MainApp(QMainWindow , Ui_MainWindow):
    #def __init__(self, parent=None):
    def __init__(self):
        #super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.Handel_ui()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.Form.setPlaceholderText("Diplome,Licence ....")
        self.Etabl.setPlaceholderText("Lycée,Université  ....")
        self.lineEdit_4.setPlaceholderText("Fés,Rabat ....")
        self.phone.setPlaceholderText("06.66.66.66.00")
        self.Email.setPlaceholderText("name@gmail.com")
        self.F_name.setPlaceholderText("Dana")
        self.L_name.setPlaceholderText("Brown")
        self.Addr.setPlaceholderText("2242 Rosemont Avenue Eau Gallie, FL 32903")
        self.lineEdit_5.setPlaceholderText("Ingénieur Cloud,Chef Comptable ...")
        self.Entrep.setPlaceholderText("Société MySoft,Dell,Cisco .....")
        self.Poste.setPlaceholderText("Ingénieur Cloud,Chef Comptable ...")
        self.Ville_1.setPlaceholderText("Fés,Rabat ....")
        self.textEdit_2.setPlaceholderText("""- Intégration des offres (préparation subjects, créatives) ;\n
- Effectuer une série de tests pour assurer l'envoi des offres;\n
- Assurer un suivi permanent des envois en terme de revenu ;\n
- Participer à l'optimisation des offres et des ressources attribuées.""")
        
        self.frame_19.setVisible(True)
        img = \
        ".QPushButton{\n"\
        +"image:url(./icon/imp_img.png);\n"\
        +"width: 150px;\n"\
        +"height: 150px;\n"\
        +"border:1px solid #00aaff;\n"\
	+"border-radius:15px;\n"\
        +"background-color: none;\n"\
        +"}"
        self.img.setStyleSheet(img)

        # ###############################################
        # Function to Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################

        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.frame.mouseMoveEvent = moveWindow
        #######################################################################
        #Button disable per default
        self.pushButton_3.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.pushButton_9.setVisible(False)
        self.pushButton_13.setVisible(False)
        self.pushButton_16.setVisible(False)

        

    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window

    def Handel_ui(self):
        self.setWindowTitle("Creation CV")
        #self.setFixedSize(700,564)
        self.setFixedSize(900,564)

    def Handel_Buttons(self):
        global c,count
        #PAGE
        self.HOME.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Home))
        self.pushButton_11.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Info_1))
        self.Btn_cr.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Page_CV))
        self.CV1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.info_2))
        self.CV2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.info_2))
        self.CV3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.info_2))
        self.CV4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.info_2))
        self.CV5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.info_2))
        self.CV6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.info_2))

        self.B_pre.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.info_2))
        self.B_suiv.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Formation))
        self.B_pre_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Info_1))
        self.B_suiv_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Exper))
        self.B_pre_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Formation))
        self.B_suiv_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.B_pre_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Exper))
        self.B_suiv_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_9))
        #self.B_pre_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        #self.B_suiv_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_9))
        self.B_pre_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.B_suiv_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7))

        
        self.pushButton_11.clicked.connect(self.reserve_var)
        self.CV1.clicked.connect(self.choix_cv1)
        self.CV2.clicked.connect(self.choix_cv2)
        self.CV3.clicked.connect(self.choix_cv3)
        self.CV4.clicked.connect(self.choix_cv4)
        self.CV5.clicked.connect(self.choix_cv5)
        self.CV6.clicked.connect(self.choix_cv6)

        # BTN_Close
        self.Bn_Close.clicked.connect(lambda: self.close())
        # BTN_Minimized
        self.Bn_Min.clicked.connect(lambda: self.showMinimized())
        #Maximized
        #self.MAX.clicked.connect(lambda: self.showMaximized())
        self.Terminer.clicked.connect(self.infor)
        self.Terminer.clicked.connect(self.R_FOR)
        self.Terminer_1.clicked.connect(self.infor)
        self.Terminer_1.clicked.connect(self.R_EXP)
        self.img.clicked.connect(self.select_image)
        #self.B_suiv_2.clicked.connect(self.remplie_cv)
        #self.B_suiv_4.clicked.connect(self.remplie_cv)
        
        self.pushButton.clicked.connect(self.add_toolbox)
        self.pushButton_2.clicked.connect(self.add_exp)
        self.pushButton_5.clicked.connect(self.add_compt)
        self.pushButton_8.clicked.connect(self.add_compt2)
        self.pushButton_7.clicked.connect(self.infor)
        self.pushButton_7.clicked.connect(self.R_COMP1)
        self.pushButton_10.clicked.connect(self.infor)
        self.pushButton_10.clicked.connect(self.R_COMP2)
        self.pushButton_12.clicked.connect(self.add_Lang)
        self.pushButton_15.clicked.connect(self.add_loiser)
        self.pushButton_14.clicked.connect(self.infor)
        self.pushButton_14.clicked.connect(self.R_LANG)
        self.pushButton_17.clicked.connect(self.infor)
        self.pushButton_17.clicked.connect(self.R_LOIS)
        self.B_suiv_6.clicked.connect(self.remplie_cv)
        #supp_toolbox
        self.pushButton_13.clicked.connect(self.supp_lang)
        self.pushButton_16.clicked.connect(self.supp_lois)
        self.pushButton_3.clicked.connect(self.supp_form)
        self.pushButton_4.clicked.connect(self.supp_exp)
        self.pushButton_6.clicked.connect(self.supp_comp1)
        self.pushButton_9.clicked.connect(self.supp_comp2)
        
        #Page_choissez_cv
        self.precedent.setVisible(False)
        c = 0
        #count1 = 2
        count = -1
        self.suivant.clicked.connect(self.Btn)
        self.precedent.clicked.connect(self.Btn1)
        
    def Btn(self):
        global c,count
        #count = 0
        
        while count < c:
            print(count)
            self.suivant.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(count))
            count+=1
            if count == 1:
                self.precedent.setVisible(True)
            if count == 5:
                self.suivant.setVisible(False)
        c+=1
        """if count == 4:
            count = 0
            c = 1"""

    def Btn1(self):
        global count,c
        #global count1
        #c1 = 3
        while c > count:
            print(c)
            self.precedent.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(c))
            c-=1

            if c == 4:
                self.suivant.setVisible(True)
            if c == 0:
                self.precedent.setVisible(False)
        count-=1
        """if c == -1:
            count = 2
            c1 = 3"""


    def select_image(self):
        global path
        image = QFileDialog.getOpenFileName(self,'Open Image','',"Image File(*.jpg)")
        path = image[0]
        
        imagel = \
        ".QPushButton {\n"\
        +"image:url("+path+");\n"\
        +"width: 150px;\n"\
        +"height: 150px;\n"\
        +"background-color: none;\n"\
	+"border:0px solid;\n"\
        +"}"
        self.img.setStyleSheet(imagel)

        self.pushButton_18.setStyleSheet(imagel)


    def choix_cv1(self):
        global CV
        CV = "CV1.docx"
    def choix_cv2(self):
        global CV
        CV = "CV2.docx"
    def choix_cv3(self):
        global CV
        CV = "CV3.docx"
    def choix_cv4(self):
        global CV
        CV = "CV4.docx"
    def choix_cv5(self):
        global CV
        CV = "CV5.docx"
    def choix_cv6(self):
        global CV
        CV = "CV7.docx"
    
        

    def add_toolbox(self):
        global count3,index_form,T_1
        
        self.page = QWidget()
        self.page.setGeometry(QRect(0, 0, 682, 438))
        self.page.setObjectName("page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QFrame(self.page)
        self.frame.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    background-color: rgb(239, 239, 239);\n"
"    /*border:1px solid gray;*/\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Etabl = QLineEdit(self.frame)
        self.Etabl.setMinimumSize(QSize(0, 50))
        self.Etabl.setObjectName("Etabl")
        self.gridLayout_3.addWidget(self.Etabl, 4, 0, 1, 6)
        spacerItem = QSpacerItem(406, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 6)
        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 3)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 2)
        self.Form = QLineEdit(self.frame)
        self.Form.setMinimumSize(QSize(0, 50))
        self.Form.setObjectName("Form")
        self.gridLayout_3.addWidget(self.Form, 1, 0, 1, 9)
        spacerItem1 = QSpacerItem(122, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 8, 0, 1, 1)
        spacerItem2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 5, 5, 1, 1)
        spacerItem3 = QSpacerItem(92, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 6, 4, 1, 1)
        spacerItem4 = QSpacerItem(20, 43, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 5, 8, 3, 1)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 6, 5, 1, 2)
        spacerItem5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 5, 1, 1, 2)
        spacerItem6 = QSpacerItem(20, 135, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 9, 2, 1, 1)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 6, 1, 1, 3)
        spacerItem7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 1)
        spacerItem8 = QSpacerItem(97, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 8, 6, 1, 3)
        self.Date_F = QComboBox(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Date_F.sizePolicy().hasHeightForWidth())
        self.Date_F.setSizePolicy(sizePolicy)
        self.Date_F.setMinimumSize(QSize(150, 40))
        self.Date_F.setObjectName("Date_F")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.setItemText(40, "")
        self.gridLayout_3.addWidget(self.Date_F, 7, 5, 2, 1)
        self.Date_D = QComboBox(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Date_D.sizePolicy().hasHeightForWidth())
        self.Date_D.setSizePolicy(sizePolicy)
        self.Date_D.setMinimumSize(QSize(150, 40))
        self.Date_D.setObjectName("Date_D")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.setItemText(40, "")
        self.gridLayout_3.addWidget(self.Date_D, 7, 1, 2, 3)
        spacerItem9 = QSpacerItem(352, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 3, 2, 1, 4)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 6, 1, 2)
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setMinimumSize(QSize(0, 50))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 4, 6, 1, 3)
        spacerItem10 = QSpacerItem(20, 135, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 9, 5, 1, 1)
        self.Terminer = QPushButton(self.frame)
        self.Terminer.setMinimumSize(QSize(110, 27))
        self.Terminer.setMaximumSize(QSize(16777215, 28))
        self.Terminer.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: white;\n"
"    border:0px solid;\n"
"    border-radius:5px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Terminer.setObjectName("Terminer")
        self.gridLayout_3.addWidget(self.Terminer, 9, 6, 1, 3)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.toolBox.addItem(self.page, "Formation") 

        _translate = QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Formation"))
        self.label_2.setText(_translate("MainWindow", "Etablissement"))
        self.label_6.setText(_translate("MainWindow", "Date de fin"))
        self.label_4.setText(_translate("MainWindow", "Date de début"))
        self.Date_F.setItemText(0, _translate("MainWindow", "2030"))
        self.Date_F.setItemText(1, _translate("MainWindow", "2029"))
        self.Date_F.setItemText(2, _translate("MainWindow", "2028"))
        self.Date_F.setItemText(3, _translate("MainWindow", "2027"))
        self.Date_F.setItemText(4, _translate("MainWindow", "2026"))
        self.Date_F.setItemText(5, _translate("MainWindow", "2025"))
        self.Date_F.setItemText(6, _translate("MainWindow", "2024"))
        self.Date_F.setItemText(7, _translate("MainWindow", "2023"))
        self.Date_F.setItemText(8, _translate("MainWindow", "2022"))
        self.Date_F.setItemText(9, _translate("MainWindow", "2021"))
        self.Date_F.setItemText(10, _translate("MainWindow", "2020"))
        self.Date_F.setItemText(11, _translate("MainWindow", "2019"))
        self.Date_F.setItemText(12, _translate("MainWindow", "2018"))
        self.Date_F.setItemText(13, _translate("MainWindow", "2017"))
        self.Date_F.setItemText(14, _translate("MainWindow", "2016"))
        self.Date_F.setItemText(15, _translate("MainWindow", "2015"))
        self.Date_F.setItemText(16, _translate("MainWindow", "2014"))
        self.Date_F.setItemText(17, _translate("MainWindow", "2013"))
        self.Date_F.setItemText(18, _translate("MainWindow", "2012"))
        self.Date_F.setItemText(19, _translate("MainWindow", "2011"))
        self.Date_F.setItemText(20, _translate("MainWindow", "2010"))
        self.Date_F.setItemText(21, _translate("MainWindow", "2009"))
        self.Date_F.setItemText(22, _translate("MainWindow", "2008"))
        self.Date_F.setItemText(23, _translate("MainWindow", "2007"))
        self.Date_F.setItemText(24, _translate("MainWindow", "2006"))
        self.Date_F.setItemText(25, _translate("MainWindow", "2005"))
        self.Date_F.setItemText(26, _translate("MainWindow", "2004"))
        self.Date_F.setItemText(27, _translate("MainWindow", "2003"))
        self.Date_F.setItemText(28, _translate("MainWindow", "2002"))
        self.Date_F.setItemText(29, _translate("MainWindow", "2000"))
        self.Date_F.setItemText(30, _translate("MainWindow", "1999"))
        self.Date_F.setItemText(31, _translate("MainWindow", "1998"))
        self.Date_F.setItemText(32, _translate("MainWindow", "1997"))
        self.Date_F.setItemText(33, _translate("MainWindow", "1996"))
        self.Date_F.setItemText(34, _translate("MainWindow", "1995"))
        self.Date_F.setItemText(35, _translate("MainWindow", "1994"))
        self.Date_F.setItemText(36, _translate("MainWindow", "1993"))
        self.Date_F.setItemText(37, _translate("MainWindow", "1992"))
        self.Date_F.setItemText(38, _translate("MainWindow", "1991"))
        self.Date_F.setItemText(39, _translate("MainWindow", "1990"))
        self.Date_D.setItemText(0, _translate("MainWindow", "2030"))
        self.Date_D.setItemText(1, _translate("MainWindow", "2029"))
        self.Date_D.setItemText(2, _translate("MainWindow", "2028"))
        self.Date_D.setItemText(3, _translate("MainWindow", "2027"))
        self.Date_D.setItemText(4, _translate("MainWindow", "2026"))
        self.Date_D.setItemText(5, _translate("MainWindow", "2025"))
        self.Date_D.setItemText(6, _translate("MainWindow", "2024"))
        self.Date_D.setItemText(7, _translate("MainWindow", "2023"))
        self.Date_D.setItemText(8, _translate("MainWindow", "2022"))
        self.Date_D.setItemText(9, _translate("MainWindow", "2021"))
        self.Date_D.setItemText(10, _translate("MainWindow", "2020"))
        self.Date_D.setItemText(11, _translate("MainWindow", "2019"))
        self.Date_D.setItemText(12, _translate("MainWindow", "2018"))
        self.Date_D.setItemText(13, _translate("MainWindow", "2017"))
        self.Date_D.setItemText(14, _translate("MainWindow", "2016"))
        self.Date_D.setItemText(15, _translate("MainWindow", "2015"))
        self.Date_D.setItemText(16, _translate("MainWindow", "2014"))
        self.Date_D.setItemText(17, _translate("MainWindow", "2013"))
        self.Date_D.setItemText(18, _translate("MainWindow", "2012"))
        self.Date_D.setItemText(19, _translate("MainWindow", "2011"))
        self.Date_D.setItemText(20, _translate("MainWindow", "2010"))
        self.Date_D.setItemText(21, _translate("MainWindow", "2009"))
        self.Date_D.setItemText(22, _translate("MainWindow", "2008"))
        self.Date_D.setItemText(23, _translate("MainWindow", "2007"))
        self.Date_D.setItemText(24, _translate("MainWindow", "2006"))
        self.Date_D.setItemText(25, _translate("MainWindow", "2005"))
        self.Date_D.setItemText(26, _translate("MainWindow", "2004"))
        self.Date_D.setItemText(27, _translate("MainWindow", "2003"))
        self.Date_D.setItemText(28, _translate("MainWindow", "2002"))
        self.Date_D.setItemText(29, _translate("MainWindow", "2000"))
        self.Date_D.setItemText(30, _translate("MainWindow", "1999"))
        self.Date_D.setItemText(31, _translate("MainWindow", "1998"))
        self.Date_D.setItemText(32, _translate("MainWindow", "1997"))
        self.Date_D.setItemText(33, _translate("MainWindow", "1996"))
        self.Date_D.setItemText(34, _translate("MainWindow", "1995"))
        self.Date_D.setItemText(35, _translate("MainWindow", "1994"))
        self.Date_D.setItemText(36, _translate("MainWindow", "1993"))
        self.Date_D.setItemText(37, _translate("MainWindow", "1992"))
        self.Date_D.setItemText(38, _translate("MainWindow", "1991"))
        self.Date_D.setItemText(39, _translate("MainWindow", "1990"))
        self.label_3.setText(_translate("MainWindow", "Ville"))
        self.Terminer.setText(_translate("MainWindow", ""))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Formation"))
        count3+=1
        
        if count3 == int(Nb_Forma):
            self.pushButton.setEnabled(False)
        self.pushButton_3.setVisible(True)
        index_form = (self.toolBox.currentIndex())
            

    def add_exp(self):
        global count4,index_exp
        self.page_5 = QWidget()
        self.page_5.setGeometry(QRect(0, 0, 662, 335))
        self.page_5.setObjectName("page_5")
        self.gridLayout_2 = QGridLayout(self.page_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QFrame(self.page_5)
        self.frame_2.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(239, 239, 239);\n"
"    /*border:1px solid gray;*/\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius:4px;\n"
"}\n"
"QTextEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.Entrep = QLineEdit(self.frame_2)
        self.Entrep.setMinimumSize(QSize(0, 50))
        self.Entrep.setObjectName("Entrep")
        self.gridLayout_3.addWidget(self.Entrep, 1, 0, 1, 4)
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 2, 1, 1)
        self.Poste = QLineEdit(self.frame_2)
        self.Poste.setMinimumSize(QSize(0, 50))
        self.Poste.setObjectName("Poste")
        self.gridLayout_3.addWidget(self.Poste, 3, 0, 1, 2)
        self.Ville_1 = QLineEdit(self.frame_2)
        self.Ville_1.setMinimumSize(QSize(0, 50))
        self.Ville_1.setObjectName("Ville_1")
        self.gridLayout_3.addWidget(self.Ville_1, 3, 2, 1, 2)
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 4, 0, 1, 1)
        self.comboBox_4 = QComboBox(self.frame_2)
        self.comboBox_4.setMinimumSize(QSize(0, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_4, 5, 0, 1, 1)
        self.comboBox_5 = QComboBox(self.frame_2)
        self.comboBox_5.setMinimumSize(QSize(0, 30))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_5, 5, 1, 1, 1)
        self.comboBox_6 = QComboBox(self.frame_2)
        self.comboBox_6.setMinimumSize(QSize(0, 30))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_6, 5, 2, 1, 1)
        self.comboBox_7 = QComboBox(self.frame_2)
        self.comboBox_7.setMinimumSize(QSize(0, 30))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_7, 5, 3, 1, 1)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 6, 0, 1, 1)
        self.textEdit_2 = QTextEdit(self.frame_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_3.addWidget(self.textEdit_2, 7, 0, 1, 4)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.toolBox_2.addItem(self.page_5, "")

        _translate = QCoreApplication.translate
        self.label_13.setText(_translate("MainWindow", "NOM DE L’ENTREPRISE  "))
        self.label_14.setText(_translate("MainWindow", "POSTE"))
        self.label_15.setText(_translate("MainWindow", "VILLE"))
        self.label_16.setText(_translate("MainWindow", "Date de début"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Janv"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Févr"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Mars"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Avri"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Mai"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Juin"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "Juil"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "Auot"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "Sept"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "Oct"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "Nov"))
        self.comboBox_4.setItemText(11, _translate("MainWindow", "Déc"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "1990"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "1991"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "1992"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "1993"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "1994"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "1995"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "1996"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "1997"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "1998"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "1999"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "2000"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "2001"))
        self.comboBox_5.setItemText(12, _translate("MainWindow", "2002"))
        self.comboBox_5.setItemText(13, _translate("MainWindow", "2003"))
        self.comboBox_5.setItemText(14, _translate("MainWindow", "2004"))
        self.comboBox_5.setItemText(15, _translate("MainWindow", "2005"))
        self.comboBox_5.setItemText(16, _translate("MainWindow", "2006"))
        self.comboBox_5.setItemText(17, _translate("MainWindow", "2007"))
        self.comboBox_5.setItemText(18, _translate("MainWindow", "2008"))
        self.comboBox_5.setItemText(19, _translate("MainWindow", "2009"))
        self.comboBox_5.setItemText(20, _translate("MainWindow", "2010"))
        self.comboBox_5.setItemText(21, _translate("MainWindow", "2011"))
        self.comboBox_5.setItemText(22, _translate("MainWindow", "2012"))
        self.comboBox_5.setItemText(23, _translate("MainWindow", "2013"))
        self.comboBox_5.setItemText(24, _translate("MainWindow", "2014"))
        self.comboBox_5.setItemText(25, _translate("MainWindow", "2015"))
        self.comboBox_5.setItemText(26, _translate("MainWindow", "2016"))
        self.comboBox_5.setItemText(27, _translate("MainWindow", "2017"))
        self.comboBox_5.setItemText(28, _translate("MainWindow", "2018"))
        self.comboBox_5.setItemText(29, _translate("MainWindow", "2019"))
        self.comboBox_5.setItemText(30, _translate("MainWindow", "2020"))
        self.comboBox_5.setItemText(31, _translate("MainWindow", "2021"))
        self.comboBox_5.setItemText(32, _translate("MainWindow", "2022"))
        self.comboBox_5.setItemText(33, _translate("MainWindow", "2023"))
        self.comboBox_5.setItemText(34, _translate("MainWindow", "2024"))
        self.comboBox_5.setItemText(35, _translate("MainWindow", "2025"))
        self.comboBox_5.setItemText(36, _translate("MainWindow", "2026"))
        self.comboBox_5.setItemText(37, _translate("MainWindow", "2027"))
        self.comboBox_5.setItemText(38, _translate("MainWindow", "2028"))
        self.comboBox_5.setItemText(39, _translate("MainWindow", "2029"))
        self.comboBox_5.setItemText(40, _translate("MainWindow", "2030"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Janv"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Févr"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Mars"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Avri"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "Mai"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "Juin"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "Juil"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "Auot"))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "Sept"))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "Oct"))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "Nev"))
        self.comboBox_6.setItemText(11, _translate("MainWindow", "Déc"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "1990"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "1991"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "1992"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "1993"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "1994"))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "1995"))
        self.comboBox_7.setItemText(6, _translate("MainWindow", "1996"))
        self.comboBox_7.setItemText(7, _translate("MainWindow", "1997"))
        self.comboBox_7.setItemText(8, _translate("MainWindow", "1998"))
        self.comboBox_7.setItemText(9, _translate("MainWindow", "1999"))
        self.comboBox_7.setItemText(10, _translate("MainWindow", "2000"))
        self.comboBox_7.setItemText(11, _translate("MainWindow", "2001"))
        self.comboBox_7.setItemText(12, _translate("MainWindow", "2002"))
        self.comboBox_7.setItemText(13, _translate("MainWindow", "2003"))
        self.comboBox_7.setItemText(14, _translate("MainWindow", "2004"))
        self.comboBox_7.setItemText(15, _translate("MainWindow", "2005"))
        self.comboBox_7.setItemText(16, _translate("MainWindow", "2006"))
        self.comboBox_7.setItemText(17, _translate("MainWindow", "2007"))
        self.comboBox_7.setItemText(18, _translate("MainWindow", "2008"))
        self.comboBox_7.setItemText(19, _translate("MainWindow", "2009"))
        self.comboBox_7.setItemText(20, _translate("MainWindow", "2010"))
        self.comboBox_7.setItemText(21, _translate("MainWindow", "2011"))
        self.comboBox_7.setItemText(22, _translate("MainWindow", "2012"))
        self.comboBox_7.setItemText(23, _translate("MainWindow", "2013"))
        self.comboBox_7.setItemText(24, _translate("MainWindow", "2014"))
        self.comboBox_7.setItemText(25, _translate("MainWindow", "2015"))
        self.comboBox_7.setItemText(26, _translate("MainWindow", "2016"))
        self.comboBox_7.setItemText(27, _translate("MainWindow", "2017"))
        self.comboBox_7.setItemText(28, _translate("MainWindow", "2018"))
        self.comboBox_7.setItemText(29, _translate("MainWindow", "2019"))
        self.comboBox_7.setItemText(30, _translate("MainWindow", "2020"))
        self.comboBox_7.setItemText(31, _translate("MainWindow", "2021"))
        self.comboBox_7.setItemText(32, _translate("MainWindow", "2022"))
        self.comboBox_7.setItemText(33, _translate("MainWindow", "2023"))
        self.comboBox_7.setItemText(34, _translate("MainWindow", "2024"))
        self.comboBox_7.setItemText(35, _translate("MainWindow", "2025"))
        self.comboBox_7.setItemText(36, _translate("MainWindow", "2026"))
        self.comboBox_7.setItemText(37, _translate("MainWindow", "2027"))
        self.comboBox_7.setItemText(38, _translate("MainWindow", "2028"))
        self.comboBox_7.setItemText(39, _translate("MainWindow", "2029"))
        self.comboBox_7.setItemText(40, _translate("MainWindow", "2030"))
        self.label_18.setText(_translate("MainWindow", "Tâches réalisées "))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), _translate("MainWindow", "Experience"))
        count4+=1
        
        if count4 == int(Nb_Exp):
            self.pushButton_2.setEnabled(False)
            
        self.pushButton_4.setVisible(True)
        index_exp = (self.toolBox_2.currentIndex())
        
            
    def add_compt(self):
        global count5,add_comp1
        self.page = QWidget()
        self.page.setGeometry(QRect(0, 0, 668, 117))
        self.page.setObjectName("page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(239, 239, 239);\n"
"    /*border:1px solid gray;*/\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius:4px;\n"
"}\n"
"QTextEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setMinimumSize(QSize(0, 60))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.toolBox_3.addItem(self.page, "")
        
        _translate = QCoreApplication.translate
        self.label_19.setText(_translate("MainWindow", "Compétence"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page), _translate("MainWindow", "Compétence"))
        count5+=1
        if count5 == int(Nb_comp):
            self.pushButton_5.setEnabled(False)
            #self.pushButton_5.setVisible(False)
            #self.toolBox_3.setVisible(False)
            #self.pushButton_6.setVisible(False)
            #self.pushButton_7.setVisible(False)
            #self.frame_18.setVisible(False)
            #self.frame_19.setVisible(True)
        self.pushButton_6.setVisible(True)   
        add_comp1 = (self.toolBox_3.currentIndex())
        print(add_comp1)
            
    def add_compt2(self):
        global count6,add_comp2
        self.page = QWidget()
        self.page.setGeometry(QRect(0, 0, 668, 117))
        self.page.setObjectName("page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(239, 239, 239);\n"
"    /*border:1px solid gray;*/\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius:4px;\n"
"}\n"
"QTextEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 0, 0, 1, 1)
        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setMinimumSize(QSize(0, 60))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.toolBox_4.addItem(self.page, "")

        _translate = QCoreApplication.translate
        self.label_20.setText(_translate("MainWindow", "Compétence Personnel"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.page), _translate("MainWindow", "Compétence Personnel"))
        count6+=1
        if count6 == int(Nb_comp_1):
            self.pushButton_8.setEnabled(False)
        self.pushButton_9.setVisible(True)
        add_comp2 = (self.toolBox_4.currentIndex())
            
    def add_Lang(self):
        global count8,indx_lang
        self.page_16 = QWidget()
        self.page_16.setGeometry(QRect(0, 0, 418, 129))
        self.page_16.setObjectName("page_16")
        self.gridLayout_34 = QGridLayout(self.page_16)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.frame_28 = QFrame(self.page_16)
        self.frame_28.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    background-color: rgb(239, 239, 239);\n"
"    /*border:1px solid gray;*/\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.gridLayout_33 = QGridLayout(self.frame_28)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.comboBox_8 = QComboBox(self.frame_28)
        self.comboBox_8.setMinimumSize(QSize(0, 30))
        self.comboBox_8.setCursor(QCursor(Qt.OpenHandCursor))
        self.comboBox_8.setIconSize(QSize(19, 19))
        self.comboBox_8.setObjectName("comboBox_8")
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/flag/flag/ar.PNG"), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(":/flag/flag/eng.PNG"), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(":/flag/flag/fr.PNG"), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(":/flag/flag/russ.PNG"), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addPixmap(QPixmap(":/flag/flag/chin.PNG"), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addPixmap(QPixmap(":/flag/flag/germ.PNG"), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addPixmap(QPixmap(":/flag/flag/jap.PNG"), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addPixmap(QPixmap(":/flag/flag/esp.PNG"), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon12, "")
        self.gridLayout_33.addWidget(self.comboBox_8, 0, 0, 1, 1)
        self.comboBox_9 = QComboBox(self.frame_28)
        self.comboBox_9.setMinimumSize(QSize(0, 30))
        self.comboBox_9.setCursor(QCursor(Qt.OpenHandCursor))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_33.addWidget(self.comboBox_9, 0, 1, 1, 1)
        self.gridLayout_34.addWidget(self.frame_28, 0, 0, 1, 1)
        self.toolBox_5.addItem(self.page_16, "")

        _translate = QCoreApplication.translate
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Arabic"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "English"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Francais"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Russien"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "Chine"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "Germany"))
        self.comboBox_8.setItemText(6, _translate("MainWindow", "Japan"))
        self.comboBox_8.setItemText(7, _translate("MainWindow", "Espane"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Langue maternelle"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Courant"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Notions"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "Scolaire"))
        self.toolBox_5.setItemText(self.toolBox_5.indexOf(self.page_16), _translate("MainWindow", "LANGUES"))
        count8+=1
        if count8 == int(Nb_lang):
            self.pushButton_12.setEnabled(False)
        self.pushButton_13.setVisible(True)
        indx_lang = (self.toolBox_5.currentIndex())
        print(indx_lang)

    def add_loiser(self):
        global count7,indx_lois
        self.page_18 = QWidget()
        self.page_18.setGeometry(QRect(0, 0, 418, 129))
        self.page_18.setObjectName("page_18")
        self.gridLayout_36 = QGridLayout(self.page_18)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.frame_29 = QFrame(self.page_18)
        self.frame_29.setStyleSheet("QLineEdit{\n"
"    \n"
"    \n"
"    background-color: rgb(239, 239, 239);\n"
"    /*border:1px solid gray;*/\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border:1px solid #00aaff;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.gridLayout_35 = QGridLayout(self.frame_29)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.comboBox_10 = QComboBox(self.frame_29)
        self.comboBox_10.setMinimumSize(QSize(20, 30))
        self.comboBox_10.setCursor(QCursor(Qt.OpenHandCursor))
        self.comboBox_10.setObjectName("comboBox_10")
        icon13 = QIcon()
        icon13.addPixmap(QPixmap(":/loiser/loiser/icons8-sports-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addPixmap(QPixmap(":/loiser/loiser/gaming.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addPixmap(QPixmap(":/loiser/loiser/icons8-drawing-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon15, "")
        icon16 = QIcon()
        icon16.addPixmap(QPixmap(":/loiser/loiser/icons8-lire-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon16, "")
        icon17 = QIcon()
        icon17.addPixmap(QPixmap(":/loiser/loiser/icons8-musique-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon17, "")
        icon18 = QIcon()
        icon18.addPixmap(QPixmap(":/loiser/loiser/icons8-natation-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon18, "")
        icon19 = QIcon()
        icon19.addPixmap(QPixmap(":/loiser/loiser/icons8-cyclisme-de-montagne-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon19, "")
        icon20 = QIcon()
        icon20.addPixmap(QPixmap(":/loiser/loiser/icons8-boxing-glove-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon20, "")
        icon21 = QIcon()
        icon21.addPixmap(QPixmap(":/loiser/loiser/icons8-person-surfing-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon21, "")
        icon22 = QIcon()
        icon22.addPixmap(QPixmap(":/loiser/loiser/icons8-football-2-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon22, "")
        icon23 = QIcon()
        icon23.addPixmap(QPixmap(":/loiser/loiser/icons8-chess-pawn-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon23, "")
        icon24 = QIcon()
        icon24.addPixmap(QPixmap(":/loiser/loiser/icons8-équitation-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon24, "")
        icon25 = QIcon()
        icon25.addPixmap(QPixmap(":/loiser/loiser/icons8-trekking-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon25, "")
        icon26 = QIcon()
        icon26.addPixmap(QPixmap(":/loiser/loiser/icons8-skateboard-48.png"), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon26, "")
        self.gridLayout_35.addWidget(self.comboBox_10, 0, 1, 1, 1)
        spacerItem32 = QSpacerItem(110, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem32, 0, 0, 1, 1)
        spacerItem33 = QSpacerItem(110, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem33, 0, 2, 1, 1)
        self.gridLayout_36.addWidget(self.frame_29, 0, 0, 1, 1)
        self.toolBox_6.addItem(self.page_18, "")
        
        _translate = QCoreApplication.translate
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Sport"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Gaming"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "Dessin"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "Lecture"))
        self.comboBox_10.setItemText(4, _translate("MainWindow", "Musique"))
        self.comboBox_10.setItemText(5, _translate("MainWindow", "Natation"))
        self.comboBox_10.setItemText(6, _translate("MainWindow", "Cyclisme de montagne"))
        self.comboBox_10.setItemText(7, _translate("MainWindow", "Boxe"))
        self.comboBox_10.setItemText(8, _translate("MainWindow", "Surf"))
        self.comboBox_10.setItemText(9, _translate("MainWindow", "Football"))
        self.comboBox_10.setItemText(10, _translate("MainWindow", "Chess"))
        self.comboBox_10.setItemText(11, _translate("MainWindow", "équitation"))
        self.comboBox_10.setItemText(12, _translate("MainWindow", "Trekking"))
        self.comboBox_10.setItemText(13, _translate("MainWindow", "Skateboard"))
        self.toolBox_6.setItemText(self.toolBox_6.indexOf(self.page_18), _translate("MainWindow", "LOISER"))
        count7+=1
        if count7 == int(Nb_lois):
            self.pushButton_15.setEnabled(False)
        self.pushButton_16.setVisible(True)
        indx_lois = (self.toolBox_6.currentIndex())

    def reserve_var(self):
        global Nb_Forma,Nb_comp,Nb_comp_1,Nb_Exp,Nb_lois,Nb_lang,doc1
        L = []
        C1 = []
        C2 = []
        D = []
        D2 = []
        EXR = []
        Ls = []
        Lg = []
        doc1 = DocxTemplate("./CV/"+CV)
        Nb_Forma = (self.Nb_Form.text())
        Nb_comp = (self.com_1.text())
        Nb_comp_1 = (self.com_2.text())
        Nb_Exp = (self.lineEdit_7.text())
        Nb_lois = (self.lineEdit_11.text())
        Nb_lang = (self.lineEdit_10.text())
        
        for i in range(0,int(Nb_Forma)):
            context1 = {'exp':"{{D_F"+str(i+1)+"}}\t{{Form"+str(i+1)+"}}\n\t\t{{Etabl"+str(i+1)+"}} {{Ville"+str(i+1)+"}}"}
            L.append(context1)
            #DT = {'DT_1':"{{D_F"+str(i+1)+"}}\n"}
            #D.append(DT)
            
        for j in range(0,int(Nb_comp)):
            comp1 = {'Comp':"{{Comp"+str(j+1)+"}}"}
            C1.append(comp1)

        for k in range(0,int(Nb_comp_1)):
            comp2 = {'Comp2':"{{Comp_"+str(k+1)+"}}"}
            C2.append(comp2)
            
        for d in range(0,int(Nb_Exp)):
            exp = {'exp_1':"{{Date_d"+str(d+1)+"}}\{{Date_f"+str(d+1)+"}}:{{Ville1"+str(d+1)+"}}\n{{Entrp"+str(d+1)+"}}\n{{Poste"+str(d+1)+"}}\n{{Desc"+str(d+1)+"}}"}
            EXR.append(exp)
            #D_EX = {'exp_D':"{{Date_d"+str(d+1)+"}}\n{{Date_f"+str(d+1)+"}}\n{{Ville1"+str(d+1)+"}}"}
            #D2.append(D_EX)
            
        for l in range(0,int(Nb_lois)):
            lois = {'lois_1':"{{Lois_"+str(l+1)+"}}"}
            Ls.append(lois)

        for a in range(0,int(Nb_lang)):
            lang = {'lang':"{{Lang_"+str(a+1)+"}} : {{Lev_"+str(a+1)+"}}"}
            Lg.append(lang)
            
            
        context = {
            'L': L,
            'C1': C1,
            'C2' : C2,
            'D' : D,
            'D2': D2,
            'EXR': EXR,
            'Ls': Ls,
            'Lg': Lg,
            'NP': "{{Prenom}} {{Name}}",
            'Phone':"{{Phone}}",
            'Email':"{{Email}}",
            'Adresse':"{{Adresse}}",
            'DateN':"{{Date_N}}",
            'Poste':"{{Poste}}"
        }
       

        doc1.render(context)
        #doc1.save("CV_A.docx")
        
    #fonction_supp_toolbox
    def supp_lang(self):
        global indx_lang
        print("index : "+str(indx_lang))
        if indx_lang == 0:
            self.pushButton_13.setVisible(False)
        self.toolBox_5.removeItem(indx_lang)
        indx_lang=indx_lang-1

    def supp_lois(self):
        global indx_lois
        print("index : "+str(indx_lois))
        if indx_lois == 0:
            self.pushButton_16.setVisible(False)
        self.toolBox_6.removeItem(indx_lois)
        indx_lois=indx_lois-1

    def supp_form(self):
        global index_form
        print("index : "+str(index_form))
        if index_form == 0:
            self.pushButton_3.setVisible(False)
        self.toolBox.removeItem(index_form)
        index_form=index_form-1

    def supp_exp(self):
        global index_exp
        print("index : "+str(index_exp))
        if index_exp == 0:
            self.pushButton_4.setVisible(False)
        self.toolBox_2.removeItem(index_exp)
        index_exp=index_exp-1
        

    def supp_comp1(self):
        global add_comp1
        print("index : "+str(add_comp1))
        if add_comp1 == 0:
            self.pushButton_6.setVisible(False)
        self.toolBox_3.removeItem(add_comp1)
        add_comp1=add_comp1-1
        
            
    def supp_comp2(self):
        global add_comp2
        print("index : "+str(add_comp2))
        if add_comp2 == 0:
            self.pushButton_9.setVisible(False)
        self.toolBox_4.removeItem(add_comp2)
        add_comp2=add_comp2-1

    #fonction_add_formation_sur_CV   
    def infor(self):
        global count3,count4,D1,L4,FOR,EXP,COMP1,COMP2,LANG,LOIS
        
        for i in range(0,1):
            Form = (self.Form.text())
            Etabl = (self.Etabl.text())
            Ville = (self.lineEdit_4.text())
            D_D = self.Date_D.currentText()
            D_F = self.Date_F.currentText()
            Entrp = (self.Entrep.text())
            Post = (self.Poste.text())
            Ville1 = (self.Ville_1.text())
            Desc = (self.textEdit_2.toPlainText())
            D_Debut = self.comboBox_4.currentText()
            D_Fin = self.comboBox_6.currentText()
            Annee_D = self.comboBox_5.currentText()
            Annee_F = self.comboBox_7.currentText()

            Date_d = "Du "+D_Debut+"/"+Annee_D
            Date_f = "Au "+D_Fin+"/"+Annee_F

            D_F1 = D_D+"/"+D_F
            Comp = self.lineEdit_2.text()
            Comp_1 = self.lineEdit_3.text()
            Lang_2 = self.comboBox_8.currentText()
            Level_lg = self.comboBox_9.currentText()
            Loiser = self.comboBox_10.currentText()
        
        FOR = {
            'Form'+str(count3):Form,
            'Etabl'+str(count3):Etabl,
            'Ville'+str(count3):Ville,
            'D_F'+str(count3):D_F1
            }
        
        EXP = {
            'Entrp'+str(count4):Entrp,
            'Poste'+str(count4):Post,
            'Ville1'+str(count4):Ville1,
            'Desc'+str(count4):Desc,
            'Date_d'+str(count4):Date_d,
            'Date_f'+str(count4):Date_f
            }
        
        COMP1 = {
            'Comp'+str(count5):Comp}
        
        COMP2 = {
            'Comp_'+str(count6):Comp_1}

        LANG = {
            'Lang_'+str(count8):Lang_2,
            'Lev_'+str(count8):Level_lg}

        LOIS = {
            'Lois_'+str(count7):Loiser}
        
        D = {
            'Form'+str(count3):Form,
            'Etabl'+str(count3):Etabl,
            'Ville'+str(count3):Ville,
            'D_F'+str(count3):D_F1,
            'Entrp'+str(count4):Entrp,
            'Poste'+str(count4):Post,
            'Ville1'+str(count4):Ville1,
            'Desc'+str(count4):Desc,
            'Date_d'+str(count4):Date_d,
            'Date_f'+str(count4):Date_f,
            'Comp'+str(count5):Comp,
            'Comp_'+str(count6):Comp_1,
            'Lang_'+str(count8):Lang_2,
            'Lev_'+str(count8):Level_lg,
            'Lois_'+str(count7):Loiser
            }
        D1 = D
        L4.append(D)
    
    #function afficher fin info result
    def R_FOR(self):
        #print(FOR['D_F'+str(count3)]+"\n"+FOR['Form'+str(count3)]+"\n"+FOR['Etabl'+str(count3)]+" "+FOR['Ville'+str(count3)]+"\n")
        self.textBrowser.append(FOR['D_F'+str(count3)]+"\n"+FOR['Form'+str(count3)]+"\n"+FOR['Etabl'+str(count3)]+" "+FOR['Ville'+str(count3)]+"\n")
   
    def R_EXP(self):
        self.textBrowser_2.append(EXP['Date_d'+str(count4)]+" au "+EXP['Date_f'+str(count4)]+"\n"+EXP['Entrp'+str(count4)]+":"+EXP['Ville1'+str(count4)]+"\n"+EXP['Poste'+str(count4)]+"\n"+EXP['Desc'+str(count4)]+"\n")

    def R_COMP1(self):
        self.textBrowser_3.append(str(count5)+"-"+COMP1['Comp'+str(count5)]+"\n")

    def R_COMP2(self):
        self.textBrowser_4.append(str(count6)+"-"+COMP2['Comp_'+str(count6)]+"\n")

    def R_LANG(self):
        self.textBrowser_5.append(LANG['Lang_'+str(count8)]+":"+LANG['Lev_'+str(count8)]+"\n")

    def R_LOIS(self):
        self.textBrowser_6.append(LOIS['Lois_'+str(count7)]+"\n")

    def remplie_cv(self):
        global path
        context = dict()
        F_Name = (self.F_name.text())
        L_Name = (self.L_name.text())
        Phone = (self.phone.text())
        Email = (self.Email.text())
        Adresse = (self.Addr.text())
        Poste = (self.lineEdit_5.text())
        J = self.comboBox_3.currentText()
        M = self.comboBox.currentText()
        Y = self.comboBox_2.currentText()
        Date_N = J+"/"+M+"/"+Y

        self.lineEdit_6.setText(F_Name+" "+L_Name)
        self.lineEdit_8.setText(Phone)
        self.lineEdit_9.setText(Email)
        self.lineEdit_12.setText(Date_N)
        self.lineEdit_13.setText(Adresse)
        self.lineEdit_14.setText(Poste)
        #doc = DocxTemplate("./CV/"+CV)
        doc = doc1
        context = {'Prenom':L_Name,'Name':F_Name,'Phone':Phone,'Email':Email,'Adresse':Adresse,'Date_N':Date_N,'Poste':Poste}
        #print(L4)
        for i in L4:
            F = {key:value for key, value in i.items()}
            for j in F:
                context[j] = F[j]
        
        context_1 = {}
        old_img = "img.png"
        new_img = path
        doc.replace_pic(old_img,new_img)
        doc.render(context)
        doc.render(context_1)
        
        doc.save("CV_"+F_Name+L_Name+".docx")

       
            

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
    QApplication.processEvents()

if __name__ == '__main__':
    main()
        

