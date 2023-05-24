import tkinter as tk
from PIL import Image
from PIL import ImageTk
import pandas as pd
import pandastable as pt
import prolog_dfa
import prolog_scanner
import prolog_parser


def operators_DFA_button():

    op_dfa_window = tk.Toplevel(window)
    op_dfa_window.geometry("700x700")
    op_dfa_window.title("Operators DFA")

    prolog_dfa.generate_dfa_operators()

    op_image = Image.open("dfa_output\dfa_operators.gv.png")
    op_image = op_image.resize([700, 700])
    op_image = ImageTk.PhotoImage(op_image)
    tk.Label(op_dfa_window, image=op_image).pack()
    op_dfa_window.mainloop()


def res_DFA_button():

    res_dfa_window = tk.Toplevel(window)
    res_dfa_window.geometry("700x700")
    res_dfa_window.title("Reserved Words DFA")

    prolog_dfa.generate_dfa_res()

    res_image = Image.open("dfa_output\dfa_reserved_words.gv.png")
    res_image = res_image.resize([700, 700])
    res_image = ImageTk.PhotoImage(res_image)
    tk.Label(res_dfa_window, image=res_image).pack()
    res_dfa_window.mainloop()


def values_DFA_button():

    values_dfa_window = tk.Toplevel(window)
    values_dfa_window.geometry("700x700")
    values_dfa_window.title("Values DFA")

    prolog_dfa.generate_dfa_values()

    values_image = Image.open("dfa_output\dfa_values.gv.png")
    values_image = values_image.resize([700, 700])
    values_image = ImageTk.PhotoImage(values_image)
    tk.Label(values_dfa_window, image=values_image).pack()
    values_dfa_window.mainloop()


def parse_tree_button():

    input = textarea.get('1.0', 'end')
    scanner = prolog_scanner.Scanner(input)
    parse = prolog_parser.Parser(scanner)

    parse_tree = parse.parse()
    parse_tree.draw()


def tokens_list_button():

    token_window = tk.Toplevel(window)
    token_window.geometry("700x700")
    token_window.title("Token List")

    input = textarea.get('1.0', 'end')
    scanner = prolog_scanner.Scanner(input)
    tokens_list = scanner.tokens

    tokens_dict = dict()
    for item in tokens_list:
        tokens_dict[str(item.token_type)] = set()
    for item in tokens_list:
        tokens_dict[str(item.token_type)].add(item.lex)
    tokens_df = pd.DataFrame.from_dict(tokens_dict, orient='index').transpose()

    token_table = pt.Table(token_window, dataframe=tokens_df)
    token_table.show()

    token_window.mainloop()


# Create a Tkinter window
window = tk.Tk()
window.title("Enter Your Code")

# Set the initial size of the window
# Set the width to 700 pixels and height to 700 pixels
window.geometry("700x700")

# Create a grid for the button and textarea
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)

# Create a frame for the textarea
textarea_frame = tk.Frame(window)
textarea_frame.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Create a textarea widget
textarea = tk.Text(textarea_frame, wrap="none")
textarea.pack(fill=tk.BOTH, expand=True)

# create the widgets for the buttons and lay them out
op_dfa = tk.Button(window, text="Operators DFA",
                   width=13, height=2, command=operators_DFA_button)
op_dfa.grid(row=1, column=0, sticky="nsew")

res_dfa = tk.Button(window, text="Reserved Words DFA",
                    width=13, height=2, command=res_DFA_button)
res_dfa.grid(row=1, column=1, sticky="nsew")

values_dfa = tk.Button(window, text="Values DFA",
                       width=13, height=2, command=values_DFA_button)
values_dfa.grid(row=1, column=2, sticky="nsew")

parse_tree = tk.Button(window, text="Parse Tree",
                       width=13, height=2, command=parse_tree_button)
parse_tree.grid(row=1, column=3, sticky="nsew")

token_list = tk.Button(window, text="Token List",
                       width=13, height=2, command=tokens_list_button)
token_list.grid(row=1, column=4, sticky="nsew")

# Start the Tkinter event loop
window.mainloop()



