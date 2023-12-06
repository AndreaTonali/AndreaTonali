# ConveyorBelt

There is a factory production line around a single a conveyor belt.

Components (of type A and B) come onto the start of the belt at random intervals; workers must take one component of each type from the belt as they come past, and combine them to make a finished product.

The belt is divided into fixed-size slots; each slot can hold only one component or one finished product. There are a number of worker stations on either side of the belt, spaced to match the size of the slots on the belt, like this (fixed-width font ASCII pic):

```bash
       v   v   v   v   v      workers
  ---------------------
  -> | A |   | B | A | P | -> conveyor belt
  ---------------------
       ^   ^   ^   ^   ^      workers
```

In each unit of time, the belt moves forwards one position, and there is time for a worker on one side of each slot to EITHER take an item from the slot or replace an item onto the belt. The worker opposite them can't touch the same belt slot while they do this.(So you can't have one worker picking something from a slot while their counterpart puts something down in the same place).

Once a worker has collected one of both types of component, they can begin assembling the finished product. This takes an amount of time, so they will only be ready to place the assembled product back on the belt on the fourth subsequent slot. While they are assembling the product, they can't touch the conveyor belt. Workers can only hold two items (component or product) at a time: one in each hand.

## Task

Create a simulation of this, with three pairs of workers. At each time interval, the slot at the start of the conveyor belt should have an equal (1/3) chance of containing nothing, a component A or a component B.

Run the simulation for 100 steps, and compute how many finished products come off the production line, and how many components of each type go through the production line without being picked up by any workers.

A few pointers:
- The code does not have to be 'production quality', but we will be looking for evidence that it's written to be somewhat flexible, and that a third party would be able to read and maintain it.
- Be sure to state (or comment) your assumptions.
- During the interview, we may ask about the effect of changing certain aspects of the simulation. (E.g. the length of the conveyor belt.)
- Flexibility in the solution is preferred, but we are also looking for a sensible decision on where this adds too much complexity. (Where would it be better to rewrite the code for a different scenario, rather than spending much more than the allotted time creating an overly complicated, but very flexible simulation engine?)

## How to run

**Note**: Assuming **Linux/MacOS** environment plus **Docker**

```shell
# make the file executable
chmod 755 init.sh

# execute
➜  app_ConveyorBelt ./init.sh
```
The above command will first build a docker image (if not alerady built) and execute the conveyor belt simulation, passing three default parameters, `conveyor belt length` = 10, number of `worker pairs` = 3 and number of simulation to be performd `num_steps` = 10. These parameters can also be dynamically passed to the `init.sh` (please see below).

```bash
# app_ConveyorBelt/init.sh

1  # Fail if any of the procesess are not returning an exit code = 0
2  set -e
3
4  # set variables
5  export IMAGE_NAME=conveyorbelt
6  export WORKER_PAIRS=3
7  export CONVEYOR_BELT_LENGTH=10
8  export NUM_STEPS=100
...

```
Alternatively, if the user environment has a Python3 interpreter up and running the user can run the simulation as per the below command.

```bash
# run with default parameters
python -m ConveyorBelt.run_simulation

# changing the parameters
python -m ConveyorBelt.run_simulation --worker-pairs 30 --conveyor-belt-length 100 --num-steps 1000
```
Please see flags description below
```bash
python -m ConveyorBelt.run_simulation -h                                                                                              
usage: run_simulation.py [-h] [-c 10] [-w 3] [-n 100]

Run the simulation of the conveyor belt production line.

Parameters:
- conveyor_belt_length (int): The length of the conveyor belt.
- worker_pairs (int): The number of worker pairs.
- num_steps (int): The number of simulation steps.

options:
  -h, --help            show this help message and exit
  -c 10, --conveyor-belt-length 10
                        The length of the conveyor belt
  -w 3, --worker-pairs 3
                        The number of worker pairs
  -n 100, --num-steps 100
                        The number of simulation steps
```
Sample results command line execution
```bash
unittest
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-7.4.3, pluggy-1.3.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /tests
collecting ... collected 7 items

tests/test_conveyor_belt.py::test_conveyor_belt_creation PASSED          [ 14%]
tests/test_conveyor_belt.py::test_generate_random_component PASSED       [ 28%]
tests/test_conveyor_belt.py::test_worker_creation PASSED                 [ 42%]
tests/test_conveyor_belt.py::test_take_from_belt PASSED                  [ 57%]
tests/test_conveyor_belt.py::test_assemble_product PASSED                [ 71%]
tests/test_conveyor_belt.py::test_incomplete_assemble_product PASSED     [ 85%]
tests/test_conveyor_belt.py::test_main_simulation PASSED                 [100%]

============================== 7 passed in 0.04s ===============================
start ConveyorBelt
2023-12-05 14:25:53 - SIMULATION RESULTS
2023-12-05 14:25:53 - Finished products: 12
2023-12-05 14:25:53 - Unused components A: 5
2023-12-05 14:25:53 - Unused components B: 18
```

## Considerations
- The simulation assumes that workers always pick components from the belt if available and try to assemble a product when they have both components.
- The assembling time is not explicitly modeled in the simulation; it's assumed that assembling happens instantly after both components are collected.
- The code does not handle edge cases or errors for brevity. In a production scenario, you'd want to handle exceptions, edge cases, and add more robust error checking.
- The code is relatively simple and focuses on readability. Depending on specific requirements and flexibility needs, more features and complexity could be added.