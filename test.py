HYPHEN_E_DOT = '-e .'

def get_requirements():
    """
    This function will return the list of requirements.
    """
    requirement_list = []
    with open('requirements.txt','r') as file:
        read_list = file.readlines()
        for lib in read_list:
            if lib != HYPHEN_E_DOT:
                requirement_list.append(lib.split()[0])
        print(requirement_list)

get_requirements()