import asyncio


class Command:

    """A command, an asynchronous task, imagine an asynchronous action."""

    async def run(self):
        """To be defined in sub-classes."""
        pass

    async def start(self, condition: asyncio.Condition, commands: set["Command"]):
        """
        Start the task, calling run asynchronously.

        This method also keeps track of the running commands.

        """
        commands.add(self)
        await self.run()
        commands.remove(self)

        # At this point, we should ask the condition to update
        # as the number of running commands might have reached 0.
        async with condition:
            condition.notify()


class Look(Command):

    """A subclass of a command, running a dummy task."""

    async def run(self):
        print("Before looking...")
        await asyncio.sleep(5)
        print("After looking")


class Scan(Command):

    """A subclass of a command, running a dummy task."""

    async def run(self):
        print("Before scanning...")
        await asyncio.sleep(5)
        print("After scanning")


async def main():
    """Our main coroutine, starting commands."""
    condition = asyncio.Condition()
    commands = set()
    commands.add(Look())
    commands.add(Scan())
    asyncio.gather(*(cmd.start(condition, commands) for cmd in commands))

    # Wait for the number of commands to reach 0
    async with condition:
        await condition.wait_for(lambda: len(commands) == 0)
        print("There's no running command now, exiting.")


asyncio.run(main())
