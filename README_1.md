**Online Shopping Discount System**  
A beginner-level Python program that calculates a customer's final  
   
 shopping amount after applying a discount based on the purchase amount  
   
 and premium membership status.  
This is **Problem 1** from a Python mentoring class assignment on  
   
 **Conditional Statements (`if`, `elif`, and `else`)**.  
**What the Program Does**  
The program asks the user to enter:  
- Customer name  
- Purchase amount (as a whole number)  
- Premium membership status (`yes` or `no`)  
It then checks the purchase amount, calculates the applicable discount,  
   
 and displays the original amount, discount percentage, discount amount,  
   
 and final amount.  
If the customer is a premium member and spends \$500 or more, the  
   
 program also displays a VIP benefits message.  
**Discount Rules**  
Purchase amount     Standard discount  
  
---  
\$500 or above                    20%  
   
 \$300--\$499                      15%  
   
 \$100--\$299                      10%  
   
 Below \$100                        0%  
Premium members receive an additional 5 percentage points of discount in the program.  
A purchase amount of zero or less is treated as invalid.  
   
**Example**  
**Input**  
```  
Enter Customer Name: Ahmed  
 Purchase amount: 600  
 Are you a premium member? (yes/no) yes  
   
```  
**Output**  
```  
             RESULTS  
   
 Original Amount: $600  
 Discount: 25%  
 Discount Amount: $150.0  
 Final Amount: $450.0  
   
 You are eligible for VIP benefits!  
   
                END  
   
```  
**How to Run**  
1. Make sure Python 3 is installed.  
2. Download or clone this repository.  
3. Open a terminal in the project folder.  
4. Run:  
```  
python "problem 1. purchase.py"  
   
```  
On some systems, use `python3` instead of `python`.  
**Concepts Practiced**  
- Getting user input with `input()`  
- Converting input to an integer with `int()`  
- Cleaning and normalizing text with `.strip()` and `.lower()`  
- Conditional statements: `if`, `elif`, and `else`  
- Comparison operators (`>=` and `<=`)  
- Updating a variable with `+=`  
- Calculating percentages  
- Displaying results with f-strings  
- Combining conditions with `and`  
**Notes**  
- The program expects the purchase amount to be a whole number.  
- Enter `yes` to receive the premium-member discount; other responses  
   
 are treated as non-premium.  
- The VIP message is displayed only when the customer is a premium  
   
 member and the purchase amount is at least \$500.  
- In the current code, a premium member purchasing for less than \$100  
   
 receives the additional 5% discount even though the standard  
   
 discount for that range is 0%.  
**Learning Context**  
This program was completed as an exercise in Python mentoring classes.  
   
 It is an early practice project focused on understanding conditional  
   
 logic and applying it to a simple shopping scenario.  
