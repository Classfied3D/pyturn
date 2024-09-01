import time
path = "pyturn/turn.go"
with open(path, "r+") as file:
    contents = file.read()
while True:
    time.sleep(0.02)
    with open(path, "r+") as file:
        if file.read() != contents:
            file.seek(0)
            file.write(contents)