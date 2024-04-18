import cmd

class MyCmd(cmd.Cmd):
    intro = "Welcome to my cmd, type 'help' for more commands.\n"
    prompt = "(mycmd)"

    def do_greet(self, args):
        """Greets the user"""
        print("Hey there, how may I help you?")

    def do_sum(self, args):
        """Sums two nums"""
        try:
            num1, num2 = map(float, args.split())
            result = num1 + num2
            print(f"The sum is {result}")
        except ValueError:
            print("Invalid input. Usage sum <num1> <num2>")

    def do_multiply(self, args):
        """Multiplies two numbers"""
        try:
            num1, num2 = map(float, args.split())
            result = num1 * num2
            print(f"The product is {result}")
        except ValueError:
            print("Invalid input. Usage multiplu <num1> <num2>")

    def do_quit(self, args):
        """exits mycmd"""
        return True


if __name__ == "__main__":
    MyCmd().cmdloop()


