#!/usr/bin/python3
"""Defining HBNBCommand class."""

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the command line interpreter in my HBNB project."""
    
    prompt = "(hbnb) "
    list_class = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    list_err = [
        "** class name missing **",
        "** class doesn't exist **",
        "** instance id missing **",
        "** no instance found **",
        "** attribute name missing **",
        "** value missing **"
    ]

    def do_create(self, line):
        """Creating the  new instance of the BaseModel."""
        args = shlex.split(line)
        if not args:
            print(self.list_err[0])
        elif args[0] in self.list_class:
            obj = eval(args[0])()
            print(obj.id)
            obj.save()
        else:
            print(self.list_err[1])

    def do_show(self, line):
        """Showing the object by id"""
        args = shlex.split(line)
        if not args:
            print(self.list_err[0])
        elif args[0] not in self.list_class:
            print(self.list_err[1])
        elif len(args) == 1:
            print(self.list_err[2])
        else:
            objs = models.storage.all()
            mykey = "{}.{}".format(args[0], args[1])
            print(objs.get(mykey, self.list_err[3]))

    def do_destroy(self, line):
        """Deleting object by id."""
        args = shlex.split(line)
        if not args:
            print(self.list_err[0])
        elif args[0] not in self.list_class:
            print(self.list_err[1])
        elif len(args) == 1:
            print(self.list_err[2])
        else:
            objs = models.storage.all()
            mykey = "{}.{}".format(args[0], args[1])
            objs.pop(key, None)
            models.storage.save()

    def do_all(self, line):
        """Displaying all the instances or for a specific class."""
        args = shlex.split(line)
        if not args:
            objs = models.storage.all()
            print([str(obj) for obj in objs.values()])
        elif args[0] not in self.list_class:
            print(self.list_err[1])
        else:
            objs = models.storage.all()
            print([str(obj) for obj in objs.values() if type(obj).__name__ == args[0]])

    def do_update(self, line):
        """Updating the object by class name and id with new attributes and values."""
        args = shlex.split(line)
        if not args:
            print(self.list_err[0])
        elif args[0] not in self.list_class:
            print(self.list_err[1])
        elif len(args) < 2:
            print(self.list_err[2])
        else:
            objs = models.storage.all()
            mykey = "{}.{}".format(args[0], args[1])
            if mykey in objs:
                if len(args) < 3:
                    print(self.list_err[4])
                elif len(args) < 4:
                    print(self.list_err[5])
                else:
                    setattr(objs[mykey], args[2], args[3].replace("\"", ""))
                    models.storage.save()
            else:
                print(self.list_err[3])

    def do_quit(self, line):
        """Quit command"""
        return True

    def do_EOF(self, line):
        """EOF command"""
        return True

    def emptyline(self):
        """command line is empty and typed."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
