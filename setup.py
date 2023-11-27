from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements()->List[str]:
    """
    This function will return the list of requirements.
    """
    requirement_list:List[str] = []
    with open('requirements.txt','r') as file:
        read_list = file.readlines()
        for lib in read_list:
            if lib != HYPHEN_E_DOT:
                requirement_list.append(lib)
        print(requirement_list)
    return requirement_list

get_requirements()


setup(
    name='sensor',
    author='abhaykeni',
    version='0.0.1',
    author_email='abhaykeni@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements(),
)

