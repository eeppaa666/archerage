from .machine import *
from .lumber import *
from .ingot import *


class SeawhipSpeedboatDesign(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Seawhip Speedboat", "盈月快艇设计图")

class S200LiteDesign(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "s200 lite design", "老爷车设计图")