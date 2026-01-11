from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Any, Literal

Mode = Literal["cli", "ui", "both"]

@dataclass
class Command:
    name: str
    handler: Callable[..., Any]
    summary: str = ""
    mode: Mode = "cli"
    form_fields: List[Dict[str, Any]] = field(default_factory=list)

    def supports_cli(self) -> bool:
        return self.mode in ("cli", "both")

    def supports_ui(self) -> bool:
        return self.mode in ("ui", "both")
