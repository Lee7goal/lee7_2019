# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/27 15:01'
__author__ = 'lee7goal'
import kivy
from kivy.app import App  # 从这个包里面导入App类
from kivy.uix.button import Button  # 从uixbutton里导入button按钮类
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Button(text='Log In', background_color=(0, 0, 1, 1), font_size=50))
        self.add_widget(Button(text='Quit', background_color=(0, 0, 1, 1), font_size=50))

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()