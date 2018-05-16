import os, shutil, glob
import subprocess
from html.parser import HTMLParser
from bs4 import BeautifulSoup


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
    path_to_html = "html/"
    data = ''''''
 
    soup = BeautifulSoup(data)
    for tr in soup.find_all('tr'):
        for td in tr.find_all('td'):
            print(td.get_text())




move_attachments()
run_bash_command()
remove_files()
move_raw_to_new_dest()
html_conversion()


