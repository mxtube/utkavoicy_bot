from loguru import logger

from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from models.bug_report import BugReport
from forms import BugReportForm

from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

command_router = Router(name='Bot commands')


@command_router.message(CommandStart())
async def start(message: types.Message, session: AsyncSession):
    logger.info(f'User {message.from_user.username} send command {message.text}')
    answer_message = f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nПолучается это бот 🦆'
    await User.create_or_update(session, message.from_user.__dict__)
    await message.answer(answer_message)
    logger.info(f'Bot send to user message: {answer_message}')


@command_router.message(Command('help'))
async def help_cmd(message: types.Message):
    logger.info(f'User {message.from_user.username} send command {message.text}')
    answer_message = ('▶️ Для использования бота, необходимо упомянуть его @ в нужной беседе и выбрать необходимое '
                      'сообщение.\n'
                      '🛠️ Для того чтобы сообщить об ошибке вызовите в приватном чате команду /bug')
    await message.answer(answer_message)
    logger.info(f'Bot send to user message: {answer_message}')


@command_router.message(Command('bug'))
async def report_cmd(message: types.Message, state: FSMContext, session: AsyncSession) -> None:
    logger.info(f'User {message.from_user.username} send command {message.text}. Open bug form')
    user = await User.is_user_exists(session, message.from_user.id)
    if message.chat.type == 'private' and user:
        await state.set_state(BugReportForm.description)
        await message.answer('Опиши подробно проблему с которой ты столкнулся(-ась) и я отправлю ее разработчикам')


@command_router.message(BugReportForm.description)
async def process_description(message: types.Message, state: FSMContext, session: AsyncSession) -> None:
    await state.update_data(description=message.text)
    logger.info(f'User {message.from_user.username} send notification about bug: {message.text}')
    await BugReport.create(session, message.from_user.id, message.text)
    await state.clear()
    await message.answer('Я зарегистрировал твоё обращение и наша команда уже работает над ее решением.')
    logger.info('Close bug form')
