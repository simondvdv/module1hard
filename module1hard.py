grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)          #Создадим список студентов, чтобы его можно было упорядочить
for index, student in enumerate(students_list): #Данные в ЭЖД(Электронный-журнал-дневник) не всегда имена записаны в правильном регистре
    students_list[index] = student.title()      #В данно цикле мы поправим ошибки если они были допущены на этапе формирования множества
sorted(students_list)                   #Отсортируем список студентов по алфавиту
class_register_avg = {}                 #Объявим словарь, в который добавим, студентов с их средним баллом

for student in students_list:            #Можно было бы в ручную добавить все 5, их не так много. Но хоть мы и не изучали циклы
    marks_avg = sum(grades[students_list.index(student)])/len(grades[students_list.index(student)])        #Для списка оценок и множества ученико
    class_register_avg.update({student: round(marks_avg, 2)})            #Если их количество совпадает, то программа сработает для любого числа учеников
print(class_register_avg)               #Если мы говорим про настоящий ЭЖД, то там округляют до сотых, хоть вывод в задании другой
                                        #Но я представлю, что я настоящий разработчик и отправлю этот пуш/коммит с таким комментарием

