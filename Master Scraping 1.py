import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame


A=[]
B=[]
C=[]

for page in range(1,11):
    
    result = requests.get("https://www.admitkard.com/blog/page/"+str(page)+"/")
    src=result.content
    
    soup=BeautifulSoup(src,'lxml')
    
    Blog_title=soup.find_all('h3',attrs= "ui--content-box-title-text blue-text text-left")
    
    Blog_Date=soup.find_all('span',attrs= "floatL")
    
    Main_Image=soup.find_all('div',attrs= "ui--content-box-image-default")
    
    B1=[]
    
    for Blog_title in Blog_title:
       A.append(Blog_title.text)
       
    for Blog_Date in Blog_Date:
       B.append(Blog_Date.text)
       
    for i in B:
        B1.append(i.split('|')[1])
        
    for a in Main_Image:
        image_tag = a.findChildren("img")
        C.append(image_tag[0]["data-lazy-src"])
        
    df1 = DataFrame(A,columns=['Blog Title'])
    df2 = DataFrame(B1,columns=['Blog Date'])
    df4 = DataFrame(C,columns=['Main Image'])
    
        
    df3=pd.concat([df4, df1, df2], axis=1)
    
df3.to_excel("outputscraping1.xlsx")
    





 
