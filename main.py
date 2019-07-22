import webapp2
import jinja2
import os

env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/start.html")
        self.response.write(template.render())

class RunHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/run.html")
        self.response.write(template.render())

class EnterHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/enter.html")
        self.response.write(template.render())

class SelfieHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/selfie.html")
        self.response.write(template.render())

class Call911Handler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/911.html")
        self.response.write(template.render())

class TjayHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/tjay.html")
        self.response.write(template.render())

class HideHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/hide.html")
        self.response.write(template.render())

class FasterHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/faster.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/run', RunHandler),
    ('/enter', EnterHandler),
    ('/selfie', SelfieHandler),
    ('/faster', FasterHandler),
    ('/hide', HideHandler),
    ('/tjay', TjayHandler),
    ('/911', Call911Handler),
    
], debug = True)
