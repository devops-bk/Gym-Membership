from GymSupervisor import GymSupervisor
from GymMember import GymMember

print("-----------------------------------------")
print(" ********** World Gym Center ********** ")
print("-----------------------------------------")
print()
print("Greetings Supervisor !!")
print("Please choose from the below options given in the menu")


def options():

    print("1. Create Member")
    print("2. View Member")
    print("3. Delete Member")
    print("4. Update Member")
    print("5. Create Regimen")
    print("6. View Regimen")
    print("7. Delete Regimen")
    print("8. Update Regimen")
    print("0. Exit")
    print("\nEnter Your Choice")


options()

while True:

    option = int(input())

    if option == 1:
        print("Enter Member's Details:")
        name = str(input("Name: "))
        age = str(input("Age: "))
        gender = str(input("Gender: "))
        contactno = str(input("Mobile No.: "))
        emailid = str(input("Email ID: "))
        bmi = str(input("BMI:"))
        if bmi < '18.5':
            S = {'Monday': 'Chest', 'Tuesday': 'Biceps', 'Wednesday': 'Rest', 'Thursday': 'Back', 'Friday': 'Triceps', 'Saturday': 'Rest', 'Sunday': 'Rest'}
        elif bmi < '25':
            S = {'Monday': 'Chest', 'Tuesday': 'Biceps', 'Wednesday': 'Cardio/Abs', 'Thursday': 'Back', 'Friday': 'Triceps', 'Saturday': 'Legs', 'Sunday': 'Rest'}
        elif bmi < '30':
            S = {'Monday': 'Chest', 'Tuesday': 'Biceps', 'Wednesday': 'Abs/Cardio', 'Thursday': 'Back', 'Friday': 'Triceps', 'Saturday': 'Legs', 'Sunday': 'Cardio'}
        elif bmi > '30':
            S = {'Monday': 'Chest', 'Tuesday': 'Biceps', 'Wednesday': 'Cardio', 'Thursday': 'Back', 'Friday': 'Triceps', 'Saturday': 'Cardio', 'Sunday': 'Cardio'}

        duration = str(input("Membership Duration(in months[1,3,6,12]): "))
        member = GymMember(name, age, gender, contactno, emailid, bmi, duration)
        GymSupervisor.regimen[contactno] = S
        GymSupervisor.addmember(member)

    elif option == 2:
        enter_contactno = input("Enter contact number of member: ")
        for memID in GymSupervisor.members.keys():
            if memID == enter_contactno:
                print()
                member = GymSupervisor.members[memID]
                print("Name: ", member.getName())
                print("Age: ", member.getAge())
                print("Gender: ", member.getGender())
                print("Mobile No.: ", member.getContactno())
                print("Email ID: ", member.getEmailid())
                print("BMI: ", member.getBmi())
                print("Membership Duration: ", member.getDuration())
                break
            else:
                print("Member with this contact number doesn't exist, Please check the number !!! ")
        print("\n")

    elif option == 3:
        enter_contactno = input("Enter contact number of member you want to delete: ")
        try:
            for memID in GymSupervisor.members.keys():
                if memID == enter_contactno:
                    print("Member Deleted")
                GymSupervisor.members.pop(enter_contactno)

        except:
            print("Member doesn't exist\n")

    elif option == 4:
        enter_contactno = input("Enter contact number of member you want to extend or revoke duration: ")
        choose = input("Enter if you want to extend or revoke: ")
        if choose == "extend":
            for memID in GymSupervisor.members.keys():
                if memID == enter_contactno:
                    d = member.getDuration()
                    s = int(d) + int(input("Enter for how months you want it to be extended: "))
                    res = str(s)
                    member.setDuration(res)
                    print("Extended Successfully")
        elif choose == "revoke":
            for memID in GymSupervisor.members.keys():
                member = GymSupervisor.members[memID]
                if memID == enter_contactno:
                    member.setDuration("0")
                    print("Membership Revoked")

    elif option == 5:
        phone = input("Enter the contact number of member you want to create regimen of: ")
        for i in GymSupervisor.regimen:
            if i == phone:
                for j in GymSupervisor.regimen[i]:
                    GymSupervisor.regimen[i][j] = input(j + ":")

    elif option == 6:
        phone = input("Enter contact number of member: ")
        for i in GymSupervisor.regimen:
            if i == phone:
                for key, val in GymSupervisor.regimen[i].items():
                    print(key, ":", val)
        print("\n")

    elif option == 7:
        phone = input("Enter contact number of member you want to delete regimen of: ")
        for i in GymSupervisor.regimen:
            if i == phone:
                print("Regimen deleted !!!")
        GymSupervisor.regimen.pop(phone)
        print("\n")

    elif option == 8:
        phone = input("Enter contact number of member you want to update regimen of: ")
        for i in GymSupervisor.regimen:
            if i == phone:
                day = input("Enter the day which you want to update: ")
                for j in GymSupervisor.regimen[i]:
                    if j == day:
                        GymSupervisor.regimen[i][j] = input("Enter the workout: ")
                        print("Updated Successfully !!!")
        print("\n")

    elif option == 0:
        break

    else:
        print("Enter valid number")

    options()


def memoptions():

    print("\n******** Member Portal ********\n")
    print("1. My Regimen")
    print("2. My Profile")
    print("0. Exit")
    print("\nEnter your choice")


memoptions()


while True:

    option = int(input())

    if option == 1:
        phno = input("Enter your contact number: ")
        print("Regimen based on your BMI")
        for i in GymSupervisor.regimen:
            if i == phno:
                for key, val in GymSupervisor.regimen[i].items():
                    print(key, ":", val)

        print("\n")

    elif option == 2:
        phno = input("Enter your contact number: ")
        try:
            for memID in GymSupervisor.members.keys():
                if memID == phno:
                    member = GymSupervisor.members[memID]
                    name = member.getName()
                    age = member.getAge()
                    gender = member.getGender()
                    contactno = member.getContactno()
                    emailid = member.getEmailid()
                    bmi = member.getBmi()
                    duration = member.getDuration()
                    print("***** Your Profile *****")
                    print("Name: ", name)
                    print("Age: ", age)
                    print("Gender: ", gender)
                    print("Mobile No.: ", contactno)
                    print("Email ID: ", emailid)
                    print("BMI: ", bmi)
                    print("Membership Duration: ", duration)

        except:
            print("No user with this contact number exist")

    elif option == 0:
        break

    else:
        print("Enter valid number")

    memoptions()
