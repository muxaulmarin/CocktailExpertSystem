from knowledge import Knowledge

class MLV:
	def __init__(self, knowledge):
		self.knowledge = knowledge				
	
	def inference_logical_mechanism(self, goal):
		request_goals = set([])
		derivable_goals = set([goal])
		useful_rules_ids = set([])
		all_rules = set(self.knowledge['rules'])
		
		N_rg = len(request_goals)
		N_dg = len(derivable_goals)
		N_uri = len(useful_rules_ids)
		
		while True:
			for rule_id in all_rules:
				rule = self.knowledge['rules'][rule_id]
				goal = rule['result'].split(' == ')[0]
				try:
					goal_type = self.knowledge['variables'][goal]['category']
				except KeyError:
					print('goal ',goal)
					print('ruleid ', rule_id)
					break
				if goal in derivable_goals:
					if goal_type == 'Запрашиваемая':
						request_goals.add(goal)
					else:
						derivable_goals.add(goal)
						premises = [premise for premise in rule['premises'] if premise not in ['AND', 'OR', 'NOT']]
						subgoals = [premise.split(' == ')[0] for premise in premises]
						for subgoal in subgoals:
							try:
								subgoal_type = self.knowledge['variables'][subgoal]['category']
							except KeyError:
								print(subgoal)
								print(rule_id)
							if subgoal_type == 'Запрашиваемая':
								request_goals.add(subgoal)
							else:
								derivable_goals.add(subgoal)
				useful_rules_ids.add(rule_id)
			if (len(useful_rules_ids) != N_uri or \
				len(request_goals) != N_rg or \
				len(derivable_goals) != N_dg):
				
				N_rg = len(request_goals)
				N_dg = len(derivable_goals)
				N_uri = len(useful_rules_ids)
				
				all_rules = all_rules.symmetric_difference(useful_rules_ids)
			else:
				self.derivable_goals = derivable_goals
				self.request_goals = request_goals
				self.rules = useful_rules_ids
				break