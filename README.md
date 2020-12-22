# PyGo
Go game on Python

## Idea
Create a simple go game to play on terminal with all go rules (Chinese
version). 

## ToDo
- define "board". The board should be of three sizes: 9x9, 13x13, 19x19.
- define "move": placing a "stone" on an empty intersection
- define "position": each intersection on the board is in one and only one of
  the following states: 
    - empty
    - occupied by Blacks
    - occupied by Whites
- define "connected"/"adjacent intersections": placed on intersection same
  colored stones are "connected" if they are on the same axis of the board and the differnce
  between their index is __± 1__ . (from official source: _two intersections
  are said to be "adjacent" if they are distinct and connected by a horizontal
  or vertical line with no other intersections between them_)

