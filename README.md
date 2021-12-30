# Python Microservices

- add books
- Update books
- Delete books
- Like books

### Endpoints

- http://127.0.0.1:8000/api/products [GET] (list products)
- http://127.0.0.1:8000/api/products [POST] (add products)
- - sample input data  as json`  
        "id": int,
        "title": "str",
        "image": "str",
- http://127.0.0.1:8000/api/products/{str:pk}[UPDATE] (update products)
- - sample input data  as json`  
        "id": int,
        "title": "str",
        "image": "str",
- http://127.0.0.1:8000/api/products/{str:pk} [DELETE] (delete products)
- http://127.0.0.1:8000/api/products/{str:pk} [GET] (retrieve product)
- http://127.0.0.1:8001/api/products/{str:pk} /likes  [GET] (like products)

####project user
python manage.py runserver 127.0.0.1:8001

####projectmain
python manage.py runserver 127.0.0.1:8000
