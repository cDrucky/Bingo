#!/usr/bin/python


class bingo:
        def __init__(self,b,i,n,g,o,card,data):
                self.b = [square(null,i[0],null,b[1],null,null,null,i[1],data[0]),
                          square(null,i[1],b[0],b[2],null,i[0],null,i[2],data[1]),
                          square(null,i[2],b[1],b[3],null,i[1],null,i[3],data[2]),
                          square(null,i[3],b[2],b[4],null,i[2],null,i[4],data[3]),
                          square(null,i[4],b[4],null,null,i[3],null,null,data[4])]
                self.i = [square(b[0],n[0],null,i[1],null,null,b[1],n[1],data[5]),
                          square(b[1],n[1],i[0],i[2],b[0],n[0],b[2],n[2],data[6]),
                          square(
                self.n = [0,0,0,0,0]
                self.g = [0,0,0,0,0]
                self.o = [0,0,0,0,0]
                self.card = [self.b,self.i,self.n,self.g,self.o]
                self.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]




        class square:
                def __init__(self,l,r,t,b,tl,tr,bl,br,data):
                        self.l = null
                        self.r = null
                        self.t = null
                        self.b = null
                        self.tl = null
                        self.tr = null
                        self.bl = null
                        self.br = null
                        self.data = [0,A]
