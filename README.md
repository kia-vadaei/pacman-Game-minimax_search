# Pac-Man AI Project

<img src="https://s31.picofile.com/file/8471267534/Screenshot_2024_01_06_203333.png" alt="Alt text" width="500" height="310">

## Authors

- Melika Shirian
- Kianoosh Vadaei

## Instructor

- Dr. Hossein Karshenas

## Date

2024-01-06

## Overview

This project focuses on implementing AI strategies for the classic game Pac-Man. It incorporates elements of reinforcement learning and game playing algorithms.

## Table of Contents

- [Usage](#usage)
- [Features](#Features)
- [References](#References)

## Features

- **Minimax Algorithm with Alpha-Beta Pruning**: Implements Minimax with alpha-beta pruning to enhance the efficiency of the search algorithm.

- **Multi-Agent Environment**: The project includes a multi-agent environment where Pac-Man interacts with intelligent ghosts.

## Usage

To use the environment, follow these steps after cloning the GitHub repository:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/pacman-ai-project.git
    ```

2. Navigate to the directory `multi-agent-search-pandas\Code\multiagent` using the terminal:

    ```bash
    cd pacman-ai-project/multi-agent-search-pandas/Code/multiagent
    ```

3. Run the following script to play the game:

    ```bash
    python pacman.py -p AIAgent -k 1 -a depth=4
    ```

4. Run the following script for manual play mode:

    ```bash
    python manual_play.py
    ```

## References

- Game Playing 1 - Minimax, Alpha-beta Pruning | Stanford CS221: AI (Autumn 2019). [Link](https://www.youtube.com/watch?v=3pU-Hrz_xy4&t=4317s)

- Multi-agent Pac-Man Stanford CS221 Spring 2018. [Link](https://web.stanford.edu/class/archive/cs/cs221/cs221.1186/assignments/pacman/index.html)

- OpenAI. "ChatGPT." [Link](https://www.openai.com/)

- Russell, Stuart, and Norvig, Peter. "Artificial Intelligence: A Modern Approach." (Book)

Feel free to explore and contribute!

