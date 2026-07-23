from .materials import *
from .ingot import *
from .fabric import *
from .leather import *
from .lumber import *

class LightFramework(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            Bamboo() : 20
        }, 2)
        RegisterName(self.item_id, "LightFramework", "超轻骨架")

class SteeringDevice(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            IronIngot(): 5,
            BeautifullyColoredFabric(): 1,
            FineLeather(): 1
        }, 3)
        RegisterName(self.item_id, "SteeringDevice", "转向仪")

class JetDevice(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            SturdyIngot(): 5,
            FlamingLog(): 5
        }, 4)
        RegisterName(self.item_id, "JetDevice", "喷气装置")

class SummerWindGliderDesign(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "SummerWindGliderDesign", "夏日清风滑翔翼设计图")

class SummerWindGlider(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            Lumber(): 15,
            IronIngot(): 15,
            Fabric(): 15,
            Leather(): 15,
            SummerWindGliderDesign(): 1
        }, 3)
        RegisterName(self.item_id, "SummerWindGlider", "夏日清风滑翔翼")

class HeighGliderFramework(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            LightFramework(): 1,
            SteeringDevice(): 1,
            JetDevice(): 1,
            FloatingStones(): 100,
            SummerWindGlider(): 1
        }, 5)
        RegisterName(self.item_id, "Heigh Glider Framework", "高级滑翔翼主体")