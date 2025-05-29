# mpin_4_and_6_digit_checker-
MPIN CHECKER SYSTEM - README


HOW TO RUN THE PROJECT:


1. Open terminal or command prompt.
2. Navigate to the project folder where interface.py is located.
3. Run the following command:

   <<<<"python interface.py">>>>

   This will launch the GUI interface to check pin strength.



 MODULES COVERED:


 PART A – Basic MPIN Strength Check  
• Detects common weak MPINs like: 1234, 0000, 111111, etc.  
• Recognizes patterns, repetitions, sequential digits.

 PART B – Demographic-Based Validation  
• Checks if MPIN contains sensitive dates:
   - User's date of birth
   - Spouse's date of birth
   - Anniversary date

 PART C – Output Formatting & User Interface  
• Shows clear color-coded result: WEAK or STRONG  
• Displays matched patterns or date information

PART D – Support for 6-Digit MPINs  
• Validates both 4-digit and 6-digit MPINs  
• Same checks apply (patterns, demographics)

 GUI-Based Interactive Tool  



 ABOUT TEST CASES:


We pre-defined test cases to ensure the accuracy of the pin checker.

<<<<`test_cases.py`>>>>>
•within which :
   - Weak MPINs (e.g. 1234, 000000, 1990, etc.)
   - Strong MPINs (random, non-patterned values)
   - Demographic-based matches (e.g. dob or anniversary used in MPIN)
• Both 4-digit and 6-digit MPINs tested.(10 per each)


 FILE STRUCTURE & ROLES:


 main.py  
 Used for backend MPIN checking logic — now moved to utils.py for modularity

 utils.py  
 Contains core logic functions:
  
 interface.py  
• This is the MAIN FILE to run  
• Launches a GUI using Tkinter  
• Collects user input (name, DOB, marital status, pin)  
• Calls validation logic from utils.py  
• Shows color-coded strength result  
• Can also display test case results *******

test_cases.py  
Contains structured test data  


 AUTHOR


Developed as part of a technical assessment . 
BY AANYA MITTAL - 229310435 
BTECH CSE HONOURS IN ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING 
applied for data science role @onebanc technologies 
