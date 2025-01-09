import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
import pandastable as pt
import prolog_dfa
import prolog_parser
import prolog_scanner


class PrologApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enter Your Code")
        self.root.geometry("700x700")

        self.create_widgets()

    def create_widgets(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)

        textarea_frame = tk.Frame(self.root)
        textarea_frame.grid(row=0, column=0, columnspan=5, sticky="nsew")

        self.textarea = tk.Text(textarea_frame, wrap="none")
        self.textarea.pack(fill=tk.BOTH, expand=True)

        op_dfa = tk.Button(self.root, text="Operators DFA", width=13, height=2, command=self.operators_DFA_button)
        op_dfa.grid(row=1, column=0, sticky="nsew")

        res_dfa = tk.Button(self.root, text="Reserved Words DFA", width=13, height=2, command=self.res_DFA_button)
        res_dfa.grid(row=1, column=1, sticky="nsew")

        values_dfa = tk.Button(self.root, text="Values DFA", width=13, height=2, command=self.values_DFA_button)
        values_dfa.grid(row=1, column=2, sticky="nsew")

        parse_tree = tk.Button(self.root, text="Parse Tree", width=13, height=2, command=self.parse_tree_button)
        parse_tree.grid(row=1, column=3, sticky="nsew")

        token_list = tk.Button(self.root, text="Token List", width=13, height=2, command=self.tokens_list_button)
        token_list.grid(row=1, column=4, sticky="nsew")

    def operators_DFA_button(self):
        op_dfa_window = tk.Toplevel(self.root)
        op_dfa_window.geometry("700x700")
        op_dfa_window.title("Operators DFA")

        prolog_dfa.generate_dfa_operators()

        op_image = Image.open("dfa_output/operators.png")
        op_image = op_image.resize((700, 700))
        op_image = ImageTk.PhotoImage(op_image)
        tk.Label(op_dfa_window, image=op_image).pack()
        op_dfa_window.mainloop()

    def res_DFA_button(self):
        res_dfa_window = tk.Toplevel(self.root)
        res_dfa_window.geometry("700x700")
        res_dfa_window.title("Reserved Words DFA")

        prolog_dfa.generate_dfa_res()

        res_image = Image.open("dfa_output/reserved_words.png")
        res_image = res_image.resize((700, 700))
        res_image = ImageTk.PhotoImage(res_image)
        tk.Label(res_dfa_window, image=res_image).pack()
        res_dfa_window.mainloop()

    def values_DFA_button(self):
        values_dfa_window = tk.Toplevel(self.root)
        values_dfa_window.geometry("700x700")
        values_dfa_window.title("Values DFA")

        prolog_dfa.generate_dfa_values()

        values_image = Image.open("dfa_output/dfa_values.gv.png")
        values_image = values_image.resize((700, 700))
        values_image = ImageTk.PhotoImage(values_image)
        tk.Label(values_dfa_window, image=values_image).pack()
        values_dfa_window.mainloop()

    def parse_tree_button(self):
        input_text = self.textarea.get('1.0', 'end')
        scanner = prolog_scanner.Scanner(input_text)
        parser = prolog_parser.Parser(scanner)

        parse_tree = parser.parse()
        parse_tree.draw()

    def tokens_list_button(self):
        token_window = tk.Toplevel(self.root)
        token_window.geometry("700x700")
        token_window.title("Token List")

        input_text = self.textarea.get('1.0', 'end')
        scanner = prolog_scanner.Scanner(input_text)
        tokens_list = scanner.tokens

        tokens_dict = {str(item.token_type): set() for item in tokens_list}
        for item in tokens_list:
            tokens_dict[str(item.token_type)].add(item.lex)
        tokens_df = pd.DataFrame.from_dict(tokens_dict, orient='index').transpose()

        token_table = pt.Table(token_window, dataframe=tokens_df)
        token_table.show()

        token_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PrologApp(root)
    root.mainloop()
