from waitress import serve

from patitasbackend.wsgi import application

if __name__ == '__main__':
    serve(application, host = '192.168.0.104', port='8080')