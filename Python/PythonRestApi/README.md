# Python REST API with Flask, Docker, MongoDB and AWS

## Requirements
- Flask `pip install Flask`
- flask_restfull `pip install flask_restful`

## Flask run project
- `export FLASK_APP=app.py`
- `flask run`


## Docker
- `docker-compose build`
- `docker-compose up`

## API endpoints

### GET
- `/` index.html
- `/hello` visitor counter
- `/hello_world` returns a string
  
### POST
- `/add`
- `/subtract`
- `/multiply`
- `/division`

#### POST format in JSON

``` json
{
  "x": 10,
  "y": 5
}
```

or 

``` json
{
  "x": "10",
  "y": "5"
}
```