import pytest
from ConveyorBelt.run_simulation import ConveyorBelt, Worker


@pytest.fixture
def conveyor_belt():
    return ConveyorBelt(length=10)

@pytest.fixture
def worker():
    return Worker(slot=0)
