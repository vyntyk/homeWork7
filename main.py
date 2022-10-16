# 2. Создать телефонный справочник с возможностью
# импорта и экспорта данных в нескольких форматах.

import view
import logger as lg
import adding as add


lg.logging.info('Start')
add.init_data_base('base_phone.csv')
view.ls_menu()