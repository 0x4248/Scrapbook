from typing import Dict, Optional, List
from .commands import Command

class CommandRegistry:
    def __init__(self):
        self._cmds: Dict[str, Command] = {}

    def register(self, cmd: Command):
        if cmd.name in self._cmds:
            raise ValueError(f"Duplicate command: {cmd.name}")
        self._cmds[cmd.name] = cmd

    def get(self, name: str) -> Optional[Command]:
        return self._cmds.get(name)

    def all(self) -> List[Command]:
        return list(self._cmds.values())

registry = CommandRegistry()
