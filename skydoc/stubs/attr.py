# Copyright 2016 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# internal imports
from skydoc import build_pb2


def strcmp(s1, s2):
  if s1 > s2:
    return 1
  elif s1 < s2:
    return -1
  else:
    return 0


def attr_compare(a, b):
  if a.compare_priority() > b.compare_priority():
    return 1
  elif a.compare_priority() < b.compare_priority():
    return -1
  else:
    return strcmp(a.name, b.name)


class AttrDescriptor(object):
  ATTRIBUTE_ORDERING = {
      "name": -99,
      "deps": -98,
      "src": -97,
      "srcs": -86,
      "data": -95,
      "resource": -94,
      "resources": -93,
      "out": -92,
      "outs": -91,
      "hdrs": -90,
  }

  def __init__(self,
               type=build_pb2.Attribute.UNKNOWN,
               default=None,
               mandatory=False,
               doc="",
               name=""):
    """Constructor for AttrDescriptor

    Args:
      self: The current instance
      type: The type of attribute based on the enum in the Attribute proto.
      default: The default value of the attribute.
      mandatory: True if the attribute is required, false if optional.
      doc: Documentation for this attribute. This parameter is used internally
        by skydoc and is not set by any Skylark code in .bzl files.
      name: Name of this attribute. This parameter is used internally by skydoc
        and is not set by any Skylark code in .bzl files.
    """
    self.type = type
    self.default = default
    self.mandatory = mandatory
    self.doc = doc
    self.name = name

  def compare_priority(self):
    if self.name in AttrDescriptor.ATTRIBUTE_ORDERING:
      return AttrDescriptor.ATTRIBUTE_ORDERING[self.name]
    else:
      return 0


def bool(default=False, mandatory=False, doc=""):
  return AttrDescriptor(
      build_pb2.Attribute.BOOLEAN, default=repr(default), mandatory=mandatory, doc=doc)


def int(default=0, mandatory=False, values=[], doc=""):
  return AttrDescriptor(build_pb2.Attribute.INTEGER, repr(default), mandatory, doc=doc)


def int_list(default=[], mandatory=False, non_empty=False, allow_empty=True, doc=""):
  return AttrDescriptor(build_pb2.Attribute.INTEGER_LIST, repr(default),
                        mandatory, doc)


def label(default=None,
          executable=False,
          allow_files=False,
          allow_single_file=False,
          mandatory=False,
          providers=[],
          allow_rules=None,
          single_file=False,
          cfg=None,
          aspects=[],
          doc=""):
  if default != None:
    default = repr(default)
  return AttrDescriptor(build_pb2.Attribute.LABEL, default, mandatory, doc)


def label_list(default=[],
               allow_files=False,
               allow_rules=None,
               providers=[],
               flags=[],
               mandatory=False,
               non_empty=False,
               allow_empty=True,
               cfg=None,
               aspects=[],
               doc=""):
  default_val = []
  for label in default:
    default_val.append(repr(label))
  return AttrDescriptor(build_pb2.Attribute.LABEL_LIST, repr(default_val),
                        mandatory, doc)


def license(default=None, mandatory=False, doc=""):
  if default != None:
    default = repr(default)
  return AttrDescriptor(build_pb2.Attribute.LICENSE, default, mandatory, doc)


def output(default=None, mandatory=False, doc=""):
  if default != None:
    default = repr(default)
  return AttrDescriptor(build_pb2.Attribute.OUTPUT, default, mandatory, doc)


def output_list(default=[], mandatory=False, non_empty=False, allow_empty=True, doc=""):
  default_val = []
  for label in default:
    default_val.append(repr(label))
  return AttrDescriptor(build_pb2.Attribute.OUTPUT_LIST, repr(default_val),
                        mandatory, doc)


def string(default="", mandatory=False, values=[], doc=""):
  return AttrDescriptor(build_pb2.Attribute.STRING, repr(default), mandatory, doc)


def string_dict(default={},
                mandatory=False,
                non_empty=False,
                allow_empty=True,
                doc=""):
  return AttrDescriptor(build_pb2.Attribute.STRING_DICT, repr(default),
                        mandatory, doc)


def string_list(default=[],
                mandatory=False,
                non_empty=False,
                allow_empty=True,
                doc=""):
  return AttrDescriptor(build_pb2.Attribute.STRING_LIST, repr(default),
                        mandatory, doc)


def string_list_dict(default={},
                     mandatory=False,
                     non_empty=False,
                     allow_empty=True,
                     doc=""):
  return AttrDescriptor(build_pb2.Attribute.STRING_LIST_DICT, repr(default),
                        mandatory, doc)

def label_keyed_string_dict(default={},
                            mandatory=False,
                            allow_files=False,
                            non_empty=False,
                            allow_empty=True,
                            doc=""):
  return AttrDescriptor(build_pb2.Attribute.LABEL_KEYED_STRING_DICT, repr(default),
                        mandatory, doc)
