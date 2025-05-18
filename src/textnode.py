from enum import Enum

class TextType(Enum):
    pass

class TextNode():
    def __init__(text, text_type, url):
        self.text = text
        self.text_type = text_type
        if url == "":
            self.url = None
        else:
            self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url)
        return False
    
    def __repr__(self):
        return f"{self.text}, {self.text_type}, {self.url}"
    
