from fastapi import FastAPI, HTTPException
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
        logging.error('Error connecting to database')
        return {'error': str(e)}
    
def function_a():
    raise ValueError("This is an error in function_a")

def function_b():
    function_a()

def function_c():
    function_b()

@app.get("/error2")
async def root():
    try:
        function_c()
    except Exception as e:
        error_message = "An error occurred:\n" + "".join(traceback.format_exc())
        logging.error(error_message)
        raise HTTPException(status_code=500, detail=error_message)