from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e.'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Use strip() to remove leading/trailing whitespace
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

if __name__ == '__main__':
    setup(
        name='mlproject',
        version='0.0.1',
        author='nimra',
        author_email='nimraaslam3132@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements('requirements.txt')  # Provide the correct file name
    )





