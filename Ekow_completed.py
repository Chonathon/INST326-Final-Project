def semester_two(self):
    
    print(f" Great job {self.name} you have made it to the next semester, here are the classes you are to take this semester")
    print("Here are the core classes that must be completed in order to graduate")
    
    print(self.inst_prgm[self.inst_prgm["core"] == True])
    
    

            # self.classes_taken throughout the semesters
            #initialize classes_taken at beginning of class
    self.classes_taken = []
                
    choice1 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice1].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice1 in self.classes_taken:
        print(f"You have already picked {choice1}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice1)
    elif courses == []:
        self.classes_taken.append(choice1)
    else:
        print(f"You need these courses to resister for {choice1}: {courses}")
        
    
    choice2 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice2].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice2 in self.classes_taken:
        print(f"You have already picked {choice2}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice2)
    elif courses == []:
        self.classes_taken.append(choice2)
    else:
        print(f"You need these courses to resister for {choice2}: {courses}")
        
        
    choice3 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice3].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice3 in self.classes_taken:
        print(f"You have already picked {choice3}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice3)
    elif courses == []:
        self.classes_taken.append(choice3)
    else:
        print(f"You need these courses to resister for {choice3}: {courses}")
        
        
    choice4 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice4].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice4 in self.classes_taken:
        print(f"You have already picked {choice4}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice4)
    elif courses == []:
        self.classes_taken.append(choice4)
    else:
        print(f"You need these courses to resister for {choice4}: {courses}")
        
        
    choice5 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice5].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice5 in self.classes_taken:
        print(f"You have already picked {choice5}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice5)
    elif courses == []:
        self.classes_taken.append(choice5)
    else:
        print(f"You need these courses to resister for {choice5}: {courses}")
        
    
    print("These are the classes you have taken so far")    
    print(self.classes_taken)

    credits = len(self.classes_taken)* 3
    print(f"You have taken {credits} credits so far")
    
    
def semester_three(self):
    name = "James"
    print(f"Congratulations {name} you have made it into your third semester. You're almost there!")
    print("This semester you may be able to choose upper level elective classes, here are some you can choose from")
    
    print(self.inst_prgm[self.inst_prgm["core"] == False])
    
    choice6 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice6].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice6 in self.classes_taken:
        print(f"You have already picked {choice6}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice6)
    elif courses == []:
        self.classes_taken.append(choice6)
    else:
        print(f"You need these courses to resister for {choice6}: {courses}")
        
    
    
    choice7 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice7].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice7 in self.classes_taken:
        print(f"You have already picked {choice7}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice7)
    elif courses == []:
        self.classes_taken.append(choice7)
    else:
        print(f"You need these courses to resister for {choice7}: {courses}")
        
    
    
    choice8 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice8].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice8 in self.classes_taken:
        print(f"You have already picked {choice8}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice8)
    elif courses == []:
        self.classes_taken.append(choice8)
    else:
        print(f"You need these courses to resister for {choice8}: {courses}")
        
        
    choice9 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice9].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice9 in self.classes_taken:
        print(f"You have already picked {choice9}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice9)
    elif courses == []:
        self.classes_taken.append(choice9)
    else:
        print(f"You need these courses to resister for {choice9}: {courses}")
        
        
    choice10 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice10].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice10 in self.classes_taken:
        print(f"You have already picked {choice10}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice10)
    elif courses == []:
        self.classes_taken.append(choice10)
    else:
        print(f"You need these courses to resister for {choice10}: {courses}")
        
    
    print("These are the classes you have taken so far")    
    print(self.classes_taken)

    credits = len(self.classes_taken)* 3
    print(f"You have taken {credits} credits so far")
    
    
def semester_four(self):
    print(f"Congratulations {self.name} you have made it throught the third semester. Now it is time for you to tackle your last semester!")
    print("Make sure you take all your core classes")
    
    choice11 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice11].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice11 in self.classes_taken:
        print(f"You have already picked {choice11}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice11)
    elif courses == []:
        self.classes_taken.append(choice11)
    else:
        print(f"You need these courses to resister for {choice11}: {courses}")
        
        
    choice12 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice12].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice12 in self.classes_taken:
        print(f"You have already picked {choice12}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice12)
    elif courses == []:
        self.classes_taken.append(choice12)
    else:
        print(f"You need these courses to resister for {choice12}: {courses}")
        
        
    choice13 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice13].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice13 in self.classes_taken:
        print(f"You have already picked {choice13}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice13)
    elif courses == []:
        self.classes_taken.append(choice13)
    else:
        print(f"You need these courses to resister for {choice13}: {courses}")
        
        
    choice14 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice14].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice14 in self.classes_taken:
        print(f"You have already picked {choice14}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice14)
    elif courses == []:
        self.classes_taken.append(choice14)
    else:
        print(f"You need these courses to resister for {choice14}: {courses}")
        
        
    choice15 = input("What other class would you like to enrol in?")
    course = [d.get("prereqs") for d in self.inst_courses[self.inst_courses["course_id"] == choice15].relationships]
    regex = r"""
    (?xm)
    (?P<course>[A-Z]+\d+)
    """
    courses = re.findall(regex, str(course))
    if choice15 in self.classes_taken:
        print(f"You have already picked {choice15}")
    elif courses in self.classes_taken:
        self.classes_taken.append(choice15)
    elif courses == []:
        self.classes_taken.append(choice15)
    else:
        print(f"You need these courses to resister for {choice15}: {courses}")
        
def graduate(self):
    core_classes = ["INST311", "INST314", "INST326", "INST327","INST335","INST346"]
    if credits == 60 and core_classes in self.classes_taken :
        print("All major requirements have been satisfied. Congratulations!")
    else:
        print("You have not met the graduation requirements to graduate")