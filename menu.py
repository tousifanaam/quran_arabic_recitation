import inspect
from os import system, name


def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Menu():

    class ArgumentNotFuncError(Exception):
        pass

    def __init__(self, *args, validate_zero: bool = True, show_doc: bool = False) -> None:
        for i in args:
            if not inspect.isfunction(i):
                raise self.ArgumentNotFuncError(
                    "Only functions are checked as valid arguments.")
        self.funcs = args
        self.zero = validate_zero
        self.show_doc = show_doc

    def __str__(self):
        def f(x): return f"{'0' * (len(str(len(self.funcs))) - len(str(x)))}"
        res = "Options:\n"
        for x, i in enumerate(self.funcs):
            if self.show_doc:
                try:
                    doc = "\t# " + (i.__doc__.strip())[:50]
                    if len(i.__doc__) > 50:
                        doc += " . . ."
                except TypeError:
                    doc = ""
                except AttributeError:
                    doc = ""
                res += "[{0}{1}] {2} {3}\n".format(f(x + 1),
                                                   str((x + 1)), i.__name__, doc)
            else:
                res += "[{0}] {1}\n".format(f(x + 1), i.__name__)
        return res

    def run(self, custom_str: str = None):

        while True:
            if custom_str != None and isinstance(custom_str, str):
                print(custom_str)
            else:
                print(self.__str__())
            (foo := input("Choose an option: ")) and print()
            try:
                int(foo)
            except ValueError:
                bar = [i for i in self.funcs if i.__name__.lower(
                ).startswith(foo.lower())]
                if len(bar) == 1:
                    bar[0]()
                    break
            else:
                if int(foo) > 0 and int(foo) <= len(self.funcs):
                    self.funcs[int(foo) - 1]()
                    break
                elif self.zero and int(foo) == 0:
                    for i in self.funcs:
                        i()
                    break
            clear()
            print(
                "[!] INVALID OPTION SELECTED. ( No match found for '{0}' )\n".format(foo))


if __name__ == "__main__":
    def one():
        ">>> print('ran one()')"
        print("ran one()")

    def two():
        ">>> print('ran two()')"
        print("ran two()")

    Menu(one, two).run()
