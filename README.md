

### Short Description  
A Python-based **Banking Service System** to manage customer accounts, enabling user authentication, transactions (deposits/withdrawals), customer registration, and account statement generation with robust validation and file-based data storage.

---


1. **User Authentication:**  
   - Login page for all users (admin staff and customers).  
   - Displays the logged-in user's name on the main screen.  

2. **Admin Features:**  
   - A **default Super User Account** allows the creation of admin staff accounts.  
   - Admin staff can register new customers by entering their details into the system, generating a unique customer account number (sequence-based) and default password.  
   - Admin staff can update customer details, excluding the customer's ID and name.  
   - Admin and customers can generate **Statement of Account Reports** for specified periods, summarizing total deposits and withdrawals.  

3. **Customer Features:**  
   - Customers can log in using their unique account number and password.  
   - They can perform **deposits** and **withdrawals** with real-time balance updates, provided minimum balance requirements are met (RM100 for Savings Accounts and RM500 for Current Accounts).  
   - Passwords can be updated upon login.  

4. **Additional Features:**  
   - All customer and transaction details are stored in **text files** for persistence.  
   - The program enforces strict input validation to prevent errors and ensure data integrity.  
   - Supports modular, menu-driven programming for seamless navigation and clean code structure.  

---

### Project Highlights:  
- Ensuring validation and error handling for accurate operations.  
- Comprehensive reporting with detailed transaction history and period-based summaries.  
- Python-exclusive implementation, leveraging lists and functions without global variables.  
- Good programming practices such as comments, meaningful variable names, and proper indentation.  

---

