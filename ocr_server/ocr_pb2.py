# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ocr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tocr.proto\x12\x03ocr\"\x1e\n\rCharacterBody\x12\r\n\x05image\x18\x01 \x01(\x0c\"6\n\x0e\x43haracterReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x14\n\x0c\x63onsumedTime\x18\x02 \x01(\x05\x32=\n\x03OCR\x12\x36\n\tCharacter\x12\x12.ocr.CharacterBody\x1a\x13.ocr.CharacterReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ocr_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CHARACTERBODY']._serialized_start=18
  _globals['_CHARACTERBODY']._serialized_end=48
  _globals['_CHARACTERREPLY']._serialized_start=50
  _globals['_CHARACTERREPLY']._serialized_end=104
  _globals['_OCR']._serialized_start=106
  _globals['_OCR']._serialized_end=167
# @@protoc_insertion_point(module_scope)
