class Gate:
    coordX: int = 0
    coordY: int = 0
    sprite: ""
    # To ask: when Lemmings go into Exit Gate,
    # does it need to have an Active atribute to know
    # when Lemmings reach it?
    isActive: bool = True