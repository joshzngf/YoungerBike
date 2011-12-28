import os
import cgi
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db



class HWGreeting(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)


class HWGuestbook(webapp.RequestHandler):
  def post(self):
    greeting = HWGreeting()

    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/homework')


class Homework(webapp.RequestHandler):
     def get(self):
	greetings_query = HWGreeting.all().order('-date')
#	greetings_query.reverse()
	greetings = greetings_query.fetch(10)
	if users.get_current_user():
	  url = users.create_logout_url(self.request.uri)
	  url_linktext = 'Logout'
	else:
	  url = users.create_login_url(self.request.uri)
	  url_linktext = 'To post on this guestbook, please login here'
	
	template_values = {
	  'greetings': greetings,
	  'url': url,
	  'url_linktext': url_linktext,
	  'login': users.get_current_user(),
	  }
	path = os.path.join(os.path.dirname(__file__), 'homework.html')
	self.response.out.write(template.render(path, template_values))

class Homeworkprofile(webapp.RequestHandler):
     def get(self):
	if users.get_current_user():
	  url = users.create_logout_url(self.request.uri)
	  url_linktext = 'Logout'
	else:
	  url = users.create_login_url(self.request.uri)
	  url_linktext = 'Login'
	
	template_values = {
	  'url': url,
	  'url_linktext': url_linktext,
	  'login': users.get_current_user(),
	  }
	path = os.path.join(os.path.dirname(__file__), 'homeworkprofile.html')
	self.response.out.write(template.render(path, template_values))




class Greeting(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)
  
class Knightprofile(db.Model):
  user = db.UserProperty()
  name = db.StringProperty()
  gender = db.StringProperty()
  time = db.StringProperty()
  fromm = db.StringProperty()
  to = db.StringProperty()
  email = db.StringProperty()
  day = db.StringProperty()
  fb = db.StringProperty()
  submitdate = db.DateTimeProperty(auto_now_add=True)


class Riderprofile(db.Model):
  user = db.UserProperty()
  name = db.StringProperty()
  gender = db.StringProperty()
  time = db.StringProperty()
  fromm = db.StringProperty()
  to = db.StringProperty()
  email = db.StringProperty()
  day = db.StringProperty()
  fb = db.StringProperty()
  submitdate = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
  def get(self):
	greetings_query = Greeting.all().order('-date')
#	greetings_query.reverse()
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

class Signknight(webapp.RequestHandler):
  def post(self):
    kprofile = Knightprofile()

    if users.get_current_user():
      kprofile.user = users.get_current_user()
    kprofile.name = self.request.get('name')
    kprofile.gender = self.request.get('gender')
    kprofile.time = self.request.get('time')
    kprofile.fromm = self.request.get('from')
    kprofile.to = self.request.get('to')
    kprofile.email= self.request.get('email')
    kprofile.fb = self.request.get('fb')
    kprofile.day = self.request.get('day')
    kprofile.put()
    self.redirect('/')

class Signrider(webapp.RequestHandler):
  def post(self):
    rprofile = Riderprofile()

    if users.get_current_user():
      rprofile.user = users.get_current_user()
    rprofile.name = self.request.get('name')
    rprofile.gender = self.request.get('gender')
    rprofile.time = self.request.get('time')
    rprofile.fromm = self.request.get('from')
    rprofile.to = self.request.get('to')
    rprofile.email= self.request.get('email')
    rprofile.fb = self.request.get('fb')
    rprofile.day = self.request.get('day')

    rprofile.put()
    self.redirect('/')

class Admin(webapp.RequestHandler):
  def get(self):
	kprofiles_query = Knightprofile.all().order('-submitdate')
	kprofiles = kprofiles_query.fetch(10)
	rprofiles_query = Riderprofile.all().order('-submitdate')
	rprofiles = rprofiles_query.fetch(10)
	template_values = {
          'kprofiles': kprofiles,
          'rprofiles': rprofiles,
          'login': users.get_current_user(),
        }
	path = os.path.join(os.path.dirname(__file__), 'admin.html')
	self.response.out.write(template.render(path, template_values))

class Rider(webapp.RequestHandler):
  def get(self):
    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'To use this service, please login here'

    template_values = {
      'url': url,
      'url_linktext': url_linktext,
      'login': users.get_current_user(),
      }

    path = os.path.join(os.path.dirname(__file__), 'rider.html')
    self.response.out.write(template.render(path, template_values))
    

class Knight(webapp.RequestHandler):
  def get(self):
    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'To use this service, please login here'

    template_values = {
      'url': url,
      'url_linktext': url_linktext,
      'login': users.get_current_user(),
      }

    path = os.path.join(os.path.dirname(__file__), 'knight.html')
    self.response.out.write(template.render(path, template_values))


application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/sign', Guestbook),
                                      ('/knight', Knight),
                                      ('/rider', Rider),
                                      ('/signrider', Signrider),
                                      ('/signknight', Signknight),
				      ('/admin', Admin),
				      ('/homework', Homework),
				      ('/homework/profile', Homeworkprofile),
				      ('/homework/sign',HWGuestbook)
                                     ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
