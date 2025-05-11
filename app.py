import csv
import re

pattern = r'-\d{2}$'
specObj  = {}
# 打開 CSV 檔案（請將 'your_file.csv' 換成你的檔名）
with open('tires.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    for row_index, row in enumerate(reader):
        for col_index, cell in enumerate(row):
            cell = cell.strip()
            if(len(cell) > 2 and re.search(pattern, cell)):
                inch = cell[-2:]
                if inch not in specObj:
                    specObj[inch] = [cell]
                else:
                    specObj[inch].append(cell)

for key, val in specObj.items():
    print(val)
