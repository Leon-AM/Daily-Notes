from datetime import datetime

def add_note():
    note = input("یادداشت امروزت رو بنویس: ")
    today = datetime.now().strftime("%Y-%m-%d")
    with open(f"{today}.txt", "w", encoding="utf-8") as file:
        file.write(note)
    print("یادداشت ذخیره شد! ✅")

if __name__ == "__main__":
    add_note()