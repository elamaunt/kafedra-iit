from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import models

class RegisterPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write('Привет, ' + user.nickname()+'!')
            self.response.out.write('''<form method="post">
                <p>Имя: <input type="text" name="name" /></p>
                <p>Фамилия: <input type="text" name="surname" /></p>
                <select name="type">
                    <option value="student">Студент</option>
                    <option value="employee">Работник кафедры</option>
                </select>
                <select name="group">''')
            groups = db.GqlQuery('SELECT * FROM Group')
            for group in groups:
                self.response.out.write('<option value="%s">%s</option>' % (group.key(),group.name.encode('utf-8')))
            self.response.out.write('''
                </select>
                <input type="submit" value="Зарегистрироваться" />
                </form>
            ''')
            
    def post(self):
        user = users.get_current_user()
        if user:
            if self.request.get('type') == 'student':
                student = models.Student(user=user, name=self.request.get('name'), 
                                    surname=self.request.get('surname'), 
                                    group=db.Key(self.request.get('group')))
                student.put()
                
application = webapp.WSGIApplication(
                                     [('/register', RegisterPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()