from src.Class_Node import Node
from src.Class_Arc import Arc
from src.Class_PERT import PERT

if __name__ == "__main__":
  step0 = Node(0, 0, 0, None, [taskA])
  step1 = Node(1, 30, 30)
  step2 = Node(2, 120, 120)
  step3 = Node(3, 150, 210)
  step4 = Node(4, 40, 200)
  step5 = Node(5, 50, 210)
  step6 = Node(6, 150, 150)
  step7 = Node(7, 210, 210)
  step8 = Node(8, 220, 220)
  

  taskA = Arc("A", 30, step0, step1)
  taskB = Arc("B", 90, step1, step2)
  taskC = Arc("C", 30, step2, step3)
  taskD = Arc("D", 10, step1, step4)
  taskE = Arc("E", 10, step4, step5)
  taskF = Arc("F", 30, step2, step6)
  taskG = Arc("G", 60, step6, step7)
  taskH = Arc("H", 10, step7, step8)