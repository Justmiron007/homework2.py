quantity_home_work = 12
quantity_hours = 1.5
course_name = 'Python'
time_per_task = quantity_hours / quantity_home_work
quantity_home_work = str(12)
quantity_hours = str(1.5)
print('Курс:', course_name + ',','всего задач: ' +
      quantity_home_work + ', ' + 'затрачено часов:',
      quantity_hours + ',' + ' среднее время выполнения:',
      time_per_task, 'часа.')