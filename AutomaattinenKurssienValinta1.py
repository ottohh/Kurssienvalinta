# -*- coding: utf-8 -*-
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



#Avaa kaikki jakso tarjottimet
def AvaaJaksoTarjottimet():
    
    driver.execute_script("""
    
    var i=0;
    Jaksot = document.querySelectorAll(".list-group-item a");
    
    for(i=0;i<5;i++)
    {
    Jaksot[i].click()
    
    }
    
    """)
    
    time.sleep(1)
    return
def ValitseAine(Aine):

    Element = driver.find_element_by_partial_link_text(Aine)

    Element.click()
    driver.execute_script("arguments[0].scrollIntoView();", Element)
    time.sleep(1)
    if(Element.get_attribute("class")=="ksuor-on"):return True
    return False
    


Aineet = [
#1 jakson aineet
"KE04.1"
,
#2 jakson aineet
"FI04.1"
,
#3 jakson aineet
"YH02.2"
,
"ÄI04.2"
#4 jakson aineet

,
#5 jakson aineet
"KE02.2"
]

#Käyttäjä tunnukset
Username = ""
Password = ""
driver = webdriver.Chrome("C:\\Users\\ottop\\Downloads\\chromedriver_win32\\chromedriver.exe")

def main():

    #synkronoidaan serverin kellon kanssa
    response = requests.get("https://ayl.inschool.fi/")
    hours, minutes, seconds = response.headers["date"].split(" ")[4].split(":")
    opening_hour = 13
    print(response.headers["date"].split(" ")[4])
    time_left=opening_hour-int(hours)
    time_left*=60
    print(time_left);
    time_left=time_left-int(minutes)
    time_left*=60
    print(time_left);
    time_left=time_left-int(seconds)
    print(time_left)



    driver.get("https://ayl.inschool.fi/")
    # time

    #Kirjautuminen palveluun ja navigointi jakso paneeliin
    driver.find_element_by_name("Login").send_keys(Username)
    driver.find_element_by_name("Password").send_keys(Password)
    driver.find_element_by_name("submit").send_keys(Keys.ENTER)
    driver.get("https://ayl.inschool.fi/selection/view")




    #odota kunnes valinta tarjotin avautuu
    time.sleep(time_left-3)
    time.sleep(1)

    Valitsemattajääneet = [1]
    while(True):


        if(Valitsemattajääneet[0]!=1):
            Aineet=Valitsemattajääneet


        print(Aineet)
        print(Valitsemattajääneet)

        driver.refresh()
        AvaaJaksoTarjottimet()

        Valitsemattajääneet=[]
        for Aine in Aineet:

            print("Valitaan Aine  "+Aine)
            Valittu = ValitseAine(Aine)
            print(Valittu)
            if(Valittu==False):Valitsemattajääneet.append(Aine)


        # sleep(time_left-3);
        time.sleep(1)
        input()

if __name__=="__main__":
    main()




    
    
    
  






