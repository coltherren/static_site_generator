class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):
        props_list = []
        if self.props != None:
            for key, value in self.props.items():
                props_list.append(f' {key}="{value}"')
        return "".join(props_list)


    def __repr__(self):
        return f'''
                Tag: {self.tag}
                Value: {self.value}
                Children: {self.children}
                Props: {self.props}
        '''


class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)


    def to_html(self):
        if self.value == None:
            raise ValueError("Tags must contain content (value)")
        elif self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
