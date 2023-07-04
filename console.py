#!/usr/bin/python3
'''Module of AirBNB console'''
import cmd
import sys
import os


class HBNBCommand(cmd.Cmd):
    '''console func'''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''Exit the program with EOF'''
        return True

    def emptyline(self):
        ''' dont execute empty line entered'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
