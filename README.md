# Prolog Scanner and Parser

This project implements a scanner and parser for the Prolog language. It includes a graphical user interface (GUI) built with Tkinter to visualize the deterministic finite automata (DFA) and parse trees.

## Features

- **Scanner**: Tokenizes the input Prolog code.
- **Parser**: Parses the tokenized input and generates a parse tree.
- **DFA Generation**: Generates and visualizes DFAs for operators, reserved words, and values.
- **GUI**: Provides a simple GUI to interact with the scanner and parser, and to visualize the DFAs and parse trees.

## Requirements

- Python 3.x
- Tkinter
- Pillow
- Pandas
- Pandastable
- Graphviz
- NLTK

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AbdelrahmanKhaled18/Prolog_Scanner_and_Parser.git
    cd Prolog_Scanner_and_Parser
    ```

2. Install the required Python packages:
    ```sh
    pip install tkinter pillow pandas pandastable graphviz nltk
    ```

3. Ensure Graphviz is installed on your system. You can download it from [Graphviz](https://graphviz.org/download/).

## Usage

1. Run the main application:
    ```sh
    python Main.py
    ```

2. Enter your Prolog code in the provided text area.

3. Use the buttons to:
    - **Operators DFA**: Visualize the DFA for operators.
    - **Reserved Words DFA**: Visualize the DFA for reserved words.
    - **Values DFA**: Visualize the DFA for values.
    - **Parse Tree**: Generate and display the parse tree for the entered Prolog code.
    - **Token List**: Display the list of tokens generated by the scanner.

## Project Structure

- `Main.py`: The main application file that sets up the GUI.
- `prolog_dfa.py`: Contains functions to generate and visualize DFAs.
- `prolog_parser.py`: Contains the parser implementation.
- `prolog_scanner.py`: Contains the scanner implementation.
- `README.md`: Project documentation.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.# Prolog_Scanner_and_Parser

Scanner and parser for prolog language with the language description as a pdf and generating dfa and parse tree using tkinter simple GUI
