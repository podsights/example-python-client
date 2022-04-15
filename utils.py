from dataclasses import dataclass

@dataclass
class Option:
    id: str
    name: str


def selector(question, options):
    selections = '\n'.join([f"{i}: {option.name}" for i, option in enumerate(options)])
    try:
        selection = int(input(f"{question}\n\n{selections}\n\n"))
    except ValueError:
        print("\n\nPlease enter a valid integer!")
        return selector(question, options)

    if 0 <= selection < len(options):
        option = options[selection]
        return option.id
    print("Please select a valid option number!")
    return selector(question, options)

def confirm_variables(question):
    try:
        selection = int(input(f"{question}\n\n0:YES\n1:NO\n\n"))
    except ValueError:
        print("\n\nPlease enter a valid option!")
        return selector(question)

    if selection == 1:
        print("\n\nThe variables were not valid...\n\n")
        print("Exiting\n\n")
        exit()
    elif selection == 0:
        print("\n\nContinuing with creating a campaign...\n\n")
        return
    else:
        print("Please select a valid option number!")
        return selector(question)
