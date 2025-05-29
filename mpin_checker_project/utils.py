from datetime import datetime

def generate_date_combinations(date_str: str) -> set:
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return set()

    year_full = f"{date.year:04d}"      # 2003
    year_short = year_full[2:]          # 30
    month = f"{date.month:02d}"         # 13
    day = f"{date.day:02d}"             # 10

    combos = set()

    # 4-digit
    combos.update({
        day + month, month + day,
        year_short + month, month + year_short,
        year_short + day, day + year_short
    })

    # 6-digit
    combos.update({
        day + month + year_short,
        year_short + month + day,
        month + day + year_short,
        year_full + month + day,
        year_full + day + month,
        month + day + year_full,
        day + month + year_full
    })

    return combos

def demographic_check(mpin: str, user_dob: str, spouse_dob: str, anniversary: str) -> list:
    reasons = []

    if mpin in generate_date_combinations(user_dob):
        reasons.append("easy to guess — it matches your date of birth!")
    if mpin in generate_date_combinations(spouse_dob):
        reasons.append("easy to guess — it matches your spouse's date of birth!")
    if mpin in generate_date_combinations(anniversary):
        reasons.append("easy to guess — it matches your anniversary date!")

    return reasons  
from datetime import datetime



COMMON_4_DIGIT_MPINS = {
    "1234", "0000", "1111", "1212", "7777", "1004", "2000", "4444", "2222", "6969",
    "9999", "3333", "5555", "6666", "1122", "1313", "8888", "4321", "2001", "1010",
    "2580", "1230", "1110", "0001", "0852", "5683", "1998", "1211", "9990", "2220"
}

COMMON_6_DIGIT_MPINS = {
    "123456", "000000", "111111", "121212", "654321", "999999",
    "112233", "102030", "123123", "789456", "456123", "222222",
    "123321", "110110", "666666", "696969", "101010", "111222",
    "147258", "159753"
}

def is_sequential(mpin: str, ascending=True):
    sequence = ''.join(str((int(mpin[0]) + i) % 10) for i in range(len(mpin)))
    return mpin == sequence if ascending else mpin == sequence[::-1]

def is_repeated(mpin: str):
    return all(d == mpin[0] for d in mpin)

def is_mirrored(mpin: str):
    return mpin == mpin[::-1]

def check_common_and_demographic_mpin(mpin: str, user_dob: str, spouse_dob: str, anniversary: str) -> dict:
    reasons = []

    # common pin checks
    if len(mpin) == 4 and mpin in COMMON_4_DIGIT_MPINS:
        reasons.append("COMMONLY_USED")
    elif len(mpin) == 6 and mpin in COMMON_6_DIGIT_MPINS:
        reasons.append("COMMONLY_USED")

    if is_repeated(mpin):
        reasons.append("REPEATED_DIGITS")
    if is_sequential(mpin, ascending=True):
        reasons.append("SEQUENTIAL_ASC")
    elif is_sequential(mpin, ascending=False):
        reasons.append("SEQUENTIAL_DESC")
    if is_mirrored(mpin):
        reasons.append("MIRRORED_PATTERN")
    if mpin in {"2580", "159753", "147258"}:
        reasons.append("KEYBOARD_PATTERN")

    # demo check
    reasons += demographic_check(mpin, user_dob, spouse_dob, anniversary)

    return {
        "strength": "WEAK" if reasons else "STRONG",
        "reasons": list(set(reasons))  # to avoid duplicate
    }
