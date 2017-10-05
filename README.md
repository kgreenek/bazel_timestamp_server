# Bazel Protobuf Issue Test

This repository is set up to illustrate an issue with the py_proto_library() rule when depending on
multiple external proto libraries.

## System Requirements

This repository has been tested only on Ubuntu 16.04.

## Install System Dependencies

```bash
# Add the bazel PPA
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -

sudo apt-get update
sudo apt-get install openjdk-8-jdk bazel virtualenv
```

## Setup Virtualenv

```bash
virtualenv -p python3 env
source env/bin/activate
```

## Install Pip3 Dependencies

```bash
pip3 install -r requirements.txt
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

## The Issue

Both the client and server build successfully, but fail to run. The following errors are printed:

```bash
Traceback (most recent call last):
  File "/home/kevin/Projects/bazel_protobuf_issue/bazel-bin/client.runfiles/__main__/client.py", line 3, in <module>
    import timestamp_service_pb2
  File "/home/kevin/Projects/bazel_protobuf_issue/bazel-bin/client.runfiles/__main__/timestamp_service_pb2.py", line 6, in <module>
    from google.protobuf import descriptor as _descriptor
ImportError: No module named 'google.protobuf'
```
