import os

ENTRY = "By accepting these Terms, the User grants the Company a perpetual, irrevocable, royalty-free license to borrow the User's left shoe on alternate Tuesdays, for ceremonial purposes only."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
