from .machine import *
from .lumber import *
from .ingot import *
from .design import *

class ScrollSeawhipSpeedboat(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            SeawhipSpeedboatDesign(): 1,
            CarpentryWorkbench(): 10,
            HighPowerEngine(): 2,
            SturdyIngot(): 10,
            FineLumber(): 20
        }, 6)
        RegisterName(self.item_id, "Scroll: Seawhip Speedboat", "卷轴：盈月快艇")

class ScrollS200Lite(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            S200LiteDesign(): 1,
            SportsCarChassis(): 1,
            S200VehicleFrame(): 1,
        }, 6)
        RegisterName(self.item_id, "Scroll: S200 lite", "卷轴：老爷车")

class ScrollWoodenSkateboard(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            FineLumber(): 20,
            SturdyIngot(): 30,
            CopperIngot(): 100,
        }, 6)
        RegisterName(self.item_id, "", "卷轴：木质滑板")

class ScrollToothedEdgeSkateboard(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            ScrollWoodenSkateboard(): 1,
            GearPowerMachine(): 1,
        }, 6)
        RegisterName(self.item_id, "", "卷轴：锯齿滑板")

