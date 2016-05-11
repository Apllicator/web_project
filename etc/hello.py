CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=5',
        '--timeout=60',
        '--log-file=/home/box/web/gunicorn.log',
        'hello:app',
    )
}
