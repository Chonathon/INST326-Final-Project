import numpy as np
import pandas as pd
import re
from typing import Dict, List, Union


question_type = Dict[str, str]
course_plan_type = Dict[str, List[str]]


def intro(questions: question_type) -> course_plan_type:
    """A series of questions that will be presented to the user to determine if 
    they have completed Benchmark courses.

    Args:
        questions (dict_str): Calling questions from a dict.
    """
    course_plan = {'Benchmarks_Met': list(), 'Benchmarks_Unmet': list()}
    print("Please answer all questions using \"yes\" or \"no\".")
    for q_key, q_val in questions.items():
        q_resp = input(q_key + ' ')
        while q_resp not in ('yes', 'no'):
            print("Please answer all questions using \"yes\" or \"no\".")
            q_resp = input(q_key + ' ')
        if q_resp == 'yes':
            course_plan['Benchmarks_Met'] += [q_val]
        else:
            course_plan['Benchmarks_Unmet'] += [q_val]
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
            psyc100 = info[info["course_id"] == "PSYC100"]
            stat100 = info[info["course_id"] == "STAT100"]
            inst_courses = info[info["dept_id"] == "INST"]
            inst_prgm = pd.concat([math115, psyc100, stat100, inst_courses])
            
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
        allprereqslist = re.findall(regex,str(find))
        onlyinstprereqs = [i for i in allprereqslist if i[0] == "I"  or i == "PSYC100"] 
         
        return onlyinstprereqs
    
    def credits(self, course):
        """Finds the number of credits in the given course.

        Args:
            course (str ): An INST program course code.

        Returns:
            int: Course credits as an integer.
        """
        find = self.inst_prgm.loc[self.inst_prgm["course_id"] == course]["credits"].values[0]
        return find
    
    
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

    def semester_one(self, from_course_plan: course_plan_type, num_courses: int = 5) -> course_plan_type:
        """
        students be allowed to choose courses for which he is potentially eligible. If that course entails
        prerequisites, they will be shown, and the student will have the opportunity to add them to his 
        course plan. If he meets all of the prerequisites, then the course will be added.
        
        (In other semesters), if certain benchmark courses haven't been completed by the time of the
        last possible semester, they will be forcibly added to the course plan.
        
        Args:
            from_course_plan (course_plan_type): a dictionary of met and unmet benchmarks.
            num_courses (int, 5): the number of courses you can take in a semester. Defaults to 5, 
            meaning 5 courses required to be taken in each semester.
        
        Returns:
            course_plan_type: sem_list , a list containing all selescted courses for the given semester.        
        """
        pd.set_option("display.max_columns", 6)
        pd.set_option("display.expand_frame_repr", False)
        pd.set_option("display.max_colwidth", None)
        pd.set_option("display.max_rows", None)
        done_list = [val for key, val in from_course_plan.items() if key in ("Benchmarks_Met")]
        done_list = [dli for sublist in done_list for dli in sublist]  # This flattens the list.
        todo_list = [val for key, val in from_course_plan.items() if key in ("Benchmarks_Unmet")]
        todo_list = [tli for sublist in todo_list for tli in sublist]  # This flattens the list.
        sem_list = list()
        while len(sem_list) < num_courses:
            # Select any available course.
            avail_courses = self.inst_prgm[np.logical_not(self.inst_prgm["course_id"].isin(done_list + sem_list))]
            # Core courses are not available if there are benchmark_I in our todo_list.
            if any([c in ('MATH115', 'PSYC100') for c in todo_list]):
                avail_courses = avail_courses[np.logical_not(avail_courses['core'])]
            if sem_list == list():
                print("You've chosen 0 courses for the first semester.")
            else:
                print(f"You've chosen {len(sem_list)} course(s) for the first semester: ",
                      ', '.join(sem_list), ".", sep="")
            choice = input("Choose a course by course ID that you'd like to take, "
                           "enter \"p\" to print out the available courses, or enter \"d\" when done: ")
            if choice == 'p':
                print(avail_courses[['course_id', 'name', 'credits', 'core', 'benchmark_I', 'benchmark_II']])
            elif choice == 'd':
                break
            elif choice in sem_list:
                print(f"{choice} is already in your course list for this semester.")
            elif choice not in list(avail_courses['course_id'].values):
                print(f"{choice} is not an available course for this program.")
            else:  # A valid choice (course_id) was selected.
                choice_prereqs = [c for c in self.prereq(course=choice) if c not in done_list]
                if choice_prereqs == list():
                    sem_list += [choice]
                    continue
                n = 0
                while n < len(choice_prereqs):
                    cpq = choice_prereqs[n]
                    cpq_prereqs = [c for c in self.prereq(course=cpq) if c not in done_list + choice_prereqs]
                    if cpq_prereqs == list():  # This prerequisite has no other prerequisites.
                        n += 1
                    else:
                        choice_prereqs = choice_prereqs[:n] + choice_prereqs[n + 1:] + cpq_prereqs
                choice_prereqs = sorted(list(set(choice_prereqs)))  # Keep only the unique prerequisites.
                while choice_prereqs != list():  # Make any wanted pre-requisite course choices (pq_choice).
                    # You can't add the same course twice, so prereqs_to_add makes them invalid options.
                    prereqs_to_add = [c for c in choice_prereqs if c not in sem_list]
                    if prereqs_to_add == list():  # You've added the prerequisites, but can't yet take the course.
                        print(f"You've added the prerequisites for {choice}, but can't yet take {choice}.")
                        break
                    print(f"You can take these prerequisites for {choice}: ", ', '.join(prereqs_to_add), ".", sep="")
                    pq_choice = input("Enter a prerequisite course ID, or enter \"o\" to select another course: ")
                    if pq_choice == 'o':
                        break
                    if pq_choice not in prereqs_to_add:
                        print(f"{pq_choice} is not a valid prerequisite course ID.")
                    else:
                        sem_list += [pq_choice]
                        if len(sem_list) == num_courses:
                            break
        # Reassert the chosen courses for the semester.
        if sem_list == list():
            print("You've chosen 0 courses for the first semester.")
        else:
            print(f"You've chosen {len(sem_list)} course(s) for the first semester: ", ', '.join(sem_list), ".", sep="")
        from_course_plan['Semester_1'] = sem_list
        from_course_plan['Benchmarks_Met'] += [c for c in sem_list if c in from_course_plan['Benchmarks_Unmet']]
        from_course_plan['Benchmarks_Unmet'] = [c for c in from_course_plan['Benchmarks_Unmet']
                                                if c not in from_course_plan['Benchmarks_Met']]
        return from_course_plan

    def semester_two(self, from_course_plan: course_plan_type, num_courses: int = 5) -> course_plan_type:
        """
        students be allowed to choose courses for which he is potentially eligible. If that course entails
        prerequisites, they will be shown, and the student will have the opportunity to add them to his 
        course plan. If he meets all of the prerequisites, then the course will be added. 
        
        (In Semester 2), if certain benchmark courses haven't been completed by the time of the
        last possible semester, they will be forcibly added to the course plan.
        
        Args:
            from_course_plan (course_plan_type): a dictionary of met and unmet benchmarks, 
            as well as semester course loads from previous semesters.
            num_courses (int, 5): the number of courses you can take in a semester. Defaults to 5,
            meaning 5 courses required to be taken in each semester.
            
        Returns:
            course_plan_type: sem_list , a list containing all selescted courses for the given semester.
        """       
        pd.set_option("display.max_columns", 6)
        pd.set_option("display.expand_frame_repr", False)
        pd.set_option("display.max_colwidth", None)
        pd.set_option("display.max_rows", None)
        done_list = [val for key, val in from_course_plan.items() if key in ("Benchmarks_Met", "Semester_1")]
        done_list = [dli for sublist in done_list for dli in sublist]  # This flattens the list.
        todo_list = [val for key, val in from_course_plan.items() if key in ("Benchmarks_Unmet")]
        todo_list = [tli for sublist in todo_list for tli in sublist]  # This flattens the list.
        sem_list = list()
        # In the second semester, all of the benchmark_I courses have to be completed.
        if any([c in ('MATH115', 'PSYC100') for c in todo_list]):
            sem_list = [c for c in todo_list if c in ('MATH115', 'PSYC100')]
        while len(sem_list) < num_courses:
            # Select any available course.
            avail_courses = self.inst_prgm[np.logical_not(self.inst_prgm["course_id"].isin(done_list + sem_list))]
            # Core courses are not available if there are benchmark_I in our todo_list.
            if any([c in ('MATH115', 'PSYC100') for c in todo_list]):
                avail_courses = avail_courses[np.logical_not(avail_courses['core'])]
            if sem_list == list():
                print("You've chosen 0 courses for the second semester.")
            else:
                print(f"You've chosen {len(sem_list)} course(s) for the second semester: ",
                      ', '.join(sem_list), ".", sep="")
            choice = input("Choose a course by course ID that you'd like to take, "
                           "enter \"p\" to print out the available courses, or enter \"d\" when done: ")
            if choice == 'p':
                print(avail_courses[['course_id', 'name', 'credits', 'core', 'benchmark_I', 'benchmark_II']])
            elif choice == 'd':
                break
            elif choice in sem_list:
                print(f"{choice} is already in your course list for this semester.")
            elif choice not in list(avail_courses['course_id'].values):
                print(f"{choice} is not an available course for this program.")
            else:  # A valid choice (course_id) was selected.
                choice_prereqs = [c for c in self.prereq(course=choice) if c not in done_list]
                if choice_prereqs == list():
                    sem_list += [choice]
                    continue
                n = 0
                while n < len(choice_prereqs):
                    cpq = choice_prereqs[n]
                    cpq_prereqs = [c for c in self.prereq(course=cpq) if c not in done_list + choice_prereqs]
                    if cpq_prereqs == list():  # This prerequisite has no other prerequisites.
                        n += 1
                    else:
                        choice_prereqs = choice_prereqs[:n] + choice_prereqs[n + 1:] + cpq_prereqs
                choice_prereqs = sorted(list(set(choice_prereqs)))  # Keep only the unique prerequisites.
                while choice_prereqs != list():  # Make any wanted pre-requisite course choices (pq_choice).
                    # You can't add the same course twice, so prereqs_to_add makes them invalid options.
                    prereqs_to_add = [c for c in choice_prereqs if c not in sem_list]
                    if prereqs_to_add == list():  # You've added the prerequisites, but can't yet take the course.
                        print(f"You've added the prerequisites for {choice}, but can't yet take {choice}.")
                        break
                    print(f"You can take these prerequisites for {choice}: ", ', '.join(prereqs_to_add), ".", sep="")
                    pq_choice = input("Enter a prerequisite course ID, or enter \"o\" to select another course: ")
                    if pq_choice == 'o':
                        break
                    if pq_choice not in prereqs_to_add:
                        print(f"{pq_choice} is not a valid prerequisite course ID.")
                    else:
                        sem_list += [pq_choice]
                        if len(sem_list) == num_courses:
                            break
        # Reassert the chosen courses for the semester.
        if sem_list == list():
            print("You've chosen 0 courses for the second semester.")
        else:
            print(f"You've chosen {len(sem_list)} course(s) for the second semester: ",
                  ', '.join(sem_list), ".", sep="")
        from_course_plan['Semester_2'] = sem_list
        from_course_plan['Benchmarks_Met'] += [c for c in sem_list if c in from_course_plan['Benchmarks_Unmet']]
        from_course_plan['Benchmarks_Unmet'] = [c for c in from_course_plan['Benchmarks_Unmet']
                                                if c not in from_course_plan['Benchmarks_Met']]
        return from_course_plan

    def semester_three(self, from_course_plan: course_plan_type, num_courses: int = 5) -> course_plan_type:
        """
        students be allowed to choose courses for which he is potentially eligible. If that course entails
        prerequisites, they will be shown, and the student will have the opportunity to add them to his 
        course plan. If he meets all of the prerequisites, then the course will be added. 
        
        Args:
            from_course_plan (course_plan_type): a dictionary of met and unmet benchmarks, 
            as well as semester course loads from previous semesters.
            num_courses (int, 5): the number of courses you can take in a semester. Defaults to 5,
            meaning 5 courses required to be taken in each semester.
        Returns:
            course_plan_type: sem_list , a list containing all selescted courses for the given semester.
        """ 
        pd.set_option("display.max_columns", 6)
        pd.set_option("display.expand_frame_repr", False)
        pd.set_option("display.max_colwidth", None)
        pd.set_option("display.max_rows", None)
        done_list = [val for key, val in from_course_plan.items()
                     if key in ("Benchmarks_Met", "Semester_1", "Semester_2")]
        done_list = [dli for sublist in done_list for dli in sublist]  # This flattens the list.
        todo_list = [val for key, val in from_course_plan.items() if key in ("Benchmarks_Unmet")]
        todo_list = [tli for sublist in todo_list for tli in sublist]  # This flattens the list.
        sem_list = list()
        while len(sem_list) < num_courses:
            # Select any available course.
            avail_courses = self.inst_prgm[np.logical_not(self.inst_prgm["course_id"].isin(done_list + sem_list))]
            # Core courses are not available if there are benchmark_II in our todo_list
            # and we will not be taking them all in this semester.
            if len(set([c for c in done_list + sem_list if c in ('STAT100', 'INST126', 'INST201')])) != 3:
                avail_courses = avail_courses[np.logical_not(avail_courses['core'])]
            if sem_list == list():
                print("You've chosen 0 courses for the third semester.")
            else:
                print(f"You've chosen {len(sem_list)} course(s) for the third semester: ",
                      ', '.join(sem_list), ".", sep="")
            choice = input("Choose a course by course ID that you'd like to take, "
                           "enter \"p\" to print out the available courses, or enter \"d\" when done: ")
            if choice == 'p':
                print(avail_courses[['course_id', 'name', 'credits', 'core', 'benchmark_I', 'benchmark_II']])
            elif choice == 'd':
                break
            elif choice in sem_list:
                print(f"{choice} is already in your course list for this semester.")
            elif choice not in list(avail_courses['course_id'].values):
                print(f"{choice} is not an available course for this program.")
            else:  # A valid choice (course_id) was selected.
                choice_prereqs = [c for c in self.prereq(course=choice) if c not in done_list]
                if choice_prereqs == list():
                    sem_list += [choice]
                    continue
                n = 0
                while n < len(choice_prereqs):
                    cpq = choice_prereqs[n]
                    cpq_prereqs = [c for c in self.prereq(course=cpq) if c not in done_list + choice_prereqs]
                    if cpq_prereqs == list():  # This prerequisite has no other prerequisites.
                        n += 1
                    else:
                        choice_prereqs = choice_prereqs[:n] + choice_prereqs[n + 1:] + cpq_prereqs
                choice_prereqs = sorted(list(set(choice_prereqs)))  # Keep only the unique prerequisites.
                while choice_prereqs != list():  # Make any wanted pre-requisite course choices (pq_choice).
                    # You can't add the same course twice, so prereqs_to_add makes them invalid options.
                    prereqs_to_add = [c for c in choice_prereqs if c not in sem_list]
                    if prereqs_to_add == list():  # You've added the prerequisites, but can't yet take the course.
                        print(f"You've added the prerequisites for {choice}, but can't yet take {choice}.")
                        break
                    print(f"You can take these prerequisites for {choice}: ", ', '.join(prereqs_to_add), ".", sep="")
                    pq_choice = input("Enter a prerequisite course ID, or enter \"o\" to select another course: ")
                    if pq_choice == 'o':
                        break
                    if pq_choice not in prereqs_to_add:
                        print(f"{pq_choice} is not a valid prerequisite course ID.")
                    else:
                        sem_list += [pq_choice]
                        if len(sem_list) == num_courses:
                            break
        # Reassert the chosen courses for the semester.
        if sem_list == list():
            print("You've chosen 0 courses for the third semester.")
        else:
            print(f"You've chosen {len(sem_list)} course(s) for the third semester: ",
                  ', '.join(sem_list), ".", sep="")
        from_course_plan['Semester_3'] = sem_list
        from_course_plan['Benchmarks_Met'] += [c for c in sem_list if c in from_course_plan['Benchmarks_Unmet']]
        from_course_plan['Benchmarks_Unmet'] = [c for c in from_course_plan['Benchmarks_Unmet']
                                                if c not in from_course_plan['Benchmarks_Met']]
        return from_course_plan

    def semester_four(self, from_course_plan: course_plan_type, num_courses: int = 5) -> course_plan_type:
        """
        students be allowed to choose courses for which he is potentially eligible. If that course entails
        prerequisites, they will be shown, and the student will have the opportunity to add them to his 
        course plan. If he meets all of the prerequisites, then the course will be added. 
        
        Args:
            from_course_plan (course_plan_type): a dictionary of met and unmet benchmarks, 
            as well as semester course loads from previous semesters.
            num_courses (int, 5): the number of courses you can take in a semester. Defaults to 5,
            meaning 5 courses required to be taken in each semester.
        Returns:
            course_plan_type: sem_list , a list containing all selescted courses for the given semester.
        """ 
        pd.set_option("display.max_columns", 6)
        pd.set_option("display.expand_frame_repr", False)
        pd.set_option("display.max_colwidth", None)
        pd.set_option("display.max_rows", None)
        done_list = [val for key, val in from_course_plan.items()
                     if key in ("Benchmarks_Met", "Semester_1", "Semester_2", "Semester_3")]
        done_list = [dli for sublist in done_list for dli in sublist]  # This flattens the list.
        todo_list = [val for key, val in from_course_plan.items() if key in ("Benchmarks_Unmet")]
        todo_list = [tli for sublist in todo_list for tli in sublist]  # This flattens the list.
        sem_list = list()
        # In the fourth semester, all of the benchmark_II courses have to be completed.
        if any([c in ('STAT100', 'INST126', 'INST201') for c in todo_list]):
            sem_list = [c for c in todo_list if c in ('STAT100', 'INST126', 'INST201')]
        while len(sem_list) < num_courses:
            # Select any available course.
            avail_courses = self.inst_prgm[np.logical_not(self.inst_prgm["course_id"].isin(done_list + sem_list))]
            if sem_list == list():
                print("You've chosen 0 courses for the fourth semester.")
            else:
                print(f"You've chosen {len(sem_list)} course(s) for the fourth semester: ",
                      ', '.join(sem_list), ".", sep="")
            choice = input("Choose a course by course ID that you'd like to take, "
                           "enter \"p\" to print out the available courses, or enter \"d\" when done: ")
            if choice == 'p':
                print(avail_courses[['course_id', 'name', 'credits', 'core', 'benchmark_I', 'benchmark_II']])
            elif choice == 'd':
                break
            elif choice in sem_list:
                print(f"{choice} is already in your course list for this semester.")
            elif choice not in list(avail_courses['course_id'].values):
                print(f"{choice} is not an available course for this program.")
            else:  # A valid choice (course_id) was selected.
                choice_prereqs = [c for c in self.prereq(course=choice) if c not in done_list]
                if choice_prereqs == list():
                    sem_list += [choice]
                    continue
                n = 0
                while n < len(choice_prereqs):
                    cpq = choice_prereqs[n]
                    cpq_prereqs = [c for c in self.prereq(course=cpq) if c not in done_list + choice_prereqs]
                    if cpq_prereqs == list():  # This prerequisite has no other prerequisites.
                        n += 1
                    else:
                        choice_prereqs = choice_prereqs[:n] + choice_prereqs[n + 1:] + cpq_prereqs
                choice_prereqs = sorted(list(set(choice_prereqs)))  # Keep only the unique prerequisites.
                while choice_prereqs != list():  # Make any wanted pre-requisite course choices (pq_choice).
                    # You can't add the same course twice, so prereqs_to_add makes them invalid options.
                    prereqs_to_add = [c for c in choice_prereqs if c not in sem_list]
                    if prereqs_to_add == list():  # You've added the prerequisites, but can't yet take the course.
                        print(f"You've added the prerequisites for {choice}, but can't yet take {choice}.")
                        break
                    print(f"You can take these prerequisites for {choice}: ", ', '.join(prereqs_to_add), ".", sep="")
                    pq_choice = input("Enter a prerequisite course ID, or enter \"o\" to select another course: ")
                    if pq_choice == 'o':
                        break
                    if pq_choice not in prereqs_to_add:
                        print(f"{pq_choice} is not a valid prerequisite course ID.")
                    else:
                        sem_list += [pq_choice]
                        if len(sem_list) == num_courses:
                            break
        # Reassert the chosen courses for the semester.
        if sem_list == list():
            print("You've chosen 0 courses for the fourth semester.")
        else:
            print(f"You've chosen {len(sem_list)} course(s) for the fourth semester: ",
                  ', '.join(sem_list), ".", sep="")
        from_course_plan['Semester_4'] = sem_list
        from_course_plan['Benchmarks_Met'] += [c for c in sem_list if c in from_course_plan['Benchmarks_Unmet']]
        from_course_plan['Benchmarks_Unmet'] = [c for c in from_course_plan['Benchmarks_Unmet']
                                                if c not in from_course_plan['Benchmarks_Met']]
        return from_course_plan

    def graduate(self, from_course_plan: course_plan_type, num_courses: int = 5) -> None:
        """To calculate if the 60 credits requirements have been met to graduate, 
        otherwise, they will receive a message that they are not on track to graduate on time.
        This mean they are required to start from the begining and complete course planner again
        to meet the 60 credits requirements.

        Args:
            from_course_plan (course_plan_type): a dictionary of met and unmet benchmarks, 
            as well as ALL semester course loads from ALL four previous semesters.
            num_courses (int, 5): the number of courses you can take in a semester. Defaults to 5,
            meaning 5 courses required to be added in each semester.
        """        
        course_plan_courses = [val for val in from_course_plan.values()]
        course_plan_courses = list(set([cpc for sublist in course_plan_courses for cpc in sublist]))
        completed_courses = self.inst_prgm[self.inst_prgm["course_id"].isin(course_plan_courses)]
        credit_sum = completed_courses['credits'].sum()
        if credit_sum >= 60:
            print("You're on track to graduate:")
            print(f"\tSemester 1: {', '.join(from_course_plan['Semester_1'])}")
            print(f"\tSemester 2: {', '.join(from_course_plan['Semester_2'])}")
            print(f"\tSemester 3: {', '.join(from_course_plan['Semester_3'])}")
            print(f"\tSemester 4: {', '.join(from_course_plan['Semester_4'])}")
        else:
            print("You're not on track to graduate:")


if __name__ == '__main__':
    cp_questions = {f'Have you taken {cid}?': cid for cid in ["MATH115", "PSYC100", "STAT100", "INST126", "INST201"]}
    course_plan = intro(questions=cp_questions)
    cp_inst = Inst(path="202008.json")
    # Add courses for the semesters.
    course_plan = cp_inst.semester_one(from_course_plan=course_plan)
    course_plan = cp_inst.semester_two(from_course_plan=course_plan)
    course_plan = cp_inst.semester_three(from_course_plan=course_plan)
    course_plan = cp_inst.semester_four(from_course_plan=course_plan)
    cp_inst.graduate(from_course_plan=course_plan)
