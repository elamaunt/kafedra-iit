from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import models

class AddPage(webapp.RequestHandler):
    def get(self):
        models.Group(name=self.request.get('group')).put()
            
application = webapp.WSGIApplication(
                                     [('/add', AddPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
