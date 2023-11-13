#!/bin/bash

docker build -f Dockerfile_light -t doodad-test:latest .
docker tag doodad-test:latest $USER/doodad-test:latest
docker push $USER/doodad-test:latest

