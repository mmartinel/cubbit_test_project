# cubbit_test_project

## requirements
1. Python >=3.9
2. Docker
3. docker-compose

## environment setup venv
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

## data ingestion   
### run django application
1. Open a shell inside _cubbit_django_
2. Run:
   ```sh
    python manage.py runserver
   ```
 
### test /ingest api
1. Go to: 
   ```sh
    http://127.0.0.1:8000/
   ```
2. Copy the following lines and paste 
them into the _content_ window:
    ```json
    {
        "client_user_id": "00fcc34b-0b4b-4d7b-abbb-09b146be3170",
        "timestamp": 1651311068647,
        "size": 27393,
        "time_backend": 733,
        "status": "success",
        "direction": "upload"
    }
    ```
   
### inspect Sqlite data
1. Open a shell inside  _cubbit_django_
2. Run:
   ```sh
    sqlite3 db.sqlite3
   ```
3. Query the data: 
   ```sh
    select * from data_ingestion_event
   ```
   
### load event data into sqlite through /ingest api
1. Open a shell inside _jupyter_scripts_
2. Run:
   ```sh
    jupyter notebook
   ```
2. Go to: 
   ```sh
    http://localhost:8888/
   ``` 
3. Open the _events_data_loading_ notebook and run it


## data cleaning
### run postgres database 
1. Open a shell inside _cubbit_test_project_
2. Run:
   ```sh
    docker-compose up
   ```
### clean and insert user data into postgres
1. Open a shell  inside _jupyter_scripts_
2. Run:
   ```sh
    jupyter notebook
   ```
2. Go to: 
   ```sh
    http://localhost:8888/
   ``` 
3. Open the _data_cleaning_events_ notebook and run it

### clean and load event data into postgres
1. Open a shell inside _jupyter_scripts_
2. Run:
   ```sh
    jupyter notebook
   ```
2. Go to: 
   ```sh
    http://localhost:8888/
   ``` 
3. Open the _data_cleaning_users_ notebook and run it


## data analysis
### run analysis notebooks
1. Open a shell inside _jupyter_scripts_
2. Run:
   ```sh
    jupyter notebook
   ```
2. Go to: 
   ```sh
    http://localhost:8888/
   ``` 
3. Open the _data_analysis_question1_ notebook and run it
4. Open the _data_analysis_question2_ notebook and run it
5. Open the _data_analysis_question3_ notebook and run it
6. Open _presentation/presentation.pdf_ to view the results
