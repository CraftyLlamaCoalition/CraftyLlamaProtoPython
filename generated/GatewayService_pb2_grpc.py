# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import GatewayService_pb2 as GatewayService__pb2


class TestMessageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TestMessage = channel.unary_unary(
                '/craftyllamagateway.TestMessageService/TestMessage',
                request_serializer=GatewayService__pb2.TestSendMessage.SerializeToString,
                response_deserializer=GatewayService__pb2.TestResponse.FromString,
                )


class TestMessageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TestMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestMessageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TestMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.TestMessage,
                    request_deserializer=GatewayService__pb2.TestSendMessage.FromString,
                    response_serializer=GatewayService__pb2.TestResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'craftyllamagateway.TestMessageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestMessageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TestMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/craftyllamagateway.TestMessageService/TestMessage',
            GatewayService__pb2.TestSendMessage.SerializeToString,
            GatewayService__pb2.TestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
