from setuptools import setup, find_packages

setup(
    name='Cherv',
    version='0.4.3',
    packages=find_packages(),
    description='An analogue of CowSay, only instead of a cow there is a worm.',
    long_description=\
    """
    An analogue of CowSay, only instead of a cow there is a worm.\n
    Usage:\n
    ``python -m cherv [your message]``\n
    The message can be entered in any length.\n
    """,
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