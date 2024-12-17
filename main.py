import datetime


# AIMAN ADEL AWADH ABDULLAH MAHMOOD
# TP065994

# Application main menu function.
def main():
    # A list of main menu.
    options = [
        'Log In to the system',
        'Sign In a new customer',
        'Exit'
    ]
    keep_asking = True
    # Keep asking the user until they exit the program.
    while keep_asking:
        for index in range(1, 4):
            if index == 1:
                print(f'{index} => {options[0]}')
            elif index == 2:
                print(f'{index} => {options[1]}')
            elif index == 3:
                print(f'{index} => {options[2]}')

        try:
            # User choice from the above options.
            selected_option = int(input('Please select one option: '))
            # If user's choice is 1 login() funcation is called.
            if selected_option == int('1'):
                logindata = login()
                if logindata[3] == '1':
                    super_admin_account_options(logindata)
                elif logindata[3] == '2':
                    admin_stuff_options(logindata)
                else:
                    customer_options(logindata)
            # If user's choice is 2 register_customer() function is called.
            elif selected_option == int('2'):
                register_customer()
            # If user's choice is 3 exit_program() function is called.
            elif selected_option == int('3'):
                exit_program()

            else:
                print("\n")
                print('Please choose one of these options:')
        except ValueError:
            print("\n")
            print('Invalid Input! Only numeric va-lue is accepted')


# login page function.
def login():
    keep_asking = True
    while keep_asking:
        print("\n")
        userid = input('Please Enter Your ID or Q to return: ')
        if userid.upper() == 'Q':
            print("\n")
            main()
        userpass = input('Please Enter Your Password or Q to return: ')
        if userpass.upper() == 'Q':
            print("\n")
            main()
        fh = open('userpass.txt', 'r')
        foundresult = 'notfound'
        for line in fh:
            linelist = line.strip().split(':')
            if linelist[0] == userid and linelist[1] == userpass:
                foundresult = linelist
                break
        fh.close()
        if foundresult == 'notfound':
            print('\n')
            print('Invalid Password or Username. Try again!')
        else:
            print("\n")
            print("-----  Welcome to the System -----")
            return foundresult


# Function for generate Admin ID, Customer ID, and Transaction ID.
def genid(perm):
    with open("id.txt", "r") as idfh:
        rec = idfh.readline()
        reclist = rec.strip().split(":")
    if perm == "admin":
        pref = "ADM"
        oldid = reclist[0][3:]
    elif perm == "customer":
        pref = "CUS"
        oldid = reclist[1][3:]
    elif perm == "trans":
        pref = "TRN"
        oldid = reclist[2][3:]
    nextid = int(oldid) + 1
    if len(str(nextid)) == 1:
        newid = "0000" + str(nextid)
    elif len(str(nextid)) == 2:
        newid = "000" + str(nextid)
    elif len(str(nextid)) == 3:
        newid = "00" + str(nextid)
    elif len(str(nextid)) == 4:
        newid = "0" + str(nextid)
    elif len(str(nextid)) == 5:
        newid = str(nextid)
    newid = pref + newid
    if perm == "admin":
        reclist[0] = newid
    elif perm == 'customer':
        reclist[1] = newid
    else:
        reclist[2] = newid
    rec = ":".join(reclist)
    with open("id.txt", "w") as fh:
        fh.write(rec)
    return newid


# Function for getting a unique number for each customer.
def get_new_customer():
    try:
        file = open(f"register_customer.txt", "r")
        lines = file.readlines()
        file.close()
        return len(lines) + 1
    except FileNotFoundError:
        file = open(f"register_customer.txt", "r")
        file.close()
        return 1


# Function for saving customer's detail in text file.
def write_to_file(file, data):
    # Open text file in append mode.
    file = open(f"{file}.txt", "a")
    try:
        if type(data) != str:
            # Write customer's details in it.
            file.write(f"{str(data)}\n")
        file.close()
        return True
    except:
        file.close()
        return False


# Registration form function.
def register_customer():
    print("\n")
    print("----------------------------------------------- ")
    print("Fill up the following form or press 'q' to exit ")
    print("----------------------------------------------- ")
    customer_required_information = [
        "Name",
        "Email",
        "Phone Number",
        "Date Of Birth (yyyy-mm-dd)",
        "Gender M/F",
        "Bank account type you wish to have Saving/Current"
    ]
    customer_information = []

    for information in customer_required_information:
        ans = input(f"Please Enter Your {information}: ")
        if ans.lower() == 'q':
            main()
        if information == 'Phone Number':
            while True:
                if len(str(ans)) == 10:
                    break
                elif ans.lower() == 'q':
                    main()
                else:
                    print('\n')
                    ans = input("Invalid Input! Phone Number 10 min&max (Ex:01123456789): ")
        if information == 'Date Of Birth (yyyy-mm-dd)':
            while True:
                if len(str(ans)) == 10:
                    break
                elif ans.lower() == 'q':
                    main()
                else:
                    print('\n')
                    ans = input("Invalid Input! Date Of Birth (Ex:yyyy-mm-dd): ")
        if information == 'Gender M/F':
            while True:
                if ans.lower() == 'm':
                    break
                elif ans.lower() == 'f':
                    break
                elif ans.lower() == 'q':
                    main()
                else:
                    print('\n')
                    ans = input("Invalid Input! Please Enter 'M' for male or 'F' for female: ")
        if information == 'Bank account type you wish to have Saving/Current':
            while True:
                if ans.lower() == 'saving':
                    break
                elif ans.lower() == 'current':
                    break
                elif ans.lower() == 'q':
                    main()
                else:
                    print('\n')
                    ans = input('Invalid Input! Please Enter your account type Saving/Current: ')

        customer_information.append(ans)
    customer_information.append(get_new_customer())
    write_to_file("register_customer", customer_information)
    print("\n")
    print('-------------------------------------------------------------------------------')
    print('Your information has been received and is being reviewed by our team, Thank you')
    print('-------------------------------------------------------------------------------')
    print("\n")
    back_to_menu()


# Function for going back to main menu.
def back_to_menu():
    options = [
        'Return to the main menu',
        'Exit'
    ]

    keep_asking = True
    while keep_asking:
        for index in range(1, 3):
            if index == 1:
                print(f'{index} => {options[0]}')
            elif index == 2:
                print(f'{index} => {options[1]}')

        try:
            # User choice from the above options.
            selected_option = int(input('Please select one option: '))
            # If user's choice is 1 main() is called.
            if selected_option == int('1'):
                print("\n")
                main()
            # If user choose number 2 they exit the program.
            elif selected_option == int('2'):
                exit_program()
            else:
                print("\n")
                print('Please choose one of these options:')
        except ValueError:
            print('Invalid Input! Only numeric va-lue is accepted')
            print("\n")


# Customer menu function.
def customer_options(logindata):
    options = [
        'Check Balance',
        'Perform deposit',
        "perform withdrawal",
        "Print bank statement",
        'Change Password',
        'Logout'
    ]

    keep_asking = True
    while keep_asking:
        print("Customer MENU for", logindata[2])
        print('======================================')
        for index in range(1, 7):
            if index == 1:
                print(f'{index} => {options[0]}')
            elif index == 2:
                print(f'{index} => {options[1]}')
            elif index == 3:
                print(f'{index} => {options[2]}')
            elif index == 4:
                print(f'{index} => {options[3]}')
            elif index == 5:
                print(f'{index} => {options[4]}')
            elif index == 6:
                print(f'{index} => {options[5]}')

        try:
            # User choice from the above options.
            selected_option = int(input('Please select one option: '))
            if selected_option == int('1'):
                check_balance(logindata)
            elif selected_option == int('2'):
                perform_deposit(logindata)
            elif selected_option == int('3'):
                perform_withdrawal(logindata)
            elif selected_option == int('4'):
                bank_statement(logindata)
            elif selected_option == int('5'):
                changepass(logindata)
            elif selected_option == int('6'):
                exit_program()
            else:
                print("\n")
                print('Please choose one of these options:')

        except ValueError:
            print("\n")
            print('Invalid Input! Only numeric value is accepted')


# Admin staff menu function.
def admin_stuff_options(logindata):
    options = [
        'Add a new customer account',
        "Edit customer's info",
        "print bank statement for customer",
        "Display all users accounts",
        'Change Password',
        'Logout'
    ]
    keep_asking = True
    while keep_asking:
        print("ADMIN MENU for", logindata[2])
        print('======================================')
        for index in range(1, 7):
            if index == 1:
                print(f'{index} => {options[0]}')
            elif index == 2:
                print(f'{index} => {options[1]}')
            elif index == 3:
                print(f'{index} => {options[2]}')
            elif index == 4:
                print(f'{index} => {options[3]}')
            elif index == 5:
                print(f'{index} => {options[4]}')
            elif index == 6:
                print(f'{index} => {options[5]}')

        try:
            # User choice from the above options.
            selected_option = int(input('Please select one option: '))
            if selected_option == int('1'):
                add_customer_account()
            elif selected_option == int('2'):
                edit_customer_info(logindata)
            elif selected_option == int('3'):
                cus_bank_statement(logindata)
            elif selected_option == int('4'):
                display_users()
            elif selected_option == int('5'):
                changepass(logindata)
            elif selected_option == int('6'):
                exit_program()
            else:
                print("\n")
                print('Please choose one of these options:')

        except ValueError:
            print("\n")
            print('Invalid Input! Only numeric value is accepted')


# Super admin account menu function.
def super_admin_account_options(logindata):
    options = [
        'Create an admin staff account',
        'Create a customer account',
        "Edit customer's info",
        'print a bank statement for the customer',
        'Display all users accounts',
        'Change Password',
        'Logout'
    ]
    keep_asking = True
    while keep_asking:
        print("SUPER ADMIN MENU for", logindata[2])
        print('======================================')
        for index in range(1, 8):
            if index == 1:
                print(f'{index} => {options[0]}')
            elif index == 2:
                print(f'{index} => {options[1]}')
            elif index == 3:
                print(f'{index} => {options[2]}')
            elif index == 4:
                print(f'{index} => {options[3]}')
            elif index == 5:
                print(f'{index} => {options[4]}')
            elif index == 6:
                print(f'{index} => {options[5]}')
            elif index == 7:
                print(f'{index} => {options[6]}')

        try:
            # User choice from the above options.
            selected_option = int(input('Please select one option: '))
            if selected_option == int('1'):
                add_admin_account()
            elif selected_option == int('2'):
                add_customer_account()
            elif selected_option == int('3'):
                edit_customer_info(logindata)
            elif selected_option == int('4'):
                cus_bank_statement(logindata)
            elif selected_option == int('5'):
                display_users()
            elif selected_option == int('6'):
                changepass(logindata)
            elif selected_option == int('7'):
                exit_program()

            else:
                print("\n")
                print('Please choose one of these options:')

        except ValueError:
            print("\n")

            print('Invalid Input! Only numeric value is accepted')


# Function for changing password.
def changepass(logindata):
    # Create an empty list
    allrec = []
    # Open the file for reading mode
    with open("userpass.txt", "r") as fh:
        for rec in fh:
            # Reed lines and convert them to list and split them with ':'
            reclist = rec.strip().split(":")
            allrec.append(reclist)
    print('\n')
    ind = -1
    nor = len(allrec)
    for cnt in range(0, nor):
        if logindata[0] == allrec[cnt][0]:
            ind = cnt
            break
    conpassword = input('Please Enter Current Password: ')
    newpass = input("Please Enter New Password: ")
    if conpassword == allrec[ind][1]:
        allrec[ind][1] = newpass
        with open("userpass.txt", "w") as fh:
            nor = len(allrec)
            for cnt in range(0, nor):
                rec = ":".join(allrec[cnt]) + "\n"
                fh.write(rec)
            print('\n')
            print('======================================')
            print('Password Has Been Successfully Changed ')
            print('======================================')
    else:
        print('\n')
        print('====================================================================')
        print('We cannot change your password! Your current password is incorrect. ')
        print('====================================================================')

    while True:
        print('\n')
        print('1 => Go back to the menu ')
        print('2 => Logout ')
        selected_option = input('Please choose one of these options: ')
        if selected_option == '1':
            print('\n')
            break
        elif selected_option == '2':
            exit_program()


# Function for printing statement for a customer.
def cus_bank_statement(logindata):
    while True:
        nor = 0
        allrec = []
        cusid = input("Please enter customer ID or press 'q' to return: ")
        if cusid == 'q':
            print('\n')
            admin_stuff_options(logindata)
        with open("transaction.txt", "r") as fh:
            for line in fh:
                allrec.append(line.strip().split(":"))
        for cnt in range(0, len(allrec)):
            if cusid == allrec[cnt][1]:
                nor = 0
                nor += 1
                while True:
                    while True:
                        strdate = input('Please Enter Start Date (yyyy-mm-dd): ')
                        if strdate == 'q':
                            print('\n')
                            admin_stuff_options(logindata)
                        if len(str(strdate)) == 10:
                            break
                        else:
                            print('\n')
                            print("Please Enter the correct format or 'q' to go back (yyyy-mm-dd)")

                    while True:
                        enddate = input('Please Enter End Date (yyyy-mm-dd): ')
                        if enddate == 'q':
                            print('\n')
                            admin_stuff_options(logindata)
                        if len(str(enddate)) == 10:
                            break
                        else:
                            print('\n')
                            print("Please Enter the correct format or 'q' to go back (yyyy-mm-dd)")
                    nor = 0
                    print("=" * 105)
                    print(
                        "NOR".center(7) + "|" + "Transaction ID".ljust(18) + "|" + "Customer ID".ljust(
                            15) + "|" + "Trans Type".center(15)
                        + "|" + "Trans Amount".center(15) + "|" + "Date".center(15) + "|" + "Time".center(14))
                    print("=" * 105)
                    for cnt in range(0, len(allrec)):
                        if strdate <= allrec[cnt][4] and enddate >= allrec[cnt][4]:
                            if (cusid == allrec[cnt][1]):
                                nor += 1
                                print(str(nor).center(7) + "|" + allrec[cnt][0].ljust(18) + "|" + allrec[cnt][1].ljust(
                                    15) + "|" +
                                      allrec[cnt][2].center(15)
                                      + "|" + allrec[cnt][3].center(15) + "|" + allrec[cnt][4].center(15) + "|" + (
                                              allrec[cnt][5] + ":" + allrec[cnt][6]).center(15))
                    print('\n\n')
                    if nor == 0:
                        print('Record Not found'.center(100))
                        print('\n')

                    while True:
                        user_selection = input('Would you like to try another date? y/n: ')
                        if user_selection.lower() == 'y':
                            break


                        elif user_selection.lower() == 'n':
                            admin_stuff_options(logindata)
                        else:
                            print('\n')
                            print("Invalid Input, please enter 'y' for yes or 'n' for no!")
        if nor == 0:
            print('----------------')
            print('Record Not found')
            print('----------------')


# Function for displaying all user account.
def display_users():
    with open("userpass.txt", "r") as fh:
        print("=" * 60)
        print("Usre ID".center(10) + "|" + "User Password".center(14) + "|" + "User Name".center(
            17) + "|" + "Account Type")
        print("=" * 60)
        for rec in fh:
            reclist = rec.strip().split(":")
            if reclist[3] == '1':
                reclist[3] = 'Super account'
                reclist[1] = 'Hidden'
            elif reclist[3] == '2':
                reclist[3] = 'Admin account'
            elif reclist[3] == '3':
                reclist[3] = 'Customer account'
            print(reclist[0].ljust(10) + "|" + reclist[1].ljust(14) + "|" + reclist[2].ljust(17) + "|" + reclist[
                3].center(12))
    print("\n\n")
    while True:
        print('1 => Go back to the menu ')
        print('2 => Logout ')
        selected_option = input('Please choose one of these options: ')
        if selected_option == '1':
            print('\n')
            break
        elif selected_option == '2':
            exit_program()


# Function for editing customer info.
def edit_customer_info(logindata):
    break_out_flag = False
    while True:
        allrec = []
        cusid = input("Please enter customer ID or press 'q' to return: ")
        if cusid == 'q':
            print('\n')
            break
        with open("customers_information.txt", "r") as fh:
            for line in fh:
                allrec.append(line.strip().split(":"))
        for cnt in range(0, len(allrec)):
            if cusid == allrec[cnt][0]:
                options = [
                    "Email",
                    "Phone",
                    "Date Of Birth",
                    "Gender M/F",
                    "Bank Account Type Saving/Current",
                    "Account Balance",
                    "Go back to the main menu"
                ]
                keep_asking = True
                while keep_asking:
                    if break_out_flag:
                        while True:
                            print('\n')
                            print('1 => Go back to tha main menu ')
                            print('2 => Logout ')
                            selected_option = input('Please choose one of these options: ')
                            if selected_option == '1':
                                print('\n')
                                break
                            elif selected_option == '2':
                                exit_program()
                        break
                    print('\n')
                    print('Edit info for:', allrec[cnt][1])
                    print('------------------------------')
                    for index in range(1, 8):
                        if break_out_flag:
                            break
                        if index == 1:
                            print(f'{index} => {options[0]}')
                        elif index == 2:
                            print(f'{index} => {options[1]}')
                        elif index == 3:
                            print(f'{index} => {options[2]}')
                        elif index == 4:
                            print(f'{index} => {options[3]}')
                        elif index == 5:
                            print(f'{index} => {options[4]}')
                        elif index == 6:
                            print(f'{index} => {options[5]}')
                        elif index == 7:
                            print(f'{index} => {options[6]}')
                    try:
                        # User choice from the above options.
                        if break_out_flag:
                            break
                        selected_option = int(input('Please select what you would like to edit: '))

                        if selected_option == int('1'):

                            print('---------------------------------------')
                            print('This is Current email:', allrec[cnt][2])
                            print('---------------------------------------')
                            while True:
                                if break_out_flag:
                                    break
                                conformation = input('Are you sure you would like to edit it? y/n: ')
                                if conformation.lower() == 'y':
                                    newemaill = input('Please Enter New Email: ')
                                    allrec[cnt][2] = newemaill
                                    with open("customers_information.txt", "w") as fh:
                                        nor = len(allrec)
                                        for cnt in range(0, nor):
                                            rec = ":".join(allrec[cnt]) + "\n"
                                            fh.write(rec)
                                        print('\n')
                                        print('===================================')
                                        print('Info have Been Successfully Changed')
                                        print('===================================')
                                        break_out_flag = True
                                        break
                                elif conformation.lower() == 'n':
                                    break
                                else:
                                    print('\n')
                                    print("Invalid Input, please enter 'y' for yes or 'n' for no!")
                        elif selected_option == int('2'):
                            print('---------------------------------------')
                            print('This is Current Phone:', allrec[cnt][3])
                            print('---------------------------------------')
                            while True:
                                if break_out_flag:
                                    while True:
                                        print('\n')
                                        print('1 => Go back to tha main menu ')
                                        print('2 => Logout ')
                                        selected_option = input('Please choose one of these options: ')
                                        if selected_option == '1':
                                            print('\n')
                                            break
                                        elif selected_option == '2':
                                            exit_program()
                                    break
                                conformation = input('Are you sure you would like to edit it? y/n: ')
                                if conformation.lower() == 'y':
                                    newemaill = input('Please Enter New Phone: ')
                                    allrec[cnt][3] = newemaill
                                    with open("customers_information.txt", "w") as fh:
                                        nor = len(allrec)
                                        for cnt in range(0, nor):
                                            rec = ":".join(allrec[cnt]) + "\n"
                                            fh.write(rec)
                                        print('\n')
                                        print('===================================')
                                        print('Info have Been Successfully Changed')
                                        print('===================================')
                                        break_out_flag = True
                                        break
                                elif conformation.lower() == 'n':
                                    break
                                else:
                                    print('\n')
                                    print("Invalid Input, please enter 'y' for yes or 'n' for no!")
                        elif selected_option == int('3'):
                            print('---------------------------------------')
                            print('This is Current Date Of Birth:', allrec[cnt][4])
                            print('---------------------------------------')
                            while True:
                                if break_out_flag:
                                    break
                                conformation = input('Are you sure you would like to edit it? y/n: ')
                                if conformation.lower() == 'y':
                                    newemaill = input('Please Enter New Date Of Birth yyyy/mm/dd?: ')
                                    allrec[cnt][4] = newemaill
                                    with open("customers_information.txt", "w") as fh:
                                        nor = len(allrec)
                                        for cnt in range(0, nor):
                                            rec = ":".join(allrec[cnt]) + "\n"
                                            fh.write(rec)
                                        print('\n')
                                        print('===================================')
                                        print('Info have Been Successfully Changed')
                                        print('===================================')
                                        break_out_flag = True
                                        break
                                elif conformation.lower() == 'n':
                                    break
                                else:
                                    print('\n')
                                    print("Invalid Input, please enter 'y' for yes or 'n' for no!")
                        elif selected_option == int('4'):
                            print('---------------------------------------')
                            print('This is Current Gender:', allrec[cnt][5])
                            print('---------------------------------------')
                            while True:
                                if break_out_flag:
                                    break
                                conformation = input('Are you sure you would like to edit it? y/n: ')
                                if conformation.lower() == 'y':
                                    newemaill = input('Please Enter New Gender M/F?: ')
                                    allrec[cnt][5] = newemaill
                                    with open("customers_information.txt", "w") as fh:
                                        nor = len(allrec)
                                        for cnt in range(0, nor):
                                            rec = ":".join(allrec[cnt]) + "\n"
                                            fh.write(rec)
                                        print('\n')
                                        print('===================================')
                                        print('Info have Been Successfully Changed')
                                        print('===================================')
                                        break_out_flag = True
                                        break
                                elif conformation.lower() == 'n':
                                    break
                                else:
                                    print('\n')
                                    print("Invalid Input, please enter 'y' for yes or 'n' for no!")
                        elif selected_option == int('5'):
                            print('---------------------------------------')
                            print('This is Current Bank Account Type:', allrec[cnt][6])
                            print('---------------------------------------')
                            while True:
                                if break_out_flag:
                                    break
                                conformation = input('Are you sure you would like to edit it? y/n: ')
                                if conformation.lower() == 'y':
                                    newemaill = input('Please Enter New Bank Account Type Saving/Current: ')
                                    allrec[cnt][6] = newemaill
                                    with open("customers_information.txt", "w") as fh:
                                        nor = len(allrec)
                                        for cnt in range(0, nor):
                                            rec = ":".join(allrec[cnt]) + "\n"
                                            fh.write(rec)
                                        print('\n')
                                        print('===================================')
                                        print('Info have Been Successfully Changed')
                                        print('===================================')
                                        break_out_flag = True
                                        break
                                elif conformation.lower() == 'n':
                                    break
                                else:
                                    print('\n')
                                    print("Invalid Input, please enter 'y' for yes or 'n' for no!")
                        elif selected_option == int('6'):
                            print('---------------------------------------')
                            print('This is Current Account Balance:', allrec[cnt][7])
                            print('---------------------------------------')
                            while True:
                                if break_out_flag:
                                    break
                                conformation = input('Are you sure you would like to edit it? y/n: ')
                                if conformation.lower() == 'y':
                                    newemaill = input('Please Enter New Account Balance: ')
                                    allrec[cnt][7] = newemaill
                                    with open("customers_information.txt", "w") as fh:
                                        nor = len(allrec)
                                        for cnt in range(0, nor):
                                            rec = ":".join(allrec[cnt]) + "\n"
                                            fh.write(rec)
                                        print('\n')
                                        print('===================================')
                                        print('Info have Been Successfully Changed')
                                        print('===================================')
                                        break_out_flag = True
                                        break
                                elif conformation.lower() == 'n':
                                    break
                                else:
                                    print('\n')
                                    print("Invalid Input, please enter 'y' for yes or 'n' for no!")
                        elif selected_option == int('7'):
                            break

                        else:
                            print("\n")
                            print('Please choose one of these options:')
                    except ValueError:
                        print("\n")
                        print('Invalid Input! Only numeric value is accepted')
        else:
            if break_out_flag:
                break
            print('=====================')
            print('Customer ID Not Found')
            print('=====================')
            while True:
                print('\n')
                print('1 => Search Again ')
                print('2 => Go back to tha main menu ')
                print('3 => Logout ')
                selected_option = input('Please choose one of these options: ')
                if selected_option == '1':
                    print('\n')
                    break
                if selected_option == '2':
                    print('\n')
                    admin_stuff_options(logindata)
                elif selected_option == '3':
                    exit_program()


# Function for checking customer balance.
def check_balance(logindata):
    allrec = []
    with open("customers_information.txt", "r") as fh:
        for line in fh:
            allrec.append(line.strip().split(":"))
    for cnt in range(0, len(allrec)):
        if (logindata[0] == allrec[cnt][0]):
            print('\n')
            print('=============================')
            print('Your Current balance is:', allrec[cnt][7])
            print('=============================')
            while True:
                print('\n')
                print('1 => Go back to the menu ')
                print('2 => Logout ')
                selected_option = input('Please choose one of these options: ')
                if selected_option == '1':
                    print('\n')
                    break
                elif selected_option == '2':
                    exit_program()


# Function for performing deposit.
def perform_deposit(logindata):
    while True:
        chkamnt = int(input('Please enter your deposit amount: '))
        if chkamnt < 50:
            print('\n')
            print('-> The deposit amount should be more or equal than 50 ')
            continue
        elif chkamnt >= 50:
            break
        else:
            print('Invalid Input! Only numeric value is accepted')
            continue
    allrec = []
    with open("customers_information.txt", "r") as fh:
        for line in fh:
            reclist = line.strip().split(":")
            allrec.append(reclist)
    nor = len(allrec)
    for cnt in range(0, nor):
        if (logindata[0] == allrec[cnt][0]):
            cusid = allrec[cnt][0]
            transid = genid('trans')
            oldamnt = (allrec[cnt][7])
            depamnt = str(chkamnt)
            addamnt = int(oldamnt) + int(depamnt)
            newamnt = str(addamnt)
            transtype = 'Deposit'
            curdate = datetime.date.today()
            curtime = datetime.datetime.now()
            date = str(curdate)
            time = str(curtime.strftime("%H:%M"))
            ind = cnt
            with open("transaction.txt", "a") as fh:
                rec = transid + ":" + cusid + ":" + transtype + ":" + depamnt + ":" + date + ":" + time + "\n"
                fh.write(rec)
            with open("customers_information.txt", "w") as fh:
                rec = allrec[ind][7] = newamnt
                nor = len(allrec)
                for cnt in range(0, nor):
                    rec = ":".join(allrec[cnt]) + "\n"
                    fh.write(rec)
    print('\n')
    print('============================================')
    print('Transaction Has Been Successfully Processed ')
    print('============================================')
    while True:
        print('\n')
        print('1 => Go back to the menu ')
        print('2 => Logout ')
        selected_option = input('Please choose one of these options: ')
        if selected_option == '1':
            print('\n')
            break
        elif selected_option == '2':
            exit_program()


# Function for performing withdrawal.
def perform_withdrawal(logindata):
    while True:
        chkamnt = int(input('Please enter your withdrawal amount: '))
        if chkamnt < 50:
            print('\n')
            print('-> The withdrawal amount should be more or equal than 50  ')
            continue
        elif chkamnt >= 50:
            break
        else:
            print('Invalid Input! Only numeric value is accepted')
            continue
    allrec = []
    with open("customers_information.txt", "r") as fh:
        for line in fh:
            reclist = line.strip().split(":")
            allrec.append(reclist)
    nor = len(allrec)
    for cnt in range(0, nor):
        if (logindata[0] == allrec[cnt][0]):
            cusid = allrec[cnt][0]
            accnttype = (allrec[cnt][6])
            oldamnt = (allrec[cnt][7])
            withamnt = str(chkamnt)
            dedamnt = int(oldamnt) - int(withamnt)
            transtype = 'Withdrawal'
            curdate = datetime.date.today()
            curtime = datetime.datetime.now()
            date = str(curdate)
            time = str(curtime.strftime("%H:%M"))
            if accnttype.lower() == 'saving':
                if int(dedamnt) >= 100:
                    transid = genid('trans')
                    newamnt = str(dedamnt)
                    ind = cnt
                    with open("transaction.txt", "a") as fh:
                        rec = transid + ":" + cusid + ":" + transtype + ":" + withamnt + ":" + date + ":" + time + "\n"
                        fh.write(rec)
                    with open("customers_information.txt", "w") as fh:
                        rec = allrec[ind][7] = newamnt
                        nor = len(allrec)
                        for cnt in range(0, nor):
                            rec = ":".join(allrec[cnt]) + "\n"
                            fh.write(rec)
                        print('\n')
                        print('============================================')
                        print('Transaction Has Been Successfully Processed ')
                        print('============================================')
                        print('\n')
                elif int(dedamnt) <= 100:
                    print('\n')
                    print('=========================================================')
                    print('We are sorry, withdrawal will affect the minimum balance ')
                    print('=========================================================')
            elif accnttype.lower() == 'current':
                if int(dedamnt) >= 500:
                    transid = genid('trans')
                    newamnt = str(dedamnt)
                    ind = cnt
                    with open("transaction.txt", "a") as fh:
                        rec = transid + ":" + cusid + ":" + transtype + ":" + withamnt + ":" + date + ":" + time + "\n"
                        fh.write(rec)
                    with open("customers_information.txt", "w") as fh:
                        rec = allrec[ind][7] = newamnt
                        nor = len(allrec)
                        for cnt in range(0, nor):
                            rec = ":".join(allrec[cnt]) + "\n"
                            fh.write(rec)
                        print('\n')
                        print('============================================')
                        print('Transaction Has Been Successfully Processed ')
                        print('============================================')
                        print('\n')
                elif int(dedamnt) <= 500:
                    print('\n')
                    print('=========================================================')
                    print('We are sorry, withdrawal will affect the minimum balance ')
                    print('=========================================================')
            while True:
                print('1 => Go back to the menu ')
                print('2 => Logout ')
                selected_option = input('Please choose one of these options: ')
                if selected_option == '1':
                    print('\n')
                    break
                elif selected_option == '2':
                    exit_program()


# Function for printing statement.
def bank_statement(logindata):
    allrec = []
    while True:
        while True:
            strdate = input('Please Enter Start Date (yyyy-mm-dd): ')
            if strdate == 'q':
                print('\n')
                customer_options(logindata)
            if len(str(strdate)) == 10:
                break
            else:
                print('\n')
                print("Please Enter the correct format or 'q' to go back (yyyy-mm-dd)")

        while True:
            enddate = input('Please Enter End Date (yyyy-mm-dd): ')
            if enddate == 'q':
                print('\n')
                customer_options(logindata)
            if len(str(enddate)) == 10:
                break
            else:
                print('\n')
                print("Please Enter the correct format or 'q' to go back (yyyy-mm-dd)")

        nor = 0
        with open("transaction.txt", "r") as fh:
            for line in fh:
                allrec.append(line.strip().split(":"))
        print("=" * 105)
        print(
            "NOR".center(7) + "|" + "Transaction ID".ljust(18) + "|" + "Customer ID".ljust(
                15) + "|" + "Trans Type".center(15)
            + "|" + "Trans Amount".center(15) + "|" + "Date".center(15) + "|" + "Time".center(14))
        print("=" * 105)
        for cnt in range(0, len(allrec)):
            if strdate <= allrec[cnt][4] and enddate >= allrec[cnt][4]:

                if (logindata[0] == allrec[cnt][1]):
                    nor += 1
                    print(str(nor).center(7) + "|" + allrec[cnt][0].ljust(18) + "|" + allrec[cnt][1].ljust(15) + "|" +
                          allrec[cnt][2].center(15)
                          + "|" + allrec[cnt][3].center(15) + "|" + allrec[cnt][4].center(15) + "|" + (
                                      allrec[cnt][5] + ":" + allrec[cnt][6]).center(15))
        print('\n\n')

        if nor == 0:
            print('Record Not found'.center(100))

        while True:
            user_selection = input('Would you like to try another date? y/n: ')
            if user_selection.lower() == 'y':
                break
            elif user_selection.lower() == 'n':
                customer_options(logindata)
            else:
                print('\n')
                print("Invalid Input, please enter 'y' for yes or 'n' for no!")


# Function for adding new customer accounts.
def add_customer_account():
    break_out_flag = False
    print('\n')
    print("----------------------------------------------- ")
    print("Fill up the following form or press 'q' to exit ")
    print("----------------------------------------------- ")
    while True:
        if break_out_flag:
            break
        usrname = input("Please enter customer name: ")
        if usrname == 'q':
            print('\n')
            break
        email = input('Please enter the Email: ')
        if email == 'q':
            print('\n')
            break
        phone = input('Please enter the Phone: ')
        if usrname == 'q':
            print('\n')
            break
        birthdate = input('Please enter the Date Of Birth yyyy-mm-dd: ')
        if usrname == 'q':
            print('\n')
            break
        gander = input('Please enter the Gander M/F: ')
        if usrname == 'q':
            print('\n')
            break
        account = input('Please enter the account type Saving/Current: ')
        balance = '0'
        if account.lower() == 'saving':
            balance = '100'
        elif account.lower() == 'current':
            balance = '500'
        acctype = "3"
        userid = genid("customer")
        print('\n')
        print('===================================')
        print('Account has Been Successfully Added')
        print('===================================')
        userpass = userid
        print('-> '"User ID :", userid)
        print('-> '"User Password:", userpass)
        print('-> '"User Name:", usrname)
        with open("userpass.txt", "a") as fh:
            rec = userid + ":" + userpass + ":" + usrname + ":" + acctype + "\n"
            fh.write(rec)
        with open("customers_information.txt", "a") as fh:
            rec = userid + ":" + usrname + ":" + email + ":" + phone \
                  + ":" + birthdate + ":" + gander + ":" + account.lower() + ":" + balance + "\n"
            fh.write(rec)
        while True:
            print('\n')
            print('1 => Go back to the menu ')
            print('2 => Logout ')
            selected_option = input('Please choose one of these options: ')
            if selected_option == '1':
                break_out_flag = True
                print('\n')
                break
            elif selected_option == '2':
                exit_program()


# Function for adding new admin staff accounts.
def add_admin_account():
    break_out_flag = False
    while True:
        if break_out_flag:
            break
        print('\n')
        usrname = input("Please enter admin name or 'q' to return: ")
        if usrname.lower() == 'q':
            break
        acctype = "2"
        print('\n')
        userid = genid("admin")
        userpass = userid
        print('===================================')
        print('Account has Been Successfully Added')
        print('===================================')
        print("-> User ID :", userid)
        print("-> User Password:", userpass)
        print("-> User Name:", usrname)
        with open("userpass.txt", "a") as fh:
            rec = userid + ":" + userpass + ":" + usrname + ":" + acctype + "\n"
            fh.write(rec)
        while True:
            print('\n')
            print('1 => Go back to the menu ')
            print('2 => Logout ')
            selected_option = input('Please choose one of these options: ')
            if selected_option == '1':
                print('\n')
                break_out_flag = True
                break
            elif selected_option == '2':
                exit_program()


# Function for exiting the program.
def exit_program():
    print("""
#############################################
#     Thanks For Using Our Bank System      #
#############################################
""")
    exit()


# Function for displaying a welcome message.
def welcome():
    print("""
#############################################
#       Welcome to our Bank System          #
#############################################
""")


welcome()

main()
