from setuptools import setup, find_packages


setup(
    name='gears-coffeescript',
    version='0.1.dev',
    url='https://github.com/gears/gears',
    license='ISC',
    author='Mike Yumatov',
    author_email='mike@yumatov.org',
    description='CoffeeScript compiler for Gears',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
