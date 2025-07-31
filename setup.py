from setuptools import find_packages,setup
from typing import List

hyphen='-e .'

def get_requirements(filepath:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    if hyphen in requirements:
        requirements.remove(hyphen)

    return requirements
setup(
    name='ML Project',
    version='0.0.1',
    author='Tushar Badhwar',
    author_email='tusharbadhwar.bt23cseds@pec.edu.in',
    packages=find_packages(),
    install_req=get_requirements('requirements.txt')
)