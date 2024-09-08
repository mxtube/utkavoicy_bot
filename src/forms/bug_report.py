from aiogram.fsm.state import StatesGroup, State


class BugReportForm(StatesGroup):
    """ Class for bug reports """
    description = State()
