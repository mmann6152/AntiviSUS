import tkinter as tk

from AI_HelperFunc import *

class AntiVisus(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.frames = {}
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
  
        #container.grid_rowconfigure(0, weight = 1)
        #container.grid_columnconfigure(0, weight = 1)
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(StartPage)


        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        '''
        # label of frame Layout 2
        label = tk.Label(self, text ="Startpage")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = tk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        '''
        tk.Frame.__init__(self, parent)
        #root=tk.Tk()
        #root.geometry("200x200")
        self.bg = tk.PhotoImage(file = "Images//MainShip.png")
        self.label1 = tk.Label( self, image = self.bg)
        self.label1.grid(row=0, column=0, rowspan=5, columnspan=5)

        


        button1 = tk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        
        
        #frame1 = Frame(self.master)
        
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.DetectImposter
        #self.hi_there.pack(pady=20)
        
        self.quiter = tk.Button(self, text="QUIT", fg="red",
                              command=controller.destroy)
        self.quiter.grid(row = 3, column = 1, padx = 10, pady = 10)

    def DetectImposter(self):
        print("hi there, everyone!")
    


#Remove Sus Applications
class Page1(tk.Frame):
     
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
        
