from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
import random

class StartScreen(Screen):
    modePlay = NumericProperty(0)

    def exit(self):
        App.get_running_app().stop()


class RootWidget(Screen):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.posibles = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
        self.dataStart()

    def dataStart(self):
        self.player1 = "player 1"
        self.player2 = "player 2"
        self.gana = []
        self.tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.tableroControl = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.total_mueve = 0
        self.fin = False
        self.Turno = self.player1
        self.idLabel = ["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho"]

    def startGame(self, mode):
        self.modePlay = mode

    def continuee(self, event):
        self.dataStart()
        for x in self.idLabel:
            try:
                borrar = self.ids[x].children[0]
                self.ids[x].remove_widget(borrar)
            except:
                pass
        self.parent.current = 'start'

    def iaModule(self):
        listFree = list()
        free = 11
        for y in range(8):
            primera = self.posibles[y]
            same = 0
            for t in range(3):
                gg = primera[t]
                x = self.tablero[gg]
                if x == 'x':
                    same += 1
                elif x != 'o':
                    free = int(x)
                    listFree.append(free)
                else:
                    same -= 1
            if same == 2:
                return self.idLabel[free -1]
        free = random.choice(listFree)
        return self.idLabel[free -1]

    def check_win(self,tablero):
        for y in range(8):
            primera = self.posibles[y]
            marca = ""
            gana = 0
            for t in range(3):  # range 3 recorre cada posibilidad
                gg = primera[t]
                x = tablero[gg]
                if x == "x":
                    if (marca == "o"):
                        gana = gana - 1
                    else:
                        gana = gana + 1
                        marca = "x"
                elif x == "o":
                    if marca == "x":
                        gana = gana - 1
                    else:
                        marca = "o"
                        gana = gana + 1
                if gana == 3:
                    return True
        return False

    def marca_tablero(self,tableroControl, valor):
        index = "--"
        for x in range(len(tableroControl)):
            if x == (int(valor)):
                if tableroControl[x] == "--":
                    index = "--"
                    break
                else:
                    tableroControl[x] = "--"
                    index = x
                    self.total_mueve += 1
                    break
        return index

    def get_post(self, valor):
        if valor == "cero":
            return 0
        elif valor == "uno":
            return 1
        elif valor == "dos":
            return 2
        elif valor == "tres":
            return 3
        elif valor == "cuatro":
            return 4
        elif valor == "cinco":
            return 5
        elif valor == "seis":
            return 6
        elif valor == "siete":
            return 7
        elif valor == "ocho":
            return 8

    def getPopContinue(self, msg):
        content1 = Button(text=msg)
        popup1 = Popup(title='WINNER', content=content1, size_hint=(0.3, 0.2),
                       auto_dismiss=False)
        content1.bind(on_press=popup1.dismiss)
        content1.bind(on_press=self.continuee)
        popup1.open()

    def twoPlayer(self, id):
        valor = self.get_post(id)
        posMarcar = self.marca_tablero(self.tableroControl, valor)
        self.ids[id].text = ""
        if self.Turno == self.player1:
            if posMarcar != "--":
                self.tablero[posMarcar] = "x"
                self.Turno = self.player2
                self.ids[id].add_widget(
                    Image(id=id, source='circle.png', size=self.ids[id].size, y=self.ids[id].y, x=self.ids[id].x))
        else:
            if posMarcar != "--":
                self.tablero[posMarcar] = "o"
                self.Turno = self.player1
                self.ids[id].add_widget(
                    Image(id=id, source='cruz2.png', size=self.ids[id].size, y=self.ids[id].y, x=self.ids[id].x))
        gana = self.check_win(self.tablero)
        if gana:
            if self.Turno == self.player1:
                msg = 'Player 2, with X'
                self.getPopContinue(msg)
            else:
                msg = 'Player 1, with O'
                self.getPopContinue(msg)
        elif self.total_mueve == 9:
            msg = 'Sin Ganadores'
            self.getPopContinue(msg)

    def do_action(self, id, modePlay):
        checkTurn = True
        if self.total_mueve < 9:
            if modePlay == 2:
                self.twoPlayer(id)
            if modePlay == 1: #player vs IA
                while checkTurn:
                    if self.Turno == self.player2:
                        id = self.iaModule()
                    valor = self.get_post(id)
                    posMarcar = self.marca_tablero(self.tableroControl, valor)
                    self.ids[id].text = ""
                    if self.Turno == self.player1:
                        if posMarcar != "--":
                            self.tablero[posMarcar] = "x"
                            self.Turno = self.player2
                            self.ids[id].add_widget(
                                Image(id=id ,source='circle.png', size=self.ids[id].size, y=self.ids[id].y, x=self.ids[id].x))
                        else:
                            checkTurn = False
                    else:
                        if posMarcar != "--":
                            self.tablero[posMarcar] = "o"
                            self.Turno = self.player1
                            checkTurn = False
                            self.ids[id].add_widget(
                                Image(id=id, source='cruz2.png', size=self.ids[id].size, y=self.ids[id].y, x=self.ids[id].x))
                    gana = self.check_win(self.tablero)
                    if gana:
                        if self.Turno == self.player1:
                            msg = 'AI JUAN :b, with X'
                            self.getPopContinue(msg)
                        else:
                            msg = 'Player 1, with O'
                            self.getPopContinue(msg)
                            checkTurn = False
                    elif self.total_mueve == 9:
                        msg = 'Sin Ganadores'
                        self.getPopContinue(msg)
                        checkTurn = False

    def exit(self):
        App.get_running_app().stop()


class ScreenManagement(ScreenManager):
    pass

begin = Builder.load_string('''
ScreenManagement:
    StartScreen:
        id: startScreen
    RootWidget:
        modePlay: startScreen.modePlay

<StartScreen>
    name: 'start'
    canvas:
        Color:
            rgba: 0/255.0, 0/255.0, 255/255.0, 1
        Rectangle:
            size: root.size
            pos: root.pos
    BoxLayout:
        size_hint: .5, .8
        pos_hint: {'center_x': .5, 'center_y': .5}
        orientation:'vertical'
        spacing: '8sp'
        padding: '50sp', '50sp'
        Button:
            background_color: 0,0,0,0 #button transparente
            haling: 'center'
            font_name: 'TROGN.ttf'
            text: '1 Player'
            font_size: 32
            color: .8,.9,0,1
            on_press: 
                root.modePlay = 1
                root.manager.transition.direction = 'left'
                root.manager.current = 'table'

        Button:
            background_color: 0,0,0,0
            haling: 'center'
            font_name: 'TROGN.ttf'
            text: '2 Player'
            font_size: 32
            color: .8,.9,0,1
            on_press: 
                root.modePlay = 2
                root.manager.transition.direction = 'down'
                root.manager.current = 'table'

        Button:
            background_color: 0,0,0,0
            font_name: 'TROGN.ttf'
            font_size: 28
            color: 1, 0, 0, 1
            text: 'Exit'
            on_press:
                root.exit()
        Image:
            source: 'logo.png'
        Label:
            color: 1,1,1,1
            text: "Developed by Juan"


<GridLayout>
    canvas.before:
        Color:
            rgba: 0/255.0, 0/255.0, 255/255.0, 1
        BorderImage:
       #     # BorderImage behaves like the CSS BorderImage
            border: 10, 10, 10, 10
            pos: self.pos
            size: self.size

<RootWidget>
    name: 'table'
    canvas:
        Color:
            rgba: 0, 0, 1, 1
        Rectangle:
            size: root.size
            pos: root.pos

    GridLayout:
        id: grid
        size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:3
        cols:3
        Button:
            background_color: (255, 255, 255, 1)
            id: seis
            on_press: root.do_action("seis", root.modePlay)
        Button:
            background_color: (255, 255, 255, 1)
            id: siete
            on_press: root.do_action("siete", root.modePlay)
        Button:
            background_color: (255, 255, 255, 1)
            id: ocho
            on_press: root.do_action("ocho", root.modePlay)
        Button:
            background_color: (255, 255, 255, 1)
            id: tres
            on_press: root.do_action("tres", root.modePlay)
        Button:
            background_color: (255, 255, 255, 1)
            id: cuatro
            on_press: root.do_action("cuatro", root.modePlay)
        Button:
            background_color: (255, 255, 255, 1)
            id: cinco
            on_press: root.do_action("cinco", root.modePlay)
        Button:
            background_color: (255, 255, 255, 1)
            id: cero
            on_press: root.do_action("cero", root.modePlay)
        Button:
            background_color: (255, 255, 255, 1)
            id: uno
            on_press: root.do_action("uno", root.modePlay)
        Button:
            background_color: (255, 255, 255, 1)
            id: dos
            on_press: root.do_action("dos", root.modePlay)

''')

class MainApp(App):

    def build(self):
        return begin

if __name__ == '__main__':
    MainApp().run()
