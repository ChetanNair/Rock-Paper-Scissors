# OpenCV Rock, Paper, Scissors

## Overview

- The user can play a game of rock, paper, scissors against the computer.
- Uses video input from the webcam to capture the user's move (rock, paper or scissors).
- The computer also generates its move.

The winner is calculated and the scores are incremented appropriately.
Ties contribute zero points while invalid hand signs are reported as invalid by the program.

# Getting Started

## Dependencies

* [Mediapipe](https://google.github.io/mediapipe/)
* [OpenCV](https://opencv.org).

## Program Execution

```
python3 RPS_Game.py
```

\*\* Must allow the program to use webcam.

## Detailed Explanation

Using OpenCV, the webcam input is read in frame by frame. The mediapipe library's hand module is called and isolates the hand's skeletal structure if it is in frame. An alogrithm* decides whether the player's move is rock, paper or scissors using the skeletal coordinates from the module and the computer also plays a move. The user then needs to move their hand out of the frame and back in to play the next round. The winner is calculated each time the hand enters back into the frame after leaving and a running tally is maintained.

*This algorithm works by counting the number of fingers that are open. For rock, this would be zero. This scissors, this would be two fingers. And finally, for paper, this would be 5 fingers. The number of fingers is counted by checking the y-coordinate of different finger segments. If the fingertip is below the middle of the same finger, it is considers closed. Hence, it does not count towards the number of open fingers. For the thumb, the x-coordinate is used. The limitation of this strategy is that the palm needs to face the camera in order for the open fingers to be counted properly. 

## Author

Chetan Nair - chetan.r.nair@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
