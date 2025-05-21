


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this")


    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

    class LeafNode(HTMLNode):
        def __init__(self, tag=None, value=None, text=None):
            super().__init__(tag, value)
            self.text = text
            markup = HTMLNode.to_html(self.tag, self.value)
            return markup