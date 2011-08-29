from setuptools import setup, find_packages
setup(
    name='django-portfolio',
    version='0.1.0',
    description='A reusable Django app for displaying a portfolio',
    author='Will Larson',
    packages=['portfolio'],
    classifiers=[
        'Development Status :: 1  - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

