from datetime import datetime
datenow = datetime.now()
formatted_date = datenow.strftime("%y-%m-%d %H:%M:%S")

with open("rwx/log.txt","w") as f:
    f.write("Hello world!\n")


while True:
    logs = input("Input message: ")
    if logs == "exit".strip().casefold():
        print("Save changed")
        break
    else:
        with open("rwx/log.txt","a") as f:
            f.write(f"\n[{formatted_date}]")
            f.write(logs)

    