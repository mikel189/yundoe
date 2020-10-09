from waitress import serve
from server import app
import schedule
import time

def print_hi():
    print('hi world')

schedule.every(0.1).minutes.do(print_hi)


while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)