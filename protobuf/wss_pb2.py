# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wss.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\twss.proto\"\xdd\x01\n\x0bWssResponse\x12\x18\n\x10wss_push_room_id\x18\x01 \x01(\x03\x12\x14\n\x0cwss_push_did\x18\x02 \x01(\x03\x12\x17\n\x0fwss_push_log_id\x18\x03 \x01(\x03\x12\x14\n\x0cwss_fetch_ms\x18\x04 \x01(\x03\x12\x13\n\x0bwss_push_ms\x18\x05 \x01(\x03\x12\x14\n\x0cwss_msg_type\x18\x06 \x01(\t\x12\n\n\x02pb\x18\x07 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\x0c\x12\x13\n\x0bserver_time\x18\t \x01(\x03\x12\x15\n\rcompress_type\x18\n \x01(\tb\x06proto3')



_WSSRESPONSE = DESCRIPTOR.message_types_by_name['WssResponse']
WssResponse = _reflection.GeneratedProtocolMessageType('WssResponse', (_message.Message,), {
  'DESCRIPTOR' : _WSSRESPONSE,
  '__module__' : 'wss_pb2'
  # @@protoc_insertion_point(class_scope:WssResponse)
  })
_sym_db.RegisterMessage(WssResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WSSRESPONSE._serialized_start=14
  _WSSRESPONSE._serialized_end=235
# @@protoc_insertion_point(module_scope)
