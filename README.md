### Hexlet tests and linter status:

[![Actions Status](https://github.com/rbgmlv/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/rbgmlv/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/2083bea65e0ffaee82c2/maintainability)](https://codeclimate.com/github/rbgmlv/python-project-49/maintainability)

### Описание

Проект реализует текстовую математическую игру. Игра задает пользователю вопрос, а пользователь отвечает. Если пользователь отвечает правильно три раза подряд, то он выиграл и получает поздравления. В противном случае игра предлагает пользователю сыграть еще раз. Пользователю в игре предстоит:
- Определять четные и нечетные числа
- Рассчитывать математические выражения
- Искать наибольший общий делитель
- Заполнять недостающие элементы арифметической прогрессии
- Определять простые числа

### Минимальные требования

Для работы пакета должны быть установлены:
- Python версии не ниже 3.13
- утилита `uv`

### Установка

Необходимо клонировать репозиторий игры и перейти в корневой каталог репозитория. Из корневого каталога выполнить команду:

```
make build
```

После этого установить собранный пакет игры в систему командой:

```
make package-install
```

### Использование

Откройте терминал и наберите одну из следующих команд:

```
brain-games
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

### Примеры игр

**brain-even**

[![asciicast](https://asciinema.org/a/VEMs1LkmY6q4dLEYS3pD13xxA.svg)](https://asciinema.org/a/VEMs1LkmY6q4dLEYS3pD13xxA)

**brain-calc**

[![asciicast](https://asciinema.org/a/oJGHloqNAAHmrzQv1mnLN67ss.svg)](https://asciinema.org/a/oJGHloqNAAHmrzQv1mnLN67ss)

**brain-gcd**

[![asciicast](https://asciinema.org/a/ShT7pOvq1QDAKYBOKGsVK3OlA.svg)](https://asciinema.org/a/ShT7pOvq1QDAKYBOKGsVK3OlA)

**brain-progression**

[![asciicast](https://asciinema.org/a/oChpVyUhkBjumONy6EDJujsIN.svg)](https://asciinema.org/a/oChpVyUhkBjumONy6EDJujsIN)

**brain-prime**

[![asciicast](https://asciinema.org/a/cODLKFWTbMr68SxGUTOKlbjAV.svg)](https://asciinema.org/a/cODLKFWTbMr68SxGUTOKlbjAV)
