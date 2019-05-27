# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/27 15:41'
__author__ = 'lee7goal'
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.app import App

class MyApp(App):
    def build(self):
        s = Scatter()
        l = Label(text='Hello World', font_size=50)
        s.add_widget(l)
        return s

if __name__ == '__main__':
    MyApp().run()
