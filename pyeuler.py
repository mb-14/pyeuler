"""
Author : Miroojin Bakshi
Description : Unofficial API for Project Euler.

"""

import urllib, urllib2, cookielib

 
LOGIN_URL='http://projecteuler.net/login'
PROBLEM_URL='http://projecteuler.net/minimal=%s'
ALL_PROBLEMS_URL='http://projecteuler.net/minimal=problems'
PROFILE_URL='http://projecteuler.net/minimal=profile'

def getProblem(_id):
	"""Get information about problem #_id."""
	try:
		html = urllib2.urlopen(PROBLEM_URL%_id).read()
	except urllib2.HTTPError:
           	print "Network error"
	return html


class User():
        opener=None
	def __init__(self, username, password):
		cookie_jar = cookielib.CookieJar()
                User.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
                urllib2.install_opener(User.opener)
		params = urllib.urlencode({'username': username, 'password': password, 'login': 'Login'})
		try:
			User.opener.open(LOGIN_URL,params)
			profile_page=User.opener.open(PROFILE_URL).read()
		except urllib2.HTTPError:
           		print "Network error"
		(self.username, self.alias,self.country,self.language,self.problems_solved,self.level,self.solved_string) = profile_page.split('##')
		
	
	@property	
        def username(self):
        	return self.username
 
	@property	
        def alias(self):
	        return self.alias
	
	@property	
        def country(self):
	        return self.country 

        @property	
        def language(self):
	        return self.language

	@property	
        def problems_solved(self):
	         return self.problems_solved

	@property	
        def level(self):
	         return self.level

	@property	
        def solved_string(self):
	        return self.solved_string

	class Problem():
		
		def __init__(self,_id):	
			_opener=User.opener
			try
				problems_page=_opener.open(ALL_PROBLEMS_URL).read()
			except urllib2.HTTPError:
           			print "Network error"
			lines=problems_page.split("\n")
			(self.number, self.title, self.published, self.updated, self.solvedby, self.solved, self.answer) = lines[_id-1].split('##')
                
		@property	
	        def number(self):
	        	return self.number
 
		@property	
	        def title(self):
		        return self.title
	
		@property	
	        def published(self):
		        return self.published
	
	        @property	
	        def updated(self):
		        return self.updated

		@property	
	        def solvedby(self):
		        return self.solvedby
		
		@property	
	        def solved(self):
		        return self.solved
	
		@property	
        	def answer(self):
		        return self.answer
