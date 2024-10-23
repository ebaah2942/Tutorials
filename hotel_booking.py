import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mysql_password = os.getenv('my_password')




mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=mysql_password

)
 

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS hotel")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=mysql_password,
    database="hotel"
)

class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.mycursor = mydb.cursor()

    def create_table(self):
        try:
            self.mycursor.execute("""CREATE TABLE Details (id INT AUTO_INCREMENT PRIMARY KEY, type_of_room VARCHAR(255), date_of_checkin VARCHAR(255), number_of_nights INT)""")
            print("Table 'Details' created successfully.")
        except mysql.connector.Error as err:
            print(f"Error creating table: {err}")
            pass

    def add_hotel(self):
        type_of_room = input("Enter type of room: KINGSIZE ROOM, DOUBLE ROOM, SINGLE ROOM: ")
        date_of_checkin = input("Enter date of checkin: (YYYY-MM-DD): ")
        number_of_nights = int(input("Enter number of nights: "))
        if type_of_room == "KINGSIZE ROOM":
            price = 500
            total_price = price * number_of_nights
            print(f"Kingsize room booked successfully. Checkin date: {date_of_checkin}. Price per night: {price}. Total price: {total_price}.")
        elif type_of_room == "DOUBLE ROOM":
            price = 300
            total_price = price * number_of_nights
            print(f"Double room booked successfully. Checkin date: {date_of_checkin}. Price per night: {price}. Total price: {total_price}.")
        elif type_of_room == "SINGLE ROOM":
            price = 200
            total_price = price * number_of_nights
            print(f"Single room booked successfully. Checkin date: {date_of_checkin}. Price per night: {price}. Total price: {total_price}.")
        else:
            print("Invalid room type.")   
        
        sql = "INSERT INTO Details (type_of_room, date_of_checkin, number_of_nights) VALUES (%s, %s, %s)"
        val = (type_of_room, date_of_checkin, number_of_nights)
        self.mycursor.execute(sql, val)
        mydb.commit()


new_data = Hotel("Accra Central View Hotel", "Accra, Ghana")
new_data.create_table()
new_data.add_hotel()        
