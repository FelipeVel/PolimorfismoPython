# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import math

class Figura:
    
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x=p1x
        self.p2x=p2x
        self.p1y=p1y
        self.p2y=p2y
        
    def distancia(self, p1x, p1y, p2x=0, p2y=0):
        return math.sqrt((p1x-p2x)**2+(p1y-p2y)**2)

class Circulo (Figura):
    
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x=p1x
        self.p2x=p2x
        self.p1y=p1y
        self.p2y=p2y    
    
    def calcArea(self):
        self.dist = self.distancia(self.p1x, self.p1y, self.p2x, self.p2y)
        self.area = math.pi * (self.dist**2)
        return self.area
    
    def calcPerimetro(self):
        self.dist = self.distancia(self.p1x, self.p1y, self.p2x, self.p2y)
        self.perimetro = 2 * math.pi * self.dist
        return self.perimetro
    
class Rectangulo(Figura):
    
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x=p1x
        self.p2x=p2x
        self.p1y=p1y
        self.p2y=p2y
    
    def calcArea1 (self):
        self.base = self.p2x-self.p1x
        self.altura = self.p2y-self.p1y  
        self.area=self.base*self.altura
        return self.area
    
    def calcArea (self):
        return self.calcArea1()
    
    def calcPerimetro(self):
        return (2*self.distancia(self.p1x, self.p2x))+(2*self.distancia(self.p1y, self.p2y))
    
class Triangulo (Rectangulo):
    
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x=p1x
        self.p2x=p2x
        self.p1y=p1y
        self.p2y=p2y
    
    def calcArea (self):
        return self.calcArea1()/2
    
    def calcPerimetro(self):
        return self.distancia(self.p1x, self.p2x)+self.distancia(self.p1y, self.p2y)+self.distancia(self.p1x, self.p1y, self.p2x, self.p2y)
    

    