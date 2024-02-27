import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QPushButton, QSlider

class Ui_MainWindowobject():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_videoBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_videoBox.setGeometry(QtCore.QRect(10, 60, 781, 291))
        self.groupBox_videoBox.setTitle("")
        self.groupBox_videoBox.setObjectName("groupBox_videoBox")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    background-color : black;\n border : None;"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_browse = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_browse.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.pushButton_browse.setStyleSheet("QPushButton{\n"
"    background-color : transparent;\n"
"    color : white;\n"
"}\n"
"")
        icon = QtGui.QIcon("browse.png")  # Corrected the path
        self.pushButton_browse.setIcon(icon)
        self.pushButton_browse.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 400, 801, 51))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    background-color : black; border : None;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_play = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.pushButton_play.setStyleSheet("QPushButton{\n"
"    background-color : transparent;\n"
"color : white;\n "
"}")
        icon1 = QtGui.QIcon("play.png")  # Corrected the path
        self.pushButton_play.setIcon(icon1)
        self.pushButton_play.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_pause = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_pause.setGeometry(QtCore.QRect(90, 10, 93, 28))
        self.pushButton_pause.setStyleSheet("QPushButton{\n"
"    background-color : transparent;\n"
"color : white;\n"
"\n"
"\n"
"}")
        icon2 = QtGui.QIcon("pause.png")  # Corrected the path
        self.pushButton_pause.setIcon(icon2)
        self.pushButton_pause.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(190, 20, 401, 22))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #94D6B9; /* light green border */\n"
"    height: 10px; /* thickness of the groove */\n"
"    background: #D8F3E0; /* light green background */\n"
"    border-radius: 5px; /* border radius */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2E8B57; /* dark green handle color */\n"
"    border: 1px solid #2E8B57; /* dark green handle border */\n"
"    width: 20px; /* handle width */\n"
"    margin: -5px 0; /* handle position */\n"
"    border-radius: 5px; /* border radius */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #228B22; /* dark green handle color on hover */\n"
"    border: 1px solid #228B22; /* dark green handle border on hover */\n"
"}\n"
"")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.groupBox_2.raise_()
        self.groupBox_videoBox.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add speedometer icon and dropdown menu
        self.speedometer_icon = QtWidgets.QPushButton(self.groupBox_2)
        self.speedometer_icon.setGeometry(QtCore.QRect(650, 10, 30, 30))
        self.speedometer_icon.setIcon(QtGui.QIcon("speedometer.png"))  # Adjust the path as needed
        self.speedometer_icon.setIconSize(QtCore.QSize(20, 20))
        self.speedometer_icon.setStyleSheet("background-color: transparent;")
        self.speedometer_icon.setObjectName("speedometer.png")
        
        self.speed_options = ["Normal" , "1.5x", "1.75x", "2x"]
        self.speed_dropdown = QtWidgets.QComboBox(self.groupBox_2)
        self.speed_dropdown.setGeometry(QtCore.QRect(690, 10, 71, 31))
        self.speed_dropdown.addItems(self.speed_options)
        self.speed_dropdown.setObjectName("speed_dropdown")
        self.speed_dropdown.setStyleSheet("QComboBox{"
                                       "border : none;"
                                       "border-radius : 5px;"
                                       "}")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_browse.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic;\">Browse Video</span></p></body></html>"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.pushButton_pause.setText(_translate("MainWindow", "Pause"))
        self.pushButton_browse.setText(_translate("MainWindow" , "Browse"))


#Video Player Class
class videoPlayer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_browse.clicked.connect(self.browse_video)
        self.ui.pushButton_play.clicked.connect(self.play_video)
        self.ui.pushButton_pause.clicked.connect(self.pause_video)  # Connect pause button to method
        self.ui.horizontalSlider.sliderMoved.connect(self.set_slider_position)
        self.ui.speed_dropdown.activated[str].connect(self.on_speed_selected)
        self.cap = None
        self.paused = False  # Flag to track if video is paused
        self.speed = 1

    def browse_video(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setNameFilter("Videos (*.mp4 *.avi *.mkv)")
        file_dialog.selectNameFilter("Videos (*.mp4 *.avi *.mkv)")
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                video_path = file_paths[0]
                self.cap = cv2.VideoCapture(video_path)
                ret, frame = self.cap.read()
                if ret:
                    groupBox_width = self.ui.groupBox_videoBox.width()
                    groupBox_height = self.ui.groupBox_videoBox.height()
                    frame_resized = cv2.resize(frame, (groupBox_width, groupBox_height))
    
                    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
                    h, w, ch = frame_rgb.shape
                    bytes_per_line = ch * w
                    q_img = QtGui.QImage(frame_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
                    pixmap = QtGui.QPixmap.fromImage(q_img)
                    label = QLabel(self.ui.groupBox_videoBox)
                    label.setPixmap(pixmap)
                    label.show()
                self.ui.horizontalSlider.setMinimum(0)
                self.ui.horizontalSlider.setMaximum(int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    def play_video(self):
        if self.cap is None or not self.cap.isOpened():
            return

        groupBox_width = self.ui.groupBox_videoBox.width()
        groupBox_height = self.ui.groupBox_videoBox.height()
        # Adjust the speed
        speed = self.on_speed_selected(self.ui.speed_dropdown.currentText())
        fps = self.cap.get(cv2.CAP_PROP_FPS) * speed
        print(fps)
        while True:
            if not self.paused:  # Check if video is paused
                ret, frame = self.cap.read()
                if ret:
                    

                    frame_resized = cv2.resize(frame, (groupBox_width, groupBox_height))
                    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
                    h, w, ch = frame_rgb.shape
                    bytes_per_line = ch * w
                    q_img = QtGui.QImage(frame_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
                    pixmap = QtGui.QPixmap.fromImage(q_img)
                    label = QLabel(self.ui.groupBox_videoBox)
                    label.setPixmap(pixmap)
                    label.show()
                    QtWidgets.QApplication.processEvents()

                    # Calculate the current frame position based on adjusted fps
                    current_frame = int(fps)
                    self.ui.horizontalSlider.setValue(current_frame)
                else:
                    break



#     def display_fps(self):
#         if self.cap is None or not self.cap.isOpened():
#             return
        
#         fps = self.cap.get(cv2.CAP_PROP_FPS)
#         self.ui.label_fps.setText("FPS: {:.2f}".format(fps))
    
    def set_slider_position(self, position):
        if self.cap is None or not self.cap.isOpened():
            return
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, position)

    def pause_video(self):
        self.paused = not self.paused 

    def on_speed_selected(self, speed):
        if speed == '1.5x':
            return 1.5
        elif speed == '1.75x':
            return 1.75
        elif speed == '2x':
            return 2
        elif speed == 'Normal':
            return 1   

        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = videoPlayer()
    MainWindow.show()
    sys.exit(app.exec_())
                