#!/usr/bin/python3
"""
console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        Quit command to exit
        """
        return True

    def do_EOF(self, arg):
        """
        Exits console
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
