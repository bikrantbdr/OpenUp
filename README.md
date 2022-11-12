# OpenUp
> OpenUp is a project constructed with the motive to have a community of individuals dealing with their mental health. Constructed with Django as a backend platform and responsive frontend technologies, OpenUp brings together like minded individuals with approximate matching of mental issues and headspaces and gives a platform for them to freely confess or vent their thoughts anonymously. 
> OpenUp attempts to create a safe and warm environment with  moderated voice meetings regularly for users to share and get opinions from others.

## Step for setup:
1. Setting up Your Virtual Environment:
    * Create Virtual Environment Using venv
    `python -m venv Virtual_Env_Name`

    * Activate Virtual Environment
    `Virtual_Env_Name\scripts\activate `

2. Download Dependencies:
    `pip install -r requirements.txt`
3. Run redis server:
    > install and launch redis server to use as server for real-time chat
    > For windows install memurai from the link.[click_here](https://www.memurai.com/get-memurai "Memurai")
4. Run migrations for database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Create SuperUser for Managing database:
    `python manage.py createsuperuser`
    > enter username, email and password to create superuser