# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    lst_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
                 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    for i in range(1, 13):
        quarter = month // 4 + 1

    quarter_ordinal = ['первого', 'второго', 'третьего', 'четвертого']
    return f'месяц {month} ({lst_month[month - 1]}) является частью {quarter_ordinal[quarter - 1]} квартала'



month_num = int(input("Введите номер месяца: "))
print(quarter_of(month_num))