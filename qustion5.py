class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('\t'*self.level, text)

with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('Hi 2')
        with indent:
            indent.print('Hi 3')
    indent.print('Hi 4')
