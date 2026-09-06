#!/usr/bin/env python3
import re, json
with open("input/raw-text.txt") as f:
    data = f.read()

patterns ={
        "official": re.compile(r"[a-zA-Z0-9._+-]+@alueducation\.com(?!\.)"),
        "alumni": re.compile(r"[a-zA-Z0-9._%+-]+@alumni\.alueducation\.com(?!\.)"),
        "si": re.compile(r"[a-zA-Z0-9._%+-]+@si\.alueducation\.com(?!\.)"),
        "general": re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}")
        }

results = {cat: patterns[cat].findall(data) for cat in patterns}



#phone number validation
phone_pattern = re.compile(
        r"(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?){2,3}\d{3,4}"
)
phones = phone_pattern.findall(data)

#validate phone numbers by digit length 
valid_phones, invalid_phones = [], []
for phone in phones:
    digits = re.sub(r"\D", "", phone)
    if 7 <= len(digits) <= 15:
        valid_phones.append(phone)
    else:
        invalid_phones.append(phone)


results["phones"] = {"valid": valid_phones, "invalid": invalid_phones}



with open("output/sample-output.json", "w") as out:
    json.dump(results, out, indent=2)
