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
                          square((i[2],g[2],n[1],n[3],i[1],g[1],i[3],g[3],data[12]),
                          square(i[3],g[3],n[2],n[4],i[2],g[2],i[4],g[4],data[13]),
                          square(i[4],g[4],n[3],null,i[3],g[3],null,null,data[14])]]
                self.n = [square(i[0],g[0],null,n[1],null,null,i[1],g[1],data[10]),
                          square(i[1],g[1],n[0],n[2],i[0],g[0],i[2],g[2],data[11]),
                          square(i[2],g[2],n[1],n[3],i[1],g[1],i[3],g[3],data[12]),
                          square(i[3],g[3],n[2],n[4],i[2],g[2],i[4],g[4],data[13]),
                          square(i[4],g[4],n[3],null,i[3],g[3],null,null,data[14])]]
                self.g = [square(o[0],n[0],null,g[1],null,null,n[1],o[1],data[15]),
                          square(o[1],n[1],g[0],g[2],n[0],o[0],n[2],o[2],data[15]),
                          square(o[2],n[2],g[1],g[3],n[1],o[1],n[3],o[3],data[16]),
                          square(o[3],n[3],g[2],g[4],n[2],o[2],n[4],o[4],data[17]),
                          square(o[4],n[4],g[3],null,n[3],o[3],null,null,data[18])]

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
