## Setup 

1. Clone the repository:
    ```sh
    $ git clone git@github.com:Vlad0n20/Yazz-Services-test-task.git
    ```
2. Populate env.example and end.db.example files and rename it on .env  and .env.db
3. Build and run containers with command:
    ```sh
    $ make build_containers
    ```
4. After step 3 populate the database with command if you use docker-compose if you want to generate new data:
    ```sh
    $ make populate_db_in_container
    ```
    or run locally:
    ```sh
    $ python manage.py populate_db
    ```
   
   if you want to use existing data:
    ```sh
    $ make load_data_in_container
    ```
    or run locally:
    ```sh
    $ python manage.py loaddata fixtures/shop.json
    $ python manage.py loaddata fixtures/products.json
    ```
5. Create superuser (username-admin, password-admin) with command if you use docker-compose:
    ```sh
    $ make create_admin_in_container
    ```
    or run locally:
    ```sh
    $ python manage.py createsuperuser
    ```

Now you can use the application.