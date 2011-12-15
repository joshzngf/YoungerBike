import os
import cgi
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Greeting(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
  def get(self):
    greetings_query = Greeting.all().order('-date')
    greetings = greetings_query.fetch(10)

    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'To use this service, please login here'

    template_values = {
      'greetings': greetings,
      'url': url,
      'url_linktext': url_linktext,
      'login': users.get_current_user(),
      }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

class Guestbook(webapp.RequestHandler):
  def post(self):
    greeting = Greeting()

    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/')

class Rider(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
      <html>
        <body>
          <a href="/"><img src="http://csie.ntu.edu.tw/~b00902084/younger.jpg" alt="younger.jpg" width="351" height="110.5s" /></a>
          <p>Take it slowly, coming soon....</p>
        </body>
      </html>""")
    

class Knight(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
      <html>
        <body>
          <a href="/"><img src="http://csie.ntu.edu.tw/~b00902084/younger.jpg" alt="younger.jpg" width="351" height="110.5s" /></a>
          <p>Take it slowly, coming soon....</p>
        </body>
      </html>""")
    

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/sign', Guestbook),
                                      ('/knight', Knight),
                                      ('/rider', Rider)
                                     ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
