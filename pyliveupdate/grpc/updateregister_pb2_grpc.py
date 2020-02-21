# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pyliveupdate.grpc.updateregister_pb2 as updateregister__pb2


class StubRegisterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send_register = channel.unary_unary(
        '/updateregister.StubRegister/send_register',
        request_serializer=updateregister__pb2.SendRegisterRequest.SerializeToString,
        response_deserializer=updateregister__pb2.SendRegisterResponse.FromString,
        )


class StubRegisterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def send_register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StubRegisterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send_register': grpc.unary_unary_rpc_method_handler(
          servicer.send_register,
          request_deserializer=updateregister__pb2.SendRegisterRequest.FromString,
          response_serializer=updateregister__pb2.SendRegisterResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'updateregister.StubRegister', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
