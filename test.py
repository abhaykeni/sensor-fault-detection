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
                lib = lib.replace('\n','')
                requirement_list.append(lib)
        print(requirement_list)
    return requirement_list

get_requirements()
