from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import models

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        if user:
            self.response.out.write('Hello, ' + user.nickname()+'!')
            self.response.out.write('<br><a href="'+users.create_logout_url(self.request.uri)+'">log out</a>')
        else:
            self.response.out.write('Hello, Guest!')
            self.response.out.write('<br><a href="'+users.create_login_url(self.request.uri)+'">log in</a>')
            
application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
