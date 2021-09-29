from datetime import date
import random

x = random.randint(0,10)
print(x)


dinner = {
    "cuisine": "Indian",
    "name": "Chickencurry",
    "side-dish": ["naan", "salad", "yoghurt"], #x=1
    "spicy": False,
    "totalpax": 2
}

print (dinner["side-dish"][0])    #print (myfood["side-dish[x]"]) 

#need to ask how can I only print one side dish like in array
#did we learn conversion from one data type to another?

myassignment = {
    "class": "Hello-world",
    "assignment name": "Object as data-type",
    "due date": "09-22",
    "current-date": date.today(),
    #import datetime
    #x = datetime.datetime.now(2021,9,22),  
    #putting dates 
    "online submission": True,
    "difficulty-level": ["1", "2", "3"]

}

print (myassignment["current-date"])


shoppingbag = {
    "store name": "Target",
    "location": "Newport",
    "Payment-method": ["cash","atm card","apple pay"],
    "items bought": 6,
    "Experience": "Great",
    "will you go again": True,


}
x = 1
print (shoppingbag["Payment-method [x]"])


portfolio = {
    "Portfolio": "Graphic and UI/UX Design",
    "Total projects": 6,
    "Case-study": "Kumbharwada-Thesis",
    "Portfolio Type": ["website", "PDF"],
    "Published In": 2019,
    "Personal Portfolio":  True,

}

print (portfolio ["Published In"])
