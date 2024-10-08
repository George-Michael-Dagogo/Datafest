# DATAFEST SCHOOL 

### Overview: Faker was used to generate data for a senior secondary school, this data was pushed to a Blob Storage container on Azure(for backup and historical data) and a Postgres database on Aiven after passing several data quality checks(mimicking a real world scenario), analysis was carried out and a dashboard built in Power BI and models were build to ascertain the likelyhood of a student would passing or failing. As part of our data solution, we built a web app with Streamlit for data entry and collection where the school can easily insert new data and update old data in the database. After every academic session(3 months), the database will be queried and all the data within that time frame will be moved to the Blob Storage as a PARQUET file and this process was automated with GitHub Actions.

## Link to Streamlit app : https://datafestschoolapp.streamlit.app/
- username = datafest_school
- password = datafest_school

## Data Pipeline Architecture
![alt text](https://github.com/George-Michael-Dagogo/Datafest/blob/main/Images/datafest_architecturee.png)

## Data Collection
### We initially utilized the Faker library to generate data, but found that its outputs didn’t fully capture the realistic nuances, particularly the Nigerian context. To address this, we enhanced the dataset by scraping authentic Nigerian male and female names from multiple sources, and incorporated Nigerian locations for better geographical relevance. Additionally, we modeled challenges that a typical West African child might face, ensuring the data was culturally and contextually accurate.

### Alongside this, we developed a custom application that allows the school to seamlessly update and insert new data into the database, ensuring real-time data management. Further details on the data dictionary are provided below.




## School Database Model
![alt text](https://github.com/George-Michael-Dagogo/Datafest/blob/main/Images/school_data_model.png)

## School Database Data Dictionary (Updated)

### class_resources_table

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Class_ID | VARCHAR(20) | 20 | Primary key, unique identifier for each class | SS1 Class A |
| Number_of_Students | SMALLINT | 2 bytes | Number of students in the class | 60 |
| Number_of_Teachers | SMALLINT | 2 bytes | Number of teachers assigned to the class |82 |
| Weekly_Teaching_Hours | SMALLINT | 2 bytes | Total teaching hours per week for the class | 40 |
| Weekly_Library_Time | SMALLINT | 2 bytes | Hours per week spent in the library | 5 |
| Weekly_Computer_Training_Time | SMALLINT | 2 bytes | Hours per week spent on computer training | 3 |
| Weekly_Lab_Hours | SMALLINT | 2 bytes | Hours per week spent in the laboratory | 4 |
| Chalkboard | SMALLINT | 2 bytes | Quantity or condition of chalkboards | 2 |
| Basic_Textbooks | SMALLINT | 2 bytes | Quantity or availability of basic textbooks | 25 |
| Chairs_Desks | SMALLINT | 2 bytes | Quantity or condition of chairs and desks | 60 |
| Functional_Fans | SMALLINT | 2 bytes | Number of functional fans in the classroom | 3 |

## student_table

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Student_ID | VARCHAR(100) | 100 | Primary key, unique identifier for each student| ccf3a17156dc4907ba6c34ab6712303a |
| Class_ID | VARCHAR(20) | 20 | Foreign key referencing class_resources_table | SS3 Class F |
| First_Name | TEXT | Variable | Student's first name | "Okorie" |
| Family_Name | TEXT | Variable | Student's family name | "Dubem" |
| Gender | TEXT | Variable | Student's gender | "Male" |
| Date_of_Birth | DATE | 3 bytes | Student's date of birth | "2005-07-15" |
| State_of_Origin | TEXT | Variable | Student's state of origin | "Lagos" |
| engagement_in_class | TEXT | Variable | Level or description of student's engagement in class | Unactive |
| health_condition | TEXT | Variable | Description of student's health condition | "None" |
| Class_Spec | TEXT | Variable | Specific class or stream the student belongs to | "Science" |

## parent_table

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Student_ID | VARCHAR(100) | 100 | Primary key and foreign key referencing student_table | ccf3a17156dc4907ba6c34ab6712303a |
| Fathers_Name | TEXT | Variable | Name of the student's father | "Michael" |
| Mothers_Name | TEXT | Variable | Name of the student's mother | "Silver" |
| Family_Name | TEXT | Variable | Family name of the parents | "Mbawike" |
| Father_Education | TEXT | Variable | Educational level of the father | Tetiary |
| Mother_Education | TEXT | Variable | Educational level of the mother | Secondary |
| Father_Occupation | TEXT | Variable | Occupation of the father | "Engineer" |
| Mother_Occupation | TEXT | Variable | Occupation of the mother | "Teacher" |
| Annual_Household_Income_NGN | TEXT | Variable | Annual household income in Nigerian Naira | 400,000-600,000 |
| Household_Size | INTEGER | 4 bytes | Number of people in the household | 5 |
| Involvement_in_Kids_Education | TEXT | Variable | Level or description of parental involvement in child's education | Very Involved |

## extracurricular_activity

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Student_ID | VARCHAR(100) | 100 | Primary key and foreign key referencing student_table | ccf3a17156dc4907ba6c34ab6712303a |
| Extracurricular_Activity | TEXT | Variable | Name or type of extracurricular activity | "Chess Club" |
| Weekly_Hours | INTEGER | 4 bytes | Hours per week spent on the activity | 6 |

## student_performance

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Student_ID | VARCHAR(100) | 100 | Primary key and foreign key referencing student_table | ccf3a17156dc4907ba6c34ab6712303a |
| Mathematics | INTEGER | 4 bytes | Student's score in Mathematics | 85 |
| English_Language | INTEGER | 4 bytes | Student's score in English Language | 78 |
| Civic_Education | INTEGER | 4 bytes | Student's score in Civic Education | 90 |
| Economics | INTEGER | 4 bytes | Student's score in Economics | 82 |
| CRS_Islam | INTEGER | 4 bytes | Student's score in Christian Religious Studies or Islamic Studies | 88 |
| Physics | FLOAT | 4 bytes | Student's score in Physics | 76.5 |
| Chemistry | FLOAT | 4 bytes | Student's score in Chemistry | 81.0 |
| Biology | FLOAT | 4 bytes | Student's score in Biology | 79.5 |
| Geography | FLOAT | 4 bytes | Student's score in Geography | 85.0 |
| Computer_Science | FLOAT | 4 bytes | Student's score in Computer Science | 92.5 |
| Government | FLOAT | 4 bytes | Student's score in Government | 88.0 |
| Commerce | FLOAT | 4 bytes | Student's score in Commerce | 77.5 |
| Literature | FLOAT | 4 bytes | Student's score in Literature | 83.0 |
| History | FLOAT | 4 bytes | Student's score in History | 86.5 |
| Accounting | FLOAT | 4 bytes | Student's score in Accounting | 80.0 |

## attendance_table

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Student_ID | VARCHAR(100) | 100 | Primary key and foreign key referencing student_table | ccf3a17156dc4907ba6c34ab6712303a |
| Days_Attended | INTEGER | 4 bytes | Number of days the student attended | 90 |
| Days_Missed | INTEGER | 4 bytes | Number of days the student missed | 5 |
| Absence_Reason | TEXT | Variable | Reason for student's absence | "Illness" |

## ss3_student_survey

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Student_ID | VARCHAR(100) | 100 | Primary key and foreign key referencing student_table | ccf3a17156dc4907ba6c34ab6712303a |
| Reason_For_Performance | TEXT | Variable | Student's explanation for their academic performance | "Regular study and parental support" |
| Access_To_Resources | TEXT | Variable | Description of student's access to educational resources | "Good access to textbooks and internet" |
| Study_Hours_Per_Week | INTEGER | 4 bytes | Number of hours spent studying per week | 20 |
| Health_Issues | TEXT | Variable | Description of any health issues affecting studies | "None" |
| Teacher_Support | INTEGER | 4 bytes | Level of support received from teachers (likely a scale) | 8 |
| Parental_Support | INTEGER | 4 bytes | Level of support received from parents (likely a scale) | 9 |
| Stress_Level | TEXT | Variable | Description of student's stress level | "Moderate" |
| Peer_Influence | TEXT | Variable | Description of peer influence on academic performance | "Positive" |
| Additional_Tutoring | TEXT | Variable | Information about any additional tutoring received | "Math tutor twice a week" |
| Use_Of_Study_Groups | TEXT | Variable | Information about participation in study groups | "Weekly science study group" |
| Exam_Anxiety | TEXT | Variable | Description of student's exam anxiety level | "Low" |
| Jamb_Scores | SMALLINT | 2 bytes | Student's JAMB (Joint Admissions and Matriculation Board) scores | 280 |
| Num_Credit_Passes_WAEC | SMALLINT | 2 bytes | Number of credit passes in WAEC (West African Examinations Council) exams | 7 |
| Verdict | Text | Variable | Pass or Fail based on getting above 200 and above 5 in Jamb and WAEC respectively  | Pass |

## staff_table

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Staff_ID | VARCHAR(100) | 100 | Primary key, unique identifier for each staff member | bdd640fb06674ad19c80317fa3b1799d |
| Name | TEXT | Variable | Name of the staff member | "Alice Johnson" |
| Gender | TEXT | Variable | Gender of the staff member | "Female" |
| Position | TEXT | Variable | Position or role of the staff member | "Teacher" |
| Monthly_Pay | INTEGER | 4 bytes | Monthly salary of the staff member | 150000 |
| Years_of_Experience | INTEGER | 4 bytes | Number of years of work experience | 8 |
| Education_Level | TEXT | Variable | Highest level of education attained | "Master's" |
| Date_of_Hire | TEXT | Variable | Date when the staff member was hired | "2015-09-01" |
| Full_time | BOOLEAN | 1 byte | Indicates whether the staff member is full-time (true) or part-time (false) | true |

## teachers_table

| Column Name | Data Type | Field Size | Description | Example |
|-------------|-----------|------------|-------------|---------|
| Teacher_ID | VARCHAR(100) | 100 | Primary key, unique identifier for each teacher | anf476539s674ad19c80317fa334g9f |
| Staff_ID | VARCHAR(100) | 100 | Foreign key referencing staff_table | bdd640fb06674ad19c80317fa3b1799d |
| Name | TEXT | Variable | Name of the teacher | "Alice Johnson" |
| Teacher_Type | TEXT | Variable | Type or category of teacher | "Senior Teacher" |
| Subject_specialization | TEXT | Variable | Subject area of specialization for the teacher | "Mathematics" |



## Data Quality Checks for School Database
### 1. Attendance Table

- Check for null values in all columns
- Ensure Student_ID is unique and matches with student_table
- Verify Days_Attended and Days_Missed are non-negative
- Check if Days_Attended + Days_Missed equals the total number of school days
- Ensure Absence_Reason is filled for all records where Days_Missed > 0

### 2. Class Resources Table.csv

- Check for null values in all columns
- Ensure Class_ID is unique
- Verify all numeric columns have non-negative values
- Check if Number_of_Students and Number_of_Teachers are reasonable (e.g., not too high or low)
- Ensure Weekly_Teaching_Hours is within a realistic range (e.g., 20-50 hours)

### 3. Extracurricular Activity Table

- Check for null values in all columns
- Ensure Student_ID exists in student_table
- Verify Weekly_Hours is non-negative and within a realistic range (e.g., 0-20 hours)

### 4. Parent Table

- Check for null values in all columns
- Ensure Student_ID is unique and matches with student_table
- Verify Household_Size is positive and within a realistic range
- Check if Annual_Household_Income(NGN) is numeric and in these ranges ['Below 200,000', '200,000-400,000', '400,000-600,000', 'Above 600,000']
- Ensure Father_Education, Mother_Education, Father_Occupation, Mother_Occupation, and Involvement_in_Kids_Education have consistent categories

### 5. Student Survey Table

- Check for null values in all columns
- Ensure Student_ID is unique and matches with student_table
- Verify Study_Hours_Per_Week is non-negative and within a realistic range
- Check if Teacher_Support and Parental_Support are within a specific range (e.g., 1-5)
- Ensure Stress_Level has consistent categories
- Verify Jamb_Scores and Num_Credit_Passes_WAEC are within expected ranges
- Check if verdict has consistent categories

### 6. Staff Table

- Check for null values in all columns
- Ensure Staff_ID is unique
- Verify Monthly Pay and Years of Experience are non-negative
- Check if Date of Hire is in a consistent date format and not in the future
- Ensure Gender, Position, and Education Level have consistent categories

### 7. Student Performance Table

- Check for null values in all columns
- Ensure Student_ID is unique and matches with student_table
- Verify all subject scores are within the expected range (e.g., 0-100)
- Check for any outliers in the scores
- Ensure consistency in the number of decimal places for float64 columns

### 8. Student Table

- Check for null values in all columns
- Ensure Student_ID is unique
- Verify Class_ID exists in class_resources_table
- Check if Date_of_Birth is in a consistent date format and makes sense for a student
- Ensure Gender, State of Origin, engagement_in_class, health_condition, and Class Spec have consistent categories

### 9. Teachers Table

- Check for null values in all columns
- Ensure Teacher_ID is unique
- Verify Staff_ID exists in staff_table
- Ensure Teacher Type and Subject specialization have consistent categories

