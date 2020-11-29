'''
Lemmings Project
Class design
'''

# To ask: Can we do a generic class named Tool for all 3 of them?
# If we can, what can we do if we have one instance (or extension)
# of that class with an extra atribute? can we extend that class like in Java?

# Tools #


class Ladder:
    coordX: int = 0
    coordY: int = 0
    appearing: bool = False
    sprite: ""
    isActive: bool = True
    # ??? different directions??
    direction: str = "right"

# is instance


class Umbrella:
    coordX: int = 0
    coordY: int = 0
    appearing: bool = False
    sprite: ""
    falling: bool = False
    isActive: bool = True


class Blocker:
    coordX: int = 0
    coordY: int = 0
    appearing: bool = False
    sprite: ""
    isActive: bool = True


class Gate:
    coordX: int = 0
    coordY: int = 0
    sprite: ""
    # To ask: when Lemmings go into Exit Gate,
    # does it need to have an Active atribute to know
    # when Lemmings reach it?
    isActive: bool = True

# Do we need to do a class for the game board values?
# Died, Alive, Lemmings...
# Marker


class Marker:
    died: str = ""
    died_value: int = 0
    alive: int = ""
    alive_value: int = 0


class Lemming:
    coordX: int = 0
    coordY: int = 0
    life: bool = True
    direction: str = "right"
    # or "left"
    ascending: bool = False
    descending: bool = False
    falling: bool = False
    sprite: ""

# To ask: We have cells (where the tools and platforms are placed) but
# do we need another class for platforms? or is it enough to add an sprite to a Cell
# when needed and if the Cell has a sprite (if Sprite is True or another atribute like "isPlatform")
# then we treat it as a platform?
# cell para gestionar las celdas
# propiedad contenedor, para decir qué estoy guardando.
# guardar varios objetos, propiedad tipo lista.
class Cell:
    coordX: int = 0
    coordY: int = 0
    container: list = ["", ""]  # ["Platform", "Umbrella"]

class Platform:
    coordX: int = 0
    coordY: int = 0
    sprite: ""