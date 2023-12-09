# Python Platformer

This is a 2 player game made with Python, including 2d physics and collision detection, jumps and double jumps, player combat, and projectile instantiation.


## Requirements:
- #### python 3.x
- #### Tkinter 8.6+
- #### random


## Setup:

1. Create a virtual environment using the latest release of virtualenv:

``` bash
> pip install virtualenv --upgrade
> virtualenv venv
```

_If there are problems with installing tkinter:_
- Install tkinter package. Ex: Homebrew:
``` bash
> brew install python-tk
```
- Then create the virtual environment as follows:
```
> virtualenv venv --system-site-packages
```

2. Access the virtual environment `./venv`
``` bash
> source ./venv/bin/activate
```


## Execution:

#### To run the game, execute the following command:

``` bash
> python ./src/main.py
```


## How to Play:

**Objective:** decrease the other player's health displayed on the screen.
#### Player 1:
    - Jump / Double Jump with Up-Arrow
    - Move with Left and Right Arrows
    - Shoot with 'M'
#### Player 2:
    - Jump /Double Jump with 'E'
    - Move with 'S' and 'F'
    - Shoot with 'Q'

