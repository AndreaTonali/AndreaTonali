import logging
from ConveyorBelt.run_simulation import Worker, main


def test_conveyor_belt_creation(conveyor_belt):
    assert len(conveyor_belt.slots) == 10


def test_generate_random_component(conveyor_belt):
    for _ in range(100):
        component = conveyor_belt.generate_random_component()
        assert component in {"A", "B", None}, f"Unexpected component: {component}"


def test_worker_creation(worker):
    assert worker.slot == 0
    assert worker.held_components == []
    assert worker.assembling_time == 4
    assert worker.assembling_steps == 0


def test_take_from_belt(worker, conveyor_belt):
    conveyor_belt.slots[0] = "A"
    worker.take_from_belt(conveyor_belt)
    assert worker.held_components == ["A"]
    assert conveyor_belt.slots[0] is None


def test_assemble_product(worker):
    worker.held_components = ["A", "B"]
    assert worker.assemble_product() is True
    assert worker.held_components == []


def test_incomplete_assemble_product(worker):
    worker.held_components = ["A"]
    assert worker.assemble_product() is False
    assert worker.held_components == ["A"]


def test_main_simulation(caplog, conveyor_belt):
    workers = [Worker(i % (conveyor_belt.length // 2)) for i in range(6)]

    with caplog.at_level(logging.INFO):
        main(
            conveyor_belt_length=conveyor_belt.length,
            worker_pairs=len(workers) // 2,
            num_steps=100,
        )

    assert "SIMULATION RESULTS" in caplog.text
    assert "Finished products:" in caplog.text
    assert "Unused components A:" in caplog.text
    assert "Unused components B:" in caplog.text
