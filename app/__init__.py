import os
import pkgutil
import importlib
import inspect
import sys
from app.commands import CommandHandler
from app.commands import Command

logs_dir = 'logs'
os.makedirs(logs_dir, exist_ok=True)

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        print("Initializing the application...")
        self.load_plugins()  # Load plugins dynamically

    def load_plugins(self):
        """Dynamically load all plugins from the `app/plugins` directory."""
        plugins_package = "app.plugins"
        print(f"Loading plugins from {plugins_package}...")
        for _, plugin_name, _ in pkgutil.iter_modules([plugins_package.replace(".", "/")]):
            try:
                print(f"Attempting to load plugin: {plugin_name}")
                plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                        init_signature = inspect.signature(item.__init__)
                        if len(init_signature.parameters) > 1:
                            self.command_handler.register_command(plugin_name.replace("_command", ""), item(self.command_handler))
                            print(f"Registered command: {plugin_name.replace('_command', '')}")
                        else:
                            self.command_handler.register_command(plugin_name.replace("_command", ""), item())
                            print(f"Registered command: {plugin_name.replace('_command', '')}")
            except Exception as e:
                print(f"Failed to load plugin {plugin_name}: {e}")

    def start(self):
        """Start the REPL loop for user interaction."""
        print("Starting the REPL loop...")
        print("Welcome to Calculator! Type 'menu' to see available commands, or 'exit' to quit.")
        self.command_handler.execute_command("menu")  # Show available commands at startup

        while True:
            user_input = input("Enter command: ").strip()
            if user_input.lower() == "exit":
                print("Exiting Calculator...")
                raise SystemExit("Exiting Calculator...")
            user_input_split = user_input.split()
            command_name = user_input_split[0]
            args = user_input_split[1:]
            print(f"Executing command: {command_name} with arguments: {args}")
            self.command_handler.execute_command(command_name, *args)
