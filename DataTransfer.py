import openpyxl as xl
# In Progress Currently
# Idea: Add parsing through all folder location and transferring automatically
print("File Location must be double \ not single")

path1 = input("Location: Original\n")
path2 = input("Location: Copy to\n")

wb1 = xl.load_workbook(filename=path1)
wb2 = xl.load_workbook(filename=path2)


ws1 = wb1.worksheets[0]
ws2 = wb2.create_sheet(ws1.title)

for row in ws1:
    for cell in row:
        ws2[cell.coordinate].value = cell.value

wb2.save(path2)



