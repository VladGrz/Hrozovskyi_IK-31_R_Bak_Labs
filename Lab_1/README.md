# Лабораторна робота №1

---

## Необхідні ресурси:
- Встановлений компілятор для Python;
- Встановлене середовище virtualenv.

### Хід роботи:  
- Знайшов пакет `num2word`, який може перетворити числа в слова;
- Додав файл `requirements.txt` та записав одразу в нього назву пакету `num2word`;
- Створив власний пакет `greeting` для програми та в ньому створив пакет з логікою `greet_and_convert`, який містить два модулі: один - запитання та привітання до користувача, інший - перетворення числа в слова;
- Додав документацію, яка відповідає стандартним правилам `pydocstyle`;
- Налаштував виконання за допомогою `python -m ...``;

### Структура проекту:
```text
.                           <- the root project directory
├── greeting                <- a package
│   ├── __init__.py         <- special module, says "greeting" is the package
│   ├── __main__.py         <- a default execution
│   └── greet_and_convert   <- an inner package
│       ├── __init__.py     <- special module, says "greet_and_convert" is the inner package for "greeting"
│       ├── converter.py    <- a module of "greet_and_convert"
│       └── phrases.py      <- a module of "greet_and_convert"
├── README.md               <- a description
└── requirements.txt        <- used packages
```

### Налаштування середовища:
```commandline
python -m venv tutor
tutor\scripts\activate.bat
python -m pip list
python -m pip install -r requirements.txt
```

### Перевірка чи відповідає проект стандартним правилам `pydocstyle`:
```
(tutor) D:\Навчання_3_курс_2_семестр\Технології програмування інформаційних систем частина 2\Lab_1>python -m pydocstyle greeting

(tutor) D:\Навчання_3_курс_2_семестр\Технології програмування інформаційних систем частина 2\Lab_1>
```

### Перевірка запуску програми:
```commandline
(tutor) D:\Навчання_3_курс_2_семестр\Технології програмування інформаційних систем частина 2\Lab_1>python -m greeting
Tape your name: Vlad
Hello, Vlad
Which number you want to convert into text: 19
Nineteen
```

### Перевірка невірно введеного числа:
```commandline
(tutor) D:\Навчання_3_курс_2_семестр\Технології програмування інформаційних систем частина 2\Lab_1>python -m greeting
Tape your name: vlad
Hello, vlad
Which number you want to convert into text: ds
Make sure that, the number you passed doesn't contain any alphabet or special symbol!
```

