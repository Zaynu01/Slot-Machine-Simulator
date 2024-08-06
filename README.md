# Slot Machine Simulator

## Description

This Python program simulates a slot machine game. It allows users to deposit money, place bets on multiple lines, spin the slot machine, and potentially win based on the symbols that appear.

## How It Works

1. The program starts by asking the user to deposit money.
2. For each play, the user selects the number of lines to bet on and the bet amount per line.
3. The program generates a random slot machine result using predefined symbols and their frequencies.
4. Winnings are calculated based on the symbols that appear and their corresponding coefficients.
5. The user's balance is updated, and they can choose to play again or quit.

## Features

1. **Deposit System**: Users can deposit money to start playing.

2. **Flexible Betting**: 
   - Users can choose the number of lines to bet on (1-3).
   - Bet amount per line can be set within a predefined range (1$-100$).

3. **Random Slot Generation**: The slot machine results are randomly generated for each spin.

4. **Symbol Weighting**: Different symbols have different frequencies of appearance.

5. **Winning Calculation**: 
   - Wins are calculated based on matching symbols across a line.
   - Different symbols have different payout coefficients.

6. **Visual Display**: The slot machine results are displayed in a visually appealing format.

7. **Balance Management**: The user's balance is tracked and updated after each spin.

8. **Input Validation**: All user inputs are validated to ensure they are within acceptable ranges.

9. **Continuous Play**: Users can play multiple rounds until they choose to quit.

10. **Winning Line Display**: When a user wins, the winning lines are displayed.

## Technologies Used

1. **Programming Language**: Python

2. **Python Standard Library**:
   - `random`: Used for generating random slot machine results.

3. **Data Structures**:
   - Lists: Used for storing slot machine columns and symbols.
   - Dictionaries: Used for storing symbol counts and coefficients.

4. **Control Structures**:
   - Loops (while and for): Used for input validation and game logic.
   - Conditional statements: Used for checking winning conditions and input validation.

5. **Functions**: The code is organized into several functions for modularity and readability.

6. **Type Hinting**: Used to indicate expected types of function parameters and return values.

7. **String Formatting**: Used for displaying game information and results.

This program provides an engaging simulation of a slot machine, complete with realistic betting mechanics and a random number generator to simulate the unpredictability of real slot machines.
