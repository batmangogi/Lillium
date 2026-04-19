#graphic module!
import tkinter as tk

class Win:
    """
    window(x,y,r,g,b,name) creates a window object based on the following parameters:
    x(width);y(height);r(red);g(green);b(blue);name(window title).
    default parameters are already inserted to avoid crashes if any arent inserted
    """
    def __init__(self,x=640,y=480,r=0,g=0,b=0,name=str(__file__)):
        if x == 640 and y == 480 and r == 0 and g == 0 and b == 0 and name == str(__file__):
            print("---[!]an error as occured")
            print("---perhaps you forgot to definy >window<? for so >window< as been given its default values")
            print("---to configure >window< fill self.vision.window()<--- with the following info...")
            print("---x(window width) y(window height) r(red) g(green) b(blue) <--(for the background coulor) name(window title)")
        self.Func_List = []
        self.custom_def = None
        self.name = name
        self.root = tk.Tk()
        self.root.title(name)
        self.root.geometry(str(x)+"x"+str(y))
        color = f'#{r:02x}{g:02x}{b:02x}'
        self.canvas = tk.Canvas(self.root,width=x,height=y,bg=color)
        self.canvas.pack()
        try:
            self.ms = int(self.ms)
            self.fps
        except:
            self.fps = 30
            ms = (1/self.fps)*1000
            self.ms = int(ms)
            print("---[!]an error as occured")
            print("---perhaps you forgot to definy >fps<? for so >fps< as been automaticaly set to 30")
            print("---to definy >fps< use the function >set_fps()<!")          

    def Upd(self):
        """
        update() serve as the software pulse and MUST run only in the run() function
        instead of using a while cycle you must set a function 
        """
        if self.Func_List is not None:
            for i in range(len(self.Func_List)):
                Func_InUse = self.Func_List[i]
                Func_InUse()
        self.root.after(self.ms,self.Upd)

    def Run(self):
        """
        run() starts the software
        """
        print("running:",self.name)
        self.Upd()
        self.root.mainloop()

    def Get_Fps(self,fps):
            """
            get_fps(fps) sets an fps value
            """
            self.fps = fps
            self.ms = int((1/self.fps)*1000)

    def Get_Func(self,func):
        """
        get_function() creates a list of functions to run during update
        """
        self.func_list.append(func)
        print("added",func,"to the list")
    #TODO: move all of this code in pulse.py module :3

    def Get_RectObj(self,obj):
        """
        get_obj(obj), creates an object on the canvas based on an already existing obj_rect()
        """
        if obj is None:
            print("---[!!]an error as occured")
            print("---the inserted obj_rect() does not exist")
            print("---perhaps you made a typo? check what you wrote in Get_RectObj()")
            print("---or if you didn't, create a Obj_Rect()")
            return
        w = obj.width
        h = obj.height
        x = obj.x
        y = obj.x





