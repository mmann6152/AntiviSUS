import tkinter as tk
from PIL import Image, ImageTk

from AI_HelperFunc import *

#Initializes all frames and shows start page
class AntiVisus(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes('-fullscreen', True)
        self.frames = {}
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
  
        for F in (StartPage, QuickScan, Page2):
  
            frame = F(container, self)
  
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(StartPage)


        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


#Page that is seen on start up        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = Image.open("Images//MainShip.png")

        
        height = self.winfo_screenheight()
        width = self.winfo_screenwidth()

        # Resize the image using resize() method
        resize_image = image.resize((width, height))
        self.bg = ImageTk.PhotoImage(resize_image)

        self.label1 = tk.Label( self, image = self.bg)
        self.label1.grid(row=0, column=0, rowspan=100, columnspan=100)

        


        button1 = tk.Button(self, text ="QuickScan",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.DetectImposter
        
        self.quiter = tk.Button(self, text="QUIT", fg="red",
                              command=controller.destroy)
        self.quiter.grid(row = 3, column = 1, padx = 10, pady = 10)

    def DetectImposter(self):
        print("hi there, everyone!")
    


#Do a scan for sus files or programs
class QuickScan(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text ="Page 1")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = tk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        


#Scan for Imposters
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text ="Page 2")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = tk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
