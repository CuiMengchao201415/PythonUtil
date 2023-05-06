import os
import sys
sys.path.append(os.path.realpath(__file__)[0])

parentClass = object
currentDir = os.path.split(os.path.realpath(__file__))[0] + '/'
if os.path.exists(currentDir + "StringUtilsEntity.py") or os.path.exists(currentDir + "StringUtilsEntity.pyc"):
    try:
        StringUtilsEntity = object
        exec('from .StringUtilsEntity import StringUtilsEntity')
        parentClass = StringUtilsEntity
    except Exception as e:
        print(f'\033[0;31mimportError: {e}\033[0m')


class StringUtils(parentClass):
    def __init__(self):
        super(StringUtils, self).__init__()
        if os.path.exists(currentDir + f'{self.__class__.__name__}'):
            data = {}
            with open(currentDir + f'./{self.__class__.__name__}', 'r', encoding='utf8') as fp:
                try:
                    data = eval(fp.read())
                except Exception as e:
                    self.printError(e)
            for key in data:
                value = data[key]
                exec(f'self.{key}="""{value}"""')
        self.printStatement()

    def get(self, key):
        value = None
        try:
            if hasattr(self, key): value = eval(f'self.{key}')
        except Exception as e:
            self.printError(e)
        finally:
            return value

    def set(self, key, value, replace=True):
        try:
            if not hasattr(self, key) or replace==True: exec(f'self.{key}="{value}"')
        except Exception as e:
            self.printError(e)

    def printError(self, e):
        print(f'\033[0;31m{self.__class__.__name__}Error: {e}\033[0m')
        with open(currentDir + f'./{self.__class__.__name__}ErrorLog', 'a+') as fp:
            fp.write(f"{e}\n")

    def printStatement(self):
        print(f'\033[1;33m{self.statement}\033[0m\n')

stringUtils = StringUtils()