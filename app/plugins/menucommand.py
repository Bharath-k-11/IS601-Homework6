from app.commands import Command

class Menu(Command):
    '''This displays available commands in the system'''
   
    def __init__(self, command_handler):
     self.command_handler=command_handler

    def execute(self, *args):
        commands=self.command_handler.Get_Registered_Commands()

        if not commands:
            print("There are no commands")
            return
        print("Commands Available:")
        for command_name in commands:
            print(f"-> {command_name}") 
        print("Type 'exit' to quit" )
