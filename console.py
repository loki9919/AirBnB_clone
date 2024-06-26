#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
import json
import re

classes = ["BaseModel", "User", "Place", "City", "Amenity", "State", "Review"]


def check_arg(arg):
    """check for the arg to print if something is missing"""
    my_list = arg.split(" ")
    key = ""
    if len(arg) < 1:
        print("** class dosn't exist **")
        return True
    elif my_list[0] not in classes:
        print("** class doesnt exist **")
        return True
    elif len(my_list) < 2:
        print("** instance id missing **")
        return True
    else:
        return False

def count(obj):
    """count instances"""
    counter = 0
    allobjs = storage.all()
    for key, value in allobjs.items():
        allclass = (key.split(".")[0])
        if allclass == obj:
            counter += 1
    print(counter)


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""
    prompt = "(hbnb) "

    def precmd(self, line):
        """this method is called after the line has been input but before
            it has been  interpreted"""
        if "." in line:
            args = re.split(r'\.|\(|\)|, |{|}|: ', line)
            line = args[1] + " " + args[0]
            if len(args) > 3:
                line = line + " " + args[2][1:-1]
            if len(args) > 4:
                if len(args[3]) == 0:
                    i = 4
                    while args[i]:
                        upline = args[0] + " " + args[2][1:-1]
                        upline = upline + " " + args[i][1:-1] + " " + args[i+1]
                        self.do_update(upline)
                        i += 2
                    return " "
                else:
                    line = line + " " + args[3][1:-1] + " " + args[4]
            if "count" in args:
                count(args[0])
                line = "\n"
        return line

    def emptyline(self):
        """called when an empty line is entered in response to the prompt"""
        pass

    def do_EOF(self, line):
        """EOF command"""
        return True

    def do_quit(self, arg):
        """quit command"""
        return True

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if len(arg) <= 0:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """prints the string representation of an instance based on the
        class name and id"""
        if check_arg(arg) is False:
            my_list = arg.split(" ")
            key = my_list[0] + "." + my_list[1]
            allobjs = storage.all()
            try:
                print(allobjs[key])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id (save the
        change into the JSON file)"""
        if check_arg(arg) is False:
            try:
                my_list = arg.split(" ")
                key = my_list[0] + "." + my_list[1]
                allobjs = storage.all()
                del allobjs[key]
                with open("file.json", mode="w", encoding='UTF-8') as f:
                    for key, value in allobjs.items():
                        allobjs[key] = value.to_dict()
                    json.dump(allobjs, f)
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """prints all string representation of all instances based
        or not on the class name"""
        allobjs = storage.all()
        objlist = []
        if len(arg) <= 0:
            for key, value in allobjs.items():
                objlist.append(str(value))
            print(objlist)
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            for key, value in allobjs.items():
                allclass = (key.split(".")[0])
                if allclass == arg:
                    objlist.append(str(value))
            print(objlist)

    def do_update(self, arg):
        """updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)"""
        if check_arg(arg) is False:
            my_list = arg.split(" ")
            key = my_list[0] + "." + my_list[1]
            allobjs = storage.all()
            if key in allobjs:
                if len(my_list) < 3:
                    print("** attribute name missing **")
                elif len(my_list) < 4:
                    print("** value missing **")
                else:
                    setattr(allobjs[key], my_list[2], eval(my_list[3]))
                    with open("file.json", mode="w", encoding='UTF-8') as f:
                        for k, v in allobjs.items():
                            allobjs[k] = v.to_dict()
                        json.dump(allobjs, f)
                    allobjs = storage.reload()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
