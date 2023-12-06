import random
import logging
from typing import Optional, List
import plac


class ConveyorBelt:
    def __init__(self, length: int):
        """
        Initialize a ConveyorBelt object.

        Parameters:
        - length (int): The length of the conveyor belt.
        """
        self.length = length
        self.slots = [None] * length

    def generate_random_component(self) -> Optional[str]:
        """
        Generate a random component (A, B, or None) with equal probability.

        Returns:
        - Optional[str]: The randomly generated component.
        """
        rand_num = random.random()
        if rand_num < 1 / 3:
            return "A"
        elif rand_num < 2 / 3:
            return "B"
        else:
            return None


class Worker:
    def __init__(self, slot: int):
        """
        Initialize a Worker object.

        Parameter:
        - slot (int): The slot index associated with the worker on the conveyor belt.
        """
        self.slot = slot
        self.held_components: List[str] = []
        self.assembling_time = 4
        self.assembling_steps = 0

    def take_from_belt(self, belt: ConveyorBelt) -> None:
        """
        Take a component from the conveyor belt.

        Parameters:
        - belt (ConveyorBelt): The conveyor belt from which the worker takes a component.
        """
        item = belt.slots[self.slot]
        if item:
            self.held_components.append(item)
            belt.slots[self.slot] = None

    def assemble_product(self) -> bool:
        """
        Assemble a product if the worker has the required components.

        Returns:
        - bool: True if a product is successfully assembled, False otherwise.
        """
        if len(self.held_components) >= 2:
            product = "".join(self.held_components[:2])
            if product in {"AB", "BA"}:
                self.held_components = []
                return True
        return False


@plac.opt("conveyor_belt_length", help="The length of the conveyor belt", type=int)
@plac.opt("worker_pairs", help="The number of worker pairs", type=int)
@plac.opt("num_steps", help="The number of simulation steps", type=int)
def main(
    conveyor_belt_length: int = 10, worker_pairs: int = 3, num_steps: int = 100
) -> None:
    """
    Run the simulation of the conveyor belt production line.

    Parameters:
    - conveyor_belt_length (int): The length of the conveyor belt.
    - worker_pairs (int): The number of worker pairs.
    - num_steps (int): The number of simulation steps.
    """
    conveyor_belt = ConveyorBelt(conveyor_belt_length)
    workers = [Worker(i % (conveyor_belt_length // 2)) for i in range(worker_pairs * 2)]

    finished_products = 0
    unused_components_a = 0
    unused_components_b = 0

    for step in range(num_steps):
        conveyor_belt.slots[0] = conveyor_belt.generate_random_component()  # type: ignore

        for worker in workers:
            worker.take_from_belt(conveyor_belt)

        # Workers attempt to assemble products
        for worker in workers:
            if worker.assemble_product():
                finished_products += 1

        # Workers put components back on the belt after assembling time
        for worker in workers:
            worker.assembling_steps += 1
            if worker.assembling_steps == worker.assembling_time:
                if worker.held_components:
                    # Put the first held component back on the belt
                    conveyor_belt.slots[worker.slot] = worker.held_components.pop(0)  # type: ignore
                worker.assembling_steps = 0

        # Count unused components in all slots
        for slot in conveyor_belt.slots:
            if slot == "A":
                unused_components_a += 1
            elif slot == "B":
                unused_components_b += 1

    # Log simulation results
    logging.info("SIMULATION RESULTS")
    logging.info(f"Finished products: {finished_products}")
    logging.info(f"Unused components A: {unused_components_a}")
    logging.info(f"Unused components B: {unused_components_b}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Run the simulation with 3 pairs of workers, 10 conveyor belt slots, and 100 steps
    plac.call(main)
