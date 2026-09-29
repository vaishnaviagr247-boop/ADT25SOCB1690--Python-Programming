class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def category(self):
        if self.treatment_cost >= 20000:
            return "Special"
        else:
            return "General"


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patients(self):
        for p in self.patients:
            print("Patient ID:", p.patient_id)
            print("Name:", p.name)
            print("Treatment Cost:", p.treatment_cost)
            print("Category:", p.category())
            print("----------------------")


hospital = Hospital()

hospital.add_patient(Patient(101, "Rahul", 15000))
hospital.add_patient(Patient(102, "Amit", 30000))
hospital.add_patient(Patient(103, "Sneha", 18000))

hospital.display_patients()




#unit 1 que 6

class Vehicle:
    def __init__(self, vehicle_no, brand, price):
        self.vehicle_no = vehicle_no
        self.brand = brand
        self.price = price

    def category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        for v in self.vehicles:
            print("Vehicle Number:", v.vehicle_no)
            print("Brand:", v.brand)
            print("Price:", v.price)
            print("Category:", v.category())
            print("----------------------")


showroom = Showroom()

showroom.add_vehicle(Vehicle("MH12AB1234", "Toyota", 1500000))
showroom.add_vehicle(Vehicle("MH14CD5678", "Maruti", 700000))
showroom.add_vehicle(Vehicle("MH12EF9012", "BMW", 2500000))

showroom.display_vehicles()


#unit 2 que 5

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1
    return dp[amount]


coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

result = coin_change(coins, amount)

if result == -1:
    print("Amount cannot be formed")
else:
    print("Minimum number of coins:", result)


    #uint  2 que 6


    def count_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter target amount: "))

result = count_ways(coins, amount)

print("Total number of ways:", result)

#uint 3 que 5

import csv

filename = "patients.csv"

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    patients = list(reader)

print("All Patient Records:")
for patient in patients:
    print(patient)

patient_id = input("Enter Patient ID to search: ")

found = False

for patient in patients:
    if patient["Patient ID"] == patient_id:
        print("Patient Found:")
        print(patient)
        found = True
        break

if not found:
    print("Patient not found")



    #unit 3 que 6

    import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)

args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)

    groceries = list(reader)

print("All Grocery Items:")

for item in groceries:
    print(item)

item_id = input("Enter Item ID to search: ")

found = False

for item in groceries:
    if item["Item ID"] == item_id:
        print("Item Found:")
        print(item)
        found = True
        break

if not found:
    print("Item not found")


    #unit 4 que 5

    import numpy as np
import pandas as pd

consumers = ["Rahul", "Amit", "Sneha", "Priya", "Rohan"]
bills = np.array([2500, 3500, 1800, 4200, 3000])

print("Mean Bill:", np.mean(bills))
print("Median Bill:", np.median(bills))
print("Maximum Bill:", np.max(bills))
print("Minimum Bill:", np.min(bills))

data = {
    "Consumer": consumers,
    "Bill": bills
}

df = pd.DataFrame(data)

print("\nAll Consumer Records:")
print(df)

print("\nConsumers with bill greater than 3000:")
print(df[df["Bill"] > 3000])

#unit 4 que 6


import numpy as np
import pandas as pd

players = ["Virat", "Rohit", "Rahul", "Dhoni", "Gill"]
runs = np.array([12000, 10500, 7000, 5500, 4500])

print("Average Runs:", np.mean(runs))
print("Highest Runs:", np.max(runs))
print("Lowest Runs:", np.min(runs))

data = {
    "Player": players,
    "Runs": runs
}

df = pd.DataFrame(data)

print("\nAll Player Records:")
print(df)

print("\nPlayers scoring more than 5000 runs:")
print(df[df["Runs"] > 5000])