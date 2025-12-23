This project was developed as part of a technical assessment during an internship drive, focusing on security awareness, logic building, and user-centric validation.

MPIN Checker System – 4 Digit AND 6 Digit 
 Objective

To design a secure and user-friendly system that:

Detects weak MPINs

Prevents use of personally predictable numbers

Encourages stronger authentication practices

Works for both 4-digit and 6-digit MPINs

❓ Problem Statement

Many users choose MPINs that are:

Sequential (1234, 654321)

Repetitive (0000, 111111)

Personally identifiable (birth year, anniversary)

Such MPINs are easy to guess and pose serious security risks in banking and authentication systems.

💡 Solution Overview

The MPIN Checker System:

Validates MPIN length (4 or 6 digits)

Detects common weak patterns

Cross-checks MPINs against demographic dates

Provides instant feedback through a GUI interface

 Features & Modules
🔹 Part A – Basic MPIN Strength Check

Detects:

Sequential numbers (1234, 4567, 123456)

Repeated digits (0000, 111111)

Common weak MPINs

Works for both 4-digit and 6-digit MPINs

🔹 Part B – Demographic-Based Validation

Checks whether MPIN contains:

User’s Date of Birth

Spouse’s Date of Birth

Anniversary date

Flags MPINs derived from personal information

🔹 Part C – Output & User Interface

GUI built using Tkinter

Color-coded results:

 WEAK MPIN

 STRONG MPIN

Displays:

Detected patterns

Demographic matches (if any)

 Part D – 6-Digit MPIN Support

Same validation logic applied to:

4-digit MPINs

6-digit MPINs

Ensures consistency across PIN lengths

 How to Run the Project
Step-by-Step:

Open Terminal / Command Prompt

Navigate to the project directory

Run the following command:

python interface.py


The GUI window will open

Enter:

User details (name, DOB, marital status)

MPIN (4 or 6 digits)

View the strength result instantly

 Test Case Coverage

Predefined test cases are included to verify accuracy.

test_cases.py includes:

Weak MPINs

1234, 000000, 1990, etc.

Strong MPINs

Random, non-patterned values

Demographic-based matches

DOB / anniversary-based MPINs

10 test cases each for:

4-digit MPINs

6-digit MPINs

 Project Structure
mpin_4_and_6_digit_checker/
│
├── interface.py      # Main GUI file (Tkinter)
├── utils.py          # Core MPIN validation logic
├── test_cases.py     # Predefined test cases
└── README.md

File Roles:

interface.py

Main entry point

Handles GUI and user input

Displays strength results

utils.py

Contains all MPIN validation logic

Pattern detection & demographic checks

test_cases.py

Automated testing of weak/strong MPINs

🛠️ Technologies Used

Python

Tkinter (GUI)

Rule-based logic & pattern matching

Author

Aanya Mittal
Developed as part of a technical assessment during an internship drive.
