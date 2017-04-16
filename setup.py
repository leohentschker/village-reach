from setuptools.command.install import install
from distutils.core import setup


class PybluezInstall(install):
    def run(self):
        install.run(self)

setup(
    name='VillageReach',
    version='0.1.0',
    author='D4D',
    author_email='leohentschker@college.harvard.edu',
    packages=['villagereach', 'villagereach.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/VillageReach/',
    license='LICENSE.txt',
    description='Facilitating file transfer between drones and basis',
    long_description=open('README.md').read(),
    install_requires=[],
    cmdclass={"install": PybluezInstall}
)
