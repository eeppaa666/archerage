from .materials import *
from .ingot import *
from .lumber import *
from .leather import *
from .fabric import *

class HighPowerEngine(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            ThunderStruckTree(): 2,
            FlamingLog(): 5,
            SunridgeIngot(): 2,
            GoldIngot(): 15,
        }, 5)
        RegisterName(self.item_id, "High Power Engine", "高功率发动机")

class CarpentryWorkbench(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            IronIngot(): 20,
            GoldIngot(): 2,
            Diamond(): 1,
            ArcheumIngot(): 5,
        }, 3)
        RegisterName(self.item_id, "Carpentry Workbench", "组装工具箱")

class MetalWheelFrame(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            YuanJingmu(): 4,
            SturdyIngot(): 1
        }, 3)
        RegisterName(self.item_id, "", "金属轮框x2")

class S200VehicleFrame(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            NuriForestLumber(): 10,
            CloudspunFabric(): 10,
            WindSpiritLeather(): 10,
            GoldIngot(): 10
        }, 3)
        RegisterName(self.item_id, "", "s200车身")

class SportsCarChassis(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            HighPowerEngine(): 2,
            CarpentryWorkbench(): 30,
            FishOil(): 5,
            NaturalRubber(): 50,
            MetalWheelFrame(): 1,
            OceanWarm(): 8,
        }, 3)
        RegisterName(self.item_id, "sports car chassis", "跑车底盘")

class GearPowerMachine(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            ThunderStruckLog(): 15,
            CarpentryWorkbench(): 2,
        }, 3)
        RegisterName(self.item_id, "", "齿轮原动机")