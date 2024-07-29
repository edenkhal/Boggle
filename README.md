# Overview
This project involves implementing the game Boggle as a part of the course "Introduction to Computer Science 67101" for Semester A 2022/23.
The project requires developing both the game logic and the GUI for Boggle, following specific requirements and guidelines.

# Game Rules
# Game Board
* The Boggle game board is a 4x4 grid of cubes, each cube displaying a letter.
* Each position on the board is defined by a pair of indices (x, y), where y is the row number and x is the column number.
* The top-left corner of the board is at (0,0), and the bottom-right corner is at (3,3).
* At the start of the game, a random 4x4 board is generated.
# Gameplay
* The game has a single player.
* The player has 3 minutes to find as many valid words as possible on the board.
* A valid word is a word that appears in the dictionary and is formed by tracing a path through adjacent letters on the board.
  Adjacency includes horizontal, vertical, and diagonal neighbors.
* The same cube can be used for different words but not multiple times in the same word.
* Special rule: the letter pair "QU" is treated as a single unit.
# Scoring
* Each valid word scores points equal to the square of the word's length (e.g., a 3-letter word scores 9 points).
* Duplicate words found on the board do not score points more than once.
