# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:05:28 2021

@author: marcb
"""
#superclass : description du sous-marin
class submarine ():
    def __init__(self, sm_name, sm_country, sm_length):
        self.name = sm_name
        self.country = sm_country
        self.length = sm_length
        
    def display(self):
        print(self.name, "is a submarine")
    
    def nationality(self):
        if self.country == "France" :
            print(self.name, "is a French submarine")

#subclass 1
#nuclear submarine
class nuclear(submarine):
    def __init__(self, nuc_name, nuc_country, nuc_length, nuc_propulsion, nuc_speed):
        self.propulsion = nuc_propulsion
        self.speed = nuc_speed
        super().__init__(nuc_name, nuc_country, nuc_length)
     
    def displaypropnuc(self):
        print('the propulsion of the %s is %s' % (self.name, self.propulsion))
        
    def speednuc(self, vmax):
        if self.speed > vmax :
            print(self.name, "is a very fast submarine")
            
#subclass 2 
#sous-marin diesel
class fuel(submarine):
    def __init__(self, nuc_name, nuc_country, nuc_length, nuc_propulsion, nuc_speed):
        self.propulsion = nuc_propulsion
        self.speed = nuc_speed
        super().__init__(nuc_name, nuc_country, nuc_length)
     
    def displaypropfuel(self):
        print('the propulsion of %s is %s' % (self.name, self.propulsion))
        
    def speedfuel(self, vmin):
        if self.speed < vmin :
            print(self.name, "is a slow submarine")
            
def main() :
    favorite = fuel("Favorite", "France", 73, "fuel", 10)
    terrible = nuclear("Le Terrible", "France", 128, "nuclear", 25)
    
    favorite.display()
    terrible.nationality()
    
    favorite.displaypropfuel()
    favorite.speedsfuel(15)
    
    terrible.displaypropnuc()
    terrible.speednuc(20)
    
    
    