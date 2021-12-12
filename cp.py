import pandas as pd
import re
from typing import Dict, List, Union

cp_questions = {'Benchmark_I': [{'prompt': 'Have you taken MATH115?', 'label': 'MATH115', 'yes': True, 'no': False},
                                {'prompt': 'Have you taken PSYC100?', 'label': 'PSYC100', 'yes': True, 'no': False}],
                'BenchMark_II': [{'prompt': 'Have you taken STAT100?', 'label': 'STAT100', 'yes': True, 'no': False},
                                 {'prompt': 'Have you taken INST126?', 'label': 'INST126', 'yes': True, 'no': False},
                                 {'prompt': 'Have you taken INST201?', 'label': 'INST201', 'yes': True, 'no': False}]
                }


def intro(questions: Dict[str, List[Dict[str, Union[str, bool]]]]) -> Dict[str, bool]:
    """[summary]

    Args:
        questions (Dict[str, List[Dict[str, Union[str, bool]]]]): [description]

    Returns:
        Dict[str, bool]: [description]
    """    
    print("Please answer all questions using \"yes\" or \"no\".")
    course_plan = dict()
    for q_keys, q_vals in questions.items():
        for qv in q_vals:
            q_resp = input(qv['prompt'] + ' ')
            while q_resp not in ('yes', 'no'):
                print("Please answer all questions using \"yes\" or \"no\".")
                q_resp = input(qv['prompt'] + ' ')
            course_plan[qv['label']] = qv[q_resp]
    return course_plan


# Provided Class for dataframe
class Inst:
    """Creates a new dataframe out of data gathered the original JSON file.
    In addition to the available attributes, this class creates 
    columns to identify courses as being core, benchmark I, or benchmark II.
    """
    def __init__(self, path):
         with open(path, 'r', encoding='utf-8') as df:
            df = pd.read_json(path)
            info = df[["course_id", "dept_id", "name", "credits", "relationships"]]
            math115 = info[info["course_id"] == "MATH115"]
            psych100 = info[info["course_id"] == "PSYCH100"]
            stat100 = info[info["course_id"] == "STAT100"]
            inst_courses = info[info["dept_id"] == "INST"]
            inst_prgm = pd.concat([math115, psych100, stat100, inst_courses])
            
            # creating core attribute and identifying core classes as True
            core = False
            inst_prgm["core"] = core
            inst_prgm.loc[inst_prgm['course_id'] == 'INST201', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST311', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST314', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST326', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST327', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST335', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST346', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST352', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST362', ['core']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST490', ['core']] = True
            
            # creating benchmark attribute and identifying benchmark courses as 
            # True
            benchmark_I = False
            inst_prgm["benchmark_I"] = benchmark_I

            inst_prgm.loc[inst_prgm['course_id'] == 'MATH115', ['benchmark_I']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'PSYCH100', ['benchmark_I']] = True
            
            benchmark_II = False
            inst_prgm["benchmark_II"] = benchmark_II

            inst_prgm.loc[inst_prgm['course_id'] == 'STAT100', ['benchmark_II']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST126', ['benchmark_II']] = True
            inst_prgm.loc[inst_prgm['course_id'] == 'INST201', ['benchmark_II']] = True
            
            self.inst_prgm = inst_prgm 
             
    def prereq(self, course):
        """Identifies the prerequisite classes for the given course in the INST 
        program

        Args:
            course (str): An INST program course code.

        Returns:
            list: Items are course id's for the prerequisite classes
        """
        find = ([d.get("prereqs") for d in self.inst_prgm[self.inst_prgm
                                        ["course_id"] == course].relationships])
        regex = r"""(?xm)
        (?P<course>[A-Z]+\d+)
        """
        return re.findall(regex,str(find))
    
    def core(self, course):
        """Identifies whether a class is a 'core' class to the INST program.

        Args:
            course (str): An INST program course code.

        Returns:
            boolean: True if the class is a core class, False if the class is 
            not.
        """
        find = self.inst_prgm.loc[self.inst_prgm["course_id"] == course]["core"].values[0]
        return find
    
    def benchmark_I(self, course):
        """Identifies whether a class is a 'benchmark_I' class to the INST 
        program.

        Args:
            course (str): An INST program course code.

        Returns:
            boolean: True if the class is a benchmark_I class, False if the 
            class is not.
        """
        find = self.inst_prgm.loc[self.inst_prgm["course_id"] == course]["benchmark_I"].values[0]
        return find
  
    def benchmark_II(self, course):
        """Identifies whether a class is a 'benchmark_II' class to the INST 
        program.

        Args:
            course (str): An INST program course code.

        Returns:
            boolean: True if the class is a benchmark_II class, False if the 
            class is not.
        """
        find = self.inst_prgm.loc[self.inst_prgm["course_id"] == course]["benchmark_II"].values[0]
        return find

    def semester_one(self, from_bm_stats: Dict[str, bool], course_num: int = 5) -> List[str]:
        sem_list = list()
        while len(sem_list) < course_num:
            pass  # TODO: Fill in needed courses and allow the user to pick other courses.
        return sem_list

    def semester_two(self):

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

        credits = len(self.classes_taken) * 3
        print(f"You have taken {credits} credits so far")


    def semester_three(self):

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
        print(f"Congratulations {self.applicant} you have made it throught the third semester. Now it is time for you "
              f"to tackle your last semester!")
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
        

if __name__ == '__main__':
    course_plan = dict()
    cp_inst = Inst(path="202008.json")
    course_plan['Semester 1'] = cp_inst.semester_one(from_bm_stats=intro(questions=cp_questions))
