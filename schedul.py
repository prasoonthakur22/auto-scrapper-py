import schedule #don't keep name of file same as package u import
import time as tm
from datetime import time,datetime
from queue import Queue
q=Queue() #creates an object of the Queue class that was defined in the queue.py file. 
#The Queue class provides methods like put() and get() for adding and removing items from a queue. 
#The q object can be used to call these methods to add and remove items from the queue.
#import pytz
from tribune import Tribune
current_time=datetime.now()#this is to check if scheduler is working fine
print(current_time)
#timezone = pytz.timezone('Asia/Kolkata')
q=Queue()#here we created an object of the Queue class in queue.py file
#@repeat(every().day.at("10:00"))
print("hi1")
def add_to_queue():
    #we imported it here due to this
 #AttributeError: partially initialized module 'schedule' has no attribute 'every' (most likely due to a circular import)
 tribune=Tribune()
 q.put(tribune.data)#When you call q.put(tribune.data) {which is a reference to the data method of the tribune class}
# in schedule.py, it adds it to the
    #Queue object q. This value is passed as the item parameter to the put method of the Queue class, 
    #and the method adds it to the q object's queue using the put method of the queue module.
 print("I am standing in a queue")
 print (f"size of the queue is {q.qsize()}")
#schedule.every().second: this means every second note that second is singular
#schedule.every(5).seconds.do(job)#its basicallly english lang like schedule every 5 sec to do smt.we just 
#pass the job and don't do anythhing
#schedule.every().day.at("10:30").do(job)
print(type(q))
def process_queue():
 while not q.empty():
  item=q.get()#we'll process the item here
  item()
  print("I did all the work u asked me to do!")
  print (f"Right now i processed {item} and my size is {q.qsize()}")
schedule.every().day.at("18:41").do(add_to_queue)
#In Python, parentheses are used to call a function. When you pass a function as a parameter to another function, 
#you do not use parentheses, because you do not want to call the function at that point in time.
#If we had written add_to_queue() with parentheses, this would have called the function immediately and passed its 
#return value as a parameter to schedule.every().day.at("10:00").do(), which is not what we want.
while True:
    schedule.run_pending()#we'll do this to apply the schedule
    process_queue()
    tm.sleep(1)

