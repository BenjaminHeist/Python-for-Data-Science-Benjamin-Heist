Read-Me for the repository 'Python-for-Data-Science-Benjamin-Heist'. 

This repository contains the individual assignments of this Python course and was updated continiously. Along the course I created a new branch for each individual assignment, that all were merged into the main branch. 

Additional Comments:
  I have decided not to create a folder structure with individual README files, as repeating information from the main README would be counterproductive. I believe it would not  only be redundant, but also unnecessarily complicate the repository. Instead, you will find an overview of each task in the relevant section of this README as well as in the respective files through Markdown cells. I believe that this structure makes the repository clearer and easier to follow. 

  Thank you for this course! I truly enjoyed the classes with the both of you. It was clear that you not only enjoyed teaching but also enjoyed working together, which made the experience even better for us. I also noticed how the teaching style and course structure improved significantly as the course progressed, which made learning even more engaging.

ASSIGNMENT 1 

- In the notebook you will find exercises 1-17 of Individual Assignment 1, followed by the respective code solutions in the subsequent cells.

- In order to run all of the cells correctly Python version 3.10 or higher is needed. 

ASSIGNMENT 2 

- In this notebook you'll find exercises 1-4 related to Individual Assignment 2. You can see the tasks followed by the respective code solutions in the subsequent cells.

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

This file contains the content covered in class followed by a Python script to analyze a set of annotation files stored in a zip file. Each file follows a specific naming convention:
{DATE}_{TIME}_SN{SATELLITE_NUMBER}_QUICKVIEW_VISUAL_{VERSION}_{UNIQUE_REGION}.txt

ATTENTION: I decided to include the annotations that don't follow the naming convention in number 5, because the date-part still followed the convention. Opposingly I decided to exclude the annotations not following the naming convention in exercise 6, since the satellite-part didn't follow the standard pattern.


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

Libraries Utilized

- os: For interacting with the file system (e.g., listing directories, checking file paths).
- shutil: For moving files between directories.


ASSIGNMENT 5 

Advanced Annotation Analysis: In this assignment, we build upon the annotations data analyzed in Assignment 4, adding new insights and enhancing data handling using libraries introduced in this session.

Task Overview

The script provides answers to the following questions based on the annotation files:

1. Annotations by Month and Year:
- Count of annotations for each month and year.
- Identify the month with the highest number of annotations.
2. Annotations Organized by Month (Dictionary Storage)
- Create a Dictionary: Develop a dictionary where each key represents a month, and each value is a list of annotation names corresponding to that month.
- JSON Serialization: Save the dictionary in JSON format. Load the JSON file to confirm the data integrity.
- Pickle Serialization: Save the dictionary using Pickle for efficient storage and loading.
- Enhanced Storage with Datetime Objects: Instead of just storing a list of annotation names, create a dictionary for each annotation entry with the keys name (annotation name) and date (a Python datetime object).
3. Sort and Print Annotations for the Second Half of 2024
- Filter annotations from July to December 2024 and print these annotations in chronological order, from the oldest to the newest.


Libraries Utilized

- datetime: For working with dates and times, particularly to parse annotation dates, store them as datetime objects, and enable accurate date-based sorting.
- json: For serializing (saving) data structures into JSON format, allowing for human-readable, cross-platform storage and easy data exchange.
- pickle: For efficient binary serialization, enabling quick saving and loading of complex Python objects, like dictionaries with datetime objects.


ASSIGNMENT 6

This file contains the content covered in class followed by Python scripts analyzing two datasets: a Netflix dataset and a Titanic survival dataset. 

The Netflix file used can be found here: https://ecampus.esade.edu/pluginfile.php/186007426/mod_folder/content/0/netflix_titles.csv.zip?forcedownload=1

The Titanic file used can be found here: https://ecampus.esade.edu/pluginfile.php/186007429/mod_folder/content/0/titanic.zip?forcedownload=1

Task Overview

The script provides answers to the following questions based on the Netflix Dataset:

1. Missing Ratings: Check if there are any missing values in the rating column.
2. Country-Specific Films in 2021: Count the number of films released in 2021 that correspond to your country.
3. Movies in 2020 with Full Information: Identify how many movies from 2020 have no missing values across all columns.
- excludes rows with incomplete data when analyzing full information for movies in 2020
5. Year with the Most Titles: Find the year with the highest number of titles in the dataset.
6. Average Releases Since 2010: Calculate the average number of titles released annually from 2010 onwards.

The script provides answers to the following questions based on the Titanic Dataset: 

1. Gender-Based Survival Percentage: Calculate survival percentages for males and females.
- please note that the 'Survived' header is spelled wrong, I adjusted according to it: '2urvived'. Nevertheless I chose to not change it in the dataframe itself 
2. Survival Percentage Grouped by Gender and Class: Analyze survival rates grouped by gender and passenger class.

Key Visualizations (Out of scope)

- A bar chart visualizing survival percentages for males and females across passenger classes.

Libraries Utilized

- pandas: For data manipulation and analysis.
- matplotlib: For creating visualizations.


ASSIGNMENT 7

This file contains solutions to Python exercises that focus on manipulating and combining DataFrames using pandas. The tasks include creating new columns, performing joins, and combining DataFrames using advanced string and merge operations. The data used in the file is provided within the code.

Tasks Overview

1. Create a Column with Professor Initials
- Added a new column called professor_initials to store the initials of each professor's first and last names.
2. Join DataFrames based on the Professor Column
- Used the join function to combine the original DataFrame with a new DataFrame containing additional data, matching rows based on the professor column.
3. Merge DataFrames based on the Professor Column
- Merged the original DataFrame with the df_courses DataFrame to consolidate course-related information.
4. Extract Professor Last Name and create a new column
- Created a new column called professor_last_name by extracting the last name of each professor from the professor column using string operations.

Libraries Utilized

- pandas: For DataFrame manipulation, including string operations and joins.


ASSIGNMENT 8

This file contains solutions to Python exercises that focus on data visualization using Seaborn and Matplotlib. The tasks include creating various types of plots to analyze and interpret patterns in the data, such as trends, distributions, and relationships. The data used in the file is provided within the code. 

Tasks Overview

1. Create a Lineplot for Study Time by Student Name
- Generated a lineplot to visualize how study time varies across students. Identified the student with the highest study time.
2. Histogram of Grade Distribution
- Created a histogram to observe the distribution of grades and determine the grade range with the highest frequency of students.
3. ECDF Plot for Grades
- Visualized the cumulative distribution of grades using an ECDF plot and calculated the percentage of students scoring below 85.
4. Stripplot of Grade Distribution by Course
- Designed a stripplot to analyze how grades are distributed for each course and identified the course with the most spread in grades.
5. Swarmplot for Gender vs. Study Time
- Plotted a swarmplot to examine the relationship between gender and study time. Determined which gender has a higher average study time.
6. Pointplot of Average Grades by Course
- Developed a pointplot to display the average grades for each course and identified the course with the highest average grade.

Libraries Utilized

- Seaborn: For creating advanced visualizations like ECDF, swarmplot, stripplot, and pointplot.
- Matplotlib: For customizing and enhancing the plots.
- Pandas: For data manipulation and aggregation to prepare the data for visualization.


How to Use
  - Clone the repository.
  - pip install the required libraries
  - run the script
