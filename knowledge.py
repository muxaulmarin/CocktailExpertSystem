class Knowledge(dict):
    def __init__(self):
        self.domains = {}
        self.variables = {}
        self.nodes = []
        self.edges = []
        self.labels = {}
    
    def addDomain(self, domain):
        name, values, domain_type = domain
        max_N = len(self.domains.keys())
        self.domains[max_N] = {'name': name, 'values': values, 'type': domain_type}

    def editDomain(self, editDomain):
        N, name, values, domain_type = editDomain
        self.domains[N] = {'name': name, 'values': values, 'type': domain_type}

    def mergeDomain(self, domains):
        self.domains.update(domains)
