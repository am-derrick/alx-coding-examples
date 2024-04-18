import cmd

class MyCmdInterpreter(cmd.Cmd):
    intro = "Welcome to the Enhanced Command Interpreter. Type 'help' to list available commands."
    prompt = "> "

    def do_greet(self, args):
        """Greet the user."""
        print("Hello, how can I help you?")

    def do_sum(self, args):
        """Calculate the sum of two numbers. Usage: sum <num1> <num2>"""
        try:
            num1, num2 = map(float, args.split())
            result = num1 + num2
            print(f"Sum: {result}")
        except ValueError:
            print("Invalid input. Usage: sum <num1> <num2>")

    def do_multiply(self, args):
        """Multiply two numbers. Usage: multiply <num1> <num2>"""
        try:
            num1, num2 = map(float, args.split())
            result = num1 * num2
            print(f"Product: {result}")
        except ValueError:
            print("Invalid input. Usage: multiply <num1> <num2>")

    def do_divide(self, args):
        """Divide two numbers. Usage: divide <num1> <num2>"""
        try:
            num1, num2 = map(float, args.split())
            if num2 == 0:
                print("Error: Division by zero")
            else:
                result = num1 / num2
                print(f"Quotient: {result}")
        except (ValueError, ZeroDivisionError):
            print("Invalid input or division by zero. Usage: divide <num1> <num2>")

    def do_power(self, args):
        """Calculate the power of a number. Usage: power <base> <exponent>"""
        try:
            base, exponent = map(float, args.split())
            result = base ** exponent
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Usage: power <base> <exponent>")

    def do_quit(self, args):
        """Exit the interpreter."""
        return True

if __name__ == "__main__":
    MyCmdInterpreter().cmdloop()

