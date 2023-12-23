build_containers:
	docker-compose -f docker-compose.yml up --build --remove-orphans

start_containers:
	docker-compose -f docker-compose.yml up

stop_containers:
	docker-compose -f docker-compose.yml down

remove_containers:
	docker-compose -f docker-compose.yml down -v


create_admin:
	python manage.py createsuperuser

create_admin_in_container:
	docker exec -it app python manage.py createsuperuser

populate_db:
	python manage.py shell -c "from apps import populate_db; populate_db.populate_db()"

populate_db_in_container:
	docker exec -it app python manage.py shell -c "from apps import populate_db; populate_db.populate_db()"
