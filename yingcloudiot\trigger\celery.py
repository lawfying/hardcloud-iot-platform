from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('trigger',
             broker='pyamqp://guest@localhost//',
             backend='redis://localhost',
             include=['trigger.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=10,
)

if __name__ == '__main__':
    print("good")
    app.start()