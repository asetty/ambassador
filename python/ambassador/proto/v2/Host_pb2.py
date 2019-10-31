# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getambassador.io/v2/Host.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from k8s.io.apimachinery.pkg.apis.meta.v1 import generated_pb2 as k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2
from k8s.io.api.core.v1 import generated_pb2 as k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='getambassador.io/v2/Host.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1egetambassador.io/v2/Host.proto\x1a\x34k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto\x1a\"k8s.io/api/core/v1/generated.proto\"\x80\x01\n\x04Host\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta\x12\x17\n\x04spec\x18\x02 \x01(\x0b\x32\t.HostSpec\x12\x1b\n\x06status\x18\x03 \x01(\x0b\x32\x0b.HostStatus\"\xf4\x01\n\x08HostSpec\x12\x15\n\rambassador_id\x18\x01 \x03(\t\x12\x12\n\ngeneration\x18\x02 \x01(\x05\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x45\n\x08selector\x18\x04 \x01(\x0b\x32\x33.k8s.io.apimachinery.pkg.apis.meta.v1.LabelSelector\x12\'\n\x0c\x61\x63meProvider\x18\x05 \x01(\x0b\x32\x11.ACMEProviderSpec\x12;\n\ttlsSecret\x18\x06 \x01(\x0b\x32(.k8s.io.api.core.v1.LocalObjectReference\"\xb6\x01\n\nHostStatus\x12\x37\n\x14tlsCertificateSource\x18\x01 \x01(\x0e\x32\x19.HostTLSCertificateSource\x12\x19\n\x05state\x18\x02 \x01(\x0e\x32\n.HostState\x12\"\n\x0ephaseCompleted\x18\x03 \x01(\x0e\x32\n.HostPhase\x12 \n\x0cphasePending\x18\x04 \x01(\x0e\x32\n.HostPhase\x12\x0e\n\x06reason\x18\x05 \x01(\t\"\x8e\x01\n\x10\x41\x43MEProviderSpec\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x42\n\x10privateKeySecret\x18\x03 \x01(\x0b\x32(.k8s.io.api.core.v1.LocalObjectReference\x12\x14\n\x0cregistration\x18\x04 \x01(\t*F\n\x18HostTLSCertificateSource\x12\x0b\n\x07Unknown\x10\x00\x12\x08\n\x04None\x10\x01\x12\t\n\x05Other\x10\x02\x12\x08\n\x04\x41\x43ME\x10\x03*.\n\tHostState\x12\x0b\n\x07Pending\x10\x00\x12\t\n\x05Ready\x10\x01\x12\t\n\x05\x45rror\x10\x02*|\n\tHostPhase\x12\x06\n\x02NA\x10\x00\x12\x12\n\x0e\x44\x65\x66\x61ultsFilled\x10\x01\x12\x1d\n\x19\x41\x43MEUserPrivateKeyCreated\x10\x02\x12\x16\n\x12\x41\x43MEUserRegistered\x10\x03\x12\x1c\n\x18\x41\x43MECertificateChallenge\x10\x04\x62\x06proto3')
  ,
  dependencies=[k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2.DESCRIPTOR,k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2.DESCRIPTOR,])

_HOSTTLSCERTIFICATESOURCE = _descriptor.EnumDescriptor(
  name='HostTLSCertificateSource',
  full_name='HostTLSCertificateSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='None', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Other', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACME', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=832,
  serialized_end=902,
)
_sym_db.RegisterEnumDescriptor(_HOSTTLSCERTIFICATESOURCE)

HostTLSCertificateSource = enum_type_wrapper.EnumTypeWrapper(_HOSTTLSCERTIFICATESOURCE)
_HOSTSTATE = _descriptor.EnumDescriptor(
  name='HostState',
  full_name='HostState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Pending', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ready', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Error', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=904,
  serialized_end=950,
)
_sym_db.RegisterEnumDescriptor(_HOSTSTATE)

HostState = enum_type_wrapper.EnumTypeWrapper(_HOSTSTATE)
_HOSTPHASE = _descriptor.EnumDescriptor(
  name='HostPhase',
  full_name='HostPhase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DefaultsFilled', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACMEUserPrivateKeyCreated', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACMEUserRegistered', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACMECertificateChallenge', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=952,
  serialized_end=1076,
)
_sym_db.RegisterEnumDescriptor(_HOSTPHASE)

HostPhase = enum_type_wrapper.EnumTypeWrapper(_HOSTPHASE)
Unknown = 0
None = 1
Other = 2
ACME = 3
Pending = 0
Ready = 1
Error = 2
NA = 0
DefaultsFilled = 1
ACMEUserPrivateKeyCreated = 2
ACMEUserRegistered = 3
ACMECertificateChallenge = 4



_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='Host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='Host.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='Host.spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Host.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=125,
  serialized_end=253,
)


_HOSTSPEC = _descriptor.Descriptor(
  name='HostSpec',
  full_name='HostSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ambassador_id', full_name='HostSpec.ambassador_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generation', full_name='HostSpec.generation', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='HostSpec.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selector', full_name='HostSpec.selector', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acmeProvider', full_name='HostSpec.acmeProvider', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tlsSecret', full_name='HostSpec.tlsSecret', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=256,
  serialized_end=500,
)


_HOSTSTATUS = _descriptor.Descriptor(
  name='HostStatus',
  full_name='HostStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tlsCertificateSource', full_name='HostStatus.tlsCertificateSource', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='HostStatus.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phaseCompleted', full_name='HostStatus.phaseCompleted', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phasePending', full_name='HostStatus.phasePending', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='HostStatus.reason', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=503,
  serialized_end=685,
)


_ACMEPROVIDERSPEC = _descriptor.Descriptor(
  name='ACMEProviderSpec',
  full_name='ACMEProviderSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authority', full_name='ACMEProviderSpec.authority', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='ACMEProviderSpec.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='privateKeySecret', full_name='ACMEProviderSpec.privateKeySecret', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registration', full_name='ACMEProviderSpec.registration', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=688,
  serialized_end=830,
)

_HOST.fields_by_name['metadata'].message_type = k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2._OBJECTMETA
_HOST.fields_by_name['spec'].message_type = _HOSTSPEC
_HOST.fields_by_name['status'].message_type = _HOSTSTATUS
_HOSTSPEC.fields_by_name['selector'].message_type = k8s_dot_io_dot_apimachinery_dot_pkg_dot_apis_dot_meta_dot_v1_dot_generated__pb2._LABELSELECTOR
_HOSTSPEC.fields_by_name['acmeProvider'].message_type = _ACMEPROVIDERSPEC
_HOSTSPEC.fields_by_name['tlsSecret'].message_type = k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2._LOCALOBJECTREFERENCE
_HOSTSTATUS.fields_by_name['tlsCertificateSource'].enum_type = _HOSTTLSCERTIFICATESOURCE
_HOSTSTATUS.fields_by_name['state'].enum_type = _HOSTSTATE
_HOSTSTATUS.fields_by_name['phaseCompleted'].enum_type = _HOSTPHASE
_HOSTSTATUS.fields_by_name['phasePending'].enum_type = _HOSTPHASE
_ACMEPROVIDERSPEC.fields_by_name['privateKeySecret'].message_type = k8s_dot_io_dot_api_dot_core_dot_v1_dot_generated__pb2._LOCALOBJECTREFERENCE
DESCRIPTOR.message_types_by_name['Host'] = _HOST
DESCRIPTOR.message_types_by_name['HostSpec'] = _HOSTSPEC
DESCRIPTOR.message_types_by_name['HostStatus'] = _HOSTSTATUS
DESCRIPTOR.message_types_by_name['ACMEProviderSpec'] = _ACMEPROVIDERSPEC
DESCRIPTOR.enum_types_by_name['HostTLSCertificateSource'] = _HOSTTLSCERTIFICATESOURCE
DESCRIPTOR.enum_types_by_name['HostState'] = _HOSTSTATE
DESCRIPTOR.enum_types_by_name['HostPhase'] = _HOSTPHASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Host = _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), dict(
  DESCRIPTOR = _HOST,
  __module__ = 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:Host)
  ))
_sym_db.RegisterMessage(Host)

HostSpec = _reflection.GeneratedProtocolMessageType('HostSpec', (_message.Message,), dict(
  DESCRIPTOR = _HOSTSPEC,
  __module__ = 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:HostSpec)
  ))
_sym_db.RegisterMessage(HostSpec)

HostStatus = _reflection.GeneratedProtocolMessageType('HostStatus', (_message.Message,), dict(
  DESCRIPTOR = _HOSTSTATUS,
  __module__ = 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:HostStatus)
  ))
_sym_db.RegisterMessage(HostStatus)

ACMEProviderSpec = _reflection.GeneratedProtocolMessageType('ACMEProviderSpec', (_message.Message,), dict(
  DESCRIPTOR = _ACMEPROVIDERSPEC,
  __module__ = 'getambassador.io.v2.Host_pb2'
  # @@protoc_insertion_point(class_scope:ACMEProviderSpec)
  ))
_sym_db.RegisterMessage(ACMEProviderSpec)


# @@protoc_insertion_point(module_scope)
