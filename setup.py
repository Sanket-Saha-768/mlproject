from setuptools import find_packages, setup
from typing import List

# Define Metadata
NAME = "mlproject"
VERSION = "0.0.1"
DESCRIPTION = "1st End to End Machine Learning Project"
AUTHOR = "Sanket Saha"
EMAIL = "absccd@email.com"
HYPHEN_E_DOT = '-e .'

# Define project dependencies
def get_requirements(file_path:str) -> List[str]:
    '''
        this function returns the list of requirements needed for the project
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


# Find all Python packages in the project
PACKAGES = find_packages()

setup (
name=NAME,
version=VERSION,
description=DESCRIPTION,
author=AUTHOR,
author_email=EMAIL,
install_requires = get_requirements('requirements.txt'),
packages=PACKAGES
)