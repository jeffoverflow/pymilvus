# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema.proto',
  package='milvus.proto.schema',
  syntax='proto3',
  serialized_options=_b('Z3github.com/milvus-io/milvus/internal/proto/schemapb'),
  serialized_pb=_b('\n\x0cschema.proto\x12\x13milvus.proto.schema\x1a\x0c\x63ommon.proto\"\xfc\x01\n\x0b\x46ieldSchema\x12\x0f\n\x07\x66ieldID\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0eis_primary_key\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x30\n\tdata_type\x18\x05 \x01(\x0e\x32\x1d.milvus.proto.schema.DataType\x12\x36\n\x0btype_params\x18\x06 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x37\n\x0cindex_params\x18\x07 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\"w\n\x10\x43ollectionSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06\x61utoID\x18\x03 \x01(\x08\x12\x30\n\x06\x66ields\x18\x04 \x03(\x0b\x32 .milvus.proto.schema.FieldSchema\"\x19\n\tBoolArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x08\"\x18\n\x08IntArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x05\"\x19\n\tLongArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x03\"\x1a\n\nFloatArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"\x1b\n\x0b\x44oubleArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x01\"\x1a\n\nBytesArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x0c\"\x1b\n\x0bStringArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\t\"\x92\x03\n\x0bScalarField\x12\x33\n\tbool_data\x18\x01 \x01(\x0b\x32\x1e.milvus.proto.schema.BoolArrayH\x00\x12\x31\n\x08int_data\x18\x02 \x01(\x0b\x32\x1d.milvus.proto.schema.IntArrayH\x00\x12\x33\n\tlong_data\x18\x03 \x01(\x0b\x32\x1e.milvus.proto.schema.LongArrayH\x00\x12\x35\n\nfloat_data\x18\x04 \x01(\x0b\x32\x1f.milvus.proto.schema.FloatArrayH\x00\x12\x37\n\x0b\x64ouble_data\x18\x05 \x01(\x0b\x32 .milvus.proto.schema.DoubleArrayH\x00\x12\x37\n\x0bstring_data\x18\x06 \x01(\x0b\x32 .milvus.proto.schema.StringArrayH\x00\x12\x35\n\nbytes_data\x18\x07 \x01(\x0b\x32\x1f.milvus.proto.schema.BytesArrayH\x00\x42\x06\n\x04\x64\x61ta\"t\n\x0bVectorField\x12\x0b\n\x03\x64im\x18\x01 \x01(\x03\x12\x37\n\x0c\x66loat_vector\x18\x02 \x01(\x0b\x32\x1f.milvus.proto.schema.FloatArrayH\x00\x12\x17\n\rbinary_vector\x18\x03 \x01(\x0cH\x00\x42\x06\n\x04\x64\x61ta\"\xbf\x01\n\tFieldData\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.milvus.proto.schema.DataType\x12\x12\n\nfield_name\x18\x02 \x01(\t\x12\x33\n\x07scalars\x18\x03 \x01(\x0b\x32 .milvus.proto.schema.ScalarFieldH\x00\x12\x33\n\x07vectors\x18\x04 \x01(\x0b\x32 .milvus.proto.schema.VectorFieldH\x00\x42\x07\n\x05\x66ield\"w\n\x03IDs\x12\x30\n\x06int_id\x18\x01 \x01(\x0b\x32\x1e.milvus.proto.schema.LongArrayH\x00\x12\x32\n\x06str_id\x18\x02 \x01(\x0b\x32 .milvus.proto.schema.StringArrayH\x00\x42\n\n\x08id_field*\x8f\x01\n\x08\x44\x61taType\x12\x08\n\x04None\x10\x00\x12\x08\n\x04\x42ool\x10\x01\x12\x08\n\x04Int8\x10\x02\x12\t\n\x05Int16\x10\x03\x12\t\n\x05Int32\x10\x04\x12\t\n\x05Int64\x10\x05\x12\t\n\x05\x46loat\x10\n\x12\n\n\x06\x44ouble\x10\x0b\x12\n\n\x06String\x10\x14\x12\x10\n\x0c\x42inaryVector\x10\x64\x12\x0f\n\x0b\x46loatVector\x10\x65\x42\x35Z3github.com/milvus-io/milvus/internal/proto/schemapbb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='milvus.proto.schema.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='None', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Bool', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Int8', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Int16', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Int32', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Int64', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Float', index=6, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Double', index=7, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='String', index=8, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BinaryVector', index=9, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FloatVector', index=10, number=101,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1460,
  serialized_end=1603,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
globals()['None'] = 0
Bool = 1
Int8 = 2
Int16 = 3
Int32 = 4
Int64 = 5
Float = 10
Double = 11
String = 20
BinaryVector = 100
FloatVector = 101



_FIELDSCHEMA = _descriptor.Descriptor(
  name='FieldSchema',
  full_name='milvus.proto.schema.FieldSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fieldID', full_name='milvus.proto.schema.FieldSchema.fieldID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='milvus.proto.schema.FieldSchema.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_primary_key', full_name='milvus.proto.schema.FieldSchema.is_primary_key', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='milvus.proto.schema.FieldSchema.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='milvus.proto.schema.FieldSchema.data_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_params', full_name='milvus.proto.schema.FieldSchema.type_params', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_params', full_name='milvus.proto.schema.FieldSchema.index_params', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=52,
  serialized_end=304,
)


_COLLECTIONSCHEMA = _descriptor.Descriptor(
  name='CollectionSchema',
  full_name='milvus.proto.schema.CollectionSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='milvus.proto.schema.CollectionSchema.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='milvus.proto.schema.CollectionSchema.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autoID', full_name='milvus.proto.schema.CollectionSchema.autoID', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='milvus.proto.schema.CollectionSchema.fields', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=306,
  serialized_end=425,
)


_BOOLARRAY = _descriptor.Descriptor(
  name='BoolArray',
  full_name='milvus.proto.schema.BoolArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='milvus.proto.schema.BoolArray.data', index=0,
      number=1, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=427,
  serialized_end=452,
)


_INTARRAY = _descriptor.Descriptor(
  name='IntArray',
  full_name='milvus.proto.schema.IntArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='milvus.proto.schema.IntArray.data', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=454,
  serialized_end=478,
)


_LONGARRAY = _descriptor.Descriptor(
  name='LongArray',
  full_name='milvus.proto.schema.LongArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='milvus.proto.schema.LongArray.data', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=480,
  serialized_end=505,
)


_FLOATARRAY = _descriptor.Descriptor(
  name='FloatArray',
  full_name='milvus.proto.schema.FloatArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='milvus.proto.schema.FloatArray.data', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=507,
  serialized_end=533,
)


_DOUBLEARRAY = _descriptor.Descriptor(
  name='DoubleArray',
  full_name='milvus.proto.schema.DoubleArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='milvus.proto.schema.DoubleArray.data', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=535,
  serialized_end=562,
)


_BYTESARRAY = _descriptor.Descriptor(
  name='BytesArray',
  full_name='milvus.proto.schema.BytesArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='milvus.proto.schema.BytesArray.data', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=564,
  serialized_end=590,
)


_STRINGARRAY = _descriptor.Descriptor(
  name='StringArray',
  full_name='milvus.proto.schema.StringArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='milvus.proto.schema.StringArray.data', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=592,
  serialized_end=619,
)


_SCALARFIELD = _descriptor.Descriptor(
  name='ScalarField',
  full_name='milvus.proto.schema.ScalarField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bool_data', full_name='milvus.proto.schema.ScalarField.bool_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_data', full_name='milvus.proto.schema.ScalarField.int_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_data', full_name='milvus.proto.schema.ScalarField.long_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_data', full_name='milvus.proto.schema.ScalarField.float_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_data', full_name='milvus.proto.schema.ScalarField.double_data', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_data', full_name='milvus.proto.schema.ScalarField.string_data', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_data', full_name='milvus.proto.schema.ScalarField.bytes_data', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='milvus.proto.schema.ScalarField.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=622,
  serialized_end=1024,
)


_VECTORFIELD = _descriptor.Descriptor(
  name='VectorField',
  full_name='milvus.proto.schema.VectorField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim', full_name='milvus.proto.schema.VectorField.dim', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_vector', full_name='milvus.proto.schema.VectorField.float_vector', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary_vector', full_name='milvus.proto.schema.VectorField.binary_vector', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
    _descriptor.OneofDescriptor(
      name='data', full_name='milvus.proto.schema.VectorField.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1026,
  serialized_end=1142,
)


_FIELDDATA = _descriptor.Descriptor(
  name='FieldData',
  full_name='milvus.proto.schema.FieldData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='milvus.proto.schema.FieldData.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_name', full_name='milvus.proto.schema.FieldData.field_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scalars', full_name='milvus.proto.schema.FieldData.scalars', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vectors', full_name='milvus.proto.schema.FieldData.vectors', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='field', full_name='milvus.proto.schema.FieldData.field',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1145,
  serialized_end=1336,
)


_IDS = _descriptor.Descriptor(
  name='IDs',
  full_name='milvus.proto.schema.IDs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_id', full_name='milvus.proto.schema.IDs.int_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_id', full_name='milvus.proto.schema.IDs.str_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='id_field', full_name='milvus.proto.schema.IDs.id_field',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1338,
  serialized_end=1457,
)

_FIELDSCHEMA.fields_by_name['data_type'].enum_type = _DATATYPE
_FIELDSCHEMA.fields_by_name['type_params'].message_type = common__pb2._KEYVALUEPAIR
_FIELDSCHEMA.fields_by_name['index_params'].message_type = common__pb2._KEYVALUEPAIR
_COLLECTIONSCHEMA.fields_by_name['fields'].message_type = _FIELDSCHEMA
_SCALARFIELD.fields_by_name['bool_data'].message_type = _BOOLARRAY
_SCALARFIELD.fields_by_name['int_data'].message_type = _INTARRAY
_SCALARFIELD.fields_by_name['long_data'].message_type = _LONGARRAY
_SCALARFIELD.fields_by_name['float_data'].message_type = _FLOATARRAY
_SCALARFIELD.fields_by_name['double_data'].message_type = _DOUBLEARRAY
_SCALARFIELD.fields_by_name['string_data'].message_type = _STRINGARRAY
_SCALARFIELD.fields_by_name['bytes_data'].message_type = _BYTESARRAY
_SCALARFIELD.oneofs_by_name['data'].fields.append(
  _SCALARFIELD.fields_by_name['bool_data'])
_SCALARFIELD.fields_by_name['bool_data'].containing_oneof = _SCALARFIELD.oneofs_by_name['data']
_SCALARFIELD.oneofs_by_name['data'].fields.append(
  _SCALARFIELD.fields_by_name['int_data'])
_SCALARFIELD.fields_by_name['int_data'].containing_oneof = _SCALARFIELD.oneofs_by_name['data']
_SCALARFIELD.oneofs_by_name['data'].fields.append(
  _SCALARFIELD.fields_by_name['long_data'])
_SCALARFIELD.fields_by_name['long_data'].containing_oneof = _SCALARFIELD.oneofs_by_name['data']
_SCALARFIELD.oneofs_by_name['data'].fields.append(
  _SCALARFIELD.fields_by_name['float_data'])
_SCALARFIELD.fields_by_name['float_data'].containing_oneof = _SCALARFIELD.oneofs_by_name['data']
_SCALARFIELD.oneofs_by_name['data'].fields.append(
  _SCALARFIELD.fields_by_name['double_data'])
_SCALARFIELD.fields_by_name['double_data'].containing_oneof = _SCALARFIELD.oneofs_by_name['data']
_SCALARFIELD.oneofs_by_name['data'].fields.append(
  _SCALARFIELD.fields_by_name['string_data'])
_SCALARFIELD.fields_by_name['string_data'].containing_oneof = _SCALARFIELD.oneofs_by_name['data']
_SCALARFIELD.oneofs_by_name['data'].fields.append(
  _SCALARFIELD.fields_by_name['bytes_data'])
_SCALARFIELD.fields_by_name['bytes_data'].containing_oneof = _SCALARFIELD.oneofs_by_name['data']
_VECTORFIELD.fields_by_name['float_vector'].message_type = _FLOATARRAY
_VECTORFIELD.oneofs_by_name['data'].fields.append(
  _VECTORFIELD.fields_by_name['float_vector'])
_VECTORFIELD.fields_by_name['float_vector'].containing_oneof = _VECTORFIELD.oneofs_by_name['data']
_VECTORFIELD.oneofs_by_name['data'].fields.append(
  _VECTORFIELD.fields_by_name['binary_vector'])
_VECTORFIELD.fields_by_name['binary_vector'].containing_oneof = _VECTORFIELD.oneofs_by_name['data']
_FIELDDATA.fields_by_name['type'].enum_type = _DATATYPE
_FIELDDATA.fields_by_name['scalars'].message_type = _SCALARFIELD
_FIELDDATA.fields_by_name['vectors'].message_type = _VECTORFIELD
_FIELDDATA.oneofs_by_name['field'].fields.append(
  _FIELDDATA.fields_by_name['scalars'])
_FIELDDATA.fields_by_name['scalars'].containing_oneof = _FIELDDATA.oneofs_by_name['field']
_FIELDDATA.oneofs_by_name['field'].fields.append(
  _FIELDDATA.fields_by_name['vectors'])
_FIELDDATA.fields_by_name['vectors'].containing_oneof = _FIELDDATA.oneofs_by_name['field']
_IDS.fields_by_name['int_id'].message_type = _LONGARRAY
_IDS.fields_by_name['str_id'].message_type = _STRINGARRAY
_IDS.oneofs_by_name['id_field'].fields.append(
  _IDS.fields_by_name['int_id'])
_IDS.fields_by_name['int_id'].containing_oneof = _IDS.oneofs_by_name['id_field']
_IDS.oneofs_by_name['id_field'].fields.append(
  _IDS.fields_by_name['str_id'])
_IDS.fields_by_name['str_id'].containing_oneof = _IDS.oneofs_by_name['id_field']
DESCRIPTOR.message_types_by_name['FieldSchema'] = _FIELDSCHEMA
DESCRIPTOR.message_types_by_name['CollectionSchema'] = _COLLECTIONSCHEMA
DESCRIPTOR.message_types_by_name['BoolArray'] = _BOOLARRAY
DESCRIPTOR.message_types_by_name['IntArray'] = _INTARRAY
DESCRIPTOR.message_types_by_name['LongArray'] = _LONGARRAY
DESCRIPTOR.message_types_by_name['FloatArray'] = _FLOATARRAY
DESCRIPTOR.message_types_by_name['DoubleArray'] = _DOUBLEARRAY
DESCRIPTOR.message_types_by_name['BytesArray'] = _BYTESARRAY
DESCRIPTOR.message_types_by_name['StringArray'] = _STRINGARRAY
DESCRIPTOR.message_types_by_name['ScalarField'] = _SCALARFIELD
DESCRIPTOR.message_types_by_name['VectorField'] = _VECTORFIELD
DESCRIPTOR.message_types_by_name['FieldData'] = _FIELDDATA
DESCRIPTOR.message_types_by_name['IDs'] = _IDS
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FieldSchema = _reflection.GeneratedProtocolMessageType('FieldSchema', (_message.Message,), {
  'DESCRIPTOR' : _FIELDSCHEMA,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.FieldSchema)
  })
_sym_db.RegisterMessage(FieldSchema)

CollectionSchema = _reflection.GeneratedProtocolMessageType('CollectionSchema', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONSCHEMA,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.CollectionSchema)
  })
_sym_db.RegisterMessage(CollectionSchema)

BoolArray = _reflection.GeneratedProtocolMessageType('BoolArray', (_message.Message,), {
  'DESCRIPTOR' : _BOOLARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.BoolArray)
  })
_sym_db.RegisterMessage(BoolArray)

IntArray = _reflection.GeneratedProtocolMessageType('IntArray', (_message.Message,), {
  'DESCRIPTOR' : _INTARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.IntArray)
  })
_sym_db.RegisterMessage(IntArray)

LongArray = _reflection.GeneratedProtocolMessageType('LongArray', (_message.Message,), {
  'DESCRIPTOR' : _LONGARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.LongArray)
  })
_sym_db.RegisterMessage(LongArray)

FloatArray = _reflection.GeneratedProtocolMessageType('FloatArray', (_message.Message,), {
  'DESCRIPTOR' : _FLOATARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.FloatArray)
  })
_sym_db.RegisterMessage(FloatArray)

DoubleArray = _reflection.GeneratedProtocolMessageType('DoubleArray', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.DoubleArray)
  })
_sym_db.RegisterMessage(DoubleArray)

BytesArray = _reflection.GeneratedProtocolMessageType('BytesArray', (_message.Message,), {
  'DESCRIPTOR' : _BYTESARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.BytesArray)
  })
_sym_db.RegisterMessage(BytesArray)

StringArray = _reflection.GeneratedProtocolMessageType('StringArray', (_message.Message,), {
  'DESCRIPTOR' : _STRINGARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.StringArray)
  })
_sym_db.RegisterMessage(StringArray)

ScalarField = _reflection.GeneratedProtocolMessageType('ScalarField', (_message.Message,), {
  'DESCRIPTOR' : _SCALARFIELD,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.ScalarField)
  })
_sym_db.RegisterMessage(ScalarField)

VectorField = _reflection.GeneratedProtocolMessageType('VectorField', (_message.Message,), {
  'DESCRIPTOR' : _VECTORFIELD,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.VectorField)
  })
_sym_db.RegisterMessage(VectorField)

FieldData = _reflection.GeneratedProtocolMessageType('FieldData', (_message.Message,), {
  'DESCRIPTOR' : _FIELDDATA,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.FieldData)
  })
_sym_db.RegisterMessage(FieldData)

IDs = _reflection.GeneratedProtocolMessageType('IDs', (_message.Message,), {
  'DESCRIPTOR' : _IDS,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.IDs)
  })
_sym_db.RegisterMessage(IDs)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
