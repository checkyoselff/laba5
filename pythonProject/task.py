import requests

token = input("Input token: ")
while True:
    command = input("Input number of command:\n"
                    "0 - create note\n"
                    "1 - read note by id\n"
                    "2 - get note info\n"
                    "3 - update note text\n"
                    "4 - delete note by id\n"
                    "5 - print list of notes\n"
                    "6 - exit\n")
    response = ""
    if command == '0':
        text = input("Input text: ")
        response = requests.post(f"http://localhost:8080/notes", params={"text": text, "token": token})
    if command == '1':
        id = input("Input id: ")
        response = requests.get(f"http://localhost:8080", params={"id": id, "token": token})
    if command == '2':
        id = input("Input id: ")
        response = requests.post(f"http://localhost:8080/notes/{id}/info", params={"id": id, "token": token})
    if command == '3':
        id = input("Input id: ")
        text = input("Input new text: ")
        response = requests.post(f"http://localhost:8080", params={"id": id, "text": text, "token": token})
    if command == '4':
        id = input("Input id: ")
        response = requests.delete(f"http://localhost:8080/notes/{id}/delete", params={"id": id, "token": token})
    if command == '5':
        response = requests.get(f"http://localhost:8080/list", params={"token": token})
    if command == '6':
        quit()
    if response != "":
        print(f"Status code: {response.status_code}\n"
              f"Response body: {response.json()}")
