# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ex.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ex.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x08\x65x.proto\"\x16\n\x06\x42ottle\x12\x0c\n\x04note\x18\n \x01(\x02\x62\x06proto3')
)




_BOTTLE = _descriptor.Descriptor(
  name='Bottle',
  full_name='Bottle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='note', full_name='Bottle.note', index=0,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=12,
  serialized_end=34,
)

DESCRIPTOR.message_types_by_name['Bottle'] = _BOTTLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Bottle = _reflection.GeneratedProtocolMessageType('Bottle', (_message.Message,), dict(
  DESCRIPTOR = _BOTTLE,
  __module__ = 'ex_pb2'
  # @@protoc_insertion_point(class_scope:Bottle)
  ))
_sym_db.RegisterMessage(Bottle)


# @@protoc_insertion_point(module_scope)
