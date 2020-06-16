import re

def converter():
    # Open index.txt
    fileobj = open(r"index.txt")

    # Regex to search for proper noun terms

    proper = re.compile(r'^[A-Z][-A-Za-z\s]+')
    num = re.compile("[0-9]+")

    # Create dict
    index = {}

    # Put in dictionary

    for line in fileobj:
        termMatch = proper.search(line)
        pageMatch = num.search(line)
        if termMatch is not None and pageMatch is not None:
            termKey = termMatch.group(0)
            termPage = pageMatch.group(0)
            index.update({termKey: int(termPage)})
            print("Added" + termKey + "to dictionary with page number: " + termPage)

    return(index)