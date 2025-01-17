"""
Release

pip3 install --user twine
Update the version string below.
Build package with `python3 setup.py sdist`
Upload package with `twine upload dist/*`
"""

import sys
from setuptools import setup
from setuptools.command.install import install

if sys.version_info[0] < 3:
    sys.stderr.write('Only Python 3 supported\n')
    sys.exit(1)


class InstallNativeApp(install):

    def run(self):
        self.do_egg_install()
        print("Execute `nativePass install` to install the native"
              "host application")


setup(
  name="chrome-pass",
  version="0.3.0",
  description="Chrome Native application for pass -"
              "the standard Unix password manager",
  url="https://github.com/hsanson/chrome-pass",
  author="Horacio Sanson",
  author_email="e@e.com",
  license="MIT",
  install_requires=['python-gnupg'],
  scripts=["nativePass"],
  cmdclass={'install': InstallNativeApp}
  )
