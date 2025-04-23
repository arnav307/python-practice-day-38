def quiz():
    Score=0
    while True:
        try:
            user=input("what is the capital city of Nepal ?").lower()
            if user=="kathmandu":
                Score+=1
            user=input("what is the capital city of india?").lower()
            if user=="New delhi":
                Score+=1
            user=input("What is the capital city of china?").lower()
            if user=="bejing":
                Score+=1
                
            
            
            user_stop=input("Quit or continue (Q) for Quit and (C) for continue")
            if user_stop!="c":
                break

                
        except ValueError:
            print("Please enter a string instead of integer!!!!!")
    return Score
def Filename():
    file_user=input("Do you want show in File(f) or console for (c) ?: ")
    result=quiz()
    try:
        if file_user=='f':
            score_entry=input("Enter  a file name!!: ")
            with open(score_entry,'w') as filename:
                filename.write(f"You have score {result}")
                print("score saved to the file check it!!!!!!!!!!!")
        else:
           print(f"You have score {result} correct")
    except FileExistsError:
        print("Your file does not exist")
Filename()
