from abc import ABC, abstractmethod

class Command(ABC):
    '''This is the abstract base for commands.'''
    @abstractmethod
    def execute(self,*args):
        pass

class CommandHandler:
    '''This is the CommandHandler class.'''
    def __init__(self):
        self.commands={}
    
    def Register_Command(self, command_name: str, command: Command):
        '''This function registers a command.'''
        self.commands[command_name]=command
        print(f"Registered command: {command_name}")
    
    def Execute_Command(self, command_name: str, *args):
        '''Executes a registered command if exists'''
        try:
            if command_name in self.commands:
                self.commands[command_name].execute(*args)
            else:
                print(f"{command_name} :Command not found")
        except (KeyError, TypeError):
            print(f"{command_name} : There is no such command or invalid arguments for the command are given")

    def get_registered_commands(self):
        '''Gives the list of registered commands'''
        return list(self.commands.keys())
