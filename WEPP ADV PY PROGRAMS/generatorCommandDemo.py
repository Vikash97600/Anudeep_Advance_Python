def userInputGen():
    while True:
        command=input("Enter a command (type 'exit' to quit): ")
        if command=='exit':
            break
        yield command

def processCommand():
    for command in userInputGen():
        print(f"Processing command: {command}")

processCommand()

