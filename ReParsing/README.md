# Обработка регулярного выражения

## Постановка задачи

Дано регулярное выражение в обратной польской записи ```alpha``` и буква ```x```. Найти максимальное ```k``` такое, что в ```L``` есть слова, содержащие подслово ```x^k```.

В случае, если регулярное выражение задано неккоректно, вывести сообщение об ошибке.

## Решение

Решение находится в файле main.py, реализовано на python 3.5.

### def main()

В def main() считываем регулярное выражение ```alpha``` и букву ```x```. Далее в цикле идём по символам регулярного выражения и вызываем соответствующие функции:
<ul>
	<li><b>def equal_x(...)</b> - если символ совпадает с буквой ```x```; </li>
	<li><b>def just_letter(...)</b> - если символ является буквой, но не совпадает с ```x```;</li>
	<li><b>def empty_word(...)</b> - если символ является пустым словом;</li> 
	<li><b>def star(...)</b> - если символ - звезда Клини;</li>	
	<li><b>def plus(...)</b> - если символ является операцией ```или```;</li> 
	<li><b>def concat(...)</b> - если символ является операцией конкатенации;</li> 
	<li><b>def star(...)</b> - если символ - звезда Клини.</li> 
</ul>

В каждую из функций передается словарь со следующими списками:
<ul>
	<li><b>count_x = []</b> - max k : x^k является подстрокой слов, задаваемых регуляркой;</li> 
    	<li><b>pref_x = []</b> - max k: x^k является префиксом слов, задаваемых регуляркой;</li> 
    	<li><b>suff_x = []</b> - max k: x^k является суффиксом слов, задаваемых регуляркой;</li> 
    	<li><b>only_x = []</b> - true - если слово, задаваемое регуляркой, может состоять только из букв x;</li>
	<li><b>max_len = []</b> - min k: слово, задаваемое регуляркой, имеет длину k;</li>
    	<li><b>min_len = []</b> - max k: слово, задаваемое регуляркой, имеет длину k.</li> 
</ul>

Сообщение об ошибке выводим, если на каком-то из шагов на стеке не оказалось нужного числа элементов или если мы встретили символ не из алфавита ```{a, b, c, ., *, +, 1}```

### def equal_x(d)

Если встретили символ, совпадающий с буквой ```x```, то кладем на стек count_x ```1```, на pref_x - ```1```, на suff_x - ```1```, на only_x - ```True```. Максимальные и минимальные длины слов - по 1.

### def just_letter(d)

Если встретили букву, отличную от ```x```, то кладем на стек count_x ```0```, на pref_x - ```0```, на suff_x - ```0```, на only_x - ```False```. Максимальные и минимальные длины слов - по 1.

### def empty_word(d)

Если встретили пустое слово, то кладем на стек count_x ```0```, на pref_x - ```0```, на suff_x - ```0```, на only_x - ```False```. Максимальные и минимальные длины слов - по 0.

### def plus(d)

Если встретили ```или```, то снимаем со всех стеков последние два элемента, т.е. значения для двух предыдущих регуляро, а затем кладем на стеки максимальные значения из двух предыдущих регулярок (```True > False```). 

### def concat(d)

Если встретили ```конкатенацию```, то в качестве нового pref_x берем ```значение pref_x для первой строки```, в качестве нового suff_x берем ```значение suff_x для второй строки```, в качестве only_x берем ```true``` если обе строки могли состоять только из x, иначе - ```false```. В качестве нового count_x берем максимум из: ```count_x первой строки```, ```count_x второй строки```, ```суффикс первой + префикс второй``` (когда новое x^k могло появится после конкатенации).
Отдельно обрабатываем случаи, когда одно из слов конкатенации могло состоять только из букв x или из пустого слова.

### def star(d)

Если встретили ```звезду Клини```, то в качестве нового pref_x и suff_x оставляем такими же, а также проверяем, что если регулярка могла состоять только из букв ```x```, то ответом будет ```INF```, иначе делаем то же, что и при конкатенации.

## Тестирование

Тестирование осуществляем в testing.py. Отдельное внимание уделяем случаям с разными ответами: INF, Error, число.

## Работу выполнил

Мутолапов Артур, 798 группа, 2 курс ФИВТ.
