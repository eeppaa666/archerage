from .materials import *
from .oil import *
from .ingot import *

class CopperKeyx5(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            CopperIngot(): 10,
        }, 6)
        RegisterName(self.item_id, "", "铜钥匙x5")


class SliverKeyx5(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            CopperKeyx5(): 1,
            CopperIngot(): 3,
            SliverIngot(): 5,
        }, 6)
        RegisterName(self.item_id, "", "银钥匙x5")


class GoldKeyx5(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            SliverKeyx5(): 1,
            CopperIngot(): 5,
            SliverIngot():3,
            GoldIngot(): 15,
        }, 6)
        RegisterName(self.item_id, "", "金钥匙x5")
