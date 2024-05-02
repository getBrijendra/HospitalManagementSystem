# Hospital Managament System


## Description
Objective: Develop a RESTful API for a Hospital Management System using a suitable
backend framework (Flask or Django) that allows users to manage patients, doctors,
and departments efficiently.
Requirements:
1. Patient Management:

● Personal Information (Name, Age, Gender, Contact Information)
● Medical History (Previous Diagnoses, Allergies, Medications)
● Appointment Records

2. Doctor Management:
· Professional Information (Name, Specialization, Contact Information)
· Availability Schedule, List of Patients Assigned
· Assign and Re-assign Patients to Doctors
3. Department Management:
· Department Name, Services Offered, Assign Doctors to Departments
4. Search Functionality:

● Search for Patients, Doctors, and Departments by some attribute
● Filtering Options (e.g., Availability and Specialization)
● Optional Enhancements: Implement pagination to limit the number of
products returned in a single request.

Deliverables:
● A fully-functional RESTful API developed using Python Flask (preferred)
● A detailed README file that provides instructions for setting up and running the
application.
● A demonstration of the API using a tool such as Curl/Postman
● This project will allow you to showcase your backend development skills


## Getting Started


### Dependencies

* requirments.txt

### Installing


### Executing program

* How to run the program
```
# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --username admin --email admin@example.com

python manage.py runserver

python manage.py flush
```

## Help

Open /docs for help of APIs

```

```

## Authors

Contributors names and contact info -- Brijendra

## Version History

* 0.2
    * Various bug fixes and optimizations
* 0.1
    * Initial Release

## License

Open Source

## Acknowledgments
