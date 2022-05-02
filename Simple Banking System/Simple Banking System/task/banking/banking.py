# Author Gerardo Ángeles Nava. México City 30-07-2021
import random
import sqlite3

customers = []
g_id = 0


def transfer(table_name, account_number, receiver_number, income):
    conn = None
    cur = None
    try:
        # First create a Connection object that represents the database
        conn = sqlite3.connect('card.s3db')
        # Once you have a Connection, you can create a Cursor object
        cur = conn.cursor()

        # Add to receiver
        current_balance = get_balance_from("card", receiver_number)
        new_balance = current_balance + int(income)
        qry = f"UPDATE {table_name} SET balance = {new_balance} WHERE number = '{receiver_number}';"
        cur.execute(qry)
        # After making some changes in DB don't forget to commit them!
        conn.commit()

        # subtract customer
        current_balance = get_balance_from("card", account_number)
        new_balance = current_balance - int(income)
        qry = f"UPDATE {table_name} SET balance = {new_balance} WHERE number = '{account_number}';"
        cur.execute(qry)

        # Executes some SQL query
        cur.execute(qry)
        # After making some changes in DB don't forget to commit them!
        conn.commit()

    except sqlite3.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        conn.close()


def get_receiver_info(table_name, transfer_card_number):
    conn = None
    cur = None
    try:
        # First create a Connection object that represents the database
        conn = sqlite3.connect('card.s3db')
        # Once you have a Connection, you can create a Cursor object
        cur = conn.cursor()

        qry = f"SELECT * FROM {table_name} WHERE number = '{transfer_card_number}';"
        cur.execute(qry)

        # Executes some SQL query
        cur.execute(qry)

        r = cur.fetchone()
        return r

    except sqlite3.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        conn.close()


def remove_card(table_name, account_number, pin_number):
    conn = None
    cur = None
    try:
        # First create a Connection object that represents the database
        conn = sqlite3.connect('card.s3db')
        # Once you have a Connection, you can create a Cursor object
        cur = conn.cursor()

        # DELETE FROM books WHERE quantity = 0

        qry = f"DELETE FROM {table_name} WHERE number = '{account_number}' AND pin = '{pin_number}';"
        # print(qry)
        cur.execute(qry)

        # Executes some SQL query
        cur.execute(qry)
        # After making some changes in DB don't forget to commit them!
        conn.commit()

    except sqlite3.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        conn.close()


def set_income(table_name, account_number, pin_number, income):
    conn = None
    cur = None
    try:
        # First create a Connection object that represents the database
        conn = sqlite3.connect('card.s3db')
        # Once you have a Connection, you can create a Cursor object
        cur = conn.cursor()

        current_balance = get_balance_from("card", account_number)

        new_balance = current_balance + int(income)

        qry = f"UPDATE {table_name} SET balance = {new_balance} WHERE number = '{account_number}' AND pin = '{pin_number}';"
        # print(qry)
        cur.execute(qry)

        # Executes some SQL query
        cur.execute(qry)
        # After making some changes in DB don't forget to commit them!
        conn.commit()

    except sqlite3.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        conn.close()


def get_customer_info(table_name, account_number, pin_number):
    conn = None
    cur = None
    try:
        # First create a Connection object that represents the database
        conn = sqlite3.connect('card.s3db')
        # Once you have a Connection, you can create a Cursor object
        cur = conn.cursor()

        qry = f"SELECT * FROM {table_name} WHERE number = '{account_number}' AND pin = '{pin_number}';"
        cur.execute(qry)

        # Executes some SQL query
        cur.execute(qry)

        r = cur.fetchone()
        return r

    except sqlite3.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        conn.close()


def get_balance_from(table_name, customer_number):
    conn = None
    cur = None
    try:
        # First create a Connection object that represents the database
        conn = sqlite3.connect('card.s3db')
        # Once you have a Connection, you can create a Cursor object
        cur = conn.cursor()

        qry = f"SELECT balance FROM {table_name} WHERE number = '{customer_number}';"
        cur.execute(qry)

        # Executes some SQL query
        cur.execute(qry)

        card_balance = cur.fetchone()
        return card_balance[0]

    except sqlite3.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        conn.close()


def get_row_from(table_name, field, value):
    conn = None
    cur = None
    try:
        # First create a Connection object that represents the database
        conn = sqlite3.connect('card.s3db')
        # Once you have a Connection, you can create a Cursor object
        cur = conn.cursor()

        qry = f"SELECT * FROM {table_name} WHERE {field} = '{value}';"
        cur.execute(qry)

        # Executes some SQL query
        cur.execute(qry)

        cards = cur.fetchall()
        #
        for c in cards:
            print("id", c[0])
            print("number", c[1])
            print("pin", c[2])
            print("balance", c[3])

    except sqlite3.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        conn.close()


def show_table(table):
    # First create a Connection object that represents the database
    conn = sqlite3.connect('card.s3db')
    # Once you have a Connection, you can create a Cursor object
    cur = conn.cursor()

    table_name = table

    qry = f"SELECT * FROM {table_name};"
    cur.execute(qry)

    # Executes some SQL query
    cur.execute(qry)

    cards = cur.fetchall()
    #
    for c in cards:
        print("id", c[0])
        print("number", c[1])
        print("pin", c[2])
        print("balance", c[3])
        print("--------------")


def store_new_card(db, table, id_card, number, pin, balance):
    # First create a Connection object that represents the database
    conn = sqlite3.connect('card.s3db')
    # Once you have a Connection, you can create a Cursor object
    cur = conn.cursor()

    table_name = table
    card_id = id_card
    card_number = number
    card_pin = pin
    card_balance = balance

    # qry = f"INSERT INTO {table_name} VALUES ({card_id}, '{card_number}', '{card_pin}', {card_balance});"
    qry = f"INSERT INTO {table_name} (number, pin) VALUES ('{card_number}', '{card_pin}');"
    cur.execute(qry)

    # After making some changes in DB don't forget to commit them!
    conn.commit()


def create_db_file(db, table):
    # First create a Connection object that represents the database
    conn = sqlite3.connect('card.s3db')
    # Once you have a Connection, you can create a Cursor object
    cur = conn.cursor()

    table_name = table

    qry = f"DROP TABLE IF EXISTS {table_name};"
    cur.execute(qry)

    qry = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, number TEXT NOT NULL, pin TEXT NOT NULL, balance INTEGER DEFAULT 0);"

    # Executes some SQL query
    cur.execute(qry)

    # After making some changes in DB don't forget to commit them!
    conn.commit()


def generate_random_number(how_many, start, end):
    num = ""
    for _ in range(0, how_many):
        num = num + str(random.randint(start, end))

    return num


def generate_cc_number():
    _bin = "400000"
    cc_number = ""
    for i in range(1, 100):
        cc_number = _bin + generate_random_number(9, 0, 9) + generate_random_number(1, 0, 9)
        if is_valid_cc_number(cc_number):
            return cc_number

    return 0


def is_valid_cc_number(number):
    # 0. get last digit
    last_digit = int(number[-1:])
    # 1. Drop the last digist
    # lst_number = list(number[0:-1])
    lst_number = [int(s) for s in number[0:-1]]
    # 2. Multiply odd digist-position by 2
    for i, d in enumerate(lst_number):
        if (i + 1) % 2 != 0:
            calc = d * 2
            # 3. Substract 9 from number over 9 value
            if calc > 9:
                lst_number[i] = calc - 9
            else:
                lst_number[i] = calc

    # 4. Add all numbers from number card
    lst_number.append(last_digit)
    suma = 0
    for d in lst_number:
        suma += d

    if suma % 10 == 0:
        return True
    else:
        return False


def generate_a_pin_code():
    # you should generate a PIN code that belongs to the generated card number
    # The PIN code is a sequence of any 4 digits.
    return generate_random_number(4, 0, 9)


class Card:
    checksum = 8
    VALID_CARD = "4"  # In our banking system, credit cards should begin with 4.
    IIN = VALID_CARD + "00000"  # In our banking system, the IIN must be 400000

    def __init__(self, account_id):
        self.account_id = account_id
        self.MII = account_id[0]  # the very first digit
        self.BIN = account_id[0:6]
        # self.tc = self.IIN + account_id + str(Card.checksum)
        self.tc = account_id
        # The seventh digit to the second-to-last digit is the customer account number.
        self.customer_account_number = self.tc[6:-1]
        self.pin = generate_a_pin_code()
        self.balance = 0

    def is_valid_card(self):
        # In our banking system, credit cards should begin with 4.
        if self.account_id[0] == self.VALID_CARD:
            return True
        else:
            return False

    def get_iin(self):
        # where the card originated from
        return self.tc[0:6]

    def get_tc_type(self):
        visa = "4"
        amex = ["34", "37"]
        mastercard = []

        for n in range(51, 55 + 1):
            mastercard.append(str(n))

        if self.account_id[-6:-5] == visa:
            return "visa"
        elif self.account_id[-7:-5] in amex:
            return "amex"
        elif self.account_id[-7:-5] in mastercard:
            return "mastercard"
        else:
            return "Otro"

    def show_mask_tc(self):
        tc_type = self.get_tc_type()

        if tc_type == "visa":
            print(f"Visa: {self.account_id[-6:-5]}*****")
        elif tc_type == "amex":
            print(f"American Express (AMEX): {self.account_id[-7:-5]}****")
        elif tc_type == "mastercard":
            print(f"Mastercard: {self.account_id[-7:-5]}****")
        else:
            return "Otro"


def create_an_account():
    # If the customer chooses ‘Create an account’,
    # you should generate a new card number

    _tc = generate_cc_number()

    card = Card(_tc)

    print("\nYour card has been created")
    print("Your card number:")
    print(card.tc)
    print("Your card PIN:")
    print(card.pin)
    print()

    global g_id
    g_id += 1
    store_new_card("card", "card", g_id, card.tc, card.pin, 0)

    # customers.append(card)

    return card


def log_into_account(customer_card):
    # If the customer chooses ‘Log into account’,
    # you should ask them to enter their card information.

    # Store all generated data until it is terminated
    # so that a user is able to log into any of
    # the created accounts by a card number and its pin.
    # You can use an array to store the information.

    card_number = input("\nEnter your card number:\n")
    pin = input("Enter your PIN:\n")

    cc = get_customer_info("card", card_number, pin)
    if cc:
        # After all information is entered correctly,
        # you should allow the user to check the account balance;
        # right after creating the account, the balance should be 0.
        # It should also be possible to log out of the account and exit the program.

        customer_id = cc[0]
        customer_number = cc[1]
        customer_pin = cc[2]
        customer_balance = cc[3]

        print("\nYou have successfully logged in!\n")

        customer_option = 3
        while customer_option != "0":
            print("1. Balance")

            print("2. Add income")
            print("3. Do transfer")
            print("4. Close account")

            print("5. Log out")
            print("0. Exit")

            customer_option = input()

            if customer_option == "1":
                # Read the balance of the account from the database and output it into the console
                b = get_balance_from("card", customer_number)
                print(f"\nBalance: {b}\n")

            elif customer_option == "2":
                # Add income item should allow us to deposit money to the account.
                print("\nEnter income:")
                income = input()
                set_income("card", card_number, pin, income)
                print("Income was added!\n")

            elif customer_option == "3":
                # Do transfer item should allow transferring money to another account.
                # You should handle the following errors:

                print("\nTransfer\nEnter card number:")
                transfer_card_number = input()

                if not is_valid_cc_number(transfer_card_number):
                    # Validation 3. If the receiver's card number doesn’t pass the Luhn algorithm
                    print("Probably you made a mistake in the card number. Please try again!\n")

                else:
                    if customer_number == transfer_card_number:
                        # Validation 2. If the user tries to transfer money to the same account
                        print("You can't transfer money to the same account!\n")

                    else:
                        # Validation 4. If the receiver's card number doesn’t exist
                        receivers_card = get_receiver_info("card", transfer_card_number)
                        if not receivers_card:
                            print("Such a card does not exist.\n")
                        else:
                            # validation 5. If there is no error,
                            # ask the user how much money they want to transfer and make the transaction.
                            print("Enter how much money you want to transfer:")
                            money = input()
                            # Validation 1. If the user tries to transfer more money than he/she has, output:
                            customer_balance = get_balance_from("card", customer_number)
                            if int(money) > customer_balance:
                                print("Not enough money!\n")
                            else:
                                transfer("card", customer_number, receivers_card[1], money)
                                print("Success!\n")

            elif customer_option == "4":
                # If the user chooses the Close account item, you should delete that account from the database.
                remove_card("card", customer_number, customer_pin)
                print("\nYou have successfully logged out!\n")
                break

            elif customer_option == "5":
                print("\nYou have successfully logged out!\n")
                break
            else:
                quit()
                # print("\nBye!\n")
        else:
            print("\nWrong card number or PIN!\n")
    else:
        print("\nWrong card number or PIN!\n")


if __name__ == '__main__':

    my_card = None

    create_db_file("card", "card")

    usr_option = 3
    while usr_option != "0":
        print("1. Create an account\n2. Log into account\n0. Exit")

        usr_option = input()

        if usr_option == "1":
            my_card = create_an_account()
        elif usr_option == "2":
            log_into_account(my_card)

        elif usr_option == 's':
            show_table("card")
        elif usr_option == 'g':
            val = input()
            # get_row_from("card", "number", val)
            get_balance_from("card", "number")

        elif usr_option == "0":
            print("Bye!\n")
            quit()
        else:
            pass
