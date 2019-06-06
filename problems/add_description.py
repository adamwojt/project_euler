import requests
import time
from bs4 import BeautifulSoup
import os
import sys    

def add(filename): # looks for number in .py file name and scrapes description from web for given problem number.
    if filename.endswith(".py") and filename.startswith('euler'): 
        with open(filename,'r') as f:lines = f.readlines()
        try:
            if lines[0]=='#_______Description_____\n':print("Description already exsists for:",filename)
            else:
                problem_number=filename.replace('.py','').replace('euler','')
                if problem_number.isdigit():
                    url = 'https://projecteuler.net/problem=%s'%(problem_number)
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    problem_text=soup.find("div", {"class": "problem_content"}).text
                    comments=problem_text.replace('\n','\n#')
                    with open(filename,'w') as newfile:
                        newfile.write('#_______Description_____\n'+"\n#"+url+comments+'#_______end_description_____:\n\n')
                        newfile.write(''.join(lines))
                    print('Description added to:',filename)
                    time.sleep(1) #antispam
                else:
                    print("No problem number for:",filename)
        except IndexError:
            print("File is empty",filename)
    else:
        print('Filename not in euler problem format',filename,"pass")
    
def add_single(): #for single use   
    filename =  os.path.basename(sys.argv[0])
    add(filename)
        
def add_loop_dir(): #loop directory
    for filename in os.listdir('./'):
        add(filename)

def delete(filename): #this was created just for testing, deletes descriptions from files.
    if filename.endswith(".py") and filename.startswith('euler'): 
            with open(filename,'r') as f:lines = f.readlines()
            try:
                if lines[0]=='#_______Description_____\n':
                    print("Description exsists for:",filename,"deleting...")
                    endline=0
                    for i in lines:
                        if 'end_description' in i:endline=lines.index(i);break
                    with open(filename,'w') as newfile:
                        n=0
                        for i in lines:
                            if n>endline:
                                newfile.write(i)
                            n+=1
                else:
                    print("No description in:",filename)
            except IndexError:
                print("File is empty:",filename)
 
def delete_loop_dir(): #as above
    for filename in os.listdir('./'):
        delete(filename)
       
def delete_single(): #as above
    filename =  os.path.basename(sys.argv[0])
    delete(filename)

