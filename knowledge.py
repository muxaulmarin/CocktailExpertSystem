class Knowledge():
    def __init__(self):
        self.domains = {}
        self.variables = {}
        self.facts = {}
        self.rules = {}
    
    def addDomain(self, domain):
        name, values = domain
        self.domains[name] = values

    def editDomain(self, name, values):
        self.domains[name] = values

    def mergeDomain(self, domains):
        self.domains.update(domains)

    def loadKnowledge(self, dict_like):
        self.domains = dict_like.domains
        self.variables = dict_like.variables
        self.facts = self.facts
        self.rules = self.rules