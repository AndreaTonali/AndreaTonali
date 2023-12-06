# Fail if any of the procesess are not returning an exit code = 0
set -e

# set variables
export IMAGE_NAME=conveyorbelt
export WORKER_PAIRS=3
export CONVEYOR_BELT_LENGTH=10
export NUM_STEPS=100

# check if the docker image is already built
if [[ "$(docker images -q conveyorbelt:latest 2> /dev/null)" == "" ]]; then

    echo build docker image
    docker build -t $IMAGE_NAME -f ConveyorBelt.Dockerfile .

    echo unittest
    docker run $IMAGE_NAME python -m pytest -v ./tests

    echo start ConveyorBelt
    docker run $IMAGE_NAME python -m ConveyorBelt.run_simulation --worker-pairs $WORKER_PAIRS --conveyor-belt-length $CONVEYOR_BELT_LENGTH --num-steps $NUM_STEPS

else
    
    echo unittest
    docker run $IMAGE_NAME python -m pytest -v ./tests

    echo start ConveyorBelt
    docker run $IMAGE_NAME python -m ConveyorBelt.run_simulation --worker-pairs $WORKER_PAIRS --conveyor-belt-length $CONVEYOR_BELT_LENGTH --num-steps $NUM_STEPS

fi
