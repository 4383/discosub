def ui(part):
    commands = {}
    for interaction, action in part.items():
        result = input(action)
        commands.update({interaction: result})
    return commands


def splash():
    success("< discosub >")

def menu():
    choice = None
    print("Available functionalities :")
    print("\t\t1 create project")
    print("\t\t2 search template")
    while not choice:
        choice = int(input("Choose action"))
        print(type(choice))
        print(choice)
        if choice != 1 and choice != 2:
            choice = None
            print("Bad input !")


def description():
    content = """
    Current available commands:
    \t\tcreate : Create a new apps
    \t\tgenerate : Generate a new project file configuration
    """
    return content


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def fail(content):
    print("{0}{1}{2}{3}".format(
        Colors.FAIL, Colors.BOLD, content, Colors.ENDC
    ))


def search(name, description):
    print("{0}{1}{2}{3}: {4}".format(
        Colors.OKGREEN,
        Colors.BOLD,
        name,
        Colors.ENDC,
        description,
    ))


def success(content):
    print("{0}{1}{2}{3}".format(
        Colors.OKGREEN,
        Colors.BOLD,
        content,
        Colors.ENDC,
    ))


def warning(content):
    print("{0}{1}{2}{3}".format(
        Colors.WARNING, Colors.BOLD, content, Colors.ENDC
    ))


def info(content):
    print("{0}{1}{2}{3}".format(
        Colors.OKBLUE, Colors.BOLD, content, Colors.ENDC
))
