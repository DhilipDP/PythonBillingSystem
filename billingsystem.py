import csv
import os
from shutil import copyfile

def writeHeader(file):
	if os.stat(file).st_size == 0:
		with open(file,"wb") as write:
			fieldnames = ["item_id", "item_name", "item_price"]
			writer = csv.DictWriter(write, fieldnames = fieldnames)
			writer.writeheader()

def check(id):
	with open("inventory.csv", "rb") as read:
		reader = csv.DictReader(read)
		for i in reader:
			if i["item_id"] == id:
				return i
				break
		else:
			return "not found"
			
def check_name(name):
	with open("inventory.csv", "rb") as read:
		reader = csv.DictReader(read)
		for i in reader:
			if i["item_name"] == name:
				return i
				break
		else:
			return "not found"
					
def additem():
	print "*********** ADD ITEM *************"
	 
	id = raw_input("enter product id\n")
	condition = check(id)
	if condition == "not found":
		name = raw_input("enter product name\n")
		price = raw_input("enter price\n")
		file = open("inventory.csv", "ab")
		fieldnames = ["item_id", "item_name", "item_price"]
		write = csv.DictWriter(file, fieldnames= fieldnames)
		write.writerow({"item_id": id, "item_name" : name, "item_price": price})
		file.close()
	else:
		print "Entered ID already exists"
	

def displayall():
	print "************ DISPLAY **************"
	file = open("inventory.csv", "rb")
	reader = csv.DictReader(file)
	print "--------------------------------------------"
	for i in reader:
		
		print i["item_id"], i["item_name"], i["item_price"]
		print "--------------------------------------------"

	file.close()
	


def search():
	print "************ SEARCH ****************"
	print "Search By \n1.ID\n2.Name"
	choice = input("Enter 1 or 2\n")
	if choice == 1:
		search_id = raw_input("Enter ID to be searched\n")
		condition = check(search_id)
		with open("inventory.csv", "rb") as read:
			reader = csv.DictReader(read)
			for i in reader:
				if i == condition:
					print i["item_id"], i["item_name"], i["item_price"]
					break
			else:
				print "Entered ID not found"
	elif choice == 2:
		search_name = raw_input("Enter product name to be searched.....case sensitive \n")
		condition = check_name(search_name)
		with open("inventory.csv", "rb") as read:
			reader = csv.DictReader(read)
			for i in reader:
				if i == condition:
					print "-----------------------------------------------"
					print i["item_id"], i["item_name"], i["item_price"]
					print "-----------------------------------------------"
					break
			else:
				print "Entered name not found"

def update():
	print "************* UPDATE ****************"
	print "Update By \n1.ID\n2.Name"
	choice = input("Enter 1 or 2")
	if choice == 1:
		print "Enter Product ID to be updated\n"
		update_id = raw_input()
		condition = check(update_id)
		if condition == "not found":
			print "Entered ID not found\n"
			return
		print "Enter Price to be Updated\n"
		price = raw_input("Enter price\n")
		with open("inventory.csv", "rb") as read:
			reader = csv.DictReader(read)
			for i in reader:
				if i == condition:
					with open("dummy.csv", "ab") as dummy:
						writeHeader("dummy.csv")
						fieldnames = ["item_id", "item_name", "item_price"]
						writer = csv.DictWriter(dummy, fieldnames = fieldnames)
						writer. writerow({"item_id" : i["item_id"], "item_name": i["item_name"], "item_price": price})
				else:
					with open("dummy.csv", "ab") as dummy:
						writeHeader("dummy.csv")
						fieldnames = ["item_id", "item_name", "item_price"]
						writer = csv.DictWriter(dummy, fieldnames = fieldnames)
						writer. writerow(i)
		
		copyfile("dummy.csv","inventory.csv")
		os.remove("dummy.csv")
	elif choice == 2:
		print "Enter Product ID to be updated\n"
		update_name = raw_input()
		condition = check_name(update_name)
		if condition == "not found":
			print "Entered Name not found"
			return
		print "Enter Price to be Updated\n"
		price = raw_input("Enter price\n")
		with open("inventory.csv", "rb") as read:
			reader = csv.DictReader(read)
			for i in reader:
				if i == condition:
					with open("dummy.csv", "ab") as dummy:
						writeHeader("dummy.csv")
						fieldnames = ["item_id", "item_name", "item_price"]
						writer = csv.DictWriter(dummy, fieldnames = fieldnames)
						writer. writerow({"item_id" : i["item_id"], "item_name": i["item_name"], "item_price": price})
				else:
					with open("dummy.csv", "ab") as dummy:
						writeHeader("dummy.csv")
						fieldnames = ["item_id", "item_name", "item_price"]
						writer = csv.DictWriter(dummy, fieldnames = fieldnames)
						writer. writerow(i)
		
		copyfile("dummy.csv","inventory.csv")
		os.remove("dummy.csv")
	else:
		print "You have entered an incorrect option\n"


def deleteitem():
	print "**************** DELETE ******************"
	print "DELETE by\n1.ID\n2.NAME\n"
	print "Enter your choice\n"
	choice = input()
	if choice == 1:
		print "Enter ID to be deleted\n"
		delete_id = raw_input()
		condition = check(delete_id)
		if condition == "not found":
			print "Entered ID not found"
			return
		with open("inventory.csv","rb") as read:
			reader = csv.DictReader(read)
			for i in reader:
				if i != condition:
					with open("dummy.csv","ab") as dummy:
						writeHeader("dummy.csv")
						fieldnames = ["item_id", "item_name", "item_price"]
						writer = csv.DictWriter(dummy, fieldnames = fieldnames)
						writer.writerow(i)
		copyfile("dummy.csv","inventory.csv")
		os.remove("dummy.csv")
	elif choice == 2:
		print "Enter the product name to be deleted\n"
		delete_name = raw_input()
		condition = check_name(delete_name)
		if condition == "not found":
			print "Entered Name not found"
			return
		with open("inventory.csv","rb") as read:
			reader = csv.DictReader(read)
			for i in reader:
				if i != condition:
					with open("dummy.csv","ab") as dummy:
						writeHeader("dummy.csv")
						fieldnames = ["item_id", "item_name", "item_price"]
						writer = csv.DictWriter(dummy, fieldnames = fieldnames)
						writer.writerow(i)
		copyfile("dummy.csv","inventory.csv")
		os.remove("dummy.csv")
	else:
		print "You have entered an incorrect option\n"

total = 0
summary = []

def billdesk():
	while 1:
		print "1. Add item for bill\n2. Thats it!Bill it\n"
		choice = input()
		if choice == 1:
			print "1. Add item by name\n2.Add item by ID\n"
			choice1 = input()
			if choice1 == 1:
				print "Enter product Name\n"
				name = raw_input()
				print "Enter quantity"
				quantity = input()
				condition = check_name(name)
				if condition == "not found":
					print "Entered Name not found"
					return
				with open("inventory.csv", "rb") as read:
					reader = csv.DictReader(read)
					for i in reader:
						if i == condition:
							j = quantity * int(i['item_price'])
							global total
							total = total + j
							print total
							summary.append(i['item_id'] + "\t" + i['item_name'] + "\t" + i['item_price'] + "\t" + "*" + "\t" + str(quantity))
							break
			elif choice1 == 2:
				print "Enter product ID\n"
				id = raw_input()
				print "Enter quantity"
				quantity = input()
				condition = check(id)
				if condition == "not found":
					print "Entered ID not found"
					return
				with open("inventory.csv", "rb") as read:
					reader = csv.DictReader(read)
					for i in reader:
						if i == condition:
							j = quantity * int(i['item_price'])
							total = total + j
							print total
							summary.append(i['item_id'] + "\t" + i['item_name'] + "\t" + i['item_price'] + "\t" + "*" + "\t" + str(quantity))
							break
			else:
				print "Incorrect option\n"
		elif choice == 2:
			print "\n ********** Bill Summary *********** \n"
			
			print "ID\t", "name\t", "price\t", "*\t", "quantity"
			for i in summary:
				print i
			print "\nTotal amount : ", total
			return
		
		else:
			print "You have entered an incorrect option\n"


			
with open("inventory.csv","ab") as write:
	writeHeader("inventory.csv")
			
while 1:
	print "WELCOME"
	print "(INITIALLY THE INVENTORY IS EMPTY..... SO ADD SOME ITEMS)"
	print "1. ADD ITEM"
	print "2. DISPLAY ALL ITEM"
	print "3. SEARCH FOR AN ITEM"
	print "4. UPDATE AN ITEM"
	print "5. DELETE AN ITEM"
	print "6. PROCEED TO CHECKOUT"
	print "7. EXIT"
	
	choice = input()
	
	if choice == 1:
		additem()
	elif choice == 2:
		displayall()
	elif choice == 3:
		displayall()
		search()
	elif choice == 4:
		update()
	elif choice == 5:
		deleteitem()
	elif choice == 6:
		billdesk()
	elif choice == 7:
		exit()
	else:
		print "Incorrect Option"