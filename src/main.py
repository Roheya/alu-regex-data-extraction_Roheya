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

#credit card number extraction
card_pattern = re.compile(r"\b(?:\d{4}[-]?){3}\d{4}\b")
cards = card_pattern.findall(data)

def mask_card(card):
    digits = re.sub(r"\D", "", card)
    return "**** **** **** " + digits[-4:]
masked_cards = [mask_card(card) for card in cards]
results["credit_cards"] = {"masked": masked_cards}

with open("output/sample-output.json", "w") as out:
    json.dump(results, out, indent=2)
