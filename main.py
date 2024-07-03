import botpy
from botpy import BotAPI
from botpy.ext.command_util import Commands
from botpy.manage import GroupManageEvent
from botpy.message import Message, DirectMessage, GroupMessage, BaseMessage
import os

_log = botpy.logging.get_logger()


@Commands("查电费")
async def query_electricity_balance(api: BotAPI, message: GroupMessage, params=None):
    _log.info(params)
    # 第一种用reply发送消息
    await message.reply(content="电费为 0 元")
    return True


handlers = [
    query_electricity_balance,
]


class MimirClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot[{self.robot.name}] is ready.")

    async def on_group_at_message_create(self, message: GroupMessage):
        for handler in handlers:
            if await handler(api=self.api, message=message):
                return
        await message.reply(content=message.content)

    async def on_group_add_robot(self, message: GroupManageEvent):
        await self.api.post_group_message(group_openid=message.group_openid, content="我进群了，哥")

    async def on_group_del_robot(self, event: GroupManageEvent):
        _log.info(f"robot[{self.robot.name}] left group ${event.group_openid}")


intents = botpy.Intents(
    public_messages=True,
    # public_guild_messages=True,
    # direct_message=True,
)
client = MimirClient(intents=intents, is_sandbox=True, log_level=10, timeout=30)
appid = os.getenv("QQBOT_APP_ID")
secret = os.getenv("QQBOT_APP_SECRET")
client.run(appid=appid, secret=secret)
