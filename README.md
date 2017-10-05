# Bazel Timestamp Server

This repository is a simple example of using bazel to build a grpc server and client, using Google API's http annotation, and a well-known proto, Timestamp.

## System Requirements

This repository has been tested only on Ubuntu 16.04.

## Install System Dependencies

```bash
# Add the bazel PPA
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -

sudo apt-get update
sudo apt-get install openjdk-8-jdk bazel
```

## Build the code with bazel

```bash
bazel build ...
```

## Run the server

```bash
./bazel-bin/server
```

## Run the client

In a new terminal:

```bash
./bazel-bin/client
```
