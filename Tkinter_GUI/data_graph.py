import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import tkinter as tk
from PIL import ImageTk, Image



LARGE_FONT = ("Helvetica", 13, "bold italic")
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

def animate():
    print("data_graph file is open")
    pullData = open("DATA_GRAPH.txt", "r").read()
    dataList = pullData.split("\n")
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(",")
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)
    a.set_xlabel("temps (s)", size=8)
    a.set_ylabel("% batterie", size=8)

class PageThree(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("600x400+90+60")
        self.resizable(False, False)
        self.attributes("-fullscreen", True)
        self.configure(bg="white")
        
        self.label = tk.Label(self, text="Évolution Batterie", font=LARGE_FONT)
        self.label.pack(pady=15, padx=10)
        
        self.close_button = tk.Button(self, text="x", command = self.destroy)
        self.close_button.config(width=1, height=1, activebackground="red")
        self.close_button.place(x=540, y=15)
        
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

ani = animation.FuncAnimation(f, animate, interval=1000)