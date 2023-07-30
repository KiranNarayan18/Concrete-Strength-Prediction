import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Concrete-Strength-regression'
AUTHOR_NAME = 'kiran-narayan1'
SRC_REPO = 'ConcreteStrength'
AUTHOR_EMAIL = '@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='python package for Concrete-Strength-Prediction',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src'),

)