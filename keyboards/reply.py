from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_keyboard(
    *btns: str,
    placeholder: str = None,
    request_contact: int = None,
    request_location: int = None,
    sizes: tuple[int] = (2,),
):
    '''
    Parameters request_contact and request_location must be as indexes of btns args for buttons you need.
    Example:
    get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",
            "Отправить номер телефона",
            placeholder="Что вас интересует?",
            request_contact=4,
            sizes=(2, 2, 1)
        )
    '''
    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(btns, start=0):
        
        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))

        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:
            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
            resize_keyboard=True, input_field_placeholder=placeholder)

# start_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Начать рассылку"),
#             # KeyboardButton(text="О магазине"),
#         ],

#     ],
#     resize_keyboard=True,
# )

# delete_keyboard = ReplyKeyboardRemove()

# # ReplyKeyboardBuilder более гибкий способ настроить инлайны

# start_keyboard2 = ReplyKeyboardBuilder()

# start_keyboard2.add(
#     KeyboardButton(text="Меню"),
#     KeyboardButton(text="О магазине"),
#     KeyboardButton(text="Варианты доставки"),
#     KeyboardButton(text="Варианты оплаты"),
# )


# start_keyboard2.adjust(2,2) # разметка

# start_keyboard3 = ReplyKeyboardBuilder()

# start_keyboard3.attach(start_keyboard2)

# start_keyboard3.row(KeyboardButton(text="Оставить отзыв"),) # добавить новую строку


# test_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType()),
#         ],
#         [
#             KeyboardButton(text="Отправить контакт ☎️", request_contact=True),
#             KeyboardButton(text="Отправить местоположение 🌍", request_location=True),
#         ],

#     ],

# )
