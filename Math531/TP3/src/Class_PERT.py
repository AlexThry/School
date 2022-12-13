class PERT:
	def __init__(self, root):
		self.root = root

	def critique(self, toStr=False, critique=[]):
		if not critique:
			if toStr:
				critique.append(self.root.get_number())
			else:
				critique.append(self.root)
		if not self.root.get_next_steps():
			return critique
		else:
			for step in self.root.get_next_steps():
				if step.get_au_plus_tard() == step.get_au_plus_tot():
					new_step = step
			if toStr:
				critique.append(new_step.get_number())
			else:
				critique.append(new_step)
			return PERT(new_step).critique(toStr, critique)

	def compute_au_plus_tot(self):
		if not self.root.get_previous_steps():
			self.root.set_au_plus_tot(0)
		for task in self.root.get_next_tasks():
			if self.root.get_next_tasks() and (not(task.get_end_step()[0].get_au_plus_tot()) or task.get_end_step()[0].get_au_plus_tot() < task.get_begin_step()[0].get_au_plus_tot() + task.get_duration()):
				task.get_end_step()[0].set_au_plus_tot(task.get_begin_step()[0].get_au_plus_tot() + task.get_duration())
			PERT(task.get_end_step()[0]).compute_au_plus_tot()
			