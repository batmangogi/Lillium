#math module!

class Vect_2d:
    """
    vect_2d(x,y) creates an object 2d vector by setting its position (x and y)
    """
    def __init__(self,x=0,y=0):
        if x == 0 and y == 0:
            print("---an error as occured")
            print("---perhaps you forgot to definy >vect_2d<? for so >vect_2d< as been its default values")
            print("---to definy >vect_2d< fill vect_2d()<---")
        self.x = x
        self.y = y 
    def Normalize(self):
        pass
    def Move_To(self,x=0,y=0,sp=0):
        """
        move_to(x,y) changes the object vector gradualy untill its values are equal to the set ones (require an already existing vect_2d to work)    
        """
        self.fx = x
        self.fy = y

        if self.x > self.fx:
                self.x-=sp
        elif self.y > self.fy:
                self.y-=sp
        elif self.x < self.fx:
                self.x+=sp
        elif self.y < self.fy:
                self.y+=sp
        else:
            print("---an unknown error as occured")

    #TODO: remember to finish move_to()! mustn't use any cicle! (like while) use update! somehow...
    def Vect_Upd(self,x=0,y=0):
        """
        vect_update(x,y) update vector values
        """
        if x == 0 and y == 0:
            print("---an error as occured")
            print("---perhaps you forgot to definy >vect_update<? for so >vect_update< as been its default values")
            print("---to definy >vect_update< fill vect_update()<---")
        self.x = x
        self.y = y   


class Obj_Rect:
    """
    obj_rect(width,height) creates a rect object
    """
    def __init__(self,width,height,pos=None):
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = (width*2)+(height*2)
        if pos is None:
            pos = Vect_2d(0,0)
            self.x = pos.x
            self.y = pos.y
        else:
            self.x = pos.x
            self.y = pos.y
        self.right = self.x+width
        self.left = self.x
        self.top = self.y
        self.bottom = self.y+height

    def Rect_Res(self,width,height):
        """
        rect_resize(width,height) resizes an already existing rect
        """
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = (width*2)+(height*2)
        self.right = self.x+width
        self.left = self.x
        self.top = self.y
        self.bottom = self.y+height



