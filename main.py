#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2
import kalkulatorDrugi

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        prvoSt = self.request.get("prvo")
        operacija = self.request.get("opera")
        drugoSt = self.request.get("drugo")

        rezultat = kalkulatorDrugi.kalkulatorD(prvoSt, drugoSt, operacija)
        print rezultat
        podatki = {"prvo število" : prvoSt, "operacija" : operacija, "drugo število" : drugoSt, "rezultat": rezultat}
        return self.render_template("hello.html", podatki)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
