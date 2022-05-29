# The Whimsical Castle

The Whimsical Castle is a text-based adventure game written in Python that runs on the command line. You play as a person who, upon waking up, finds themselves lost in a magical castle full of strange and wondrous objects. It is up to you to uncover the secrets of the castle and the reason for your current predicament. 

Starting off in the castle’s courtyard, you are allowed to explore the 15+ rooms of the castle, though some will be locked and even hidden from your view.

## Getting Started

These instructions require a basic working knowledge of navigating the command line/terminal.
It also requires having Python installed (version >= 3.6) and pip.

<strong>1. Clone the repository:</strong>  
*if using a Personal Access Token (PAT):*  
```
git clone https://github.com/katecoded/text_based_adventure.git
```  
*if using an SSH key:*  
```
git clone git@github.com:katecoded/text_based_adventure.git
```  
(see [About remote repositories](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories) for help on which URL to use)  

<strong>2. Navigate into the project folder:</strong>  
```
cd text_based_adventure
```  

<strong>3. Install dependencies using pip:</strong>  
```
pip install -r requirements.txt
```  

<strong>4. Run text based adventure.py:</strong>  
*for Windows:*  
```
py text_based_adventure.py
```  
*for Linux and Mac:*  
```
python3 text_based_adventure.py
```

## How to Play

This text-based adventure game can be played by typing in-game commands on the command line.

Here is an example of how to interact with the game's starting area:
```console
The Whimsical Castle
A text-based adventure game by Mason Stiller, Apoorva Magadi, Katelyn Lindsey, Fedor Titov

You wake up in a castle with no idea how you got there. Well, this is inconvenient.
(Use 'help' to see all available commands.)

Courtyard
The courtyard is full of moss-covered rubble. Glowing mushrooms, both big and small, grow in clusters in cracks on the floor, and vines have grown over the rusty gate that must have once been the castle's entrance. A cold breeze sweeps through, and you shudder, looking up at the towering stones from the parts of the castle that remain standing. You wonder what this place is.
You can see a dark corridor to the west, a stone staircase to the east, mushrooms, a tower, a rusty gate, and an ivory key.

> examine tower
In the distance, a stone tower looms over the rest of the castle. It appears curiously untouched compared to the rest of the outside of the castle, most of which is in ruins.

> look at rusty gate
Completely covered in vines, the castle's front gate is rusted over and old. It would have been beautiful in its prime.

>
```

There are many commands that can be used in order to play the game. Try the 'help' command in-game in order to see a list of all available commands.

## About

This game was created and developed by Fedor Titov, Katelyn Lindsey, Apoorva Magadi, and Mason Stiller as a capstone project for CS 467.
