from pyscript import document

def checkMember(e):
    # values
    fname_value = document.querySelector("#fname").value.strip()
    lname_value = document.querySelector("#lname").value.strip()
    # https://mimo.org/glossary/python/string-strip
    # https://www.w3schools.com/jsref/met_document_queryselector.asp
    
    full_name = f"{fname_value} {lname_value}".title() 
    # https://www.geeksforgeeks.org/python/title-in-python/
    
    # member list
    club_members = ["Prince Villanueva", "Neo Macaraig", "Georgina Banal", "Isaias Berdin", "Cameron Bufford"]
    
    member = full_name in club_members
    
    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }
    
    output_element = document.querySelector("#output1")
    output_element.innerText = messages[member]