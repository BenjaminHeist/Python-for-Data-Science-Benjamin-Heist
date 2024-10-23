Read-Me for the repository 'Python-for-Data-Science-Benjamin-Heist'. 

This repository contains the individual assignments of this Python course and will be updated continiously. There will be a new branch for each assignment. In the end these branches will be deleted eventually so that all assignments are just in the main branch. 

ASSIGNMENT 1 

- In the notebook you will find exercises 1-17 of Individual Assignment 1, followed by the respective code solutions in the subsequent cells.

- In order to run all of the cells correctly Python version 3.10 or higher is needed. 

ASSIGNMENT 2 

- In this notebook you'll find exercises 1-4 related to Individual Assignment 2. You can see the tasks followed by che respective code solutions in the subsequent cells.

Assumptions: 

- The instructions stated: "You will update your first repository, and for each exercise (after creating the readme), create an individual branch."
However, I interpreted this to mean that we should create a new branch for each assignment, rather than for each exercise. As a result, I have created a single branch for Assignment 2, instead of separate branches for each exercise. I hope this approach is acceptable.

- In Exercise 4, where it says "Print the Result: Output the converted temperature for 22°F, 46°F, 51°F, and 76°F", I assumed the temperatures were meant to be in Celsius, since we were asked to create a celsius_to_fahrenheit converter. Therefore, I converted the Celsius values to Fahrenheit, rather than the other way around.

ASSIGNMENT 3 

This project is a simple Python implementation of a course registration system with students, courses, and a central registration system. It allows students to enroll in courses, drop them, view their registered courses, and calculate their GPA. The system also manages a list of all students and available courses.

Features Implemented

1. Course Class
- Each course has a name, description, and a list of enrolled students.
- Methods:
  - Add a student to the course.
  - Remove a student from the course.
  - Show all students in the course.
2. Student Class
- Each student has a name, ID number, address, and a list of enrolled courses.
- Methods:
  - Enroll in a course.
  - Drop a course.
  - Show all registered student courses.
3. Registration Class
- Manages a list of students and courses.
- Methods:
  - Enroll a student in a course.
  - Drop a student from a course.
  - Show all enrolled students.
  - Show all available courses.
  - Show all courses a specific student is enrolled in.
  - Show all students in a specific course.
4. Grading System and GPA Calculation
- Each student can receive grades for their courses.
- A method to calculate the GPA of a student based on their grades has been implemented.
- Methods:
  - Set grade for a course.
  - Calculate and show GPA based on enrolled courses and grades.


ASSIGNMENT 4

This repository contains a Python script to analyze a set of annotation files stored in a zip file. Each file follows a specific naming convention:
{DATE}_{TIME}_SN{SATELLITE_NUMBER}_QUICKVIEW_VISUAL_{VERSION}_{UNIQUE_REGION}.txt

The file used can be found here: https://ecampus.esade.edu/pluginfile.php/185972110/mod_resource/content/1/session_4.zip

Task Overview
The script provides answers to the following questions based on the annotation files:

1. Total Files: How many annotation files are in the folder.
2. Valid Naming Convention: How many files follow the specified naming convention.
3. Annotations by Month and Year:
- Count of annotations for each month and year.
- Identify the month with the highest number of annotations.
4. Organize Files by Month:
- A new folder structure is created with subfolders for each month, and files are moved to the corresponding month folder.
5. Sort Annotations by Date: Print all annotation filenames from the most recent to the oldest.
6. Satellite Analysis:
- How many different satellites are represented.
- Count of annotations for each satellite.
- Identify which satellite was used in the most recent annotation file.
7. Unique Regions: How many unique regions are represented in the dataset.

Libraries Used

- os: For interacting with the file system (e.g., listing directories, checking file paths).

- shutil: For moving files between directories.




How to Use
  - Clone the repository.
  - Run the Python code to interact with the course registration system.
  - Example usage is provided in the uploaded code.
