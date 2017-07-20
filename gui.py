import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(width=512, height=400)
        self.title("Folder compare")

        # Create a Menubar and associate it with the window
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

        # Folder A Frame
        self.labelFrameFolderA = tk.LabelFrame(self, text="Folder A")
        self.labelFrameFolderA.pack(fill=tk.X)

        # Radio buttons
        self.varA = tk.IntVar()
        self.radioButtonFolderA = tk.Radiobutton(self.labelFrameFolderA, text="Folder", variable=self.varA, value=1)
        self.radioButtonFolderA.pack(side=tk.LEFT)

        self.radioButtonMD5Text = tk.Radiobutton(self.labelFrameFolderA, text="MD5 text", variable=self.varA, value=2)
        self.radioButtonMD5Text.pack(side=tk.LEFT)

        self.varA.set(1)

        # Entry
        self.entryFolderA = tk.Entry(self.labelFrameFolderA)
        self.entryFolderA.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Browse button
        self.buttonBrowse = tk.Button(self.labelFrameFolderA, text="...")
        self.buttonBrowse.pack(side=tk.RIGHT)

        # Folder B Frame
        self.labelFrameFolderB = tk.LabelFrame(self, text="Folder B")
        self.labelFrameFolderB.pack(fill=tk.X)

        # Radio buttons
        self.varB = tk.IntVar()
        self.radioButtonFolderB = tk.Radiobutton(self.labelFrameFolderB, text="Folder", variable=self.varB, value=1)
        self.radioButtonFolderB.pack(side=tk.LEFT)

        self.radioButtonMD5Text = tk.Radiobutton(self.labelFrameFolderB, text="MD5 text", variable=self.varB, value=2)
        self.radioButtonMD5Text.pack(side=tk.LEFT)

        self.varB.set(1)

        # Entry
        self.entryFolderB = tk.Entry(self.labelFrameFolderB)
        self.entryFolderB.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Browse button
        self.buttonBrowse = tk.Button(self.labelFrameFolderB, text="...")
        self.buttonBrowse.pack(side=tk.RIGHT)

        self.frameFileInfo = tk.Frame(self)
        self.frameFileInfo.pack()
