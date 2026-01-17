import tkinter as tk

returnValues = []
numFields = 2

# Draws main GUI for class submission page
# returns string
def drawMainGUI(colourFile):

    # Callback function to extract text from entry boxes and close tk window
    def submit():
        global returnValues
        for i in range(numFields):
            returnValues.append(linkVars[i].get())

        root.destroy()
    
    colours = extractColours(colourFile)

    # Create tkinter window
    root = tk.Tk()
    root.configure(background=colours[0])

    # Create label to be title for window
    title = tk.Label(root, text="Enter a classname in the format 'ENGEN101-24A'", padx=20, pady=20, background=colours[0], foreground=colours[4])
    title.grid(row=0, column=0)

    linkVars = []
    linkEntries = []

    # Create variable number of text entry boxes
    for i in range(numFields):

        linkVars.append(tk.StringVar(master=root, value=""))

        linkEntries.append(tk.Entry(root, width=50, background=colours[1], textvariable=linkVars[i]))
        linkEntries[i].grid(row=i + 1)

    # Create button to submit classnames and close window
    submitButton = tk.Button(root, text="Submit", width=42, bg=colours[2], command=submit)
    submitButton.grid(row=1 + numFields)

    tk.mainloop()

    return returnValues

# Takes file of colour codes and extracts into a list
def extractColours(colourFile):

    # Extract list of colours from passed file for drawing gui
    with open(colourFile) as file:
        colours = file.readlines()
        for colour in range(len(colours)):
            colours[colour] = colours[colour].strip("\n")

    return colours

# Takes html of assessment table from course outline and puts it in a tkinter window
def drawAssessmentTable(colourFile, htmls):

    colours = extractColours(colourFile)

    # create tkinter window
    root = tk.Tk()
    root.configure(background=colours[0])

    column = 0

    for item in htmls:

        frame = tk.Frame(root, bg=colours[0])
        frame.grid(row=1, column=column)

        html = item
        print(type(html))

        # turn html into a single string with indentation removed
        for i in range(len(html)):
            html[i] = html[i].strip()
        html = "".join(html)

        row = -1
        subColumn = 0
        foundEntry = False
        entryStarted = False
        entryString = ""
        subtags = 0
        colspan = 1
        
        # iterate through every character in html
        for i in range(len(html)):

            # if <td> or <th> tag has been opened but not closed
            if foundEntry and not entryStarted:

                # check for colspan parameter
                if html[i:i+8] == "colspan=":
                    colspan = int(html[i+10])

                # check for closing of tag
                if html[i] == ">":
                    entryStarted = True
                    continue

            # if in text portion of entry
            if entryStarted:

                # check for closing tag
                if html[i:i+4] == "</td" or html[i:i+4] == "</th":

                    # populate table with entry
                    entryLabel = tk.Label(frame, text=entryString, bg=colours[0])
                    entryLabel.grid(row=row, column=subColumn, columnspan=colspan)
                    subColumn += colspan
                    colspan = 1

                    # reset variables
                    entryString = ""
                    foundEntry = False
                    entryStarted = False

                    continue
                
                # if tag opened inside of text section (for example, <em>) TODO: sense and bold/italicise appropriately
                if html[i] == "<":
                    subtags += 1

                # if tag inside of text section closed
                if html[i] == ">":
                    subtags -= 1
                    continue

                # add character to text string unless inside of extra tag
                if subtags == 0:
                    entryString = entryString + html[i]

            # if new table row is created
            if html[i:i+3] == "<tr":
                subColumn = 0
                row += 1

            # if new data intry is found
            if html[i:i+3] == "<td" or html[i:i+3] == "<th":
                foundEntry = True
        
        column += 1


    tk.mainloop()

if __name__ == "__main__":
    from webScraping import getHTML
    from htmlParsing import getAssessmentTable
    
    # Pass default value of ENGEN101-24A for testing purposes
    html = getHTML("https://uow-func-net-currmngmt-offmngmt-aue-prod.azurewebsites.net/api/outline/view/ENGEN101-24A%20%28HAM%29")
    table = getAssessmentTable(html)

    drawAssessmentTable("colours.txt", [table])