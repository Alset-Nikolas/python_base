# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as people_room_1
from room_2 import folks as people_room_2

print('В комнате room_1 живут:', people_room_1[0], 'и', people_room_1[1])
'''print('В комнате room_1 живут:', ', '.join(people_room_1))'''
print('В комнате room_2 живет:', people_room_2[0])

# TODO что если в исходных модулях появятся новые жители? Этот код по-прежнему будет выводить только два-три человека,
#  а остальные останутся неучёными. Чтобы этого избежать используйте возможности функции ''.join(...)
