print("===Spam Messages Data Anaylizer===")
print("1. Add Message")
print("2. View All Messages")
print("3. Analyze Messages")
print("4. Search Message")
print("5. Exit")
import json
def add_messages():
    messages = [
    {
        "text": "You won a free prize!",
        "label": "Spam"
    },
    {
        "text": "Hello, how are you?",
        "label": "Not Spam"
    },
    {
        "text": "You got 100000 rupees click on link to collect",
        "label": "Spam"
    },
    {
        "text": "Plz bring my notebook to school",
        "label": "Not Spam"

    },
    {
        "text": "I will meet you tomorrow",
        "label": "Not spam"
    },
    {
        "text": "Congragulation! Claim your gift free",
        "label": "Spam"
    }
    ]
    return messages
data = add_messages()
with open("add_messages.json", "w") as file:
    json.dump(data,file,indent=4)
print ("file successfully saved")

def view_all_messages():
    with open("add_messages.json","r") as f:
     messages = json.load(f)
     for message in messages:
        print("Messages: ", message["text"])
        print("Label: ", message["label"])
        print("successfully opened")
def Anaylize_messages():
 
   with open ("add_messages.json","r") as file:
      messages = json.load(file)
      spam_count = 0
      not_spam_count = 0
      for message in messages:
         if message["label"]== "Spam":
             spam_count +=1
         elif message["label"] =="Not Spam":
            not_spam_count +=1
            print("Total Messages: ",len(messages))
            print("Spam Messages: ",spam_count)
            print("Not Spam Messages: ",not_spam_count)
    
def search_message():

       new_message = input("Enter your text : ")
       with open("add_messages.json","r") as file:
        messages = json.load(file)
        for message in messages:     
          if new_message.lower() in message["text"].lower():
              print(message["label"])
      
while True:
   choice = int(input("Enter your choice = "))
   if choice ==1:
      print (add_messages())
   elif choice == 2:
      print(view_all_messages())
   elif choice == 3:
      print(Anaylize_messages())
   elif choice == 4:
      print(search_message())
   elif choice == 5:
      print("Exit")
      print("Thanks for using this anaylizer")
   else:
      print("Invalid Choice! Plz enter between 1 to 4")
