# Importación de los modulos
from typing import Any
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# Importación de textos
from instructions import txt_instruction, txt_sits, txt_test1, txt_test2, txt_test3, txt_validation
# Colores
_White = (1, 1, 1, 1)
_Black = (0, 0, 0, 1)
_Red = (1, 0, 0, 1)
# Variables
name: str = ''
age: int = 0
frt_result: int = 0
snd_result: int = 0
thrd_result: int = 0
# Funciones
def ruffierRate(p1, p2, p3):
    return (4*(p1 + p2 + p3)-200)/10
# Clases
class input_validation(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initial_text = ''
    
    def validar(self, type:bool, txt:Label):
        '''Type se refiere a si el texto es un número o un texto.
        True para número o False para texto'''
        self.background_color = _White
        self.foreground_color = _Black
        if type:
            try:
                number = int(self.text)
                return number
            except:
                self.change(txt)
                return False
        text = self.text
        if text == '':
            self.change(txt)
            return False
        return text
    def change(self, text:Label):
        self.background_color = _Red
        self.foreground_color = _White
        text.text = txt_validation
        text.color = (1, 0, 0, 1)
        text.markup = True
# Pantallas
class Home(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        #Layouts
        main = BoxLayout(orientation='vertical', padding=20, spacing=8)
        name_input = BoxLayout(size_hint_y=.3)
        age_input = BoxLayout(size_hint_y=.3)
        # Textos
        self.txt = Label(text=txt_instruction)
        name_txt = Label(text='Ingresa tu nombre:', size_hint_x=.3)
        age_txt = Label(text='Ingresa tu edad:', size_hint_x=.3)
        # Inputs
        self.name_inp = input_validation(multiline=False, size_hint=(.8, None), height='30sp', pos_hint={'center_y': .5})
        self.age_inp = input_validation(multiline=False, size_hint=(.8, None), height='30sp',pos_hint={'center_y': .5})
        # Botones
        next_btn = Button(text='Siguiente', size_hint=(.3, .2), pos_hint={'center_x':.5, 'center_y':.5})
        next_btn.bind(on_press=lambda instance: self.changeScreen('screen1'))
        # Organización
        name_input.add_widget(name_txt)
        name_input.add_widget(self.name_inp)
        age_input.add_widget(age_txt)
        age_input.add_widget(self.age_inp)
        main.add_widget(self.txt)
        main.add_widget(name_input)
        main.add_widget(age_input)
        main.add_widget(next_btn)
        self.add_widget(main)
    def changeScreen(self, screen_name):
        global name
        global age
        # Validar los campos
        name = self.name_inp.validar(False, self.txt)
        age = self.age_inp.validar(True, self.txt)
        if not name or not age:
            return False
        self.manager.current = screen_name
# Pantalla 1
class Screen1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Layouts
        main = BoxLayout(orientation='vertical', padding=15, spacing=8)
        result_input = BoxLayout(size_hint_y=.3)
        # Texts
        self.txt = Label(text=txt_test1)
        result_txt = Label(text='Ingresar el resultado:', size_hint_x=.3)
        # Inputs
        self.result_inp = input_validation(multiline=False, size_hint=(.8, None), height='30sp', pos_hint={'center_y': .5})
        # Botones
        next_btn = Button(text='Siguiente', size_hint=(.3, .2), pos_hint={'center_x':.5, 'center_y':.5})
        next_btn.bind(on_press=lambda instance: self.changeScreen('screen2'))
        # Organización
        result_input.add_widget(result_txt)
        result_input.add_widget(self.result_inp)
        main.add_widget(self.txt)
        main.add_widget(result_input)
        main.add_widget(next_btn)
        self.add_widget(main)
    def changeScreen(self, screen_name):
        global frt_result
        frt_result = self.result_inp.validar(True, self.txt)
        if not frt_result:
            return False
        self.manager.current = screen_name
# Pantalla 2
class Screen2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Layouts
        main = BoxLayout(orientation='vertical', padding=15, spacing=8)
        # Texts
        txt = Label(text=txt_sits)
        # Botones
        next_btn = Button(text='Siguiente', size_hint=(.3, .2), pos_hint={'center_x':.5, 'center_y':.5})
        next_btn.bind(on_press=lambda instance: self.changeScreen('screen3'))
        # Organización
        main.add_widget(txt)
        main.add_widget(next_btn)
        self.add_widget(main)
    def changeScreen(self, screen_name):
        self.manager.current = screen_name
# Pantalla 3
class Screen3(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Layouts
        main = BoxLayout(orientation='vertical', padding=15, spacing=8)
        result1_input = BoxLayout(size_hint_y=.3)
        result2_input = BoxLayout(size_hint_y=.3)
        # Texts
        self.txt = Label(text=txt_test3)
        result1_txt = Label(text='Resultado:', size_hint_x=.3)
        result2_txt = Label(text='Resultado despues del descanso:', size_hint_x=.3)
        # Inputs
        self.result1_inp = input_validation(multiline=False, size_hint=(.8, None), height='30sp', pos_hint={'center_y': .5})
        self.result2_inp = input_validation(multiline=False, size_hint=(.8, None), height='30sp', pos_hint={'center_y': .5})
        # Botones
        next_btn = Button(text='Finalizar', size_hint=(.3, .2), pos_hint={'center_x':.5, 'center_y':.5})
        next_btn.bind(on_press=lambda instance: self.changeScreen('screen4'))
        # Organización
        result1_input.add_widget(result1_txt)
        result1_input.add_widget(self.result1_inp)
        result2_input.add_widget(result2_txt)
        result2_input.add_widget(self.result2_inp)
        main.add_widget(self.txt)
        main.add_widget(result1_input)
        main.add_widget(result2_input)
        main.add_widget(next_btn)
        self.add_widget(main)
    def changeScreen(self, screen_name):
        global snd_result
        global thrd_result
        snd_result = self.result1_inp.validar(True, self.txt)
        thrd_result = self.result2_inp.validar(True, self.txt)
        if not snd_result or not thrd_result:
            return False
        self.manager.current = screen_name
class FinalResult(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.txt = Label(text='')
        self.on_enter = self.before
        self.add_widget(self.txt)
    def before(self):
        global name
        global frt_result
        global snd_result
        global thrd_result
        self.txt.text = name+'\n'+'Tu índice de Ruffier: '+str(ruffierRate(frt_result, snd_result, thrd_result))
        
# Clase main
class myApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))
        sm.add_widget(FinalResult(name='screen4'))
        return sm
# Se ejecuta la app
app = myApp()
if __name__ == '__main__':
    app.run()