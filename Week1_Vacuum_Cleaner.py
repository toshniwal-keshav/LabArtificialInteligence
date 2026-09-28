#Vacuum Cleaner
def VacuumAgent(loc, statA, statB):
  if loc == 'A' :
    if statA == 'D':
      print("Suck Dirt At A")
      statA = 'C'
    if statB == 'D':
      print("Move to B")
      loc = 'B'
      VacuumAgent(loc, statA, statB)
    else :
      print("Job Done")
  else :
    if statB == 'D':
      print("Suck Dirt At B")
      statB = 'C'
    if statA == 'D':
      print("Move to A")
      loc = 'A'
      VacuumAgent(loc, statA, statB)
    else:
      print("Job Done")

(loc, statA, statB) = input("Enter Location , Status of A and B\n").split()
VacuumAgent(loc, statA, statB)
