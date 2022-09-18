#!/usr/bin/python3
"""
console
"""

import cmd
import shlex
import models
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel, "User": User
           }


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

    def emptyline(self):
        """
        Overwriting the emptyline method
        """
    def do_create(self, arg):
        """
        Creates a new instance of a class
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            instance = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance .id)
        instance.save()

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and is
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        prints all string rep of all instances based  orn not on the class name
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            for item in models.storage.all().values():
                obj_lists.appent(str(itme))
            print("[", end="")
            pritn(", ".join(obj_list), end="")
            print("]")
        elif args[0] in classes:
            for item in storage.all():
                if arg[0] in item:
                    obj_list.append(str(models.storage.all()[key]))
                print("[", end="")
                print(", ".join(obj_list), end="")
        else:
            print("** class doesn't exists **")

    def do_show(self, arg):
        """
        Prints an instance as a string based on the class and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class doesn't exist **")
            return False
        if arg[0] in classes:
            if len(args) > 1:
                value = args[0] + "." + args[1]
                if value in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based onthe class name and id
        """
        args = shlex.split(arg)
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
