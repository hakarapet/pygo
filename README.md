# PyGo
Go game on Python

## Description
Create a simple go game to play on terminal with all go rules (Chinese
version).

## Idea
Daily training of any kind of code writing, unit test techniques

## ToDo
- [x] define "open liberties"
- [x] define "board". The board should be of three sizes: 9x9, 13x13, 19x19.
- [x] define "move": placing a "stone" on an empty intersection
- [x] define "position": each intersection on the board is in one and only one of
  the following states:
    - empty
    - occupied by Blacks
    - occupied by Whites
- [x] define "connected"/"adjacent intersections": placed on intersection same
  colored stones are "connected" if they are on the same axis of the board and the differnce
  between their index is __± 1__ . (from official source: _two intersections
  are said to be "adjacent" if they are distinct and connected by a horizontal
  or vertical line with no other intersections between them_)

