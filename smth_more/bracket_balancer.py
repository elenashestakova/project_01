# Напишите функцию, которая принимает строку круглых скобок
# Если круглая скобка открыта, но не закрыта, то функцию возвращает False.
# Порядок скобок в строке может быть разным!

# Например:
#   "()"              ->  true
#   ")(()))"          ->  false
#   "("               ->  false
#   "(())((()())())"  ->  true
#   ")("              ->  false
#   ""                ->  true

# Ограничения
#   - длина строки <= 100
#   - строка состоит только из символов '(', ')'
#   - строка состоит только из символов '(', ')'
#   - пустая строка возвращает True 
#   - пустая строка возвращает True

def check_brackets(text):
    count = 0
    for i in text:
        if i == '(':
            count += 1
        elif i == ')':
            if count == 0:
                return False
            count -= 1
    return count == 0


s = input('Введите строку круглых скобок: ')
print(check_brackets(s))



# ################################
# Напишите ту же функцию, которая принимала бы и текст со скобками
# Например:
#   string = 'hi(hi)()'     ->  true
#   string = 'hi())('       ->  false
#   string = '((())()())'   ->  true

def check_brackets_text(text):
    result_s = ' '.join([i for i in text if i == '(' or i ==')'])
    return check_brackets(result_s)


s = input('Введите строку круглых скобок с текстом: ')
print(check_brackets_text(s))