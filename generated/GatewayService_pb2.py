# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GatewayService.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14GatewayService.proto\x12\x12\x63raftyllamagateway\"\x1f\n\x0fTestSendMessage\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\"\x1c\n\x0cTestResponse\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t2j\n\x12TestMessageService\x12T\n\x0bTestMessage\x12#.craftyllamagateway.TestSendMessage\x1a .craftyllamagateway.TestResponseB\x15Z\x13./craftyllamaprotosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GatewayService_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\023./craftyllamaprotos'
  _globals['_TESTSENDMESSAGE']._serialized_start=44
  _globals['_TESTSENDMESSAGE']._serialized_end=75
  _globals['_TESTRESPONSE']._serialized_start=77
  _globals['_TESTRESPONSE']._serialized_end=105
  _globals['_TESTMESSAGESERVICE']._serialized_start=107
  _globals['_TESTMESSAGESERVICE']._serialized_end=213
# @@protoc_insertion_point(module_scope)