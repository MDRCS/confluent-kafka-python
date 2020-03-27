#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import struct as _struct

__all__ = (
    'Deserializer',
    'IntegerDeserializer',
    'IntegerSerializer',
    'DoubleDeserializer',
    'DoubleSerializer',
    'StringDeserializer',
    'StringSerializer',
    'MessageField',
    'SerializationContext',
    'SerializationError',
    'Serializer')


class MessageField(object):
    """
    Enum like object for identifying Message fields.

    Attributes:
        KEY (str): Message key
        VALUE (str): Message value

    """
    KEY = 'key'
    VALUE = 'value'


class SerializationContext(object):
    """
    SerializationContext provides additional context to the
    serializer/deserializer about the data it's serializing/deserializing.

    Args:
        topic (str): Topic data is being produce to or consumed from.
        field (MessageField): Describes what part of the message is
            being serialized.

    """
    def __init__(self, topic, field):
        self.topic = topic
        self.field = field


class SerializationError(Exception):
    """Generic error from serializer package"""

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return '{klass}(error={error})'.format(
            klass=self.__class__.__name__,
            error=self.message
        )

    def __str__(self):
        return self.message


class KeySerializationError(SerializationError):
    pass


class KeyDeserializationError(SerializationError):
    pass


class ValueSerializationError(SerializationError):
    pass


class ValueDeserializationError(SerializationError):
    pass


class Serializer(object):
    """
    Extensible class from which all Serializer implementations derive.
    Serializers instruct Kafka clients on how to convert Python objects
    to bytes.

    See built-in implementations, listed below, for an example of how to
    extend this class.

    Note:
        This class is not directly instantiable. The derived classes must be
        used instead.

    The following implementations are provided by this module.

    Note:
        Unless noted elsewhere all numeric types are signed and big-endian.

    .. list-table::
        :header-rows: 1

        * - Name
          - Type
          - Binary Format
        * - DoubleSerializer
          - float
          - IEEE 764 binary64
        * - ShortSerializer
          - int
          - int16
        * - LongSerializer
          - int
          - int64
        * - IntegerSerializer
          - int
          - int32
        * - StringSerializer
          - unicode
          - unicode(encoding)

    """
    __slots__ = []

    def __call__(self, obj, ctx):
        """
        Converts obj to bytes.

        Args:
            obj (object): object to be serialized

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation

        Raises:
            SerializerError if an error occurs daring serialization

        Returns:
            bytes if obj is not None, otherwise None

        """
        raise NotImplementedError


class Deserializer(object):
    """
    Extensible class from which all Deserializer implementations derive.
    Deserializers instruct Kafka clients on how to convert bytes to objects.

    See built-in implementations, listed below, for an example of how to
    extend this class.

    Note:
        This class is not directly instantiable. The derived classes must be
        used instead.

    The following implementations are provided by this module.

    Note:
        Unless noted elsewhere all numeric types are signed and big-endian.

    .. list-table::
        :header-rows: 1

        * - Name
          - Type
          - Binary Format
        * - DoubleDeserializer
          - float
          - IEEE 764 binary64
        * - ShortDeserializer
          - int
          - int16
        * - LongDeserializer
          - int
          - int64
        * - IntegerDeserializer
          - int
          - int32
        * - StringDeserializer
          - unicode
          - unicode(encoding)

    """
    __slots__ = []

    def __call__(self, data, ctx):
        """
        Convert bytes to object

        Args:
            data (bytes): bytes to be deserialized

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation
        Raises:
            SerializerError if an error occurs daring deserialization

        Returns:
            object if data is not None, otherwise None

        """
        raise NotImplementedError


class DoubleSerializer(Serializer):
    """
    Serializes float to IEEE 764 binary64.

    .. _DoubleSerializer:
        https://docs.confluent.io/current/clients/javadocs/org/apache/kafka/common/serialization/DoubleSerializer.html

    """  # noqa: E501
    def __call__(self, obj, ctx):
        """
        Serializes float as IEEE 764 binary64 bytes.

        Args:
            obj (float): float to be serialized

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation.

        Note:
            None objects are represented as Kafka Null.

        Raises:
            SerializerError if an error occurs daring serialization.

        Returns:
            IEEE 764 binary64 bytes if obj is not None, otherwise None

        """
        if obj is None:
            return None

        try:
            return _struct.pack('>d', obj)
        except _struct.error as e:
            raise SerializationError(str(e))


class DoubleDeserializer(Deserializer):
    """
    Deserializes float to IEEE 764 binary64.

    .. _DoubleDeserializer:
        https://docs.confluent.io/current/clients/javadocs/org/apache/kafka/common/serialization/DoubleDeserializer.html

    """  # noqa: E501
    def __call__(self, data, ctx):
        """
        Deserializes float from IEEE 764 binary64 bytes.

        Args:
            data (bytes): IEEE 764 binary64 bytes

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation.

        Raises:
            SerializerError if an error occurs daring deserialization.

        Returns:
            float if data is not None, otherwise None

        """
        if data is None:
            return None

        try:
            return _struct.unpack('>d', data)[0]
        except _struct.error as e:
            raise SerializationError(str(e))


class IntegerSerializer(Serializer):
    """
    Serializes int to int32 bytes.

    .. _IntegerSerializer:
        https://docs.confluent.io/current/clients/javadocs/org/apache/kafka/common/serialization/IntegerSerializer.html

    """  # noqa: E501
    def __call__(self, obj, ctx):
        """
        Serializes int as int32 bytes.

        Args:
            obj (int): int to be serialized.

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation.

        Note:
            None objects are represented as Kafka Null.

        Raises:
            SerializerError if an error occurs daring serialization

        Returns:
            int32 bytes if obj is not None, else None

        """
        if obj is None:
            return None

        try:
            return _struct.pack('>i', obj)
        except _struct.error as e:
            raise SerializationError(str(e))


class IntegerDeserializer(Deserializer):
    """
    Deserializes int to int32 bytes.

    .._IntegerDeserializer:
        https://docs.confluent.io/current/clients/javadocs/org/apache/kafka/common/serialization/IntegerDeserializer.html

    """  # noqa: E501
    def __call__(self, data, ctx):
        """
        Deserializes int from int32 bytes.

        Args:
            data(bytes): int32 bytes

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation.

        Raises:
            SerializerError if an error occurs daring deserialization.

        Returns:
            int if data is not None, otherwise None

        """
        if data is None:
            return None

        try:
            return _struct.unpack('>i', data)[0]
        except _struct.error as e:
            raise SerializationError(str(e))


class StringSerializer(Serializer):
    """
    Serializes unicode to bytes per the configured codec. Defaults to ``utf_8``.

    Note:
        None objects are represented as Kafka Null.

    Args:
        codec (str, optional): encoding scheme. Defaults to utf_8

    .. _StandardEncodings:
        https://docs.python.org/3/library/codecs.html#standard-encodings

    .. _StringSerializer:
        https://docs.confluent.io/current/clients/javadocs/org/apache/kafka/common/serialization/StringSerializer.html

    """  # noqa: E501
    def __init__(self, codec='utf_8'):
        self.codec = codec

    def __call__(self, obj, ctx):
        """
        Serializes a str(py2:unicode) to bytes.

        Compatibility Note:
            Python 2 str objects must be converted to unicode objects.
            Python 3 all str objects are already unicode objects.

        Args:
            obj (unicode): Unicode object to serialize

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation.
        Raises:
            SerializerError if an error occurs daring serialization.

        Returns:
            serialized bytes if obj is not None, otherwise None

        """
        if obj is None:
            return None

        try:
            return obj.encode(self.codec)
        except _struct.error as e:
            raise SerializationError(str(e))


class StringDeserializer(Deserializer):
    """
    Deserializes a str(py2:unicode) from bytes.

    Args:
        codec (str, optional): encoding scheme. Defaults to utf_8

    .. _Standard Encodings:
        https://docs.python.org/3/library/codecs.html#standard-encodings


    .. _StringDeserializer:
        https://docs.confluent.io/current/clients/javadocs/org/apache/kafka/common/serialization/StringDeserializer.html

    """  # noqa: E501
    def __init__(self, codec='utf_8'):
        self.codec = codec

    def __call__(self, data, ctx):
        """
        Serializes unicode to bytes per the configured codec. Defaults to ``utf_8``.

        Compatibility Note:
            Python 2 str objects must be converted to unicode objects by the
            application prior to using this serializer.

            Python 3 all str objects are already unicode objects.

        Args:
            data (bytes): bytes to be deserialized

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation
        Raises:
            SerializerError if an error occurs during deserialization.

        Returns:
            unicode if data is not None, otherwise None

        """
        if data is None:
            return None

        try:
            return data.decode(self.codec)
        except _struct.error as e:
            raise SerializationError(str(e))
