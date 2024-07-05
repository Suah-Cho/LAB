from fastapi import FastAPI
import logging
import psycopg2

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
        logging.error('Error connecting to database')
        return {'error': str(e)}