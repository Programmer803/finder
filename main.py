# Error Code
Error = False

try:
    import bs4 
    import requests
    from print_color import print
    import sys
    
except:
    Error = True
    print("""
          First Download This libraries
          
          1) pip install beautifulsoup4
          
          2) pip install print_color
          
          Next run script
          """)
# Help - test

ht = """
Use: finder.py [OPTION] [URL] [...-l]
...-l : You should add this method at last part

-i : Choose info for target 'linux or for some "linux commands" '

-s : Choose site for target 'Site: google.com'

-t : Choose title 'Title: Book'

--file : Choose file type 'pdf'
"""

# Var
method = []

req = requests.request

args = sys.argv[1::]



def make_req(methods):
    
    final_req = ""
    
    for req in methods:
        
        final_req += req
        
    return final_req
        
    
class finder:
    
    def __init__(self):
		
        self.method = []
        self.req = ""
        self.all_url = []
        self.result = 0
        
        # Url for send req
        self.url = "https://www.google.com/search?q="
        

    def send_req(self):
		
        self.req = make_req(self.method)

        self.res = req("GET",self.url+self.req)
        
        soup = bs4.BeautifulSoup(self.res.text,"html.parser")
        
        print(f"""{self.url}{self.req}""" , tag = "Dork" , tag_color="yellow")
        
        print("Search for information" , tag = "Starting" , tag_color="red")
        
        data = soup.find_all({"div":"LC20lb MBeuO DKV0Md"})
        
        
        for s_data in data:
            
            try:
                
                data_ = s_data.find("a")["href"]  
                
                if not data_ in self.all_url:
                    self.show(data=data_)
                
            except:
                
                pass
        
        if self.result == 0:
            
            print("No Result" , tag = "404" , tag_color="yellow")
        
    
    def show(self,data):
        
        self.all_url.append(data)
        
        data = data.replace("/url?q=","")
        
        d = str(data).find("&")
        
        data = data[0:d]   
         
        if data[0:4] == "http" and not "https://www.google.com/search" in data and not "https://www.google.com/preferences" in data and not "https://support.google.com" in data:
            
            print(data,tag="+",tag_color="green",color="green")
            self.result+=1
            
   
            
# **************
Find = finder()         

def main ():
      
    if len(args) == 0 and Error == False:
        
        print(ht)
    
    elif Error == False and len(args) != 0:
        try:
            
            
            if "-s" in args:
                
                Find.method.append("site:"+(args[args.index("-s")+1])+" ")
                
            if "-i" in args:
                
                Find.method.append("intext:'"+(str(args[args.index("-i")+1]))+"' ")	
                
            if "-t" in args:
                
                Find.method.append("title:'"+(str(args[args.index("-t")+1]))+"' ")	
                
            if "--file" in args:
                
                Find.method.append("filetype:"+(str(args[args.index("--file")+1]))+" ")	
                
            Find.send_req()	
        
        except IndexError:
            
            print("Insert command",tag="Error" , tag_color="red" )
            
        except requests.exceptions.ConnectionError:
            
            print("Network Error",tag="Error" , tag_color="red" )
            
# Run 
main()
