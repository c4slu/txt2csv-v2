import cmd

class MyCmd(cmd.Cmd):
    """A simple command processor example."""
    
    def do_greet(self, line):
        """greet [name]: Greet the person identified by [name].
        If no name is given, greet the world."""
        if line:
            print("hi, " + line + "!")
        else:
            print("hi, world!")
    
    def do_quit(self, line):
        """Quit the application."""
        print("Quitting.")
        raise SystemExit

if __name__ == '__main__':
    MyCmd().cmdloop()
