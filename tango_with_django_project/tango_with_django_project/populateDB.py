import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category,Pages

#create list of Pages
def populate():
	python_pages = [
	 {"title": "Official Python Tutorial",
	 "url":"http://docs.python.org/2/tutorial/"},
	 {"title":"How to Think like a Computer Scientist",
	 "url":"http://www.greenteapress.com/thinkpython/"},
	 {"title":"Learn Python in 10 Minutes",
	 "url":"http://www.korokithakis.net/tutorials/python/"} ]

	django_pages = [
	 {"title":"Official Django Tutorial",
	 "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
	 {"title":"Django Rocks",
	 "url":"http://www.djangorocks.com/"},
	 {"title":"How to Tango with Django",
	 "url":"http://www.tangowithdjango.com/"} ]


	other_pages = [
	 {"title":"Bottle",
	 "url":"http://bottlepy.org/docs/dev/"},
	 {"title":"Flask",
	 "url":"http://flask.pocoo.org"} ]

	cats = {"Python": {"pages": python_pages},
	 "Django": {"pages": django_pages},
	 "Other Frameworks": {"pages": other_pages} }

	for cat,catsPages in cats.items():
		c=add_cat(cat)
		for page in catsPages['pages']:
			add_page(c,page['title'],page['url'])

def add_cat(category):
	c=Category.object.get_or_create(name=category)[0]
	c.save()
	return c 

def add_page(category_name,title,url_str,views=0):
	p=Pages.object.get_or_create(category=category_name,title=title)[0]
	p.url=url_str
	p.views=views
	p.save()
	return p

if __name__ == '__main__':
	print('script starts')
	populate()
	print('script ends')

