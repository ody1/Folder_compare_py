import tkinter as tk


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

        self.frameFileInfo = tk.Frame(self)
        self.frameFileInfo.pack()

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
