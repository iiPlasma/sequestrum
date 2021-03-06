# Arguments Modules

# Imports
import argparse


def get_arguments():
    """
        Return the arguments in the form of a tuple
    """

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-i", "--install", help="Install packages onto local system. Use all to install all packages.")
    group.add_argument("-r", "--refresh", help="Refresh your dotfiles based on your config.", action="store_true")
    group.add_argument("-u", "--unlink", help="Unlink packages from local system. Use all to unlink all packages.")

    args = parser.parse_args()

    if args.install is not None:
        return ("Install", args.install)
    elif args.refresh:
        return ("Refresh", "all")
    elif args.unlink is not None:
        return ("Unlink", args.unlink)
