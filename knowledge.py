class Knowledge(dict):
    def __init__(self):
        self['domains'] = {}
        self['variables'] = {}
        self['nodes'] = []
        self['edges'] = []
        self['labels'] = {}
    
    def addDomain(self, domain):
        name, values = domain
        self['domains'][name] = values

    def editDomain(self, name, values):
        self['domains'][name] = values

    def mergeDomain(self, domains):
        self['domains'].update(domains)