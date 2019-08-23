import re

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    #using set will allow only unique items. convert back to list
    uniqueNames = list(set(names))
    titleUniqueNames = []
    for name in uniqueNames:
        titleUniqueNames.append(name.title())
        
    return(titleUniqueNames)

#function to pull last name. to be used as key in sorted
def getSur(name):
    names = re.findall(r'\s+(.*)', name)
    return(names[0])

#key allows me to sort by the output of a function that takes one input
def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # using key getSur
    sortedBySur =   sorted(names, key=getSur, reverse = True)
    return(sortedBySur)


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...
    shortest = ""
    for name in names:
        name = name.split(' ')
        if shortest == "":
            shortest = name[0]
        else:
            if len(name[0]) > len(shortest):
                break
            else:
                shortest = name[0]
    return(shortest)

print(shortest_first_name(NAMES))  

