# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/unittest_no_generic_services.proto

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
  name='google/protobuf/unittest_no_generic_services.proto',
  package='google.protobuf.no_generic_services_test',
  syntax='proto2',
    serialized_options=None,
  serialized_pb=_b('\n2google/protobuf/unittest_no_generic_services.proto\x12(google.protobuf.no_generic_services_test\"#\n\x0bTestMessage\x12\t\n\x01\x61\x18\x01 \x01(\x05*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02*\x13\n\x08TestEnum\x12\x07\n\x03\x46OO\x10\x01\x32\x82\x01\n\x0bTestService\x12s\n\x03\x46oo\x12\x35.google.protobuf.no_generic_services_test.TestMessage\x1a\x35.google.protobuf.no_generic_services_test.TestMessage:N\n\x0etest_extension\x12\x35.google.protobuf.no_generic_services_test.TestMessage\x18\xe8\x07 \x01(\x05')
)

_TESTENUM = _descriptor.EnumDescriptor(
  name='TestEnum',
  full_name='google.protobuf.no_generic_services_test.TestEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FOO', index=0, number=1,
        serialized_options=None,
      type=None),
  ],
  containing_type=None,
    serialized_options=None,
  serialized_start=133,
  serialized_end=152,
)
_sym_db.RegisterEnumDescriptor(_TESTENUM)

TestEnum = enum_type_wrapper.EnumTypeWrapper(_TESTENUM)
FOO = 1

TEST_EXTENSION_FIELD_NUMBER = 1000
test_extension = _descriptor.FieldDescriptor(
  name='test_extension', full_name='google.protobuf.no_generic_services_test.test_extension', index=0,
  number=1000, type=5, cpp_type=1, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
    serialized_options=None, file=DESCRIPTOR)


_TESTMESSAGE = _descriptor.Descriptor(
  name='TestMessage',
  full_name='google.protobuf.no_generic_services_test.TestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='google.protobuf.no_generic_services_test.TestMessage.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 536870912), ],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['TestMessage'] = _TESTMESSAGE
DESCRIPTOR.enum_types_by_name['TestEnum'] = _TESTENUM
DESCRIPTOR.extensions_by_name['test_extension'] = test_extension
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMessage = _reflection.GeneratedProtocolMessageType('TestMessage', (_message.Message,), dict(
  DESCRIPTOR = _TESTMESSAGE,
  __module__ = 'google.protobuf.unittest_no_generic_services_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.no_generic_services_test.TestMessage)
  ))
_sym_db.RegisterMessage(TestMessage)

TestMessage.RegisterExtension(test_extension)

_TESTSERVICE = _descriptor.ServiceDescriptor(
    name='TestService',
    full_name='google.protobuf.no_generic_services_test.TestService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=155,
    serialized_end=285,
    methods=[
        _descriptor.MethodDescriptor(
            name='Foo',
            full_name='google.protobuf.no_generic_services_test.TestService.Foo',
            index=0,
            containing_service=None,
            input_type=_TESTMESSAGE,
            output_type=_TESTMESSAGE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
