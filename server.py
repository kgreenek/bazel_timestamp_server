import argparse
import asyncio
from concurrent import futures
import logging

import timestamp_service_pb2


class TimestampServiceServicerImpl(timestamp_service_pb2.TimestampServiceServicer):

    def __init__(self, logger):
        super().__init__()
        self._logger = logger

    def Timestamp(self, request, context):
        logging.getLogger().info("Received Timestamp request")
        reply = timestamp_service_pb2.TimestampReply()
        reply.timestamp.GetCurrentTime()
        return reply


def create_arg_parser():
    """Returns (argparse.ArgumentParser) with expected arguments configured."""
    arg_parser = argparse.ArgumentParser(description="Timestamp Server")
    arg_parser.add_argument("--port", "-p", default=50051, help="Port to run the server on")
    arg_parser.add_argument("--max_workers", "-w", default=4,
                            help="Max number of threads to allow simultanesouly")
    return arg_parser


def main():
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args()
    logger = logging.getLogger()

    timestamp_server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.max_workers))
    timestamp_service = TimestampServiceServicerImpl()
    timestamp_service_pb2.add_TimestampServiceServicer_to_server(timestamp_service,
                                                                 timestamp_server)
    timestamp_server.add_insecure_port('[::]:{}'.format(args.port))

    logger.info("Starting Timestamp server...")
    timestamp_server.start()

    try:
        logger.info("Running...")
        main_event_loop = asyncio.get_event_loop()
        main_event_loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Exiting...")


if __name__ == "__main__":
    main()
