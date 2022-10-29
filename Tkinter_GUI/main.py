import data_graph
from data_graph import PageThree
import tkinter as tk
from tkinter import ttk
import time
from time import strftime
from PIL import ImageTk, Image
import smbus
from gpiozero import PWMLED
import RPi.GPIO as GPIO
import runFILE
import DATA
import data_login
import threading
from threading import Timer
import sys
import mysql.connector



class LoginClass(tk.Tk):
    def __init__(self):
        super().__init__()

        self.obj_font = WonderfulFont()

        self.geometry("800x500+0+0")
        self.resizable(False, False)
        self.attributes("-fullscreen", True)

        self.frame_a = tk.Frame(self, height=500, width=800, bg=self.obj_font.color_6)
        self.frame_a.place(x=0, y=0)
        self.frame_b = tk.Frame(self, height=500, width=220, bg=self.obj_font.color_9)
        self.frame_b.place(x=600, y=0)
        self.frame_c = tk.Frame(self, height=70, width=800, bg=self.obj_font.color_10)
        self.frame_c.place(x=0, y=0)
        self.frame_d = tk.Frame(self, height=120, width=400, bg=self.obj_font.color_10)
        self.frame_d.place(x=130, y=130)
        self.frame_e = tk.Frame(self, height=120, width=400, bg=self.obj_font.color_10)
        self.frame_e.place(x=130, y=280)

        self.close_button = tk.Button(self, text=" X ", command=self.destroy)
        self.close_button.place(x=745, y=10)
        self.close_button.config(font=self.obj_font.font_2, fg=self.obj_font.color_2, bg=self.obj_font.color_9,
                                 width=2, height=1, activebackground=self.obj_font.color_10, bd=0)

        self.header = tk.Label(self, text="Page de connexion")
        self.header.place(x=150, y=20)
        self.header.config(font=self.obj_font.font_1, bg=self.obj_font.color_10, fg=self.obj_font.color_2)

        self.canvas_header = tk.Canvas(self, width=210, height=10, bg=self.obj_font.color_10, highlightthickness=0)
        self.canvas_header.create_line(0, 5, 210, 5, fill=self.obj_font.color_2, width=2)
        self.canvas_header.place(x=150, y=45)

        self.canvas_down = tk.Canvas(self, width=800, height=40, bg=self.obj_font.color_10, highlightthickness=0)
        self.canvas_down.place(x=0, y=460)

        self.canvas_up = tk.Canvas(self, width=800, height=10, bg=self.obj_font.color_9, highlightthickness=0)
        self.canvas_up.place(x=0, y=65)

        self.login_lab = tk.Label(self, text=" Identifiant : ")
        self.login_lab.place(x=150, y=150)
        self.login_lab.config(font=self.obj_font.font_2, bg=self.obj_font.color_9, fg=self.obj_font.color_2)

        self.password_lab = tk.Label(self, text=" Mot de passe : ")
        self.password_lab.place(x=150, y=300)
        self.password_lab.config(font=self.obj_font.font_2, bg=self.obj_font.color_9, fg=self.obj_font.color_2)

        self.canvas_logo = tk.Canvas(self, width=178, height=168, bg=self.obj_font.color_9, highlightthickness=2,
                                     highlightbackground=self.obj_font.color_4)
        self.canvas_logo.place(x=610, y=100)
        self.open_logo = (Image.open("logo_2.jpg"))
        self.resize_logo = self.open_logo.resize((180, 170), Image.ANTIALIAS)
        self.new_logo = ImageTk.PhotoImage(self.resize_logo)
        self.canvas_logo.create_image(0, 0, anchor=tk.NW, image=self.new_logo)

        self.canvas_login = tk.Canvas(self, width=70, height=70, bg=self.obj_font.color_6, highlightthickness=0)
        self.canvas_login.place(x=40, y=120)
        self.open_login = (Image.open("login.png"))
        self.resize_login = self.open_login.resize((70, 70), Image.ANTIALIAS)
        self.new_login = ImageTk.PhotoImage(self.resize_login)
        self.canvas_login.create_image(0, 0, anchor=tk.NW, image=self.new_login)

        self.canvas_password = tk.Canvas(self, width=70, height=70, bg=self.obj_font.color_6, highlightthickness=0)
        self.canvas_password.place(x=40, y=270)
        self.open_password = (Image.open("password.png"))
        self.resize_password = self.open_password.resize((70, 70), Image.ANTIALIAS)
        self.new_password = ImageTk.PhotoImage(self.resize_password)
        self.canvas_password.create_image(0, 0, anchor=tk.NW, image=self.new_password)

        self.clock = tk.Label(self)
        self.clock.place(x=670, y=280)
        self.clock.config(font=self.obj_font.font_3, fg=self.obj_font.color_2, bg=self.obj_font.color_9)

        self.clock_lab = tk.Label(self, text="Temps :")
        self.clock_lab.place(x=615, y=280)
        self.clock_lab.config(font=self.obj_font.font_3, bg=self.obj_font.color_9, fg=self.obj_font.color_2)

        self.copyright = tk.Label(self, text="| © 2022, Fonroche Company |")
        self.copyright.place(x=620,y=475)
        self.copyright.config(font=self.obj_font.font_3, bg=self.obj_font.color_10, fg=self.obj_font.color_2)

        self.entry_login = tk.Entry(self)
        self.entry_login.place(x=150, y=200)
        self.entry_login.config(highlightthickness=2, highlightcolor=self.obj_font.color_4)

        self.entry_password = tk.Entry(self)
        self.entry_password.place(x=150, y=350)
        self.entry_password.config(highlightthickness=2, highlightcolor=self.obj_font.color_4)

        self.button_login = tk.Button(self, text=" S'identifier ")
        self.button_login.place(x=150, y=415)
        self.button_login.config(font=self.obj_font.font_4, bg=self.obj_font.color_4, fg=self.obj_font.color_2,
                                 activebackground=self.obj_font.color_9, bd=1, command=self.logpass)

        self.time()

    def logpass(self):
        self.username = self.entry_login.get()
        self.password = self.entry_password.get()
        
        mydb = mysql.connector.connect(**data_login.config)
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("select * from login_table where identifiant = '"+self.username+"' and mot_de_passe = '"+self.password+"';")
        myresult = mycursor.fetchone()


        if (self.username == "" and self.password == ""):
            self.win_warn()

        elif myresult == None:
            self.win_error()

        else:
            self.win_info()    
    
    def time(self):
        self.current_time = strftime("%H:%M:%S")
        self.clock.config(text=self.current_time)
        self.clock.after(1000, self.time)

    def win_warn(self):
        self.warning = tk.Toplevel()
        self.warning.geometry("300x250+150+140")
        self.warning.resizable(False, False)
        self.warning.overrideredirect(True)

        self.frame_warn_0 = tk.Frame(self.warning, height=250, width=300, bg=self.obj_font.color_6)
        self.frame_warn_0.place(x=0, y=0)
        self.frame_warn_a = tk.Frame(self.warning, height=30, width=300, bg=self.obj_font.color_11)
        self.frame_warn_a.place(x=0, y=0)
        self.frame_warn_b = tk.Frame(self.warning, height=20, width=300, bg=self.obj_font.color_12)
        self.frame_warn_b.place(x=0, y=30)
        self.frame_warn_c = tk.Frame(self.warning, height=30, width=300, bg=self.obj_font.color_11)
        self.frame_warn_c.place(x=0, y=220)
        self.frame_warn_d = tk.Frame(self.warning, height=20, width=300, bg=self.obj_font.color_12)
        self.frame_warn_d.place(x=0, y=200)

        self.close_button_warning = tk.Button(self.warning, text=" X ", command=self.warning.destroy)
        self.close_button_warning.place(x=250, y=15)
        self.close_button_warning.config(font=self.obj_font.font_2, bg=self.obj_font.color_13, fg=self.obj_font.color_1,
                                         width=2, height=1, activebackground=self.obj_font.color_10, bd=0)

        self.lab_warn = tk.Label(self.warning, text=" warning page ")
        self.lab_warn.pack(pady=15)
        self.lab_warn.config(font=self.obj_font.font_2, bg=self.obj_font.color_2, fg=self.obj_font.color_1)

        self.canvas_warn = tk.Canvas(self.warning, width=110, height=110, bg=self.obj_font.color_6,
                                     highlightthickness=0,)
        self.canvas_warn.place(x=20, y=60)
        self.open_warn = (Image.open("warning.png"))
        self.resize_warn = self.open_warn.resize((110,110), Image.ANTIALIAS)
        self.new_warn = ImageTk.PhotoImage(self.resize_warn)
        self.canvas_warn.create_image(0, 0, anchor=tk.NW, image=self.new_warn)

        self.warn_txt = tk.Label(self.warning, text="Aucune donnée\nrentrée !")
        self.warn_txt.place(x=140, y=80)
        self.warn_txt.config(font=self.obj_font.font_4, bg=self.obj_font.color_6, fg=self.obj_font.color_1)

        self.ok_choice_warn = tk.Button(self.warning, text="OK", command=lambda: self.select_warn("OK"))
        self.ok_choice_warn.place(x=140, y=210)
        self.ok_choice_warn.config(font=self.obj_font.font_2, bg=self.obj_font.color_13, fg=self.obj_font.color_2,
                                   width=2, height=1, activebackground=self.obj_font.color_10)

    def select_warn(self, choice):
        if choice == "OK":
            self.warning.destroy()

    def win_error(self):
        self.error = tk.Toplevel()
        self.error.geometry("300x250+150+140")
        self.error.resizable(False, False)
        self.error.overrideredirect(True)

        self.frame_error_0 = tk.Frame(self.error, height=250, width=300, bg=self.obj_font.color_6)
        self.frame_error_0.place(x=0, y=0)
        self.frame_error_a = tk.Frame(self.error, height=30, width=300, bg=self.obj_font.color_13)
        self.frame_error_a.place(x=0, y=0)
        self.frame_error_b = tk.Frame(self.error, height=20, width=300, bg=self.obj_font.color_14)
        self.frame_error_b.place(x=0, y=30)
        self.frame_error_c = tk.Frame(self.error, height=30, width=300, bg=self.obj_font.color_13)
        self.frame_error_c.place(x=0, y=220)
        self.frame_error_d = tk.Frame(self.error, height=20, width=300, bg=self.obj_font.color_14)
        self.frame_error_d.place(x=0, y=200)

        self.close_button_error = tk.Button(self.error, text=" X ", command=self.error.destroy)
        self.close_button_error.place(x=250, y=15)
        self.close_button_error.config(font=self.obj_font.font_2, bg=self.obj_font.color_13, fg=self.obj_font.color_1,
                                         width=2, height=1, activebackground=self.obj_font.color_10, bd=0)

        self.lab_error = tk.Label(self.error, text=" error page ")
        self.lab_error.pack(pady=15)
        self.lab_error.config(font=self.obj_font.font_2, bg=self.obj_font.color_2, fg=self.obj_font.color_1)

        self.canvas_error = tk.Canvas(self.error, width=110, height=110, bg=self.obj_font.color_6,
                                     highlightthickness=0,)
        self.canvas_error.place(x=20, y=70)
        self.open_error = (Image.open("error.png"))
        self.resize_error = self.open_error.resize((110,110), Image.ANTIALIAS)
        self.new_error = ImageTk.PhotoImage(self.resize_error)
        self.canvas_error.create_image(0, 0, anchor=tk.NW, image=self.new_error)

        self.error_txt = tk.Label(self.error, text="Les données ne sont\npas bonnes !")
        self.error_txt.place(x=140, y=80)
        self.error_txt.config(font=self.obj_font.font_4, bg=self.obj_font.color_6, fg=self.obj_font.color_1)

        self.ok_choice_error = tk.Button(self.error, text="OK", command=lambda: self.select_error("OK"))
        self.ok_choice_error.place(x=140, y=210)
        self.ok_choice_error.config(font=self.obj_font.font_2, bg=self.obj_font.color_13, fg=self.obj_font.color_2,
                                   width=2, height=1, activebackground=self.obj_font.color_10)

    def select_error(self, choice):
        if choice == "OK":
            self.error.destroy()

    def win_info(self):
        self.info = tk.Toplevel()
        self.info.geometry("300x250+150+140")
        self.info.resizable(False, False)
        self.info.overrideredirect(True)

        self.frame_info_0 = tk.Frame(self.info, height=250, width=300, bg=self.obj_font.color_6)
        self.frame_info_0.place(x=0, y=0)
        self.frame_info_a = tk.Frame(self.info, height=30, width=300, bg=self.obj_font.color_15)
        self.frame_info_a.place(x=0, y=0)
        self.frame_info_b = tk.Frame(self.info, height=20, width=300, bg=self.obj_font.color_16)
        self.frame_info_b.place(x=0, y=30)
        self.frame_info_c = tk.Frame(self.info, height=30, width=300, bg=self.obj_font.color_15)
        self.frame_info_c.place(x=0, y=220)
        self.frame_info_d = tk.Frame(self.info, height=20, width=300, bg=self.obj_font.color_16)
        self.frame_info_d.place(x=0, y=200)

        self.close_button_info = tk.Button(self.info, text=" X ", command=self.info.destroy)
        self.close_button_info.place(x=250, y=15)
        self.close_button_info.config(font=self.obj_font.font_2, bg=self.obj_font.color_13, fg=self.obj_font.color_1,
                                         width=2, height=1, activebackground=self.obj_font.color_10, bd=0)

        self.lab_info = tk.Label(self.info, text=" info page ")
        self.lab_info.pack(pady=15)
        self.lab_info.config(font=self.obj_font.font_2, bg=self.obj_font.color_2, fg=self.obj_font.color_1)

        self.canvas_info = tk.Canvas(self.info, width=110, height=110, bg=self.obj_font.color_6,
                                     highlightthickness=0,)
        self.canvas_info.place(x=20, y=70)
        self.open_info = (Image.open("info.png"))
        self.resize_info = self.open_info.resize((110,110), Image.ANTIALIAS)
        self.new_info = ImageTk.PhotoImage(self.resize_info)
        self.canvas_info.create_image(0, 0, anchor=tk.NW, image=self.new_info)

        self.info_txt = tk.Label(self.info, text="Donnée correct")
        self.info_txt.place(x=140, y=80)
        self.info_txt.config(font=self.obj_font.font_4, bg=self.obj_font.color_6, fg=self.obj_font.color_1)

        self.ok_choice_info = tk.Button(self.info, text="OK", command=lambda: self.select_info("OK"))
        self.ok_choice_info.place(x=140, y=210)
        self.ok_choice_info.config(font=self.obj_font.font_2, bg=self.obj_font.color_13, fg=self.obj_font.color_2,
                                   width=2, height=1, activebackground=self.obj_font.color_10)

    def select_info(self, choice):
        if choice == "OK":
            self.info.destroy()
            self.obj_mywin = MyWindow(self)




class MyWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.obj_font = WonderfulFont()

        self.geometry("800x500+0+0")
        self.resizable(False, False)
        self.attributes("-fullscreen", True)

        self.frame_a = tk.Frame(self, height=400, width=300, bg=self.obj_font.color_4)
        self.frame_a.place(x=0, y=0)
        self.frame_b = tk.Frame(self, height=50, width=650, bg=self.obj_font.color_3)
        self.frame_b.place(x=300, y=0)
        self.frame_c = tk.Frame(self, height=25, width=50, bg=self.obj_font.color_2)
        self.frame_c.place(x=175, y=125)
        self.frame_d = tk.Frame(self, height=25, width=50, bg=self.obj_font.color_2)
        self.frame_d.place(x=175, y=200)
        self.frame_e = tk.Frame(self, height=25, width=50, bg=self.obj_font.color_2)
        self.frame_e.place(x=175, y=275)
        self.frame_f = tk.Frame(self, height=25, width=30, bg=self.obj_font.color_2)
        self.frame_f.place(x=230, y=200)
        self.frame_g = tk.Frame(self, height=25, width=30, bg=self.obj_font.color_2)
        self.frame_g.place(x=230, y=125)
        self.frame_h = tk.Frame(self, height=350, width=500, bg=self.obj_font.color_6)
        self.frame_h.place(x=300, y=50)
        self.frame_i = tk.Frame(self, height=100, width=800, bg=self.obj_font.color_3)
        self.frame_i.place(x=0, y=400)

        self.header = tk.Label(self, text="Informations Luminaire")
        self.header.place(x=425, y=10)
        self.header.config(font=self.obj_font.font_1, fg=self.obj_font.color_2, bg=self.obj_font.color_3)

        self.canvas_line_header = tk.Canvas(self, width=500, height=15, bg=self.obj_font.color_3, highlightthickness=0)
        self.canvas_line_header.create_line(100, 6, 415, 6, fill=self.obj_font.color_2, width=2)
        self.canvas_line_header.place(x=300, y=35)

        self.canvas_line_bar = tk.Canvas(self, width=80, height=10, bg=self.obj_font.color_6, highlightthickness=0)
        self.canvas_line_bar.create_line(0, 5, 75, 5, fill=self.obj_font.color_1, width=1)
        self.canvas_line_bar.place(x=355, y=120)

        self.canvas_line_slider = tk.Canvas(self, width=60, height=10, bg=self.obj_font.color_6, highlightthickness=0)
        self.canvas_line_slider.create_line(0, 5, 55, 5, fill=self.obj_font.color_1, width=1)
        self.canvas_line_slider.place(x=640, y=120)
        
        self.canvas_logo = tk.Canvas(self, width=260, height=85, bg=self.obj_font.color_4, highlightthickness=0)
        self.canvas_logo.place(x=15, y=15)
        self.image_logo = ImageTk.PhotoImage(Image.open("logo.jpg"))
        self.canvas_logo.create_image(0, 0, anchor=tk.NW, image=self.image_logo)

        self.current = tk.Label(self, text="Courant LED : ")
        self.current.place(x=20, y=125)
        self.current.config(font=self.obj_font.font_2, fg=self.obj_font.color_2, bg=self.obj_font.color_4)

        self.tension = tk.Label(self, text="Tension BAT : ")
        self.tension.place(x=20, y=200)
        self.tension.config(font=self.obj_font.font_2, fg=self.obj_font.color_2, bg=self.obj_font.color_4)

        self.status = tk.Label(self, text="Etat LED : ")
        self.status.place(x=20, y=275)
        self.status.config(font=self.obj_font.font_2, fg=self.obj_font.color_2, bg=self.obj_font.color_4)

        self.unit_tension = tk.Label(self, text="V")
        self.unit_tension.place(x=237, y=204)
        self.unit_tension.config(font=self.obj_font.font_2, fg=self.obj_font.color_4, bg=self.obj_font.color_2)
        self.unit_current = tk.Label(self, text="mA")
        self.unit_current.place(x=234, y=129)
        self.unit_current.config(font=self.obj_font.font_2, fg=self.obj_font.color_4, bg=self.obj_font.color_2)

        self.slider_lab = tk.Label(self, text="O/F : ")
        self.slider_lab.place(x=640, y=100)
        self.slider_lab.config(font=self.obj_font.font_2, fg=self.obj_font.color_1, bg=self.obj_font.color_6)
        self.slider = tk.Scale(self, from_=0, to=1, orient=tk.VERTICAL, tickinterval=0.5, resolution=0.01, length=260,
                               highlightthickness=0, showvalue=0, background=self.obj_font.color_2, troughcolor=self.obj_font.color_5,
                               activebackground=self.obj_font.color_4, sliderlength=20, command=self.ChangeValueLED)
        self.slider.place(x=720, y=100)

        self.bar_lab = tk.Label(self, text="% BAT : ")
        self.bar_lab.place(x=355, y=100)
        self.bar_lab.config(font=self.obj_font.font_2, fg=self.obj_font.color_1, bg=self.obj_font.color_6)
        
        self.bar_unit_0 = tk.Label(self, text="-0")
        self.bar_unit_0.place(x=470, y=345)
        self.bar_unit_0.config(font=self.obj_font.font_3, fg=self.obj_font.color_1, bg=self.obj_font.color_6)
        
        self.bar_unit_50 = tk.Label(self, text="-50")
        self.bar_unit_50.place(x=470, y=225)
        self.bar_unit_50.config(font=self.obj_font.font_3, fg=self.obj_font.color_1, bg=self.obj_font.color_6)
        
        self.bar_unit_100 = tk.Label(self, text="-100")
        self.bar_unit_100.place(x=470, y=100)
        self.bar_unit_100.config(font=self.obj_font.font_3, fg=self.obj_font.color_1, bg=self.obj_font.color_6)
        
        self.bar_style = ttk.Style()
        self.bar_style.theme_use("clam")
        self.bar_style.configure("bar.Horizontal.TProgressbar", troughcolor=self.obj_font.color_5, bordercolor=self.obj_font.color_2,
                                 background=self.obj_font.color_4, lightcolor=self.obj_font.color_4, darkcolor=self.obj_font.color_4)
        self.bar = ttk.Progressbar(self, style="bar.Horizontal.TProgressbar", orient=tk.VERTICAL, length=260,
                                   mode="determinate", maximum=100, value=50)
        self.bar.place(x=455, y=100)

        self.close_button = tk.Button(self, text=" X ", command=self.Button_Close)
        self.close_button.place(x=745, y=10)
        self.close_button.config(font=self.obj_font.font_2, fg=self.obj_font.color_2, bg=self.obj_font.color_4, width=2, height=1,
                                 activebackground=self.obj_font.color_2, bd=0)

        self.canvas_bat = tk.Canvas(self, width=60, height=60, bg=self.obj_font.color_6, highlightthickness=0)
        self.canvas_bat.place(x=380, y=155)
        self.open_image_bat = (Image.open("bat_green.png"))
        self.resize_bat = self.open_image_bat.resize((55, 55), Image.ANTIALIAS)
        self.new_image_bat = ImageTk.PhotoImage(self.resize_bat)
        self.canvas_bat.create_image(0, 0, anchor=tk.NW, image=self.new_image_bat)

        self.canvas_sli = tk.Canvas(self, width=60, height=60, bg=self.obj_font.color_6, highlightthickness=0)
        self.canvas_sli.place(x=640, y=155)
        self.open_image_sli = (Image.open("bulb_on.png"))
        self.resize_sli = self.open_image_sli.resize((55, 55), Image.ANTIALIAS)
        self.new_image_sli = ImageTk.PhotoImage(self.resize_sli)
        self.canvas_sli.create_image(0, 0, anchor=tk.NW, image=self.new_image_sli)

        self.clock_lab = tk.Label(self, text="Temps Actuel : ")
        self.clock_lab.place(x=20, y=330)
        self.clock_lab.config(font=self.obj_font.font_3, fg=self.obj_font.color_2, bg=self.obj_font.color_4)

        self.clock = tk.Label(self)
        self.clock.place(x=110, y=330)
        self.clock.config(font=self.obj_font.font_3, fg=self.obj_font.color_2, bg=self.obj_font.color_4)

        self.clock_static_lab = tk.Label(self, text="Dernière Ouverture : ")
        self.clock_static_lab.place(x=20, y=350)
        self.clock_static_lab.config(font=self.obj_font.font_3, fg=self.obj_font.color_2, bg=self.obj_font.color_4)
        self.current_time_static = strftime("%H:%M:%S")

        self.clock_static = tk.Label(self)
        self.clock_static.place(x=150, y=350)
        self.clock_static.config(text=self.current_time_static, font=self.obj_font.font_3, fg=self.obj_font.color_2, bg=self.obj_font.color_4)

        self.copyright = tk.Label(self, text="| © 2022, Fonroche Company |")
        self.copyright.place(x=625, y=480)
        self.copyright.config(font=self.obj_font.font_3, fg=self.obj_font.color_2, bg=self.obj_font.color_3)

        self.tension_lab = tk.Label(self)
        self.tension_lab.place(x=180, y=205)
        self.tension_lab.config(font=self.obj_font.font_4, fg=self.obj_font.color_1, bg=self.obj_font.color_2)

        self.current_lab = tk.Label(self)
        self.current_lab.place(x=180, y=130)
        self.current_lab.config(font=self.obj_font.font_4, fg=self.obj_font.color_1, bg=self.obj_font.color_2)

        self.graph_button = tk.Button(self, text="Évolution Batterie", fg=self.obj_font.color_1, bg=self.obj_font.color_7,
                                      activebackground=self.obj_font.color_4, bd=0, font=self.obj_font.font_2,
                                      command=self.Button_Clicked)
        self.graph_button.place(x=40, y=430)
        
        self.value_sli = tk.Label(self)
        self.value_sli.place(x=655, y=220)
        self.value_sli.config(font=self.obj_font.font_4, fg=self.obj_font.color_1, bg=self.obj_font.color_2)
        
        self.status_lab = tk.Label(self)
        self.status_lab.place(x=180, y=280)
        self.status_lab.config(font=self.obj_font.font_4, fg=self.obj_font.color_1, bg=self.obj_font.color_2)
        
        self.bar_update = tk.Label(self)
        self.bar_update.place(x=400, y=220)
        self.bar_update.config(font=self.obj_font.font_4, bg=self.obj_font.color_2, fg=self.obj_font.color_1)

        self.canvas_sli = tk.Canvas(self, width=60, height=60, bg=self.obj_font.color_6, highlightthickness=0)
        self.canvas_sli.place(x=640, y=155)
        
        self.canvas_bat = tk.Canvas(self, width=60, height=60, bg=self.obj_font.color_6, highlightthickness=0)
        self.canvas_bat.place(x=380, y=155)
        
        self.thread_graph = Timer(5.0, self.Write_Graph_Data)
        self.thread_graph.start()
        
        self.thread_data_bdd = Timer(5.0, self.Update_Data)
        self.thread_data_bdd.start()
        
        self.thread_mail = Timer(10.0, self.SEND_MAIL_PROBLEM)
        self.thread_mail.start()

        self.bus = smbus.SMBus(1)
        self.address = 0x48
        self.blue_led = PWMLED(18)
        self.file_graph = open("DATA_GRAPH.txt", "w")
        
        self.read_AIN0()
        self.read_AIN1()
        self.Value_Bat()
        self.Status()
        self.Image_Bulb()
        self.Image_Bar()
        self.time()
    
    def Write_Graph_Data(self):
        n = 0
        while 1:
            n += 1
            print("In Graph X = ", n, " AND Y = ", self.charge_integer)
            self.file_graph.write(str(n) + "," + str(self.charge_integer) + "\n")
            self.file_graph.flush()
            time.sleep(1)

    def Update_Data(self):
        while 1:
            DATA.BigData()
            print("data send to bdd")
   
    def win_dead_bat(self):
        self.dead_bat = tk.Toplevel()
        self.dead_bat.geometry("400x250+150+140")
        self.dead_bat.resizable(False, False)
        self.dead_bat.overrideredirect(True)

        self.frame_dead_bat_0 = tk.Frame(self.dead_bat, height=250, width=400, bg=self.obj_font.color_19)
        self.frame_dead_bat_0.place(x=0, y=0)
        self.frame_dead_bat_a = tk.Frame(self.dead_bat, height=30, width=400, bg=self.obj_font.color_17)
        self.frame_dead_bat_a.place(x=0, y=0)
        self.frame_dead_bat_b = tk.Frame(self.dead_bat, height=20, width=400, bg=self.obj_font.color_18)
        self.frame_dead_bat_b.place(x=0, y=30)
        self.frame_dead_bat_c = tk.Frame(self.dead_bat, height=30, width=400, bg=self.obj_font.color_17)
        self.frame_dead_bat_c.place(x=0, y=220)
        self.frame_dead_bat_d = tk.Frame(self.dead_bat, height=20, width=400, bg=self.obj_font.color_18)
        self.frame_dead_bat_d.place(x=0, y=200)

        self.close_button_dead_bat = tk.Button(self.dead_bat, text=" X ", command=self.dead_bat.destroy)
        self.close_button_dead_bat.place(x=300, y=15)
        self.close_button_dead_bat.config(font=self.obj_font.font_2, bg=self.obj_font.color_13, fg=self.obj_font.color_1,
                                         width=2, height=1, activebackground=self.obj_font.color_10, bd=0)

        self.lab_dead_bat = tk.Label(self.dead_bat, text=" dead battery ")
        self.lab_dead_bat.pack(pady=15)
        self.lab_dead_bat.config(font=self.obj_font.font_2, bg=self.obj_font.color_2, fg=self.obj_font.color_1)

        self.canvas_dead_bat = tk.Canvas(self.dead_bat, width=110, height=110, bg=self.obj_font.color_19,
                                     highlightthickness=0,)
        self.canvas_dead_bat.place(x=20, y=70)
        self.open_dead_bat = (Image.open("skull.png"))
        self.resize_dead_bat = self.open_dead_bat.resize((110,110), Image.ANTIALIAS)
        self.new_dead_bat = ImageTk.PhotoImage(self.resize_dead_bat)
        self.canvas_dead_bat.create_image(0, 0, anchor=tk.NW, image=self.new_dead_bat)

        self.dead_bat_txt = tk.Label(self.dead_bat, text="La batterie n'a presque\nplus de batterie\n\nUn mail va être envoyé au staff !")
        self.dead_bat_txt.place(x=140, y=80)
        self.dead_bat_txt.config(font=self.obj_font.font_4, bg=self.obj_font.color_19, fg=self.obj_font.color_1)

        self.ok_choice_dead_bat = tk.Button(self.dead_bat, text="OK", command=lambda: self.select_dead_bat("OK"))
        self.ok_choice_dead_bat.place(x=160, y=210)
        self.ok_choice_dead_bat.config(font=self.obj_font.font_2, bg=self.obj_font.color_13, fg=self.obj_font.color_2,
                                   width=2, height=1, activebackground=self.obj_font.color_10)

    def select_dead_bat(self, choice):
        if choice == "OK":
            self.dead_bat.destroy()
        
    def SEND_MAIL_PROBLEM(self):
        self.current_time_full = strftime("%d/%m/%Y, %H:%M:%S")
        
        while 1:
            print("Scan Status Battery")
            time.sleep(20)
            if 0 <= self.charge_integer <=10:
                self.win_dead_bat()
                
                self.file_log = open("log.txt", "w")
                self.file_log.write(self.current_time_full)
                self.file_log.write("  Batterie =  ")
                self.file_log.write(str(self.charge_integer))
                self.file_log.write(" %")
                self.file_log.close()
                
                runFILE.mail_sent()
                print("MAIL SENT TO SUPPORT")
     
    def Image_Bar(self):
        if 0 <= self.charge_integer <= 30:

            self.open_image_bat = (Image.open("bat_red.png"))
            self.resize_bat = self.open_image_bat.resize((55, 55), Image.ANTIALIAS)
            self.new_image_bat = ImageTk.PhotoImage(self.resize_bat)
            self.canvas_bat.create_image(0, 0, anchor=tk.NW, image=self.new_image_bat)
            
        elif 30 <= self.charge_integer <= 60:

            self.open_image_bat = (Image.open("bat_orange.png"))
            self.resize_bat = self.open_image_bat.resize((55, 55), Image.ANTIALIAS)
            self.new_image_bat = ImageTk.PhotoImage(self.resize_bat)
            self.canvas_bat.create_image(0, 0, anchor=tk.NW, image=self.new_image_bat)
            
        elif 60 <= self.charge_integer <= 100:
            
            self.open_image_bat = (Image.open("bat_green.png"))
            self.resize_bat = self.open_image_bat.resize((55, 55), Image.ANTIALIAS)
            self.new_image_bat = ImageTk.PhotoImage(self.resize_bat)
            self.canvas_bat.create_image(0, 0, anchor=tk.NW, image=self.new_image_bat)
        else:
            
            self.open_image_bat = (Image.open("bat_default.png"))
            self.resize_bat = self.open_image_bat.resize((55, 55), Image.ANTIALIAS)
            self.new_image_bat = ImageTk.PhotoImage(self.resize_bat)
            self.canvas_bat.create_image(0, 0, anchor=tk.NW, image=self.new_image_bat)
        
        self.bar.config(value=self.charge_integer)
        self.bar.after(500, self.Image_Bar)
        
    def Value_Bat(self):
        """
        self.difference_now = self.read_0 - 12
        self.difference_range = 15 - 12
        self.charge = (self.difference_now / self.difference_range)*100
        print(self.charge)
        """
        print("Tension pour calcul BAT = ", self.value_tension)
        self.difference_max = 5 - 0
        self.difference_range = self.value_tension - 0
        self.charge = (self.difference_range / self.difference_max)*100
        self.charge_integer = int(self.charge)
        print("Value BAT in % = ", self.charge_integer)
        
        self.bar_update.config(text=self.charge_integer)
        self.bar_update.after(300, self.Value_Bat)
  
    def Image_Bulb(self):
        if self.blue_led.value == 0.00:

            self.open_image_sli = (Image.open("bulb_off.png"))
            self.resize_sli = self.open_image_sli.resize((55, 55), Image.ANTIALIAS)
            self.new_image_sli = ImageTk.PhotoImage(self.resize_sli)
            self.canvas_sli.create_image(0, 0, anchor=tk.NW, image=self.new_image_sli)
            
        elif self.blue_led.value >= 0.01:

            self.open_image_sli = (Image.open("bulb_on.png"))
            self.resize_sli = self.open_image_sli.resize((55, 55), Image.ANTIALIAS)
            self.new_image_sli = ImageTk.PhotoImage(self.resize_sli)
            self.canvas_sli.create_image(0, 0, anchor=tk.NW, image=self.new_image_sli)
            
        else:

            self.open_image_sli = (Image.open("bulb_default.png"))
            self.resize_sli = self.open_image_sli.resize((55, 55), Image.ANTIALIAS)
            self.new_image_sli = ImageTk.PhotoImage(self.resize_sli)
            self.canvas_sli.create_image(0, 0, anchor=tk.NW, image=self.new_image_sli)
            
        self.value_sli.config(text=self.blue_led.value)
        self.value_sli.after(500, self.Image_Bulb)
            
    def Status(self):
        if self.blue_led.value == 0.0:
            print("Label OFF")
            self.status_lab.config(text="OFF")
            
        else:
            print("Label ON")
            self.status_lab.config(text="ON")
        self.status_lab.after(300, self.Status)
        
    def Button_Close(self):
        GPIO.cleanup()
        sys.exit()
        self.destroy()

    def Button_Clicked(self):
        data_graph.animate()
        self.obj_graph = PageThree()

    def ChangeValueLED(self, value):
        self.led_value = float(value)
        print(value, self.led_value, self.blue_led)
        self.blue_led.value = self.led_value

    def read_AIN1(self):
        self.bus.write_byte(self.address, 0x40)
        self.read_0 = self.bus.read_byte(self.address)
        print("AIN0 = ", self.read_0, "\n")
        
        self.value_tension = (self.read_0 * 5) / 255
        self.tension_lab.config(text=round(self.value_tension, 2))
        print("Data on AIN0 = ", self.value_tension, "\n")
        self.tension_lab.after(300, self.read_AIN1)

    def read_AIN0(self):
        self.bus.write_byte(self.address, 0x41)
        self.read_1 = self.bus.read_byte(self.address)
        print("AIN1 = ", self.read_1, "\n")
        
        self.value_current = (self.read_1 * 20) / 255
        self.current_lab.config(text=round(self.value_current, 2))
        print("Data on AIN1 = ", self.value_current, "\n")
        self.current_lab.after(300, self.read_AIN0)

    def time(self):
        self.current_time = strftime("%H:%M:%S")
        self.clock.config(text=self.current_time)
        self.clock.after(1000, self.time)

             
        
class WonderfulFont:
    def __init__(self):

        self.font_1 = ("Courier", 15, "bold")
        self.font_2 = ("Courier", 12, "bold")
        self.font_3 = ("Courier", 8, "bold")
        self.font_4 = ("Courier", 10, "bold")

        self.color_1 = "black"
        self.color_2 = "white"
        self.color_3 = "#FFC2A1"
        self.color_4 = "#FF9A65"
        self.color_5 = "#D1D1E0"
        self.color_6 = "#F0F0F0"
        self.color_7 = "#D7D7D7"
        self.color_8 = "#4CFF70"
        self.color_9 = "#4C95FF"
        self.color_10 = "#003B90"
        self.color_11 = "#E8FF00"
        self.color_12 = "#FFEA84"
        self.color_13 = "#FF0000"
        self.color_14 = "#FF8F8F"
        self.color_15 = "#002EFF"
        self.color_16 = "#758EFF"
        self.color_17 = "#7E7E7E"
        self.color_18 = "#D0D0D0"
        self.color_19 = "#9CA4C8"



if __name__ == "__main__":
    obj_loginclass = LoginClass()
    obj_loginclass.mainloop()