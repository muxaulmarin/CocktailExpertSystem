class Knowledge(dict):
    def __init__(self):
        self['domains'] = {}
        self['variables'] = {}
        self['nodes'] = []
        self['edges'] = []
        self['labels'] = {}
    
    def addDomain(self, domain):
        name, values, domain_type = domain
        max_N = len(self['domains'].keys())
        self['domains'][max_N] = {'name': name, 'values': values, 'type': domain_type}

    def editDomain(self, editDomain):
        N, name, values, domain_type = editDomain
        self['domains'][N] = {'name': name, 'values': values, 'type': domain_type}

    def mergeDomain(self, domains):
        self['domains'].update(domains)

    def loadKnowledge(self, json_file):
        self['domains'] = json_file['domains']
        self['variables'] = json_file['variables']
        self['nodes'] = json_file['nodes']
        self['edges'] = json_file['edges']
        self['labels'] = json_file['labels']