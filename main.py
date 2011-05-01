from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import models

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        if user:
            self.response.out.write('Привет, ' + user.nickname()+'!')
            registered_user = db.GqlQuery('SELECT * FROM User WHERE user=:user', user = user)
            if registered_user.count() == 0:
                self.response.out.write('<br><a href="/register">зарегистрироваться</a>')
            else:
                registered_user = registered_user.fetch(1)[0]
                self.response.out.write('<br>' + registered_user.name.encode('utf-8') + ' ' + registered_user.surname.encode('utf-8'))
            
            self.response.out.write('<br><a href="'+users.create_logout_url(self.request.uri)+'">выйти</a>')
        else:
            self.response.out.write('<br><a href="'+users.create_login_url(self.request.uri)+'">Залогиниться в гугловский акк</a>')
            
application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
