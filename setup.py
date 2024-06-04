from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
    name='Cherv',
    version='0.1',
    packages=find_packages(),
    description='Аналог CowSay, только вместо коровы - червь.',
    long_description=readme(),
    author='Павел, Евгений',
    maintainer='Павел',
    maintainer_email='nadokto8@gmail.com',
    author_email='nadokto8@gmail.com',
    url='https://github.com/AyaalTech/wormsay-python.git',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='cherv cowsay python library',
    install_requires=[],
    python_requires='>=3.7'
)