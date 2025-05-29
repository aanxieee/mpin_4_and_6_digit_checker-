from utils import demographic_check
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)  

# common pins
COMMON_4_DIGIT_MPINS = {
    "1234", "0000", "1111", "1212", "7777", "1004", "2000", "4444", "2222", "6969",
    "9999", "3333", "5555", "6666", "1122", "1313", "8888", "4321", "2001", "1010",
    "2580", "1230", "1110", "0001", "0852", "5683", "1998", "1211", "9990", "2220"
}
# taken from online server reports 
COMMON_6_DIGIT_MPINS = {
    "123456", "000000", "111111", "121212", "654321", "999999",
    "112233", "102030", "123123", "789456", "456123", "222222",
    "123321", "110110", "666666", "696969", "101010", "111222",
    "147258", "159753"
}

# pattern help
def is_sequential(mpin: str, ascending=True):
    sequence = ''.join(str((int(mpin[0]) + i) % 10) for i in range(len(mpin)))
    return mpin == sequence if ascending else mpin == sequence[::-1]

def is_repeated(mpin: str):
    return all(d == mpin[0] for d in mpin)

def is_mirrored(mpin: str):
    return mpin == mpin[::-1]

# Logic
def check_common_mpin(mpin: str) -> list:
    reasons = []

    if len(mpin) == 4 and mpin in COMMON_4_DIGIT_MPINS:
        reasons.append("commonly used PINs like 1234, 0000 etc.")
    elif len(mpin) == 6 and mpin in COMMON_6_DIGIT_MPINS:
        reasons.append("commonly used 6-digit PINs like 123456 etc.")

    if is_repeated(mpin):
        reasons.append("all digits are repeated")
    if is_sequential(mpin, ascending=True):
        reasons.append("digits are in ascending order")
    elif is_sequential(mpin, ascending=False):
        reasons.append("digits are in descending order")
    if is_mirrored(mpin):
        reasons.append("the MPIN is a mirrored pattern")
    if mpin in {"2580", "159753", "147258"}:
        reasons.append("keyboard pattern used")

    return reasons

# rum loop
if __name__ == "__main__":
    print(Fore.CYAN + " Welcome to MPIN Checker System")

    while True:
        name = input("\nPlease enter your name: ").strip()
        want_questions = input(f"{name}, can I ask you a few questions before setting your MPIN? (yes/no): ").strip().lower()

        mpin_input = input("Enter your MPIN (4 or 6 digits): ").strip()

        if not (len(mpin_input) in [4, 6] and mpin_input.isdigit()):
            print(Fore.RED + " Invalid input. Please enter a 4 or 6 digit MPIN.")
            continue


        reasons = check_common_mpin(mpin_input)

        if want_questions == "yes":
            user_dob = input("Enter your DOB (YYYY-MM-DD): ").strip()
            spouse_dob = input("Enter your Spouse's DOB (YYYY-MM-DD): ").strip()
            anniversary = input("Enter your Wedding Anniversary (YYYY-MM-DD): ").strip()
            reasons += demographic_check(mpin_input, user_dob, spouse_dob, anniversary)

        # output with color
        if reasons:
            print(Fore.RED + f"\nSorry {name}, you can't keep this MPIN. Reasons:")
            for reason in reasons:
                print(Fore.YELLOW + f" {reason}")
            print(Fore.RED + "\nResult: WEAK ")
        else:
            print(Fore.GREEN + f"\nGreat choice {name}! Your MPIN is STRONG ")

        # retry loop
        again = input("\nWould you like to check another MPIN? (yes/no): ").strip().lower()
        if again != "yes":
            print(Fore.CYAN + "\nThank you for using MPIN Checker System!")
            break
