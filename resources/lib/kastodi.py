# kastodi.py - main module of the addon
#
# Copyright 2016 kharts (https://github.com/kharts)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

import xbmc
import xbmcgui
from common import *


IDLE_TIME = 1 # 1 second
PLAYER_CONTROLS_ID = 10114 # player controls window ID
WINDOW_OSD = 12901 # video on screen display window ID

def run():
    """
    Main function of the addon
    :return: None
    """

    player = CustomPlayer()

    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        if monitor.waitForAbort(IDLE_TIME):
            # Abort was requested while waiting. We should exit
            break


class CustomPlayer(xbmc.Player):
    """ Class for catching Player events"""

    def onPlayBackStarted(self):
        """
        Start when players playback is started
        :return: None
        """

        #info("onPlayBackStarted")
        self.add_cast_button()

    def add_cast_button(self):
        """
        Add Cast button to player
        :return: None
        """

        #player_window = PlayerWindow(WINDOW_OSD)
        player_window = PlayerWindow()
        player_window.add_cast_button()
        player_window.doModal()


class PlayerWindow(xbmcgui.Window):
    """
    Class for accessing Video OSD window
    """

    def add_cast_button(self):
        """
        Add Cast button to Video OSD window
        :return: None
        """

        if not hasattr(self, "cast_button"):
            self.cast_button = xbmcgui.ControlButton(
                x=50,
                y=50,
                width=72,
                height=72,
                label="",
                focusTexture=image("ic_cast_blue_24dp.png"),
                noFocusTexture=image("ic_cast_white_24dp.png"))
            self.addControl(self.cast_button)
            self.cast_button.setVisible(True)

    def onClick(self, controlId):
        """
        "onClick" event handler
        :param controlId: id of the source of the event
        :type control: xbmcgui.Control
        :return: None
        """

        debug("onClick")
        info("Click")
        if hasattr(self, "cast_button"):
            if controlId == self.cast_button.getId():
                info("Click on cast_button")

    def onControl(self, control):
        """
        onControl event handler
        :param control: source of the event
        :type control: xbmcgui.Control
        :return: None
        """

        debug("onControl")
        info("Some control is pressed")
        if hasattr(self, "cast_button"):
            if control == self.cast_button:
                info("Cast button is pressed")

    def onAction(self, Action):
        """
        onAction event handler
        :param Action: xbmcgui.Action
        :return: None
        """

        debug("onAction")
        info("Action")


if __name__ == "__main__":
    run()
