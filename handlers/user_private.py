from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import orm_get_products
from filters.chat_types import ChatTypeFilter
from keyboards.reply import get_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет, я виртуальный помощник",
        reply_markup=get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",
            placeholder="Что вас интересует?",
            sizes=(2,2)
        ),
    )


@user_private_router.message((F.text.lower() == "о магазине"))
@user_private_router.message(Command("about"))
async def command(message: types.Message):
    await message.answer("Мы пиццерия Bylba4kaPizza, ознакомься с ассортиментом в нашем боте и сделай заказ!")


@user_private_router.message((F.text.lower().contains("оплат")) | (F.text.lower() == "варианты оплаты"))
@user_private_router.message(Command("payment"))
async def command(message: types.Message):
    text = as_marked_section(
        Bold("Варианты оплаты:"),
        "При получении карта/наличные",
        "В заведении",
        marker="✅ "
    )

    await message.answer(text.as_html())


@user_private_router.message((F.text.lower().contains("доставк")) | (F.text.lower() == "варианты доставки"))
@user_private_router.message(Command("shipping"))
async def command(message: types.Message):
    text = as_list(
            as_marked_section(
                Bold("Варианты доставки:"),
                "Курьер",
                "Самовывоз",
                "В заведении",
                marker="✅ "
            ),
            as_marked_section(
                Bold("Нельзя:"),
                "Почта",
                "Голуби",
                marker="❌ "
            ),
            sep='\n-------------------\n'
        )
    await message.answer(text.as_html())


@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def command(message: types.Message, session:AsyncSession):
    data = await orm_get_products(session)
    if data:
        for product in data:
            await message.answer_photo(
                product.image,
                caption=f"<strong>{product.name}\
                </strong>\n{product.description}\nСтоимость: {round(product.price, 2)}",
            )
    else:
        await message.answer("Товара в наличии нет")

# Словить контакт
@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer('Номер получен')
    await message.answer(str(message.contact))


# Словить Локацию
@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer('Локация получена')
    await message.answer(str(message.location))

