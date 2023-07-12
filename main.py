import bs4 
import requests
req = requests.request
from print_color import print

class finder:
    
    def __init__(self):
        self.method = ["intext:","inurl:"]
        self.all_url = []
        
        # Url for send req
        self.url = "https://www.google.com/search?q='"
        
    def send_req(self , detail):
        
        self.res = req("GET",self.url+self.method[0]+detail+"'")
        soup = bs4.BeautifulSoup(self.res.text,"html.parser")
        data = soup.find_all({"div":"LC20lb MBeuO DKV0Md"})
        
        for s_data in data:
            
            try:
                data_ = s_data.find("a")["href"]  
                if not data_ in self.all_url:
                    self.show(data=data_)
                
            except:
                
                pass
    
    def show(self,data):
        self.all_url.append(data)
        data = data.replace("/url?q=","")
        d = str(data).find("&")
        
        
        
        data = data[0:d]   
         
        if data[0:4] == "http" and not "https://www.google.com/search" in data and not "https://www.google.com/preferences" in data and not "https://support.google.com" in data:
            
            print(data,tag="+",tag_color="green",color="green")
            
        
    
        


while True:
    
    f = finder()
    i =  input(": ")
    f.send_req(i)
        
        