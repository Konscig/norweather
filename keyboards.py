from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(row_width=8)
btn_1= InlineKeyboardButton(text="Погода сейчас",callback_data ="k1")
btn_2= InlineKeyboardButton(text="Статус подписки",callback_data ="k2")
main_menu.add(btn_1)
main_menu.add(btn_2)

exitor_menu = InlineKeyboardMarkup(row_width=5)
btn_exit = InlineKeyboardButton(text="Назад", callback_data ="k3")
exitor_menu.add(btn_exit)


