# Python REST API - Bank

## Note
Project are tested on Linux (Pop!_OS)

## Requirements
- [Docker](https://docs.docker.com/get-docker/)
- [Docker-Compose](https://docs.docker.com/compose/install/)
- [MongoDB](https://docs.mongodb.com/manual/installation/)
- [Python](https://www.python.org/)
- [Pip](https://docs.python.org/3/installing/index.html)


## Python requirements
- Flask `pip install Flask`
- flask_restful `pip install flask_restful`
- pymongo`pip install pymongo`
- bcrypt `pip install bcrypt`


## Flask run project
- `export FLASK_APP=app.py`
- `flask run`


## Docker
- `docker-compose build`
- `docker-compose up`


## API endpoints

### GET
#### `localhost/` index.html

#### `localhost/all`
  

### POST
#### `localhost/register`
``` json
{
	"username": "BANK",
	"password": "secure_password"
}
```

``` json
{
	"username": "User1",
	"password": "user_password"
}
```

#### `localhost/balance`
``` json
{
	"username": "BANK",
	"password": "secure_password"
}
```

``` json
{
	"username": "User1",
	"password": "user_password"
}
```

#### `localhost/add`
``` json
{
	"username": "User1",
	"password": "user_password",
	"amount": 100
}
```

#### `localhost/transfer`
``` json
{
	"username": "User1",
	"password": "user_password",
	"to": "User2"
	"amount": 100
}
```

#### `localhost/takeloan`
``` json
{
	"username": "User1",
	"password": "user_password",
	"amount": 100
}
```

#### `localhost/payloan`
``` json
{
	"username": "User1",
	"password": "user_password",
	"amount": 50
}
```

#### `localhost/delete`
``` json
{
	"username": "User1",
	"password": "user_password"
}
```

## IMPORTANT NOTE!
Before start using the API for customers you need to create The BANK

## Example transfers 

### GET

#### Index
`localhost/`


### POST

#### `localhost/register`
``` json
{
	"username": "BANK",
	"password": "secure_password"
}
```
``` json
{
	"username": "adam",
	"password": "adam_password"
}
```
``` json
{
	"username": "bengt",
	"password": "bengt_password"
}
```
``` json
{
	"username": "cesar",
	"password": "cesar_password"
}
```

#### `localhost/balance`
``` json
{
	"username": "BANK",
	"password": "secure_password"
}
```
``` json
{
	"username": "adam",
	"password": "adam_password"
}
```
``` json
{
	"username": "bengt",
	"password": "bengt_password"
}
```

#### `localhost/add`
``` json
{
	"username": "adam",
	"password": "adam_password",
	"amount": 100
}
```
``` json
{
	"username": "bengt",
	"password": "bengt_password",
	"amount": 200
}
```

#### `localhost/transfer`
``` json
{
	"username": "adam",
	"password": "adam_password",
	"to": "bengt",
	"amount": 10
}
```
``` json
{
	"username": "bengt",
	"password": "bengt_password",
	"to": "adam",
	"amount": 20
}
```

#### `localhost/takeloan`
``` json
{
	"username": "adam",
	"password": "adam_password",
	"amount": 100
}
```

#### `localhost/payloan`
``` json
{
	"username": "adam",
	"password": "adam_password",
	"amount": 50
}
```

#### `localhost/delete`
``` json
{
	"username": "cesar",
	"password": "cesar_password"
}
```

