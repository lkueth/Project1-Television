from gui import *
from PyQt6.QtWidgets import *

MIN_VOLUME = 0
MAX_VOLUME = 3
MIN_CHANNEL = 1
MAX_CHANNEL = 9


class Logic(QMainWindow, Ui_television_gui):
    """
    This class handles the logic for the television GUI. It manages power, mute,
    volume, and channel functions.
    """

    def __init__(self) -> None:
        """
        Initializes the television GUI and sets up the defaults for the GUI
        """
        super().__init__()
        self.setupUi(self)
        self.__status = False
        self.__muted = False
        self.__volume = MIN_VOLUME
        self.__channel = MIN_CHANNEL
        self.mute_button.setEnabled(False)
        self.channelup_button.setEnabled(False)
        self.channeldown_button.setEnabled(False)
        self.volumeup_button.setEnabled(False)
        self.volumedown_button.setEnabled(False)
        self.channelnumber_indicator.setHidden(True)

        self.__channel_list = [
            self.channel1_button, self.channel2_button, self.channel3_button,
            self.channel4_button, self.channel5_button, self.channel6_button,
            self.channel7_button, self.channel8_button, self.channel9_button
        ]
        for button in self.__channel_list:
            button.setEnabled(False)

        self.power_button.clicked.connect(lambda: self.power())
        self.mute_button.clicked.connect(lambda: self.mute())
        self.channelup_button.clicked.connect(lambda: self.channel_up())
        self.channeldown_button.clicked.connect(lambda: self.channel_down())
        self.volumeup_button.clicked.connect(lambda: self.volume_up())
        self.volumedown_button.clicked.connect(lambda: self.volume_down())
        self.channel1_button.clicked.connect(lambda: self.channel1_input())
        self.channel2_button.clicked.connect(lambda: self.channel2_input())
        self.channel3_button.clicked.connect(lambda: self.channel3_input())
        self.channel4_button.clicked.connect(lambda: self.channel4_input())
        self.channel5_button.clicked.connect(lambda: self.channel5_input())
        self.channel6_button.clicked.connect(lambda: self.channel6_input())
        self.channel7_button.clicked.connect(lambda: self.channel7_input())
        self.channel8_button.clicked.connect(lambda: self.channel8_input())
        self.channel9_button.clicked.connect(lambda: self.channel9_input())

    def power(self) -> None:
        """
        Toggles the power status of the television.
        Enables or disables buttons and updates the display based on the status.
        """
        if self.__status == False:
            self.__status = True
            self.televisionscreen.setPixmap(QtGui.QPixmap(f"channels/channel{self.__channel}.png"))
            self.mute_button.setEnabled(True)
            self.channelup_button.setEnabled(True)
            self.channeldown_button.setEnabled(True)
            self.volumeup_button.setEnabled(True)
            self.volumedown_button.setEnabled(True)
            self.channelnumber_indicator.setHidden(False)
            self.channelnumber_indicator.setProperty("value", self.__channel)
            for button in self.__channel_list:
                button.setEnabled(True)
        elif self.__status == True:
            self.__status = False
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/off.png"))
            self.mute_button.setEnabled(False)
            self.channelup_button.setEnabled(False)
            self.channeldown_button.setEnabled(False)
            self.volumeup_button.setEnabled(False)
            self.volumedown_button.setEnabled(False)
            self.channelnumber_indicator.setHidden(True)
            for button in self.__channel_list:
                button.setEnabled(False)

    def mute(self) -> None:
        """
        Toggles the mute status.
        Disables volume buttons when muted and restores volume when unmuted.
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
                self.volume_progressbar.setProperty("value", 0)
                self.volumeup_button.setEnabled(False)
                self.volumedown_button.setEnabled(False)
            elif self.__muted == True:
                self.__muted = False
                self.volume_progressbar.setProperty("value", self.__volume)
                self.volumeup_button.setEnabled(True)
                self.volumedown_button.setEnabled(True)

    def volume_up(self) -> None:
        """
        Increases the volume by 1 if not at the maximum volume level.
        """
        if self.__status:
            if not self.__volume == MAX_VOLUME:
                self.__volume += 1
                self.volume_progressbar.setProperty("value", self.__volume)

    def volume_down(self) -> None:
        """
        Decreases the volume by 1 if not at the minimum volume level.
        """
        if self.__status:
            if not self.__volume == MIN_VOLUME:
                self.__volume -= 1
                self.volume_progressbar.setProperty("value", self.__volume)

    def channel_up(self) -> None:
        """
        Changes to the next channel.
        Wraps around to the first channel if the current channel is the last.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > MAX_CHANNEL:
                self.__channel = MIN_CHANNEL
            self.televisionscreen.setPixmap(QtGui.QPixmap(f"channels/channel{self.__channel}.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel_down(self) -> None:
        """
        Changes to the previous channel.
        Wraps around to the last channel if the current channel is the first.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < MIN_CHANNEL:
                self.__channel = MAX_CHANNEL
            self.televisionscreen.setPixmap(QtGui.QPixmap(f"channels/channel{self.__channel}.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel1_input(self) -> None:
        """
        Switches to channel 1 and updates the display.
        """
        if self.__status:
            self.__channel = 1
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel1.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel2_input(self) -> None:
        """
        Switches to channel 2 and updates the display.
        """
        if self.__status:
            self.__channel = 2
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel2.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel3_input(self) -> None:
        """
        Switches to channel 3 and updates the display.
        """
        if self.__status:
            self.__channel = 3
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel3.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel4_input(self) -> None:
        """
        Switches to channel 4 and updates the display.
        """
        if self.__status:
            self.__channel = 4
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel4.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel5_input(self) -> None:
        """
        Switches to channel 5 and updates the display.
        """
        if self.__status:
            self.__channel = 5
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel5.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel6_input(self) -> None:
        """
        Switches to channel 6 and updates the display.
        """
        if self.__status:
            self.__channel = 6
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel6.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel7_input(self) -> None:
        """
        Switches to channel 7 and updates the display.
        """
        if self.__status:
            self.__channel = 7
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel7.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel8_input(self) -> None:
        """
        Switches to channel 8 and updates the display.
        """
        if self.__status:
            self.__channel = 8
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel8.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)

    def channel9_input(self) -> None:
        """
        Switches to channel 9 and updates the display.
        """
        if self.__status:
            self.__channel = 9
            self.televisionscreen.setPixmap(QtGui.QPixmap("channels/channel9.png"))
            self.channelnumber_indicator.setProperty("value", self.__channel)
