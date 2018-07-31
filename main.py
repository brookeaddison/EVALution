'''This python code creates the main page of our glass bottle website, loads in
the main page template, the glass bottle template'''

import webapp2
import os
import jinja2
from google.appengine.api import users
from models import Post

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("templates/mainpage.html")
        self.response.write(start_template.render())

class BottleHandler(webapp2.RequestHandler):
    def get(self):
        bottle_template = jinja_env.get_template("templates/glassbottle.html")
        self.response.write(bottle_template.render())
# need to fix so that it works only if you are logged in
    # def post(self):
    #     text = self.request.get("entry")
    #     post = Post(post_content=text, post_user_id="")
    #     post.put()

class LGBottleHandler(webapp2.RequestHandler):
    def get(self):
        bottle_template = jinja_env.get_template("templates/glassbottlelg.html")
        self.response.write(bottle_template.render())
    def post(self):
        text = self.request.get("entry")
        post = Post(post_content=text, post_user_id="")
        post.put()

class PostsHandler(webapp2.RequestHandler):
    def get(self):
        bottle_template = jinja_env.get_template("templates/posts.html")
        self.response.write(bottle_template.render())

    def post(self):
        text = self.request.get("entry")

class LoginHandler(webapp2.RequestHandler):
    def post(self):
        login_template = jinja_env.get_template("Login/templates/login.html")

class ResourceHandler(webapp2.RequestHandler):
    def get(self):
        resources_template = jinja_env.get_template("templates/resources.html")

class MusicHandler(webapp2.RequestHandler):
    def get(self):
        music_template = jinja_env.get_template("templates/music.html")

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_env.get_template("templates/about.html")

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/glass-bottle", BottleHandler),
    ("/glass-bottle-lg", LGBottleHandler),
    ("/posts", PostsHandler),
    ("/login", LoginHandler),
    ("/resources", ResourceHandler),
    ("/music", MusicHandler),
    ("/about", AboutHandler)

], debug=True)
