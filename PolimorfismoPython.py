# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import math

class Figura:
    
    def __init__(self, p1x, p1y, p2x, p2y):
        self.__p1x=p1x
        self.__p2x=p2x
        self.__p1y=p1y
        self.__p2y=p2y
        
    def distancia(self):
        self._distancia = math.sqrt((self.__p1x-self.__p2x)**2+(self.__p1y-self.__p2y)**2)      

class Circulo (Figura):    
    
    def calcArea(self):
        self.distancia()
        self.__area = math.pi * 2 * (self.__radio**2)
        return self.__area
    
    def calcPerimetro(self):
        self.distancia()
        self.__perimetro = 2 * math.pi * self.__radio
        return self.__perimetro
    
class Rectangulo(Figura):
    
    def calcArea (self):
        self.__base = self.__p2x-self.__p1x
        self.__altura = self.__p2y-self.__p1y  
        self.__area=self.__base*self.__altura
        return self.__area
    
class Triangulo (Rectangulo):
    
    def calcArea (self):
        