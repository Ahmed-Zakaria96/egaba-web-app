from waitress import serve

from Egaba.wsgi import application

if __name__ == '__main__':
    serve(application)
