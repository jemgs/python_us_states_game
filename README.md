# python_us_states_game

A simple game built with Python's Turtle graphics module and pandas library that tests your knowledge of U.S. states. The game displays an image of a blank map of the United States, and you need to correctly guess the names of the states by typing them in. If you guess all 50 states correctly, you win the game!

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/jemgs/python_us_states_game.git

2. Navigate to the project directory:
cd us-states-game

3. Make sure you have Python 3.x installed.

4. Install the required dependencies:
pip install pandas turtle

## Usage

1. Run the `main.py` file to start the game:
python main.py

2. A Turtle graphics window will open displaying a blank map of the United States.

3. Enter the name of a U.S. state in the pop-up prompt.

4. If your guess is correct, the state will be filled on the map, and you will move on to the next guess.

5. If your guess is incorrect, the correct answer will be revealed, and you can continue guessing the remaining states.

6. To exit the game, type "Exit" in the prompt.

7. If you successfully guess all 50 states, a message will be displayed indicating that you have won the game.

## Files

The project contains the following files:

- `main.py`: The main Python script that runs the U.S. States game.
- `state.py`: A module defining the `State` class used to represent individual states on the map.
- `50_states.csv`: A CSV file containing data about the U.S. states, including their names and coordinates.
- `blank_states_img.gif`: An image file displaying a blank map of the United States.
- `your_missed_states.csv`: A CSV file that will be generated if you exit the game before guessing all 50 states correctly. It contains the names of the states you missed.

Enjoy playing and learning about the U.S. states!

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is currently not licensed.
