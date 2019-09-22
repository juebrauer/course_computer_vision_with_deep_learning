"""
Meine Mathe-Hilfsfunktionen

Da gibt es so einige.
"""

def quadriere(x):
    """
    Gib mir x, ich gebe dir x*x zurück!
    
    Toll, oder?
    """
    return x**2
    
def invers(x):
    """
    Gib mir x, ich gebe dir 1/x zurück!
    """
    return 1/x
    
class coord:
    """
    Eine 2D-Koordinate
    """

    def __init__(self,x,y):
        """
        Der Initialisierer.
        """
        self.koord = (x,y)
        
    def __str__(self):
        """
        Damit kann sich eine 2D-Koordinate ausgeben.
        """
        return "Ich bin eine 2D-Koordinate: " + str(self.koord)
        
print("Willkommen im Modul mein_modul")