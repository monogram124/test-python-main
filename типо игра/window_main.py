from customtkinter import *
from window_game import WindowGame
from window_settings import Settings
from PIL import Image

class Main:
    def __init__(self) -> None:
        # настройка окна
        self.window = CTk()
        self.window.geometry('300x200')
        self.window.title("Главное меню")
        self.window._set_appearance_mode('dark')
        self.window.resizable(width=False, height=False)
        
        # импортирование картинок
        self.start_img = CTkImage(Image.open('./типо игра/img/start.png'))
        self.settings_img = CTkImage(Image.open('./типо игра/img/gear.png'))
        self.close_img = CTkImage(Image.open('./типо игра/img/close_.jpg'), size=(20, 25))
        
        
        # создание кнопок
        self.start = CTkButton(self.window, text="Начать",image=self.start_img,command=self.start_game, font=CTkFont(family='Benzin-bold', size=20), text_color='black', fg_color='white', hover=False, bg_color='transparent') 
        self.settings = CTkButton(self.window, text="Настройки", image=self.settings_img ,command=self.settings, font=CTkFont(family='Benzin-bold', size=20), text_color='black', fg_color='white', hover=False)
        self.close = CTkButton(self.window, text="Закрыть", image=self.close_img,command=self.close, font=CTkFont(family='Benzin-Bold', size=20), text_color='black', fg_color='white', hover=False) 
        self.count_window_game = 0
        self.count_window_settings = 0
            
    # я создаю здесь, ну и типо я не могу к ним обратиться из-за того, что после они удаляются
    def start_game(self):
        if self.count_window_game >= 1:
            return
        self.count_window_game += 1
        self.windowgame = WindowGame()
        self.windowgame.run()


    def settings(self):
        if self.count_window_settings >= 1:
            return
        self.count_window_settings += 1
        self.windowsettings = Settings()
        self.windowsettings.run()
        
            
        
    def close(self):
        try:
            self.windowgame.destroy()
            self.count_win_game -= 1
        except:
            pass
        try:
            self.windowsettings.destroy()
            self.count_win_settings -= 1
        except:
            pass
        self.window.destroy()
        
    
    
    def run(self):
        self.start.place(x=63, y=38)
        self.settings.place(x=60, y= 86)
        self.close.place(x=61, y=134)
        self.window.mainloop()
        
if __name__ == '__main__':
    start = Main()
    start.run()
    