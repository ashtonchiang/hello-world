#Ashton Chiang
#1869119
#CIS 2348
#Professor Ratner

#store the data in a dictionary
data = {"id" : [1167234, 2347800, 2390112, 9034210, 7346234, 1009453, 3001265],
"manufacturer":["Apple", "Apple", "Dell", "Dell", "Lenovo", "Lenovo", "Samsung"],
"type" : ["phone", "laptop", "laptop", "tower", "laptop", "tower", "phone"],
"price": [534, 999, 799, 345, 239, 599, 1200]}

while True:
    #prompt the user for the query
    q = input("Type a query or q to quit: ")
    #if the user enters q exit the program
    if(q == "q"):
        break
    #intialize the manufacturer and type
    item = ""
    types = ""
    #iterate over the dictionary
    for i in data["manufacturer"]:
        #if the current manufacturer is present in the query
        if i in q:
            #assign the manufacturer to item
            item = i
    #iterate over all the types in data
    for i in data["type"]:
        #if the current type in the query
        if i in q:
            #assign the type
            types = i
    #if either item or type is empty print it
    if(item == "" or types == ""):
        print("No such item in invetory")
    else:
        #initialize the list to store the values
        details = ["", "", "", 0]
        #iterate over the dictonary
        for i in range(len(data["id"])):
            #check the data of mannufacturer and type in the data dictionary
            if(data["manufacturer"][i] == item and data["type"][i] == types):
                #check if current price is the most expensive
                if(details[3] < data["price"][i]):
                    #store the details in the list
                    details[0] = data["id"][i]
                    details[1] = data["manufacturer"][i]
                    details[2] = data["type"][i]
                    details[3] = data["price"][i]
        #print the item
        print("Your item is " + str(details[0]) + " " + str(details[1]) + " " + str(details[2]) + " " + str(details[3]))
        #create a list to store the recommended items
        extra = []
        #iterate over the data dictionary
        for i in range(len(data["id"])):
            #check all the items of same type and different manufacturer
            if(data["type"][i] == types and data["manufacturer"][i] != item):
                extra.append([data["id"][i], data["manufacturer"][i], data["type"][i], data["price"][i]])
        #check whether there are any items to recommend
        if(len(extra) != 0):
            print("You may also like ")
            #iterate over the list
            for i in range(len(extra)):
                print(str(extra[i][0]) + " " + extra[i][1] + " " + extra[i][2] + " " + str(extra[i][3]))







