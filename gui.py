import tkinter as tk

returnValues = []
numFields = 1

# Draws main GUI for url submission page
# returns URL as string
def drawMainGUI(colourFile):

    def submit():
        global returnValues
        for i in range(numFields):
            returnValues.append(linkVars[i].get())

        root.destroy()
    
    with open(colourFile) as file:
        colours = file.readlines()
        for colour in range(len(colours)):
            colours[colour] = colours[colour].strip("\n")

    # Create tkinter window
    root = tk.Tk()
    root.configure(background=colours[0])

    title = tk.Label(root, text="Hello World!", padx=20, pady=20, background=colours[0], foreground=colours[4])
    title.grid(row=0, column=0)

    linkVars = []
    linkEntries = []

    for i in range(numFields):

        linkVars.append(tk.StringVar(master=root, value=""))

        linkEntries.append(tk.Entry(root, width=50, background=colours[1], textvariable=linkVars[i]))
        linkEntries[i].grid(row=i + 1)

    submitButton = tk.Button(root, text="Submit", width=42, bg=colours[2], command=submit)
    submitButton.grid(row=1 + numFields)

    tk.mainloop()

    return returnValues

if __name__ == "__main__":
    drawMainGUI("colours.txt")