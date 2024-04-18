try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

import cmd
from func.add.py import add


class HelloWorld(cmd.Cmd):
    """our hello world class for our cli"""

    intro = "My CLI. Type 'help' for more details."
    prompt = '(mycli) '

    PROGRAMS = ['SE', 'introSE', 'Salesforce', 'AWS', 'DataAnalytics']

    def do_hello(self, program):
        if program and program in self.PROGRAMS:
            hello = f'Hello there, you have selected ALX\'s {program} program.'
        elif program:
            hello = f'Hello there, unfortunately the {program} isn\'t available at ALX.'
        else:
            hello = 'Hello there, please select a program of choice.'
        print(hello)

    def help_hello(self):
        print('\n'.join([
            'hello [program]',
            'Says hello to a user based on a chosen program.']))

    def do_print(self, name):
        name = 'Brian'
        print(f'Hey {name}.')

    def do_adds(self, line):
        add(2,3)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
