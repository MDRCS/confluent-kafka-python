# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common_proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import metadata_proto_pb2 as metadata__proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common_proto.proto',
  package='Criteo.Glup',
  syntax='proto3',
  serialized_pb=_b('\n\x12\x63ommon_proto.proto\x12\x0b\x43riteo.Glup\x1a\x14metadata_proto.proto\"\xda\x01\n\x07\x43onsent\x12 \n\x18identification_forbidden\x18\x01 \x01(\x08\x12:\n\x06reason\x18\x02 \x01(\x0e\x32*.Criteo.Glup.IdentificationForbiddenReason\x12\x39\n\nset_fields\x18\xda\x86\x03 \x03(\x0b\x32#.Criteo.Glup.Consent.SetFieldsEntry\x1a\x30\n\x0eSetFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01:\x04\x88\xb5\x18\x01*/\n\x16MarketingObjectiveType\x12\x08\n\x04Sale\x10\x00\x12\x0b\n\x07Install\x10\x01*\xd0\x01\n\x1dIdentificationForbiddenReason\x12\x0c\n\x08NoReason\x10\x00\x12\x1b\n\x17\x45xplicitConsentRequired\x10\x01\x12\x10\n\x0cOptoutCookie\x10\x02\x12\x13\n\x0f\x43toOptoutCookie\x10\x03\x12\x15\n\x11LimitedAdTracking\x10\x04\x12\x0e\n\nHstsOptout\x10\x05\x12\x14\n\x10\x44oNotTrackHeader\x10\x06\x12\r\n\tOoOCookie\x10\x07\x12\x11\n\rPendingOptout\x10\x08\x42\x11\n\x0f\x63om.criteo.glupb\x06proto3')
  ,
  dependencies=[metadata__proto__pb2.DESCRIPTOR,])

_MARKETINGOBJECTIVETYPE = _descriptor.EnumDescriptor(
  name='MarketingObjectiveType',
  full_name='Criteo.Glup.MarketingObjectiveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Sale', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Install', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=278,
  serialized_end=325,
)
_sym_db.RegisterEnumDescriptor(_MARKETINGOBJECTIVETYPE)

MarketingObjectiveType = enum_type_wrapper.EnumTypeWrapper(_MARKETINGOBJECTIVETYPE)
_IDENTIFICATIONFORBIDDENREASON = _descriptor.EnumDescriptor(
  name='IdentificationForbiddenReason',
  full_name='Criteo.Glup.IdentificationForbiddenReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoReason', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ExplicitConsentRequired', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OptoutCookie', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CtoOptoutCookie', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LimitedAdTracking', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HstsOptout', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DoNotTrackHeader', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OoOCookie', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PendingOptout', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=328,
  serialized_end=536,
)
_sym_db.RegisterEnumDescriptor(_IDENTIFICATIONFORBIDDENREASON)

IdentificationForbiddenReason = enum_type_wrapper.EnumTypeWrapper(_IDENTIFICATIONFORBIDDENREASON)
Sale = 0
Install = 1
NoReason = 0
ExplicitConsentRequired = 1
OptoutCookie = 2
CtoOptoutCookie = 3
LimitedAdTracking = 4
HstsOptout = 5
DoNotTrackHeader = 6
OoOCookie = 7
PendingOptout = 8



_CONSENT_SETFIELDSENTRY = _descriptor.Descriptor(
  name='SetFieldsEntry',
  full_name='Criteo.Glup.Consent.SetFieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Criteo.Glup.Consent.SetFieldsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Criteo.Glup.Consent.SetFieldsEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=270,
)

_CONSENT = _descriptor.Descriptor(
  name='Consent',
  full_name='Criteo.Glup.Consent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identification_forbidden', full_name='Criteo.Glup.Consent.identification_forbidden', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='Criteo.Glup.Consent.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_fields', full_name='Criteo.Glup.Consent.set_fields', index=2,
      number=50010, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONSENT_SETFIELDSENTRY, ],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\265\030\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=276,
)

_CONSENT_SETFIELDSENTRY.containing_type = _CONSENT
_CONSENT.fields_by_name['reason'].enum_type = _IDENTIFICATIONFORBIDDENREASON
_CONSENT.fields_by_name['set_fields'].message_type = _CONSENT_SETFIELDSENTRY
DESCRIPTOR.message_types_by_name['Consent'] = _CONSENT
DESCRIPTOR.enum_types_by_name['MarketingObjectiveType'] = _MARKETINGOBJECTIVETYPE
DESCRIPTOR.enum_types_by_name['IdentificationForbiddenReason'] = _IDENTIFICATIONFORBIDDENREASON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Consent = _reflection.GeneratedProtocolMessageType('Consent', (_message.Message,), dict(

  SetFieldsEntry = _reflection.GeneratedProtocolMessageType('SetFieldsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONSENT_SETFIELDSENTRY,
    __module__ = 'common_proto_pb2'
    # @@protoc_insertion_point(class_scope:Criteo.Glup.Consent.SetFieldsEntry)
    ))
  ,
  DESCRIPTOR = _CONSENT,
  __module__ = 'common_proto_pb2'
  # @@protoc_insertion_point(class_scope:Criteo.Glup.Consent)
  ))
_sym_db.RegisterMessage(Consent)
_sym_db.RegisterMessage(Consent.SetFieldsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\017com.criteo.glup'))
_CONSENT_SETFIELDSENTRY.has_options = True
_CONSENT_SETFIELDSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CONSENT.has_options = True
_CONSENT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\210\265\030\001'))
# @@protoc_insertion_point(module_scope)
