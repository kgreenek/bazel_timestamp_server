import argparse
import grpc

import timestamp_service_pb2
import timestamp_service_pb2_grpc


def create_arg_parser():
    arg_parser = argparse.ArgumentParser(
            description="Send a Timestamp request to the Timestamp server")
    arg_parser.add_argument("--server", "-a", default="localhost:50051",
                            help="The address of the Timestamp server")
    return arg_parser


def main():
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args()
    print("Connecting to Timestamp server:")
    print(args.server)
    print("")
    channel = grpc.insecure_channel(args.server)
    stub = timestamp_service_pb2_grpc.TimestampServiceStub(channel)
    request = timestamp_service_pb2.TimestampRequest()
    print("Sending Timestamp request:")
    print("{}\n")
    reply = stub.Timestamp(request)
    print("Received reply:")
    print(reply)


if __name__ == "__main__":
    main()
