

def dependencies():
    try: 
        os.system("pip install pywhatkit")
    except:
        print("Try downloading pip manually then pywhatkit.")
    try:
        os.system("pip install pyfiglet")

    except:
        print("Try manually downloading pip and pyfiglet.")

dependencies()
import os
import pywhatkit as wh
import requests
import re
def get():
    file=open('site.html','w+')
    url = " https://armyareapune.kvs.ac.in/school-announcement"
    res = requests.get(url)

    if res.status_code == 200:
        try:
            
            file.write(res.text)
            print("Site info successfully downloaded.\nFetching the assignments for you.......")
        except:
            print("Error in get request, try again later.")


def scrape_title():
    file=open('site.html',"r+")
    buffer=open('buffer.txt','w+')
    k=file.readlines()
    try:    
        for i in range(0,len(k)):
        
            eleminate=['''<th class="views-field views-field-title" scope="col">
            Title          </th>''','''<th class="views-field views-field-field-date" scope="col">
            Publish Date          </th>''']
            if( ("views-field views-field-title" in k[i])and ( k[i+1] not in eleminate)):
                buffer.write("Announcement"+k[i+1])
                
            if (("views-field views-field-field-date" in k[i])and(k[i+1] not in eleminate)):
                buffer.write("Date" +k[i+1])
        print("Data succesfully extracted/scrapped and stored in buffer.\nCleaning data....... ")
    except:
        print("Error in scraping/ fetching the data from the site.")

def get_date(s):
    val=re.split('">',re.split("</span>",s)[0])[1]
    
    return((val))


def get_ann(s):
    val=re.split('Announcement',re.split("</td>",s)[0])[1]
    return (val)
def cleaning():
    buffer=open('buffer.txt',"r+")
    clean=open('clean_buffer.txt','w+')
    l=buffer.readlines()
    for i in range(2,len(l)):
        if ("Date" in l[i]):
            #print(l[i])
            clean.write(get_date(l[i])+"\n")
        if (("Announcement"in l[i])and("CLASS XI ADMISSION_FORM_SUBMISSION_SCHEDULE_2022_23" not in l[i])):
            clean.write(get_ann(l[i])+"\n")



#Automating the messages on whatsapp.

def whatsapp():
    file=open("clean_buffer.txt","r")
    a=file.readlines()
    
    text=""

    for i in range(0,len(a)):
        text+=a[i]
     
       

        
    wh.sendwhatmsg_to_group_instantly("EJGvYbQsBWTFgG2fJLj5Z7",f"Good morning students and parents.\nFollowing are the school related announcements\n{text}")






while True:
    from datetime import datetime

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if(0==0):
    #if (str(current_time)=="21:54:00"):
        dependencies()
        try:
            get()
        except:
            print("Error in geting the website details")

        try:
            scrape_title()
        except:
            print("Error in scraping the data from the site.")
        try:
            cleaning()
        except:
            print("Error in cleaning the raw data.")
        
        whatsapp()

         #   print("Error in whatsappbot, try agan later")
          #  break





