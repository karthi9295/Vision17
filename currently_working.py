#import os
#def get_size(start_path = 'C:/Users/31696/Desktop/download'):
#    total_size = 0
#    for dirpath, dirnames, filenames in os.walk(start_path):
#        for f in filenames:
#            fp = os.path.join(dirpath, f)
#            total_size += os.path.getsize(fp)
#    return total_size
#
#if(get_size()>0):
#    print "value"
import sys
sys.path.append("C:\\Python27\\Lib\\site-packages")
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from bs4 import BeautifulSoup
import urllib2
import time,re
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import pandas as pd
import os.path
import csv
import argparse

class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
  

           def strcleaner(fullData):
               text = fullData.replace(" ",".")
               return text.strip()
           def strCleaner(fullData):
               text = fullData.replace("nan","") 
               return text.strip()
           def StrCleaner(fullData):
               text=fullData.replace("'"," ").replace(","," ").replace("\n"," ")  
               return text
           def listToString(listData):
               return ' '.join(str(e) for e in listData)

           def listToString1(listData):
               return ''.join(str(e) for e in listData)
           browser = webdriver.Chrome("extraction/chromedriver_win32/chromedriver.exe")
           #actions= webdriver.ActionChains(browser)
           ap = argparse.ArgumentParser()
           ap.add_argument("--url", required = True,help = "Path to the url")
           args = vars(ap.parse_args())
           #url="https://www.tripadvisor.in/Hotel_Review-g304554-d304632-Reviews-Vivanta_by_Taj_President_Mumbai-Mumbai_Bombay_Maharashtra.html"
           page=urllib2.urlopen(args["url"])
           browser.get(args["url"])
           #print type(page)
           soup=BeautifulSoup(page,"lxml")
           file_path="extraction/attributes/review.csv"
           extracted_data= pd.read_csv(file_path,na_values=['nan'], keep_default_na=False)
           extracted_data.columns = extracted_data.columns.str.strip()
           tagname= extracted_data.tagname
           classname=extracted_data.classname
           classname1=classname[0]
           classname1=' '.join(classname1.split())
           classname2=classname[1]
           classname2=' '.join(classname2.split())
           classname3=classname[2]
           classname3=' '.join(classname3.split())
           classname4=classname[3]
           classname4=' '.join(classname4.split())
           classname5=classname[4]
           classname4=' '.join(classname4.split())
           tagname1=tagname[0].lower()
           tagname2=tagname[1].lower()
           tagname3=tagname[2].lower()
           tagname4=tagname[3].lower()
           tagname5=tagname[4].lower()
          
           with open('extraction/output/data_review.csv', 'wb') as csvfile:
            w=csv.writer(csvfile)   
            fifth_parent = soup.find_all(tagname5,{"class":classname5})
            for m in fifth_parent:
              
                         fourth_parent = m.find_all(tagname4,{"class":classname4})
                         for l in fourth_parent:
                             Third_parent=l.find_all(tagname3,{"class":classname3})
                             #print tagname3,classname3
                             for n in Third_parent:
                                 #print n.text
                                 second_parent=n.find_all(tagname2,{"class":classname2})
                                 for j in second_parent:
                                     Parent_value=j.find_all(tagname1,{"class":classname1})
                                     for k in Parent_value:
                                      w.writerow([(k.text).encode("utf-8")])
#                                         value=StrCleaner(filter(None,(k.text)))
#                                         print value.encode('utf8')
            while True:
             try:  
              if(browser.find_element_by_partial_link_text("Next")):
#               if(browser.find_element_by_partial_link_text("Next")):
#                     currenturl=(browser.current_url)
#                     browser.get(currenturl) 
               def find(browser): 
                     var = browser.find_element_by_partial_link_text("Next")
                     if var:
                         return var
                     else:
                         return False
               var = WebDriverWait(browser,100).until(find)
               var.click()#currenturl=(browser.current_url)
               currenturl=(browser.current_url)
               browser.get(currenturl) 
               page=urllib2.urlopen(currenturl)
               soup=BeautifulSoup(page,"lxml")
               fifth_parent = soup.find_all(tagname5,{"class":classname5})
               for m in fifth_parent:
                         fourth_parent = m.find_all(tagname4,{"class":classname4})
                         for l in fourth_parent:
                             Third_parent=l.find_all(tagname3,{"class":classname3})
                             for i in Third_parent:
                                 second_parent=i.find_all(tagname2,{"class":classname2})
                                 for j in second_parent:
                                     Parent_value=j.find_all(tagname1,{"class":classname1})
                                     for k in Parent_value:
                                         w.writerow([(k.text).encode("utf-8")])
             except:                            
              if(os.path.exists("extraction/attributes/page.csv")):
                 file_path="extraction/attributes/page.csv"
                 extracted_data= pd.read_csv(file_path,na_values=['nan'], keep_default_na=False)
                 extracted_data.columns = extracted_data.columns.str.strip()
                 pagination_tag= extracted_data.tagname
                 pagination_class=extracted_data.classname
                 if (pagination_class[0]):
                     pagination_element=pagination_tag[0].lower()+"."+strcleaner(str(pagination_class[0].rstrip()))
                 else :
                     pagination_element=pagination_tag[1].lower()+"."+strcleaner(str(pagination_class[1].rstrip()))
                 #print pagination_element    
                 if(browser.find_element_by_css_selector(pagination_element)):
                     currenturl=(browser.current_url)
                     browser.get(currenturl) 
                 def find(browser): 
                     #print pagination_element
                     var = browser.find_element_by_css_selector(pagination_element)
                     if var:
                         return var
                     else:
                         return False
                 var = WebDriverWait(browser,100).until(find)
                 var.click()
                 currenturl=(browser.current_url)
                 browser.get(currenturl) #currenturl=(browser.current_url)
                 page=urllib2.urlopen(currenturl)
                 soup=BeautifulSoup(page,"lxml")
                 fifth_parent = soup.find_all(tagname5,{"class":classname5})
                 for m in fifth_parent:
                         fourth_parent = m.find_all(tagname4,{"class":classname4})
                         for l in fourth_parent:
                             Third_parent=l.find_all(tagname3,{"class":classname3})
                             for i in Third_parent:
                                 second_parent=i.find_all(tagname2,{"class":classname2})
                                 for j in second_parent:
                                     Parent_value=j.find_all(tagname1,{"class":classname1})
                                     for k in Parent_value:
                                         w.writerow([(k.text).encode("utf-8")])
           
                
                
     
     
     
     


observer = Observer()
event_handler = ExampleHandler() # create event handler
# set observer to use created handler in directory
observer.schedule(event_handler, path='extraction/attributes')
observer.start()


# sleep until keyboard interrupt, then stop + rejoin the observer
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()
    folder = 'extraction/attributes'
    for the_file in os.listdir(folder):
     file_path = os.path.join(folder, the_file)
     os.unlink(file_path)


observer.join()

