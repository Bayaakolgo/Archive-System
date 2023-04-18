## Archive System
- A project that allows users to upload and fetch files from a database.

- Authorized users are shown a dashboard where they can view manage and download files.

- The project shows each file name, type and size uploaded.

## Installation steps

Clone the repo `git clone `

In the repo directory, create a virtual environment `python3 -m venv venv`

#### Activate the virtual environment
On Windows CMD: `venv\Scripts\activate`
On Windows mac: `source <venv>/bin/activate`

### Install django in the virtual environment
`pip install django`

### Install the needed dependencies from the requirements.txt file
`pip install -r requirements.txt`

### Make migrations
`python manage.py makemigrations`
`python manage.py migrate`

### You can create a super user (OPTIONAL)
py manage.py createsuperuser

### Lunch the project
`python manage.py runserver`

- Create a user using the Register feature
- After User Creation, Signin to upload and manage files in the project.
- The project will start as a new project when run locally hence upload files before you can either download or delete.


### GIF Demonstration
![Archive](https://user-images.githubusercontent.com/84840626/232854117-6bf43b8f-9621-416d-afd8-24f2a42eb825.gif)

### Limitations
- The project in development stage. The poject is not delployed.
- Files uploaded are stored on the local computer.
- There are features in the project that are yet to be implemented.
- 

