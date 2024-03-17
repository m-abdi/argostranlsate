from concurrent import futures
from os import getenv
from dotenv import load_dotenv

from .argostranslate_pb2_grpc import (
    add_ArgosTranslateServicer_to_server,
    ArgosTranslateServicer,
    grpc,
)


load_dotenv()  # take environment variables from .env.


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ArgosTranslateServicer_to_server(ArgosTranslateServicer(), server)
    server.add_insecure_port(f"[::]:{getenv('PORT', '50051')}")
    server.start()
    print("GRPC Server Started. PORT: 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
