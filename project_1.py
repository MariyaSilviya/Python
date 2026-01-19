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

