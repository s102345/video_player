import sys, os, datetime
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSlider
from PySide6 import QtCore
from PySide6.QtCore import QFile, QUrl
from PySide6.QtGui import QPixmap, QImage, QKeyEvent
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from Ui_video_player import Ui_video_player


class Video_player(QMainWindow, Ui_video_player):
    def __init__(self, filePath):
        super(Video_player, self).__init__()
        self.setupUi(self)
        self.filePath = filePath
        #影片
        self.qMediaPlayer = QMediaPlayer(self) 
        self.lay = QVBoxLayout(self.bufferWidget)
        self.videoWidget = QVideoWidget(self)
        self.videoWidget.resize(self.bufferWidget.size())
        self.lay.addWidget(self.videoWidget)
        self.qMediaPlayer.setVideoOutput(self.videoWidget)
        #進度條初始化
        self.videoSlider.valueChanged.connect(lambda: self.qMediaPlayer.setPosition(self.videoSlider.value()))
        self.videoSlider.setMinimum(0)
        #毫秒(ms)
        self.qMediaPlayer.durationChanged.connect(self.updateDuration)
        #更新進度條位置
        self.qMediaPlayer.positionChanged.connect(self.updatePosition)
        #播放
        self.playBtn.clicked.connect(lambda: self.qMediaPlayer.play())
        #暫停
        self.pauseBtn.clicked.connect(lambda: self.qMediaPlayer.pause())    
        #Frame rate
        video = cv2.VideoCapture(self.filePath)
        self.fps = video.get(cv2.CAP_PROP_FPS)
        video.release()
        #播放影片
        self.qMediaPlayer.setSource(QUrl.fromLocalFile(self.filePath))
        self.qMediaPlayer.play()
        #播完
        self.qMediaPlayer.mediaStatusChanged.connect(self.videoEnd)

    def videoEnd(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.qMediaPlayer.setSource(QUrl.fromLocalFile(self.filePath))
            self.qMediaPlayer.pause()

    def updatePosition(self):
        self.videoSlider.setValue(self.qMediaPlayer.position())
        sec = int(self.qMediaPlayer.position() / 1000)
        formattedTime = str(datetime.timedelta(seconds = sec)).split(':')
        #沒有小時
        if formattedTime[0] == '0':
            self.startTimeLbl.setText(':'.join(formattedTime[1:]))
        else:
            self.startTimeLbl.setText(':'.join(formattedTime))

    def updateDuration(self):
        self.videoSlider.setMaximum(self.qMediaPlayer.duration())
        sec = int(self.qMediaPlayer.duration() / 1000)
        formattedTime = str(datetime.timedelta(seconds = sec)).split(':')
        #沒有小時
        if formattedTime[0] == '0':
            self.EndTimeLbl.setText(':'.join(formattedTime[1:]))
        else:
            self.EndTimeLbl.setText(':'.join(formattedTime))

    def keyPressEvent(self, event):
        #Key D
        if str(event.key()) == '68':
            try:
                event.accept()
                self.qMediaPlayer.setPosition(self.qMediaPlayer.position() + int(self.fps))
            except:
                pass
        #Key A
        if str(event.key()) == '65':
            try:
                event.accept()
                self.qMediaPlayer.setPosition(self.qMediaPlayer.position() - int(self.fps))
            except:
                pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Video_player("./LavaLoot_盤面辨識錄製狀態.mkv")
    window.show()
    sys.exit(app.exec())