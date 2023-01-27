class Story:
    def __init__(self, page, story, scenario, description):
        self.page = page
        self.story = story
        self.scenario = scenario
        self.description = description

    def __str__(self):
        str = self.page + '\n'
        str += self.story + '\n'
        str += self.scenario + '\n'
        str += self.description
        return str
