from llm_task_handler.dispatch import TaskDispatcher

from llm_discord_bot.bot import LLMDiscordBot


class TestLLMDiscordBot(LLMDiscordBot):
    def bot_token(self) -> str:
        return 'test_token'

    def task_dispatcher(self) -> TaskDispatcher:
        return TaskDispatcher([])


def test_bot():
    # TODO: Write tests
    TestLLMDiscordBot(command_prefix='$', intents=None)
