import pyxel

class Lemming:
    __cx,__cy=0,0
    __image=[]
    __direccion="L"
    __images=[]
    
    def __init__(self,x,y,direccion,imagenes):
        self.__cx=x
        self.__cy=y
        self.__direccion=direccion
        self.__images=imagenes  #R,L
        
    
    @property
    def x(self):
        return self.__cx

    @x.setter
    def x(self,value):
        self.__cx=value
    
    @property
    def y(self):
        return self.__cy
    
    @y.setter
    def y(self,value):
        self.__cy=value
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self,value):
        self.__image=value

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,value):
        self.__direccion=value
    
    def cambiarDireccion(self):        
        if self.direccion=="R":
            self.direccion="L"
            self.image=[self.__imagenes[0],self.__imagenes[1]]
        else:
            self.direccion="R"
            self.image=[self.__imagenes[2],self.__imagenes[3]]
            
    def avanzar(self):  
        if self.direccion=="R":
            self.self.__cx+=1
        else:
            self.__cx-=1
        
        
    def avanzarR(self):        
        self.__cx+=1
    def avanzarL(self):        
        self.__cx-=1
        


class Cell:
    __cx,__cy=0,0
    __image=""
    
    def __init__(self,x,y):
        self.__cx=x
        self.__cy=y
        self.__image="V"
    
    @property
    def x(self):
        return self.__cx;
    
    @x.setter
    def x(self,value):
        self.__cx=value
    
    @property
    def y(self):
        return self.__cy;
    
    @y.setter
    def y(self,value):
        self.__cy=value
    
    @property
    def image(self):
        return self.__image;
    
    @image.setter
    def image(self,value):
        self.__image=value


class App:
    x=0
    sqX,sqY=0,0 #Coordenadas cursor para seleccionar celda
    WIDHT,HEIGHT=160,128
    grid=[]
    color=3
    fila=int(WIDHT/16)
    columna=int(HEIGHT/16)
    Max_Lemmings=5
    lemmings=[]    
    def __init__(self):
        pyxel.init(self.WIDHT, self.HEIGHT, caption="Pyxel Lemmings")
        pyxel.image(0).load(0, 0, "../assets/umbrella.png")
        pyxel.image(0).load(0, 16, "../assets/umbrella.png")
        pyxel.image(0).load(0, 32, "../assets/umbrella.png")
        pyxel.image(0).load(0, 48, "../assets/umbrella.png")
        
        #create matrix        
        for i in range(self.fila):
            self.grid.append([])
            for j in range(self.columna):
                cell=Cell(i,j)
                cell.image="v"                 
                self.grid[i].append(cell)   
                                  
        pyxel.run(self.update, self.draw)
        
        

    def update(self):
        
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #Movimientos rectangulo
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.sqX+16<=self.WIDHT-16:
                self.sqX+=16
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.sqX-16>=0:
                self.sqX-=16
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.sqY+16<=self.HEIGHT-16:
                self.sqY+=16
        if pyxel.btnp(pyxel.KEY_UP):
            if self.sqY-16>=0:
                self.sqY-=16
                
        #dIBUJO EN tABLERO
        if pyxel.btnp(pyxel.KEY_SPACE):            
            row=int(self.sqY/16) #traducir posicion del cursor (pyxels) a la matrix -> Cell
            col=int(self.sqX/16)
            self.grid[col][row].image="s"
            
        if pyxel.btnp(pyxel.KEY_ENTER):
          
            row=int(self.sqY/16)
            col=int(self.sqX/16)
            self.grid[col][row].image="u"
         
        #Lemmings
        if pyxel.frame_count%50==0:
            if self.Max_Lemmings>0: #len(list)
                lemming=Lemming(0,110, "R", [0,32,0,48])
                self.lemmings.append(lemming)
                self.Max_Lemmings-=1
                
        for lemming in self.lemmings:
            lemming.avanzar()
            if lemming.direccion=="R" :
                if lemming.x>self.WIDHT:
                    lemming.cambiarDireccion()
                    
            if  lemming.direccion=="L" :
                if lemming.x<0:
                    lemming.cambiarDireccion()
                    
            
                    

    def draw(self):
        pyxel.cls(self.color)
        pyxel.rect(self.sqX, self.sqY, 16, 16, 1)        
        for i in range(self.fila):            
            for j in range(self.columna):
                cell=self.grid[i][j]
                #pyxel.text(cell.x*16, cell.y*16, cell.image,1)
                if cell.image=="s":
                    pyxel.blt(cell.x*16, cell.y*16, 0, 0, 0,16,16,0)                    
                elif cell.image=="u":
                    pyxel.blt(cell.x*16, cell.y*16, 0, 0, 16, 16,16,0)
                '''else:
                    pyxel.text(cell.x*16, cell.y*16, cell.image,1)'''
        for lemming in self.lemmings:
            pyxel.blt(lemming.x, lemming.y, 0, lemming.image[0], lemming.image[1], 16,16,0)


App() # we`re creting an App object
