from setuptools import setup

setup(name="pycenter",
	version="0.1",
	description="Calculate percentages from your command line",
	url="https://github.com/Crytlig/pycenter",
	author="Claes Rytlig",
	author_email="no@gmail.com",
	license='MIT',
	packages=["pycenter"],
	scripts=["bin/pycenter"],
	zip_safe=False)