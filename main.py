import asyncio
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

async def main():
    await notifier.send(title="Hello World!", message="send from python")


asyncio.run(main())