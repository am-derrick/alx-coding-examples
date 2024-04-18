try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

import cmd


class HelloWorld(cmd.Cmd):

    intro = 'My CLI. Type "help" for more information.'
    prompt = '(mycli) '

    PROGRAMS = ['SE', 'IntroSE', 'Salesforce', 'AWS', 'DataAnalytics']

    def do_hello(self, program):
        if program and program in self.PROGRAMS:
            hello = f'Hello, you have been admitted to the ALX {program} program.' 
        elif program:
            hello = f'Hello, unfortunately {program} isn\'t part of ALX\'s programs.'
        else:
            hello = 'Hello there, please select a program.'
        print(hello)


    def help_hello(self):
        print('\n'.join([
            'hello [program]',
            'Says hello to a user after selecting a program',
            ]))

    def complete_hello(self, text, line, begidx, endidx):
        if not text:
            completions = self.PROGRAMS[:]
        else:
            completions = [p for p in self.PROGRAMS if p.startswith(text)]
        return completions

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
