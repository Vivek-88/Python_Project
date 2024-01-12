import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Vivek Kumar")
    while(True) :
        x = input("Enter what you want to speak : ")
        if(x=="q") :
            os.system("say 'Bye Bye Friend'")
            break
        command = f"say {x}"
        os.system(command)
