from typing import Dict, Optional, List

# Manual funcions
# Commands can create manual pages by doing manual.register(NAME, TEXT, ALIASES (List, optional))

class ManualPage:
    def __init__(self, name: str, text: str, aliases: Optional[List[str]] = None):
        self.name = name
        self.text = text
        self.aliases = aliases if aliases is not None else []
class ManualRegistry:
    def __init__(self):
        self._manuals: Dict[str, ManualPage] = {}

    def register(self, name: str, text: str, aliases: Optional[List[str]] = None):
        if name in self._manuals:
            raise ValueError(f"Duplicate manual page: {name}")
        manual_page = ManualPage(name, text, aliases)
        self._manuals[name] = manual_page
        if aliases:
            for alias in aliases:
                if alias in self._manuals:
                    raise ValueError(f"Duplicate manual page alias: {alias}")
                self._manuals[alias] = manual_page

    def get(self, name: str) -> Optional[ManualPage]:
        return self._manuals.get(name)

    def all(self) -> List[ManualPage]:
        # Return only unique manual pages (avoid duplicates from aliases)
        unique_manuals = {mp.name: mp for mp in self._manuals.values()}
        return list(unique_manuals.values())
    
manual_registry = ManualRegistry()
