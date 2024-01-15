#this code is for building the car game
command=""
started=False
while True:
    command=input(">")
    if command.lower()=="start":
        if started:
            print("Car is already started....")
        else:
            started=True
            print("Car is started....")

    elif command.lower()=="stop":
        if not started:
            print("Car is already stopped..")
        else:
            started=False
            print("Car is stopped..")

    elif command.lower()=="help":
        print("""
              start-to start the car
              stop-to stop the car
              quit-to quit
              """)

    elif command.lower()=="quit":
        break
    else:
        print("Wrong command")
        
    
