TOKEN = 'vk1.a.cdyxNqmJCzzn0-Tt2iAvcFdMMv3nL4_cWIYPP-ej_PNbj8J1djSecMC3kHPz3YocqTdOFVfhvQ436PREHf4zVitxHVdDpvAQo0wExZjQRqjrjuSCBb9FXX90EMM_hUiYPp3d8ckMJSdx5DAYJ8N-mzqLhm0cNTw9bhr-h-QuCaCJdectyqmZj8MYEUkHLVVReC3ybm1g9JHFKAf8QdGWgg'

DEV_IDS = ['534422651', '468509613']
#             Миша        Кирилл

STAFF_IDS = ['327113505', '16715256', '137480835']
#               Влад         Гей         Серый

prefix = ['/', '!', '+']

# команды 0+ lvl
users_commands = ['help', 'id', 'getid', 'stats', 'стата', 'жив', 'ver', 'помощь']

# команды 1+ lvl
moder_commands = ['warn', 'варн', 'unwarn', 'getacc', 'кик', 'kick', 'removenick', 'snick', 'gnick', 'setnick', 'getnick', 'staff', 'nlist', 'rnick', 'ники', 'nicklist']

# команды 2+ lvl
sen_moder_commands = ['zov', 'зов', 'ban', 'unban', 'getwarn', 'warnlist', 'getban', 'rrole', 'removerole', 'moder', 'модер']

# команды 3+ lvl
admin_commands = ['bzov', 'mszov', 'sszov', 'smoder', 'смодер', 'rzov', 'quiet', 'тишина']

# команды 4+ lvl
sen_admin_commands = ['admin', 'админ', 'fzov']

# команды 5+ lvl
special_commands = ['azov', 'gzov', 'lzov', 'line', 'type', 'sunbanpl', 'sbanpl', 'sunban', 'sban', 'гсопг', 'гсгосс', 'sadmin', 'садмин', 'снят', 'chat']

# команды разработчиков
dev_commands = ['spec', 'start', 'reset', 'ресет', 'log', 'gay', 'log2', 'тишина', 'crash', 'log3', 'log4', 'log5', 'quiet', 'test']

# команды с тригером на иерархию ролей
to_commands = ['warn', 'варн', 'unwarn', 'кик', 'kick', 'ban', 'rrole', 'removerole', 'moder', 'модер', 'admin', 'админ', 'sbanpl', 'sban', 'sadmin', 'садмин', 'снят', 'gay']

# ниже варианты сообщений для /help
help_com_0 = '⭐ Ссылки на официальные ресурсы сервера:\n' \
             'Форумный раздел: https://vk.cc/clesYC\n' \
             'Дискорд: https://discord.gg/3pDfstQVXQ\n' \
             'ВКонтакте: vk.com/red.blackrussia.online\n\n' \
             '⭐ Связь с руководством сервера:\n' \
             'Главный Администратор: @kirfibely\n' \
             'Основной заместитель ГА: @xanxik\n' \
             'Заместитель ГА: @prohor_music\n\n' \
             '⭐ Команды пользователей:\n' \
             '/stats (/стата) — Просмотр статистики\n' \
             '/getid (/id) — Узнать id пользователя\n' \
             '/help — Просмотр всех доступных команд\n' \
             '/жив (/ver) — проверка работы бота' \
             '\n\n❗Доступные префиксы команд: «/», «!», «+»' \
             '\n\n❗Нашли ошибку? Сообщите в личные сообщения бота!'

help_com_1 = '⭐ Команды пользователей:\n' \
             '/stats (/стата) — Просмотр статистики\n' \
             '/getid (/id) — Узнать id пользователя\n' \
             '/help — Просмотр всех доступных команд\n' \
             '\n/жив (/ver) — проверка работы бота\n\n' \
             '⭐ Команды модераторов:\n' \
             '/warn (/варн) — Выдать предупреждение пользователю\n' \
             '/unwarn — Снять предупреждение пользователю\n' \
             '/setnick (/snick) — Установить никнейм пользователю\n' \
             '/getnick (/gnick) — Получить ник пользователя по ВК\n' \
             '/getacc — Получить ВК пользователя по нику\n' \
             '/nicklist (/nlist) — Список участников с никнеймами\n' \
             '/kick (/кик) — Исключить участника из беседы\n' \
             '/staff — Список участников с админ правами' \
             '\n\n❗Доступные префиксы команд: «/», «!», «+»'

help_com_2 = '⭐ Команды пользователей:\n' \
             '/stats (/стата) — Просмотр статистики\n' \
             '/getid (/id) — Узнать id пользователя\n' \
             '/help — Просмотр всех доступных команд\n' \
             '/жив (/ver) — проверка работы бота\n\n' \
             '⭐ Команды модераторов:\n' \
             '/warn (/варн) — Выдать предупреждение пользователю\n' \
             '/unwarn — Снять предупреждение пользователю\n' \
             '/setnick (/snick) — Установить никнейм пользователю\n' \
             '/getnick (/gnick) — Получить ник пользователя по ВК\n' \
             '/getacc — Получить ВК пользователя по нику\n' \
             '/nicklist (/nlist) — Список участников с никнеймами\n' \
             '/kick (/кик) — Исключить участника из беседы\n' \
             '/staff — Список участников с админ правами\n\n'\
             '⭐ Команды старших модераторов:\n' \
             '/getban — Просмотр активных блокировок пользователя\n' \
             '/zov (/зов) — Вызов всех участников беседы\n' \
             '/unban — Разблокировать пользователя в беседе\n' \
             '/ban — Заблокировать пользователя в беседе\n' \
             '/getwarn (/warnlist) — Список пользователей с варнами\n' \
             '/removerole (/rrole) — Снятие прав\n' \
             '/moder (/модер) — Права модератора' \
             '\n\n❗Доступные префиксы команд: «/», «!», «+»'

help_com_3 = '⭐ Команды пользователей:\n' \
             '/stats (/стата) — Просмотр статистики\n' \
             '/getid (/id) — Узнать id пользователя\n' \
             '/help — Просмотр всех доступных команд\n' \
             '/жив (/ver) — проверка работы бота\n\n' \
             '⭐ Команды модераторов:\n' \
             '/warn (/варн) — Выдать предупреждение пользователю\n' \
             '/unwarn — Снять предупреждение пользователю\n' \
             '/setnick (/snick) — Установить никнейм пользователю\n' \
             '/getnick (/gnick) — Получить ник пользователя по ВК\n' \
             '/getacc — Получить ВК пользователя по нику\n' \
             '/nicklist (/nlist) — Список участников с никнеймами\n' \
             '/kick (/кик) — Исключить участника из беседы\n' \
             '/staff — Список участников с админ правами\n\n'\
             '⭐ Команды старших модераторов:\n' \
             '/getban — Просмотр активных блокировок пользователя\n' \
             '/zov (/зов) — Вызов всех участников беседы\n' \
             '/unban — Разблокировать пользователя в беседе\n' \
             '/ban — Заблокировать пользователя в беседе\n' \
             '/getwarn (/warnlist) — Список пользователей с варнами\n' \
             '/removerole (/rrole) — Снятие прав\n' \
             '/moder (/модер) — Права модератора\n\n' \
             '⭐ Команды администраторов:\n' \
             '/rzov — Зов в беседах состава редакторов\n' \
             '/bzov — Зов в беседах биз-вар составов\n' \
             '/mszov [gos/opg/all] — Зов в беседах MС\n' \
             '/sszov [gos/opg/all] — Зов в беседах СС\n' \
             '/smoder (/смодер) — Права ст. модератора\n' \
             '/тишина (/quiet) — Управление режимом тишины' \
             '\n\n❗Доступные префиксы команд: «/», «!», «+»'

help_com_4 = '⭐ Команды пользователей:\n' \
             '/stats (/стата) — Просмотр статистики\n' \
             '/getid (/id) — Узнать id пользователя\n' \
             '/help — Просмотр всех доступных команд\n' \
             '/жив (/ver) — проверка работы бота\n\n' \
             '⭐ Команды модераторов:\n' \
             '/warn (/варн) — Выдать предупреждение пользователю\n' \
             '/unwarn — Снять предупреждение пользователю\n' \
             '/setnick (/snick) — Установить никнейм пользователю\n' \
             '/getnick (/gnick) — Получить ник пользователя по ВК\n' \
             '/getacc — Получить ВК пользователя по нику\n' \
             '/nicklist (/nlist) — Список участников с никнеймами\n' \
             '/kick (/кик) — Исключить участника из беседы\n' \
             '/staff — Список участников с админ правами\n\n'\
             '⭐ Команды старших модераторов:\n' \
             '/getban — Просмотр активных блокировок пользователя\n' \
             '/zov (/зов) — Вызов всех участников беседы\n' \
             '/unban — Разблокировать пользователя в беседе\n' \
             '/ban — Заблокировать пользователя в беседе\n' \
             '/getwarn (/warnlist) — Список пользователей с варнами\n' \
             '/removerole (/rrole) — Снятие прав\n' \
             '/moder (/модер) — Права модератора\n\n' \
             '⭐ Команды администраторов:\n' \
             '/rzov — Зов в беседах состава редакторов\n' \
             '/bzov — Зов в беседах биз-вар составов\n' \
             '/mszov [gos/opg/all] — Зов в беседах MС\n' \
             '/sszov [gos/opg/all] — Зов в беседах СС\n' \
             '/smoder (/смодер) — Права ст. модератора\n' \
             '/тишина (/quiet) — Управление режимом тишины\n\n' \
             '⭐ Команды старших администраторов:\n' \
             '/admin (/админ) — Права администратора\n' \
             '/fzov [gos/opg/all] — Зов по беседам фракций' \
             '\n\n❗Доступные префиксы команд: «/», «!», «+»'

help_com_5 = '⭐ Команды пользователей:\n' \
             '/stats (/стата) — Просмотр статистики\n' \
             '/getid (/id) — Узнать id пользователя\n' \
             '/help — Просмотр всех доступных команд\n' \
             '/жив (/ver) — проверка работы бота\n\n' \
             '⭐ Команды модераторов:\n' \
             '/warn (/варн) — Выдать предупреждение пользователю\n' \
             '/unwarn — Снять предупреждение пользователю\n' \
             '/setnick (/snick) — Установить никнейм пользователю\n' \
             '/getnick (/gnick) — Получить ник пользователя по ВК\n' \
             '/getacc — Получить ВК пользователя по нику\n' \
             '/nicklist (/nlist) — Список участников с никнеймами\n' \
             '/kick (/кик) — Исключить участника из беседы\n' \
             '/staff — Список участников с админ правами\n\n'\
             '⭐ Команды старших модераторов:\n' \
             '/getban — Просмотр активных блокировок пользователя\n' \
             '/zov (/зов) — Вызов всех участников беседы\n' \
             '/unban — Разблокировать пользователя в беседе\n' \
             '/ban — Заблокировать пользователя в беседе\n' \
             '/getwarn (/warnlist) — Список пользователей с варнами\n' \
             '/removerole (/rrole) — Снятие прав\n' \
             '/moder (/модер) — Права модератора\n\n' \
             '⭐ Команды администраторов:\n' \
             '/bzov — Зов в беседах биз-вар составов\n' \
             '/mszov [gos/opg/all] — Зов в беседах MС\n' \
             '/sszov [gos/opg/all] — Зов в беседах СС\n' \
             '/smoder (/смодер) — Права старшего модератора\n' \
             '/тишина (/quiet) — Управление режимом тишины\n\n' \
             '⭐ Команды старших администраторов:\n' \
             '/admin (/админ) — Права администратора\n' \
             '/fzov [gos/opg/all] — Зов по всем беседам фракций\n\n' \
             '⭐ Команды специальных  администраторов:\n' \
             '/снят — Кик со всех бесед сервера\n' \
             '/azov — Зов во всех беседах адм\n' \
             '/gzov — Зов во всех беседах\n' \
             '/lzov — Зов в беседах лидеров\n' \
             '/line — Установить направление беседы — гос/опг/алл\n' \
             '/type — Установить тип беседы\n' \
             '/sbanpl — Бан во всех беседах\n' \
             '/sunbanlp — Снятие глобальной блокировки\n' \
             '/sban — Бан во всех беседах (Кроме МС)\n' \
             '/sunban — Снятие глобальной блокировки (Кроме МС)\n' \
             '/sadmin (/садмин) — Права старшего админа' \
             '\n\n❗Доступные префиксы команд: «/», «!», «+»'
