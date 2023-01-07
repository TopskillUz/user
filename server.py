import random
from concurrent import futures
from google.protobuf.wrappers_pb2 import BoolValue
import grpc

from grpc_generated_files import auth_pb2_grpc, auth_pb2


class AuthServicer(auth_pb2_grpc.AuthServiceServicer):
    def check_username(self, request, context):
        print("UsersServicer received request from AuthClient")
        if request.username == 'test':
            is_exists = True
        else:
            is_exists = False
        return BoolValue(value=is_exists)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthServicer(), server)
    print('Starting server. Listening on port 9998.')
    server.add_insecure_port("[::]:9998")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
