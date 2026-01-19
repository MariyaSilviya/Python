# At the start of the day you have a checklist The tasks which you were able to finish, should get added to completed_tasks
#  The tasks which you were not able to finish, should get added to incomplete_tasks 
# This project is about organizing your daily tasks into two categories: completed tasks and incomplete tasks.
#  Here’s how it works: 1. At the start of the day, you create a checklist of tasks you want to accomplish.
#  2. At the end of the day, you review which tasks you could finish and which you couldn’t. – If a task is finished, you move it to the completed tasks list. – If a task is not finished, you move it to the incomplete tasks list.
#  This way, by the end of each day, you’ll have a clear overview of what you completed and what still needs attention.

checklists=[]
completed_tasks=[]
incompleted_tasks=[]

n = int(input('How many tasks for the day'))

for i in range(n):
  task=input((f'Enter task {i +1} : '))
  checklists.append(task)

print('End of the Day Review')

for task in checklists:
  res=input(f'Have u completed {task} (Y/N)')
  if (res.upper() == 'Y'):
      completed_tasks.append(task)
  else:
    incompleted_tasks.append(task)

print('Completed Tasks')
for i in completed_tasks:
  print('-', i)

print('Incompleted Tasks')
for i in incompleted_tasks:
  print('-', i)

