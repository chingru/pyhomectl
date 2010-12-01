from distutils.core import setup

setup(name='pyhomectl',
        version='1.0',
        description='Python tool for controlling LG TVs and other domestic devices',
        author='Thomas Medhurst',
        author_email='tom@tommed.co.uk',
        url='http://www.tommed.co.uk'
        packages=[
                'pyhomectl',
                'pyhomectl.televisions',
                'pyhomectl.televisions.lg',
                'pyhomectl.test',
                'pyhomectl.test.tools',
                ],
        )
