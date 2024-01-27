## How to run this project
I higly recommend you to have ```make``` util installed on your machine, but if you don't, just go to ```Makefile``` and copy the required commands. E.g. ```make venv``` might be replaced with ```python3 -m venv venv``` and so on

- Run ```make migrate``` to apply all migrations
- Run ```make run``` to run the development server
- Run ```make superuser``` to create admin user, might want before docker
- Run ```make docker``` to build and run this app in Docker container on http://127.0.0.1:8000

## Admin
You can access admin panel on ```http://127.0.0.1:8000/admin```
