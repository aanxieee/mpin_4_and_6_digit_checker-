from utils import check_common_and_demographic_mpin

test_cases = [
    # ---- 4-digit MPINs ----
    {"mpin": "1234", "dob": "1990-01-01", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "WEAK"},
    {"mpin": "0000", "dob": "1995-05-05", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "WEAK"},
    {"mpin": "1990", "dob": "1990-12-25", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "WEAK"},
    {"mpin": "2580", "dob": "1988-08-08", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "WEAK"},
    {"mpin": "1212", "dob": "1980-12-12", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "WEAK"},
    {"mpin": "4731", "dob": "1999-11-11", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "STRONG"},
    {"mpin": "8593", "dob": "2000-06-15", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "STRONG"},
    {"mpin": "7643", "dob": "1975-04-04", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "STRONG"},
    {"mpin": "4412", "dob": "2002-02-20", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "STRONG"},
    {"mpin": "3267", "dob": "1985-07-21", "spouse_dob": "0000-01-01", "anniversary": "0000-01-01", "expected": "STRONG"},

    # ---- 6-digit MPINs ----
    {"mpin": "123456", "dob": "1990-01-01", "spouse_dob": "1989-02-02", "anniversary": "2010-03-03", "expected": "WEAK"},
    {"mpin": "000000", "dob": "1995-05-05", "spouse_dob": "1995-06-06", "anniversary": "2020-07-07", "expected": "WEAK"},
    {"mpin": "199089", "dob": "1990-08-09", "spouse_dob": "1992-10-10", "anniversary": "2015-12-12", "expected": "WEAK"},
    {"mpin": "251290", "dob": "1990-12-25", "spouse_dob": "1988-05-01", "anniversary": "2017-04-02", "expected": "WEAK"},
    {"mpin": "070720", "dob": "1993-07-07", "spouse_dob": "1993-07-07", "anniversary": "2000-07-07", "expected": "WEAK"},
    {"mpin": "739205", "dob": "1980-01-01", "spouse_dob": "1985-02-02", "anniversary": "2010-03-03", "expected": "STRONG"},
    {"mpin": "948162", "dob": "1979-11-09", "spouse_dob": "1982-05-06", "anniversary": "2012-10-11", "expected": "STRONG"},
    {"mpin": "843920", "dob": "1991-12-31", "spouse_dob": "1994-01-01", "anniversary": "2015-05-05", "expected": "STRONG"},
    {"mpin": "265431", "dob": "1987-06-12", "spouse_dob": "1986-09-09", "anniversary": "2009-10-10", "expected": "STRONG"},
    {"mpin": "561827", "dob": "1999-02-17", "spouse_dob": "2000-03-03", "anniversary": "2022-04-04", "expected": "STRONG"},
]

def run_test_cases_and_get_output():
    results = []
    passed = 0
    for idx, case in enumerate(test_cases, 1):
        result = check_common_and_demographic_mpin(
            case["mpin"], case["dob"], case["spouse_dob"], case["anniversary"]
        )
        status = result["strength"]
        expected = case["expected"]

        success = status == expected
        if success:
            passed += 1

        results.append({
            "index": idx,
            "mpin": case["mpin"],
            "dob": case["dob"],
            "spouse_dob": case["spouse_dob"],
            "anniversary": case["anniversary"],
            "expected": expected,
            "actual": status,
            "result": "✅ Passed" if success else "❌ Failed"
        })

    return results, passed, len(test_cases)
