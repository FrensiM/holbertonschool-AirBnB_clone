#!/usr/bin/python3
'''Module of AirBNB console'''
import cmd
import sys
import os


class HBNBCommand(cmd.Cmd):
    '''console func'''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''exit the console'''
        return True

    def do_EOF(self, arg):
        '''exit with end of life'''
        return True

    def empty_line(self):
        '''line wiht empty element'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
