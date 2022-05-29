# cubbit_test_project
### environment setup venv
1. Open a shell 

2. Create a virtual environment inside the basedir of the project
    ```sh
    python -m venv venv
    ```
3. On Windows, run:
    ```sh
    venv\Scripts\activate.bat
    ```
4. On Unix or MacOS, run:
    ```sh
    source venv/bin/activate
    ```
5. Install the required dependencies
    ```sh
    pip install -r requirements.txt
    ```

   
### run application
1. Open a shell inside the basedir of the project
2. Run:
   ```sh
    python manage.py runserver
   ```
3. Go to: 
   ```sh
    http://127.0.0.1:8000/
   ```
   
### inspect Sqlite data
1. Open a shell inside the basedir of the project
2. Run:
   ```sh
    sqlite3 db.sqlite3
   ```
3. List tables: 
   ```sh
    .table
   ```

