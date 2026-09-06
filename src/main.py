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
with open("output/sample-output.json", "w") as out:
    json.dump(results, out, indent=2)
