from setuptools import setup, find_packages

setup(
    name='bandcamp-radio',
    version='0.1',
    description='Make your own mix tape. I cannot stress it enough: Always support bands you like!',
    url='https://github.com/Virusmater/bandcamp-radio',
    author='Dima Kompot',
    author_email='virusmater@gmail.com',
    license='MIT',
    install_requires=['requests', 'python-vlc', 'urllib3'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['bandcamp-radio=bandcamp_radio.__main__:main']
    )
)