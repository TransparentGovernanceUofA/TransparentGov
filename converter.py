import os, shutil, glob
import subprocess
import re
import json
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from itertools import product
from pprint import pprint

class json_data(object):
    
    def __init__(self):
        
        self.json = dict()
        self.table = []
    
    def table_to_2d(self, table_tag):
        rowspans = []  # track pending rowspans
        rows = table_tag.find_all('tr')
        
        # first scan, see how many columns we need
        colcount = 0
        for r, row in enumerate(rows):
            cells = row.find_all(['td', 'th'], recursive=False)
            colcount = max(
                           colcount,
                           sum(int(c.get('colspan', 1)) or 1 for c in cells[:-1]) + len(cells[-1:]) + len(rowspans))
                           # update rowspan bookkeeping; 0 is a span to the bottom.
                           rowspans += [int(c.get('rowspan', 1)) or len(rows) - r for c in cells]
                           rowspans = [s - 1 for s in rowspans if s > 1]
        
        # build an empty matrix for all possible cells
        self.table = [[None] * colcount for row in rows]
        
        # fill matrix from row data
        rowspans = {}  # track pending rowspans, column number mapping to count
        for row, row_elem in enumerate(rows):
            span_offset = 0  # how many columns are skipped due to row and colspans
            for col, cell in enumerate(row_elem.find_all(['td', 'th'], recursive=False)):
                # adjust for preceding row and colspans
                col += span_offset
                while rowspans.get(col, 0):
                    span_offset += 1
                    col += 1
                
                # fill table data
                rowspan = rowspans[col] = int(cell.get('rowspan', 1)) or len(rows) - row
                colspan = int(cell.get('colspan', 1)) or colcount - col
                # next column is offset by the colspan
                span_offset += colspan - 1
                value = cell.get_text()
                for drow, dcol in product(range(rowspan), range(colspan)):
                    try:
                        self.table[row + drow][col + dcol] = value
                    except IndexError:
                        # rowspan or colspan outside the confines of the table
                        pass
            
            # update rowspan bookkeeping
                               rowspans = {c: s - 1 for c, s in rowspans.items() if s > 1}
                           
    return self.table

def html_conversion(self):
    path_to_html = "html/*"
        html_files = glob.glob(path_to_html)
        for file in html_files:
            print(file)
            page = open(file)
            
            soup = BeautifulSoup(page.read())
            
            firsttable = soup.findAll('table')[0]
            secondtable = soup.findAll('table')[1]
            
            
            for row in firsttable.find_all("tr"):
                
                col = row.find_all("td")
                label = col[0].get_text().strip()
                content = col[1].get_text().strip()
                
                label = label.replace("\t"," ")
                label = re.sub(r'[\ \n]{2,}', r' ', label.strip())
                
                content = content.replace("\t"," ")
                content = re.sub(r'[\ \n]{2,}', r' ', content.strip())
                
                self.json.update({label:content})
        
            for row in secondtable.find_all("tr"):
                
                col = row.find_all("td")
                label = col[0].get_text().strip()
                content = col[1].get_text().strip()
                
                label = label.replace("\t"," ")
                label = re.sub(r'[\ \n]{2,}', r' ', label.strip())
                
                content = content.replace("\t"," ")
                content = re.sub(r'[\ \n]{2,}', r' ', content.strip())
                
                self.json.update({label:content})
            print(self.json)
    
        return self.json




def move_attachments():
    att_dir = "attachment/"
    os.makedirs(os.path.dirname(att_dir), exist_ok=True)
    
    everything = glob.glob('*')
    for file in everything:
        if ".py" in file:
            continue
        elif "Agenda" in file:
            continue
        elif "approved-Minutes" in file:
            continue
        elif 'Item' in file:
            continue
        else:
            shutil.move(file, att_dir)




def run_bash_command():
    bashCommand = "/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to txt:Text *.docx"
    output = subprocess.check_output(['bash','-c', bashCommand])
    
    bashCommand_2 = "/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to txt:Text *.doc"
    output = subprocess.check_output(['bash','-c', bashCommand_2])
    
    bashCommand_3 = "/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to html *.docx"
    output = subprocess.check_output(['bash','-c', bashCommand_3])
    
    bashCommand_4 = "/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to html *.doc"
    output = subprocess.check_output(['bash','-c', bashCommand_4])



def move_raw_to_new_dest():
    txt_files = glob.glob('*.txt')
    html_files = glob.glob('*.html')
    txt_dir = "text/"
    html_dir = "html/"
    os.makedirs(os.path.dirname(txt_dir), exist_ok=True)
    os.makedirs(os.path.dirname(html_dir), exist_ok=True)
    
    for txt in txt_files:
        shutil.move(txt, txt_dir)
    
    for html in html_files:
        shutil.move(html, html_dir)


def remove_files():
    png_files = glob.glob('*.png')
    gif_files = glob.glob('*.gif')
    jpg_files = glob.glob('*.jpg')
    
    for png in png_files:
        os.remove(png)
    
    for gif in gif_files:
        os.remove(gif)
    
    for jpg in jpg_files:
        os.remove(jpg)



def html_conversion():
    path_to_html = "html/*"
    html_files = glob.glob(path_to_html)
    
    for file in html_files:
        json_dict = {}
        print(file)
        page = open(file)
        
        soup = BeautifulSoup(page.read())
        
        firsttable = soup.findAll('table')[0]
        secondtable = soup.findAll('table')[1]
        thirdtable = soup.findAll('table')[2]
        
        firsttable_content = handle_table(firsttable, json_dict)
        secondtable_content = handle_table(secondtable, firsttable_content)
        thirdtable_content = handle_thirdtable(thirdtable, secondtable_content)
        
        #print(thirdtable_content)
        
        json_filename = "JSON/" + file + '.txt'
        os.makedirs(os.path.dirname(json_filename), exist_ok=True)
        with open(json_filename, "w") as o_file:
            json.dump(thirdtable_content, o_file, indent=4, ensure_ascii=False)



def handle_table(table, table_dict):
    for row in table.find_all("tr"):
        
        col = row.find_all("td")
        label = col[0].get_text().strip()
        content = col[1].get_text().strip()
        
        label = label.replace("\t"," ")
        label = re.sub(r'[\ \n]{2,}', r' ', label.strip())
        
        content = content.replace("\t"," ")
        content = re.sub(r'[\ \n]{2,}', r' ', content.strip())
        
        table_dict.update({label:content})
    
    return table_dict

def handle_thirdtable(table, table_dict):
    first_row = table.find_all("tr")[0]
    second_col = first_row.find_all("td")[1]
    
    informed_label = second_col.find_all("p")[0].get_text().strip()
    informed_label = informed_label.replace("\t"," ")
    informed_label = re.sub(r'[\ \n]{2,}', r' ', informed_label.strip())
    try:
        informed_content = second_col.find_all("ul")[0].get_text().strip()
        informed_content = informed_content.replace("\t"," ")
        informed_content = re.sub(r'[\ \n]{2,}', r' ', informed_content.strip())
    
    except:
        informed_content = "N/A"
    
    table_dict.update({informed_label:informed_content})

for row in table.find_all("tr")[1:3]:
    for col in row.find_all("td"):
        label = col.find_all("p")[0].get_text().strip()
            content = col.find_all("ul")[0].get_text().strip()
            
            label = label.replace("\t"," ")
            label = re.sub(r'[\ \n]{2,}', r' ', label.strip())
            
            content = content.replace("\t"," ")
            content = re.sub(r'[\ \n]{2,}', r' ', content.strip())
            
            table_dict.update({label:content})


for row in table.find_all("tr")[4:]:
    col = row.find_all("td")
        label = col[0].get_text().strip()
        content = col[1].get_text().strip()
        
        label = label.replace("\t"," ")
        label = re.sub(r'[\ \n]{2,}', r' ', label.strip())
        
        content = content.replace("\t"," ")
        content = re.sub(r'[\ \n]{2,}', r' ', content.strip())
        
        table_dict.update({label:content})
    
    return table_dict



def get_motion():
    
    path_to_text = "agenda/*"
    text_file = glob.glob(path_to_text)
    with open(text_file) as infile:
        content = infile.readlines()
        
        for line in content:
            if line.startwith("Agenda Title"):
                title_start = "Agenda Title"
                title_end = "Motion"
                block_of_lines(cotent, title_start, title_end)
            
            if line.startwith("Motion"):
                motion_start = "Motion"
                motion_start = "Item"
                block_of_lines(cotent, motion_start, motion_start)


def block_of_lines(content, start, end):
    block = ""
    found = False
    
    for line in content:
        line = line.rstrip()
        #print(line)
        if found:
            
            if line.startswith(end): break
            else:
                block += line + ' '
        # print("DAH", block)
        else:
            if line.startswith(start):
                found = True
                block = line.replace(start, '') + ' '

return block









# move_attachments()
# run_bash_command()
# remove_files()
# move_raw_to_new_dest()
#text_conversion()

#thirdtable()
html_conversion()

# j = json_data()
# j.html_conversion()




