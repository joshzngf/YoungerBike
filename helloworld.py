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
  
class Matchprofile(db.Model):
	knight = db.UserProperty()
	kname = db.StringProperty()
	rider = db.UserProperty()
	rname = db.StringProperty()
	time = db.StringProperty()
	fromm = db.StringProperty()
	to = db.StringProperty()
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
    rprofiles_query = Riderprofile.all().order('-submitdate')
    rprofiles = rprofiles_query.fetch(10)
    for rprofile in rprofiles:
	if (rprofile.time == kprofile.time) and (rprofile.fromm == kprofile.fromm) and (rprofile.to == kprofile.to) and (rprofile.day == kprofile.day) :
				Match = Matchprofile()
				Match.knight = kprofile.user
				Match.kname = kprofile.name
				Match.rider = rprofile.user
				Match.rname = rprofile.name
				Match.time = rprofile.time
				Match.fromm = rprofile.fromm
				Match.to = rprofile.to				
				Match.put()
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


    kprofiles_query = Knightprofile.all().order('-submitdate')
    kprofiles = kprofiles_query.fetch(10)

    for kprofile in kprofiles:
	if (rprofile.time == kprofile.time) and (rprofile.fromm == kprofile.fromm) and (rprofile.to == kprofile.to) and (rprofile.day == kprofile.day) :
				Match = Matchprofile()
				Match.knight = kprofile.user
				Match.kname = kprofile.name
				Match.rider = rprofile.user
				Match.rname = rprofile.name
				Match.time = rprofile.time
				Match.fromm = rprofile.fromm
				Match.to = rprofile.to				
				Match.put()


    rprofile.put()
    self.redirect('/')

class Admin(webapp.RequestHandler):
  def get(self):
	kprofiles_query = Knightprofile.all().order('-submitdate')
	kprofiles = kprofiles_query.fetch(10)
	rprofiles_query = Riderprofile.all().order('-submitdate')
	rprofiles = rprofiles_query.fetch(10)
	matchprofiles_query = Matchprofile.all().order('-submitdate')
	matchprofiles = matchprofiles_query.fetch(10)

	template_values = {
		'kprofiles': kprofiles,
		'rprofiles': rprofiles,
		'matchprofiles': matchprofiles,
		'login': users.get_current_user(),
      }


	path = os.path.join(os.path.dirname(__file__), 'admin.html')
	self.response.out.write(template.render(path, template_values))


class Result(webapp.RequestHandler):
  def get(self):
	matchkprofiles_query = Matchprofile.all().order('-submitdate')
	matchkprofiles = matchkprofiles_query.filter('knight = ', users.get_current_user())

	matchrprofiles_query = Matchprofile.all().order('-submitdate')
	matchrprofiles = matchrprofiles_query.filter('rider = ', users.get_current_user())

	template_values = {
		'matchkprofiles': matchkprofiles,
		'matchrprofiles': matchrprofiles,
		'login': users.get_current_user(),
      }


	path = os.path.join(os.path.dirname(__file__), 'result.html')
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
				      ('/homework/sign',HWGuestbook),
				      ('/result',Result)
                                     ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
