class todo:
    def __init__(self,title,description,completestatus):
        self.title = title
        self.description = description
        self.completestatus = completestatus

    def maketitle(self,prompt):
        user_input = input(prompt)
        self.title = user_input
        return self.title
#Make this into an input outside the class