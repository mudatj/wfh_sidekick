#!/usr/bin/env python
# coding: utf-8
from kivy.config import Config 
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '350')

from datetime import datetime
from threading import Thread
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s', filename='example1.log', filemode='w', 
level=logging.INFO)
import subprocess
import sys
import time
import pyautogui
import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.factory import Factory
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivymd.uix.button import MDIconButton, MDTooltip
from kivy.factory import Factory

class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass

class Work_From_Home_Side_Kick(MDApp):

    #count = 0
    #source kivy_venv/bin/activate

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "600"
        return Wfh_main_window()

    Config.set('graphics', 'resizable', True)

class Wfh_main_window(MDFloatLayout):
    #number = NumericProperty()  
    count = 0

    def noidle(self, nap):
        x, y = pyautogui.position()
        pyautogui.click(x, y+20)
        x, y = pyautogui.position()
        pyautogui.click(x, y-10)
        print('done: ', datetime.now())
        logging.info(datetime.now())

    def time_a(self):
        #self.ids['activelbl'].text = 'ACTIVE'
        self.sch1 = Clock.schedule_interval(self.noidle, 5)

    def stop_a(self):
        #self.ids['activelbl'].text = 'INACTIVE'
        Clock.unschedule(self.sch1)
        
    #def displaytime(self, dt, instance):
        #self.count = self.count + 1
        #self.displaytime = "Time: % d"% self.count

#create a function for the screen shot button and a variable to save the file as new name each time
    def screenshot_a(self):
        self.count = self.count + 1
        self.im = pyautogui.screenshot('screenshot%d.png' % self.count)
        print('screen shot taken')

if __name__ == '__main__':
    Work_From_Home_Side_Kick().run()