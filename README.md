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
`python manage.py migrate`

### Lunch the project
`python manage.py runserver`