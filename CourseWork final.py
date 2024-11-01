#Initialize global dictionaries
MetaDetails = {}
Ranks = []
GroupName = []

# Function to add horse details
def ahd():
    while True:
        # Check if the race has begun
        condition = input("Enter 'yes' if the race has begun, and 'no' if not: ")

        if condition == 'yes':
            print("You can't add horse details after the race starts.")
            break
        elif condition == 'no':
            try:
                # Get input for new horse details
                HorseID = int(input("Enter horse ID: "))
            except ValueError:
                print("HorseID should be an integer.")
                continue
            if HorseID in MetaDetails:
                print("Horse ID already exists. Please choose a different ID.")
                continue
            HorseGroup = input("Enter group letter (A/B/C/D): ").upper()
            if HorseGroup not in ('A', 'B', 'C', 'D'):
                print("Invalid group letter. Choose (A/B/C/D).")
                continue
            try:
                # Get input for horse age and check if it is numeric
                HorseAge = int(input("Enter age: "))
            except ValueError:
                print("Age should be an integer.")
                continue

            MetaDetails[HorseID] = {
                'HorseName': input("Enter Horse name: "),
                'JockeyName': input("Enter jockey name: "),
                'Age': HorseAge,
                'Breed': input("Enter breed: "),
                'RaceRecord': input("Enter past race records: "),
                'Group': HorseGroup
            }

            # Update the file with horse details
            with open('CourseWork.txt', 'w') as f:
                for horse_id, details in MetaDetails.items():
                    f.write(f'Group {details["Group"]}: {str(details)}, HorseID: {horse_id}\n')

            add_another = input("Do you want to add another horse? (yes/no): ")
            if add_another.lower() != 'yes':
                break
        else:
            print("You have neither entered 'yes' nor 'no'")

# Function to delete horse details
def dhd():
    while True:
        # Check if the race has begun
        status = input("Has the race begun? Enter 'yes' or 'no': ")
        if status == 'yes':
            print("Race has begun. So I am not allowed to let you delete.")
            break
        elif status == 'no':
            # Get input for horse ID to be deleted
            DelHorseID = input("Enter the horse ID of the horse whose details need to be deleted: ")
            DelHorseID = int(DelHorseID)

            if DelHorseID in MetaDetails:
                # Delete horse details and update the file
                del MetaDetails[DelHorseID]
                with open('CourseWork.txt', 'w') as f:
                    for horse_id, details in MetaDetails.items():
                        f.write(f'Group {details["Group"]}: {str(details)}, HorseID: {horse_id}\n')
                print("Done deleting the particular data")
                break
            else:
                print("Horse ID not available. Please try again.")
        else:
            print("Oops, I think you made a typo. Maybe type again.")

# Function to update horse details
def uhd():
    # Check if the race has begun
    status = input("Has the race began? Enter 'yes' or 'no': ")
    if status == 'yes':
        print("Sorry, I am not allowed to let you update as the race has began.")
        pass
    elif status == 'no':
        # Get input for HorseID to be updated
        UpHorseID=input("Enter the horse ID of the horse whose details need to be changed: ")
        UpHorseID = int(UpHorseID)

        if UpHorseID in MetaDetails:
            # Update horse details and the file
            MetaDetails[UpHorseID] ={
                'HorseName' : input("Enter Horse name: "),
                'JockeyName' : input("Enter jockey name: "),
                'Age' : int(input("Enter age: ")),
                'Breed' : input("Enter breed: "),
                'RaceRecord' :  input("Enter past race records, if any: "),
                'Group' : input("Enter group letter (A,B,C,D): ")
            }
            with open('CourseWork.txt', 'w') as f:
                for horse_id, details in MetaDetails.items():
                    f.write(f'Group {details["Group"]}: {str(details)}, HorseID: {horse_id}\n')
            print("Done updating the particular data")
        else:
            print("Horse ID not available. ")
    else:
        print("Woops, I think you made a typo.")

# Function to view horse details
def vhd():
    Metalist = list(MetaDetails.keys())
    Metalist.sort()
    #print(Metalist)
    for horse_id in Metalist:
        print("Horse ID:", horse_id, MetaDetails[horse_id])

# Function to randomly select horses for the major round
def sdd():
    if len(MetaDetails) < 20:
        print("It is required to register 20 horses before selecting 4.")
        return
    listA=[]
    listB=[]
    listC=[]
    listD=[]

    with open('CourseWork.txt', 'r') as file:
        # Check if there are 20 registered horses
        file.seek(0)
        for line in file:
            # Sort horses into groups
            if line[6] == "A":
                x = line.strip()
                listA.append(x)
            elif line[6] == "B":
                x = line.strip()
                listB.append(x)
            elif line[6] == "C":
                x = line.strip()
                listC.append(x)
            elif line[6] == "D":
                x = line.strip()
                listD.append(x)
            else:
                print("You are supposed to give a horse a group among A/B/C/D only")

        import random
        # Select one horse randomly from each group
        print("The horse selected from ", random.choice(listA))
        print("The horse selected from ", random.choice(listB))
        print("The horse selected from ", random.choice(listC))
        print("The horse selected from ", random.choice(listD))

# Function to display winning horses
def whd():

    import random

    Grouplist = ["Group A", "Group B", "Group C", "Group D"]
    Timelist = []

    for i in range(4):
        Timelist.append(random.randint(1, 90))

    a = sorted(Timelist)
    Ranks.extend(a)

    first = Grouplist[Timelist.index(Ranks[0])]
    second = Grouplist[Timelist.index(Ranks[1])]
    third = Grouplist[Timelist.index(Ranks[2])]


    print("The 3rd place goes to: ", first)
    print("The 2nd place goes to: ", second)
    print("The 1st place goes to: ", third)

    groupname = [first, second, third]
    GroupName.extend(groupname)

# Function to visualize winning horses' times
def vwh():
    global Ranks, GroupName
    print(f"{GroupName[0]}: {'*' * (Ranks[0] // 10)} {Ranks[0]}s (1st Place)")
    print(f"{GroupName[1]}: {'*' * (Ranks[1] // 10)} {Ranks[1]}s (2nd Place)")
    print(f"{GroupName[2]}: {'*' * (Ranks[2] // 10)} {Ranks[2]}s (3rd Place)")

def esc():
    print("Program closed")

NEED = ''
while NEED != 'ESC':
    NEED = input("Enter the command of the respective action you need to take:\n• Type AHD for adding horse details.\n• Type UHD for updating horse details.\n• Type DHD for deleting horse details.\n• Type VHD for viewing the registered horses’ details table.\n• Type SHD for saving the horse details to the text file.\n• Type SDD for selecting four horses randomly for the major round.\n• Type WHD for displaying the Winning horses’ details.\n• Type VWH for Visualizing the time of the winning horses.\n• Type ESC to exit the program. \n")

    if NEED == 'AHD':
        ahd()
    elif NEED == 'DHD':
        dhd()
    elif NEED == 'UHD':
        uhd()
    elif NEED == 'VHD':
        vhd()
    elif NEED == 'SHD':
        print("The details are automatically saved every time you add, delete or update data.")
    elif NEED == 'SDD':
        sdd()
    elif NEED == 'WHD':
        whd()
    elif NEED == 'VWH':
        vwh()
    elif NEED == 'ESC':
        esc()
        break
    else:
        print("you have not typed one of the options given")




