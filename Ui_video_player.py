# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_player.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_video_player(object):
    def setupUi(self, video_player):
        if not video_player.objectName():
            video_player.setObjectName(u"video_player")
        video_player.resize(1314, 889)
        self.widget = QWidget(video_player)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 40, 1190, 846))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bufferWidget = QWidget(self.widget)
        self.bufferWidget.setObjectName(u"bufferWidget")
        self.bufferWidget.setMinimumSize(QSize(1024, 768))

        self.verticalLayout.addWidget(self.bufferWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startTimeLbl = QLabel(self.widget)
        self.startTimeLbl.setObjectName(u"startTimeLbl")
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(14)
        self.startTimeLbl.setFont(font)

        self.horizontalLayout_2.addWidget(self.startTimeLbl)

        self.videoSlider = QSlider(self.widget)
        self.videoSlider.setObjectName(u"videoSlider")
        self.videoSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.videoSlider)

        self.EndTimeLbl = QLabel(self.widget)
        self.EndTimeLbl.setObjectName(u"EndTimeLbl")
        self.EndTimeLbl.setFont(font)

        self.horizontalLayout_2.addWidget(self.EndTimeLbl)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.playBtn = QPushButton(self.widget)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setFont(font)

        self.horizontalLayout.addWidget(self.playBtn)

        self.pauseBtn = QPushButton(self.widget)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setFont(font)

        self.horizontalLayout.addWidget(self.pauseBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(video_player)

        QMetaObject.connectSlotsByName(video_player)
    # setupUi

    def retranslateUi(self, video_player):
        video_player.setWindowTitle(QCoreApplication.translate("video_player", u"\u64ad\u653e\u5f71\u7247", None))
        self.startTimeLbl.setText(QCoreApplication.translate("video_player", u"0:00", None))
        self.EndTimeLbl.setText(QCoreApplication.translate("video_player", u"0:00", None))
        self.playBtn.setText(QCoreApplication.translate("video_player", u"Play", None))
        self.pauseBtn.setText(QCoreApplication.translate("video_player", u"Pause", None))
    # retranslateUi

