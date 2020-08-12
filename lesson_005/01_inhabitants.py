# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as people_room_1
from room_2 import folks as people_room_2

print('В комнате room_1 живут:', people_room_1[0], 'и', people_room_1[1])
print('В комнате room_2 живет:', people_room_2[0])
