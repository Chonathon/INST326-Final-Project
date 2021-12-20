# INST326 - Team TBD

Team TBD's project revolves around course planning in information science major at the University of Maryland.  This would be helpful for people in community college backgrounds, which is where each of us in the group started.

We assume that the person using this code already has 60 credits from their previous institution and declared the information science major in this program.  We also made this because traversing through the Testudo @UMD and other websites for course requirements and requisites to graduate is tedious, so it would be nice to have all of this information in one place.

We got our information from the University Main GitHub repository.  Initially, our project starts with a questionnaire that asks about courses within Benchmark_I and Benchmark_II with a "yes" and "no" prompt.  If you've satisfied something from your previous institution, including courses from the Benchmarks list, you can cross them out.  If at the end of the questionnaire you find that you have not taken any of these classes, you can do them all in the first semester, then you can go straight into the second semester, the third semester, and the fourth semester which you will receive a message that all courses you have selected based on credit requirements, are the right one to be on track for graduation (otherwise you will need to start from the beginning.)


## Instructions

To properly use our program, you will need two files:

```txt
course-planner.py
202008.json
```
Then you can simply run the program through the command line by calling course-planner.py which will start the program. Answer the questionnaire and follow through with courses for the upcoming semesters to properly plan your school year.
Keywords that you may encounter during the use of this programs:
```txt
p:  It will print out all available from the dataframe.
d:  It will stop adding courses for that particular semester and will go the next one. Depending on what courses have been selected, this may delay the graduation, and the user need to start the program again.
```



## Attribution

(Shahin)
```txt
def intro
def semester_one
def semester_two
def semester_three
```

(Sean)

```txt
Class INST
 - def __init__
 - def prereq
 - def credits
 - def core
 - def benchmark_I
 - def benchmark_II
```

(Ekow)
```txt
def semester_four
def graduate
```

## Bibliography
 - [Readme Editor](https://readme.so/editor)
    Helped us properly format a Readme document
 - [UMDio Data](https://github.com/umdio/umdio-data)
    Source of the classes and prerequisites offered by UMD
 - [Real Python] (https://realpython.com/python-dicts/) Provided insight in to how to work with dictionaries that are within a dataframe.
