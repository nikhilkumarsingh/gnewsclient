from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name = 'gnewsclient',
      version = '1.0',
      classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
	    'Programming Language :: Python :: 2',
	    'Programming Language :: Python :: 2.6',
	    'Programming Language :: Python :: 2.7',
	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.3',
	    'Programming Language :: Python :: 3.4',
	    'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
      ],
      keywords = 'google news feed python client',
      description = 'Python client for Google News feed.',
      long_description = readme(),
      url = 'http://github.com/nikhilkumarsingh/gnewsclient',
      author = 'Nikhil Kumar Singh',
      author_email = 'nikhilksingh97@gmail.com',
      license = 'MIT',
      packages = ['gnewsclient'],
      install_requires = ['requests', 'bs4', 'html5lib'], 
      include_package_data = True,
      zip_safe = False)