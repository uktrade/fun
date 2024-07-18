import argparse 
from derec.exporters import get_countries, get_top_types_per_country

def test(arguments):
    if len(list(get_countries())) > 0:
        print("OK: There is some test data. Let's go.")
    else:
        print("ERROR: There is no test data.")


def show_countries():
    for country in get_countries():
        print(country)


def show_top_types():
    # sort exports for a specific country and return the top 3
    def top_three(items):
        return sorted(items, key=lambda i: i.value, reverse=True)[:3]

    for country in get_top_types_per_country().values():
        print(country)
        # for each country enumerate whatever top_three returns
        for index, export in enumerate(top_three(country.exports.values())):
            # and print it out
            print(f"\t{index+1}: {export}")


def show(commands):
    if commands == []:
        print("Incorrect syntax. \nUsage: derec show <what>\n")
        return 
    
    if (commands[0] == "countries"):
        show_countries()
        return
    
    if (commands[0]):
        show_top_types()
        return


def main():
    print()

    # deal with the command line arguments
    parser = argparse.ArgumentParser()
    # arguments.command will store a list of keywords passed as arguments. 
    # `python3 derec one two three` will result in 
    # arguments.command = ['one', 'two', 'three']
    parser.add_argument("command", nargs="+")
    arguments = parser.parse_args()

    # register command functions
    command_functions = {
        "test": test,
        "show": show
    }

    # invoke function corresponding to the first argument
    command_functions[arguments.command[0]](arguments.command[1:])

    print()


main()
