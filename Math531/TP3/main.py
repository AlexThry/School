from src.Class_Step import Step
from src.Class_Task import Task
from src.Class_PERT import PERT

if __name__ == "__main__":
  
  ##_______ Création des étapes _______##
  
  step0 = Step(0, 0, 0)
  step1 = Step(1, 30, 30)
  step2 = Step(2, 120, 120)
  step3 = Step(3, 150, 210)
  step4 = Step(4, 40, 200)
  step5 = Step(5, 50, 210)
  step6 = Step(6, 150, 150)
  step7 = Step(7, 210, 210)
  step8 = Step(8, 220, 220)
  
  steps = [step0, step1, step2, step3, step4, step5, step6, step7, step8]

  ##_______ Création des tâches _______##

  taskA = Task("A", 30, (step0, step1))
  taskB = Task("B", 90, (step1, step2))
  taskC = Task("C", 30, (step2, step3))
  taskD = Task("D", 10, (step1, step4))
  taskE = Task("E", 10, (step4, step5))
  taskF = Task("F", 30, (step2, step6))
  taskG = Task("G", 60, (step6, step7))
  taskH = Task("H", 10, (step7, step8))
  taskt37 = Task("t", 0, (step3, step7))
  taskt57 = Task("t", 0, (step5, step7))
  
  tasks = [taskA, taskB, taskC, taskD, taskE, taskF, taskG, taskH, taskt37, taskt57]
  
    ##_______ Ajout des tâches aux étapes _______##
  
  step0.set_tasks([], [taskA])
  step1.set_tasks([taskA], [taskB, taskD])
  step2.set_tasks([taskB], [taskF, taskC])
  step3.set_tasks([taskC], [taskt37])
  step4.set_tasks([taskD], [taskE])
  step5.set_tasks([taskE], [taskt57])
  step6.set_tasks([taskF], [taskG])
  step7.set_tasks([taskt37, taskt57, taskG], [taskH])
  step7.set_tasks([taskH], [])
  
  print(taskt37.get_connection(True))
  print(taskB.get_begin_step(True))
  print(taskB.get_end_step(True))
  print(taskA.get_end_step(True))
  print(step0.get_next_steps(True))
  print(step1.get_previous_steps())
  
  
  