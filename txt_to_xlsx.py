import openpyxl as op
from tkinter import Tk, filedialog
import os


#Extract Folder path from the dialog box
def folder_path(title="Enter the file path"):
    root = Tk()             # pointing root to Tk() to use it as Tk() in program.
    root.withdraw()         # Hides small tkinter window.
    root.title()
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    # root.attributes()
    open_file = filedialog.askdirectory(title = title) #,filetypes = (("Excel files", ".xlsx .xls"),))   # Returns opened path as str
    return open_file

#Extract selected file path from the dialog box
def file_path(title="Enter the file path",filetype=("Excel files", ["*.xlsx", "*.xls"])):
    root = Tk()             # pointing root to Tk() to use it as Tk() in program.
    root.withdraw()         # Hides small tkinter window.
    root.title()
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    # root.attributes()
    open_file = filedialog.askopenfilename(title = title,filetypes = ((filetype[0], filetype[1][0]), (filetype[0], filetype[1][1])))   # Returns opened path as str
    return open_file


folder_path = folder_path()




os.chdir(folder_path)


for file in os.listdir(folder_path):
    # if file.endswith('.txt'):
    if file == "PROP.TXT":
        input_file = file
        output_file = f'{file}.xlsx'

        wb = op.Workbook()
        ws = wb.worksheets[0]



        file = open(input_file)

        line = file.readline()
        for i in range(50):

        # while line:
            list = line.split()  # convert

            for j in range(1, len(list) + 1):
                ws.cell(row = i +1 , column = j).value = list[j-1]
            line = file.readline();  # read text

        wb.save(output_file)
        print(file)
        break
    else:
        print('No txt file found')






