from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import logging
import psycopg2
import traceback

app = FastAPI()

@app.get('/')
def read_root():
    logging.info('API root endpoint called')
    return {'Hello': 'World'}

# muli-line error
@app.get('/error')
def read_error():
    try:
        psycopg2.connect('dbname=test user=postgres password=postgres host=postgres')
    except Exception as e:
        logging.error(f'!!!Error connecting to database!!! : {e}')
        logging.error('Traceback: {}'.format(traceback.format_exc()))
        logging.error("HELLO WORLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
        return JSONResponse(status_code=500, content={'message': '!Error connecting to database!'})
    
