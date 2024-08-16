import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt
from database import DBrun

def main():
    print("Welcome to Finance Tracker.")
    print("Please select an option from the menu below:")
    while True:
        print("1. Manage Records")
        print("2. View Records")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            DBrun()
        if choice == "0":
            print("Exiting....")
            break

if __name__ == "__main__":
    main()