from .materials import *
from .ingot import *
from .pigment import *

class Fabric(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            Wool(): 3
        }, 2)
        RegisterName(self.item_id, "Fabric", "布料")

class BeautifullyColoredFabric(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            Fabric(): 10,
            SmallRootPigment(): 1
        }, 3)
        RegisterName(self.item_id, "Beautifully Colored Fabric", "亮纹布料")

class CloudspunFabric(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            BeautifullyColoredFabric(): 10,
            MysteriousGardenPowder(): 5,
            SmallLeafPigment(): 1
        }, 4)
        RegisterName(self.item_id, "Cloudspun Fabric", "云纹布料")

class BlazingCloudspunFabric(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            CloudspunFabric(): 10,
            AnyaIngot(): 9,
            DragonEssenceStabilizer(): 25,
            FlamingLog(): 6
        }, 5)
        RegisterName(self.item_id, "Blazing Cloudspun Fabric", "灼热的云纹布料")