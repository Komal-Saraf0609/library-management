# -*- coding: utf-8 -*-
# Copyright (c) 2021, komal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname


class Article(WebsiteGenerator):
    def autoname(self):
        self.name = make_autoname(self.article_name)
        self.name = self.name[:-5]
        #art/.yyyy/.####
	
    

#class Article(WebsiteGenerator):
    #def autoname(self):
        # select a project name based on customer
        #prefix = `P-{}-`.format(self.article_name)
        #self.name = getseries(prefix, 3)
