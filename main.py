# -*- coding: utf-8 -*-
"""
######## Lemmings Game project for Computer Science Degree - UC3M Madrid ########
Authors:
Rosa A. Reyes
Paloma Nuñez

Directory Organisation:
    assets/
        lemming.pyxres # all of the project's sprites made with pyxeleditor.
    classes/
        __init__.py # Archive that makes possible to put subdirectories.
        app.py
        blocker.py
        cell.py
        gate.py
        ladder.py
        lemming.py
        marker.py
        umbrella.py
    .gitignore  # default archive to tell git what to not upload to Github.
    main.py     # main archive where we call the class App() where all the logic is executed.
    README.md   # project's description with main functions and functionality.
"""

from classes.app import App

App()