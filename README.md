# Connect Four AI

This project implements an AI for the game Connect Four using the **minimax algorithm** with **alpha-beta pruning**. The AI competes against another AI using different strategies for evaluating the game board.

## Project Overview

In this project, I:
- Utilized a minimax algorithm to develop a Connect Four AI.
- Implemented my own evaluation function to replace the default one provided.
- Experimented with different AI strategies to optimize gameplay performance.

### Key Features
- **Minimax Algorithm**: Evaluates the game tree to select the optimal move for the AI player.
- **Alpha-Beta Pruning**: Optimizes the minimax algorithm by pruning unnecessary branches.
- **Custom Evaluation Functions**: Includes `my_evaluate_board()` which analyzes game positions based on streaks and winning opportunities.

## Evaluation Functions
- **My Custom Strategy**: Prioritizes winning by counting streaks of two or more and weighs streaks in different directions.
