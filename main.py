import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

REALS = 3
COLS = 3

# A dict for all symbols used in the slot machine
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
# A dict that shows the coef for each symbol to be multiplied with the bet
symbol_coefficient = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(lines, bet, slots, coef) -> (int, []):
    winnings = 0
    winning_lines = []
    # Keep in mind that we've stored the columns as rows on the slots matrix
    for line in range(lines):
        symbol = slots[0][line]
        for column in slots:
            current_symbol = column[line]
            if current_symbol != symbol:
                break
        else:
            winnings += coef[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Generate the values for a slot machine trial
def get_slot_machine_trial(reals, cols, symbols) -> [[]]:
    all_symbols = []
    # Store all the symbols in the dict to the list with respective to their count
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []   # This list will contain nested lists that contains the random generated values
    for _ in range(cols):
        column = []
        # Copy the original list elements into sub list to avoid modifying the original list
        current_symbols = all_symbols[:]
        for _ in range(reals):
            val = random.choice(current_symbols)
            column.append(val)
            current_symbols.remove(val)  # Delete the generated value from the sub list

        columns.append(column)

    return columns


# We have to apply transposing on the columns matrix, since the matrix rows are actually the columns
def display_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


# Get the amount from the user to deposit in the balance
def deposit() -> int:
    while True:
        amount = input("Enter the amount of money to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The deposited value should be bigger than 0.")
        else:
            print("Enter a valid number.")

    return amount


# Get the number of lines to bet on
def get_number_of_lines() -> int:
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"The number should be between 1 - {MAX_LINES}")
        else:
            print("Enter a valid number.")

    return lines


# Get the bet on each line
def get_bet() -> int:
    while True:
        bet = input(f"Enter the amount of money to bet ({MIN_BET}$ - {MAX_BET}$) on each line: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET < bet <= MAX_BET:
                break
            else:
                print(f"The value of the bet should be bigger between {MIN_BET}$ - {MAX_BET}$.")
        else:
            print("Enter a valid number.")

    return bet


def spin(balance) -> int:
    lines = get_number_of_lines()

    # Check whether the bet amount is in the balance
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You have insufficient funds, you current balance is {balance}$.")
        else:
            break

    print(f"Balance: "
          f"{balance}$\nNumber of Lines Bet: {lines}\nThe Bet On Each Line: {bet}$\nThe Total Bet: {total_bet}$")

    slots = get_slot_machine_trial(REALS, COLS, symbol_count)
    display_slot_machine(slots)

    winnings, winning_lines = check_winnings(lines, bet, slots, symbol_coefficient)
    print(f"You won: {winnings}$")
    if winning_lines:
        print("You won on line:", *winning_lines)

    return winnings - total_bet


# The main function
def main():
    balance = deposit()

    while True:
        print(f"Current Balance: {balance}$")
        answer = input("Press any key to play or \"q\" to quit.")
        if answer.lower() == "q":
            break
        balance += spin(balance)

    print(f"You are left with: {balance}$")


main()
