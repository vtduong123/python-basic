class InputString(object):
    def __init__(self):
        self._str = ""
        
    def get_string(self):
        self.str = input()
        
    def print_string(self):
        print (self.str.upper())
        
str_obj = InputString()
str_obj.get_string()
str_obj.print_string()
