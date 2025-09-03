from datetime import datetime

def add_note():
    note = input("Write your note for today : ")
    today = datetime.now().strftime("%Y-%m-%d")
    with open(f"{today}.txt", "w", encoding="utf-8") as file:
        file.write(note)
    print("Note saved.")

if __name__ == "__main__":
    add_note()