# that will findout all the pavkages that have in ml project...
from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    # this function will return the list of requirements...
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # to replace the \n from the requirements.txt... 
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 
    
    return requirements
# when we creating a package....
setup(
    # meta data about hte data
    name='ml_project',
    version='0.0.1',
    author='sachin',
    author_email='sachinjangir1319@gmail.com',
    packages=find_packages(),
    # IT IS NOT A GOOD WAY TO WRITE THE PACKAGES THAT WE WANT TO INSTALL...SO GIVE IT A
    # install_requires=['numpy','pandas','seaborn']
    install_requires=get_requirements('requirements.txt')
) 


'''
AFTER DOING THIS OPEN TERMINEL AND WRITE
       pip install -r requirements.txt
'''