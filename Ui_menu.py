# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_menu(object):
    def setupUi(self, menu):
        if not menu.objectName():
            menu.setObjectName(u"menu")
        menu.resize(836, 600)
        self.centralwidget = QWidget(menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 30, 731, 521))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4 Light"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.upload_frame = QFrame(self.layoutWidget)
        self.upload_frame.setObjectName(u"upload_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_frame.sizePolicy().hasHeightForWidth())
        self.upload_frame.setSizePolicy(sizePolicy)
        self.upload_frame.setAcceptDrops(True)
        self.upload_frame.setFrameShape(QFrame.StyledPanel)
        self.upload_frame.setFrameShadow(QFrame.Plain)
        self.upload_frame.setLineWidth(1)
        self.upload_frame.setMidLineWidth(1)
        self.layoutWidget1 = QWidget(self.upload_frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(220, 50, 290, 291))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.uploadBtn = QPushButton(self.layoutWidget1)
        self.uploadBtn.setObjectName(u"uploadBtn")
        sizePolicy.setHeightForWidth(self.uploadBtn.sizePolicy().hasHeightForWidth())
        self.uploadBtn.setSizePolicy(sizePolicy)
        self.uploadBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.uploadBtn)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.upload_frame)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        menu.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(menu)
        self.statusbar.setObjectName(u"statusbar")
        menu.setStatusBar(self.statusbar)

        self.retranslateUi(menu)

        QMetaObject.connectSlotsByName(menu)
    # setupUi

    def retranslateUi(self, menu):
        menu.setWindowTitle(QCoreApplication.translate("menu", u"\u4e0a\u50b3\u5f71\u7247", None))
        self.label.setText(QCoreApplication.translate("menu", u"\u4e0a\u50b3\u5f71\u7247", None))
        self.label_2.setText(QCoreApplication.translate("menu", u"\u8acb\u5c07\u5f71\u7247\u62d6\u66f3\u81f3\u6b64\u8655", None))
        self.uploadBtn.setText(QCoreApplication.translate("menu", u"\u9078\u64c7\u6a94\u6848", None))
    # retranslateUi
