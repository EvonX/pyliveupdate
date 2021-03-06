# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: updateregister.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='updateregister.proto',
  package='updateregister',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14updateregister.proto\x12\x0eupdateregister\"+\n\x0fRegisterRequest\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"B\n\x10RegisterResponse\x12.\n\nreturncode\x18\x01 \x01(\x0e\x32\x1a.updateregister.ReturnCode*&\n\nReturnCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x32_\n\x0cStubRegister\x12O\n\x08register\x12\x1f.updateregister.RegisterRequest\x1a .updateregister.RegisterResponse\"\x00\x62\x06proto3')
)

_RETURNCODE = _descriptor.EnumDescriptor(
  name='ReturnCode',
  full_name='updateregister.ReturnCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=191,
)
_sym_db.RegisterEnumDescriptor(_RETURNCODE)

ReturnCode = enum_type_wrapper.EnumTypeWrapper(_RETURNCODE)
SUCCESS = 0
FAILURE = 1



_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='updateregister.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='updateregister.RegisterRequest.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='updateregister.RegisterRequest.port', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=83,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
  name='RegisterResponse',
  full_name='updateregister.RegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='returncode', full_name='updateregister.RegisterResponse.returncode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=151,
)

_REGISTERRESPONSE.fields_by_name['returncode'].enum_type = _RETURNCODE
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterResponse'] = _REGISTERRESPONSE
DESCRIPTOR.enum_types_by_name['ReturnCode'] = _RETURNCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'updateregister_pb2'
  # @@protoc_insertion_point(class_scope:updateregister.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'updateregister_pb2'
  # @@protoc_insertion_point(class_scope:updateregister.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)



_STUBREGISTER = _descriptor.ServiceDescriptor(
  name='StubRegister',
  full_name='updateregister.StubRegister',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=193,
  serialized_end=288,
  methods=[
  _descriptor.MethodDescriptor(
    name='register',
    full_name='updateregister.StubRegister.register',
    index=0,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STUBREGISTER)

DESCRIPTOR.services_by_name['StubRegister'] = _STUBREGISTER

# @@protoc_insertion_point(module_scope)
