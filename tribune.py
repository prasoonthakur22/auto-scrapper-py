import json#json is buit in module so we don't have to install it using pip
from pymongo import MongoClient
import cloudscraper
import spacy
from bs4 import BeautifulSoup
class Tribune:
 def __init__(self):
  print("hi")
  self.client=MongoClient('mongodb://localhost:27017')
#To get a reference to a specific database from a MongoClient object, 
#you can use the [] operator and pass the name of the database as a string. For example,
# if your MongoClient object is named client and you want to get a reference to a
# database called mydatabase, you can use:
#db = client['mydatabase']
#This will give you a Database object that you can use to interact with the database.
  self.db=self.client['matrimony']
  self.collection=self.db['collections']
  print(f"Connected to database '{self.db.name}' and collection '{self.collection.name}'")
  self.nlp=spacy.load("en_core_web_sm")
  self.scraper=cloudscraper.create_scraper(delay="10",browser="chrome")
  
 def data(self):
  content=self.scraper.get("https://www.tribuneindia.com/classified/groomswanted").text
  print(content)
  soup=BeautifulSoup(content,"html.parser")
  content=soup.find(class_="tab-pane active",id="groomsWanted")
  
  print("contents:find")
  contents=content.findAll(class_="card-text")
  matrimonials=[]
  for div in contents:
   text = div.get_text('\n')#get_text() returns the text content of all the elements in the specified class. and leaves out the tags such as <br> etc
    # by default, the get_text() method of BeautifulSoup replaces all HTML line breaks with a newline character \class_="tab-pane acclass_="tab-pane active",id="groomsWanted"tive",id="groomsWanted"n. So, you don't need to add any
    # additional characters to your code to replace the <br> tags.
   doc=self.nlp(text)
   matrimonial={}
   for token in doc:
    text=token.text#because everything stored in doc is a span object
  # print(f'id:{text}')
    if text.startswith("CL"):
     matrimonial['id']=text
    else:
     matrimonial['description']=str(doc)
  
   matrimonials.append(matrimonial)
  matrimonials_json = json.dumps(matrimonials)
  #self.collection.insert_many(json.loads(matrimonials_json))
  return print("done")
#tribune=Tribune()
#Tribune.data(tribune)
#print(matrimonials)




