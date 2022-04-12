Section 1

1. Switch current directory to folder /Part1
cd ./part1
2. Run the build.sh file to create docker image with trained model inside
bash build.sh
3. Run the run.sh file to create a container with the image
bash run.sh
4. Run the infer.sh file which will pick a random image from images directory and call classify.py in Docker container to classify the image
bash infer.sh

Section 2

1. We created a shared directory images so that image is accessible to the container to classify. We could randomly chose and image and uploaded it to the container using docker cp command.

2. TO make the application accessible to users even if they do not have python or tensorflow installed on their machine.