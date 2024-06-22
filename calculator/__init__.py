import os
import importlib.util
from calculator.commands import CommandHandler, Command
from dotenv import load_dotenv
import logging
import logging.config

class Calculator:
    def __init__(self, plugin_dir = 'plugins'):
        if not os.path.exists('logs'):
            os.makedirs('logs')
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.plugin_dir = plugin_dir
        self._load_plugins()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def _load_plugins(self):
        plugins_path = os.path.join(os.path.dirname(__file__), self.plugin_dir)
        # print(f"Loading plugins from: {plugins_path}")  # Removed debug print

        if not os.path.exists(plugins_path):
            print(f"Plugin directory does not exist: {plugins_path}")
            return

        for subdir in os.listdir(plugins_path):
            subdir_path = os.path.join(plugins_path, subdir)
            if os.path.isdir(subdir_path):
                init_path = os.path.join(subdir_path, '__init__.py')
                # print(f"Checking directory: {subdir_path}")  # Removed debug print
                if os.path.exists(init_path):
                    # print(f"Loading plugin from: {init_path}")  # Removed debug print
                    module_name = f"calculator.plugins.{subdir}"
                    spec = importlib.util.spec_from_file_location(module_name, init_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for attr in dir(module):
                        if attr.endswith("Command"):
                            command_class = getattr(module, attr)
                            if callable(command_class) and issubclass(command_class, Command):
                                if command_class.__module__ == module_name:
                                        if attr == "MenuCommand":
                                            instance = command_class(self.command_handler)
                                        else:
                                            instance = command_class()
                                        command_name = instance.__class__.__name__.replace('Command', '').lower()
                                        # print(f"Registering command: {command_name}")  # Removed debug print
                                        self.command_handler.register_command(command_name, instance)

    def start(self):
        print("Type 'menu' to see the list of available commands or 'exit' to exit.")
        while True:
            try:
                user_input = input(">>> ").strip()
                if user_input.lower() == 'exit':
                    print("Exiting the calculator. Goodbye!")
                    break
                self.command_handler.execute_command(user_input)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
