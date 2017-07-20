import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk as ttk

outputWindowHeader = ['Name (Folder A)', 'MD5 (Folder A)', 'Name (Folder B)', 'MD5 (Folder B)']
outputValues = [
    ('nameA1', 'md5A1', 'nameB1', 'md5B1'),
    ('nameA2', 'md5A2', 'nameB2', 'md5B2'),
    ('nameA3', 'md5A3', 'nameB3', 'md5B3'),
    ('nameA4', 'md5A4', 'nameB4', 'md5B4'),
    ('nameA5', 'md5A5', 'nameB5', 'md5B5'),
    ('nameA6', 'md5A6', 'nameB6', 'md5B6'),
]


def sort_by(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    # data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sort_by(tree, col, int(not descending)))


class MultiColumnListBox(ttk.Treeview):
    def __init__(self):
        ttk.Treeview.__init__(self)
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=outputWindowHeader, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in outputWindowHeader:
            self.tree.heading(col, text=col.title(), command=lambda c=col: sort_by(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col, width=tkfont.Font().measure(col.title()))

        for item in outputValues:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkfont.Font().measure(val)
                if self.tree.column(outputWindowHeader[ix], width=None) < col_w:
                    self.tree.column(outputWindowHeader[ix], width=col_w)


class MainWindow(tk.Tk):
    # Gui callbacks
    def show_all(self):
        self.checkbuttonMD5MatchNameMatch.select()
        self.checkbuttonMD5MatchNameMismatch.select()
        self.checkbuttonMD5MismatchNameMatch.select()
        self.checkbuttonOnlyInFolderA.select()
        self.checkbuttonOnlyInFolderB.select()

    def apply(self):
        pass

    # Gui constructor
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(width=862, height=508)
        self.title("Folder compare")

        ### Create a Menubar and associate it with the window
        self.menubar = tk.Menu()
        self.config(menu=self.menubar)

        # File menu
        self.menuFile = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=self.menuFile)
        self.menuFile.add_command(label="Select folder A")
        self.menuFile.add_command(label="Select folder A (md5 text)")
        self.menuFile.add_command(label="Select folder B")
        self.menuFile.add_command(label="Select folder B (md5 text)")
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Exit", command=self.destroy)

        # Options menu
        self.menuOptions = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Options", menu=self.menuOptions)

        # Help menu
        self.menuHelp = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=self.menuHelp)
        self.menuHelp.add_command(label="About")

        ### Folder A Frame
        self.labelFrameFolderA = tk.LabelFrame(self, text="Folder A", padx=4, pady=2)
        self.labelFrameFolderA.pack(fill=tk.X, padx=8, pady=2)

        # Radio buttons
        self.radioButtonFolderAVar = tk.IntVar()
        self.radioButtonFolderAVar.set(1)

        self.radioButtonFolderA = tk.Radiobutton(self.labelFrameFolderA, text="Folder", variable=self.radioButtonFolderAVar, value=1, padx=4)
        self.radioButtonFolderA.pack(side=tk.LEFT)

        self.radioButtonMD5Text = tk.Radiobutton(self.labelFrameFolderA, text="MD5 text", variable=self.radioButtonFolderAVar, value=2, padx=4)
        self.radioButtonMD5Text.pack(side=tk.LEFT)

        # Entry
        self.entryFolderA = tk.Entry(self.labelFrameFolderA)
        self.entryFolderA.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=4)

        # Browse button
        self.buttonBrowse = tk.Button(self.labelFrameFolderA, text="...", padx=4)
        self.buttonBrowse.pack(side=tk.RIGHT, padx=4)

        ### Folder B Frame
        self.labelFrameFolderB = tk.LabelFrame(self, text="Folder B", padx=4, pady=2)
        self.labelFrameFolderB.pack(fill=tk.X, padx=8, pady=2)

        # Radio buttons
        self.radioButtonFolderBVar = tk.IntVar()
        self.radioButtonFolderBVar.set(1)

        self.radioButtonFolderB = tk.Radiobutton(self.labelFrameFolderB, text="Folder", variable=self.radioButtonFolderBVar, value=1, padx=4)
        self.radioButtonFolderB.pack(side=tk.LEFT)

        self.radioButtonMD5Text = tk.Radiobutton(self.labelFrameFolderB, text="MD5 text", variable=self.radioButtonFolderBVar, value=2, padx=4)
        self.radioButtonMD5Text.pack(side=tk.LEFT)

        # Entry
        self.entryFolderB = tk.Entry(self.labelFrameFolderB)
        self.entryFolderB.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=4)

        # Browse button
        self.buttonBrowse = tk.Button(self.labelFrameFolderB, text="...", padx=4)
        self.buttonBrowse.pack(side=tk.RIGHT, padx=4)

        ### Checkbuttons Frame
        self.frameCheckbuttons = tk.Frame(self, padx=4, pady=2)
        self.frameCheckbuttons.pack(fill=tk.X, padx=8, pady=2)

        # Show all button
        self.buttonShowAll = tk.Button(self.frameCheckbuttons, text="Show all", command=self.show_all, padx=4)
        self.buttonShowAll.pack(side=tk.LEFT)

        # Checkbuttons
        self.checkbuttonMD5MatchNameMatchVar = tk.BooleanVar()
        self.checkbuttonMD5MatchNameMatch = tk.Checkbutton(self.frameCheckbuttons, text="MD5 & Name match", variable=self.checkbuttonMD5MatchNameMatchVar, padx=4)
        self.checkbuttonMD5MatchNameMatch.select()
        self.checkbuttonMD5MatchNameMatch.pack(side=tk.LEFT)

        self.checkbuttonMD5MatchNameMismatchVar = tk.BooleanVar()
        self.checkbuttonMD5MatchNameMismatch = tk.Checkbutton(self.frameCheckbuttons, text="MD5 match, Name mismatch", variable=self.checkbuttonMD5MatchNameMismatchVar, padx=4)
        self.checkbuttonMD5MatchNameMismatch.select()
        self.checkbuttonMD5MatchNameMismatch.pack(side=tk.LEFT)

        self.checkbuttonMD5MismatchNameMatchVar = tk.BooleanVar()
        self.checkbuttonMD5MismatchNameMatch = tk.Checkbutton(self.frameCheckbuttons, text="MD5 mismatch, Name match", variable=self.checkbuttonMD5MismatchNameMatchVar, padx=4)
        self.checkbuttonMD5MismatchNameMatch.select()
        self.checkbuttonMD5MismatchNameMatch.pack(side=tk.LEFT)

        self.checkbuttonOnlyInFolderAVar = tk.BooleanVar()
        self.checkbuttonOnlyInFolderA = tk.Checkbutton(self.frameCheckbuttons, text="Only in folder A", variable=self.checkbuttonOnlyInFolderAVar, padx=4)
        self.checkbuttonOnlyInFolderA.select()
        self.checkbuttonOnlyInFolderA.pack(side=tk.LEFT)

        self.checkbuttonOnlyInFolderBVar = tk.BooleanVar()
        self.checkbuttonOnlyInFolderB = tk.Checkbutton(self.frameCheckbuttons, text="Only in folder B", variable=self.checkbuttonOnlyInFolderBVar, padx=4)
        self.checkbuttonOnlyInFolderB.select()
        self.checkbuttonOnlyInFolderB.pack(side=tk.LEFT)

        # Apply button
        self.buttonApply = tk.Button(self.frameCheckbuttons, text="Apply", command=self.apply, padx=4)
        self.buttonApply.pack(side=tk.RIGHT)

        ### File info
        self.listbox = MultiColumnListBox()
