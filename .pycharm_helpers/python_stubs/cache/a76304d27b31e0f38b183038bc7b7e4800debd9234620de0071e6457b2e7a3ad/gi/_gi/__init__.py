# encoding: utf-8
# module gi._gi
# from /usr/lib/python3/dist-packages/gi/_gi.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
from gobject import (GBoxed, GEnum, GFlags, GInterface, GParamSpec, GPointer, 
    GType, Warning)

import gi as __gi
import gobject as __gobject


# Variables with simple values

G_MAXDOUBLE = 1.7976931348623157e+308
G_MAXFLOAT = 3.4028234663852886e+38
G_MAXINT = 2147483647
G_MAXLONG = 9223372036854775807
G_MAXOFFSET = 9223372036854775807
G_MAXSHORT = 32767
G_MAXSIZE = 18446744073709551615
G_MAXSSIZE = 9223372036854775807
G_MAXUINT = 4294967295
G_MAXULONG = 18446744073709551615
G_MAXUSHORT = 65535
G_MINDOUBLE = 2.2250738585072014e-308
G_MINFLOAT = 1.1754943508222875e-38
G_MININT = -2147483648
G_MINLONG = -9223372036854775808
G_MINOFFSET = -9223372036854775808
G_MINSHORT = -32768
G_MINSSIZE = -9223372036854775808

PARAM_READWRITE = 3

SIGNAL_RUN_FIRST = 1

# functions

def add_emission_hook(*args, **kwargs): # real signature unknown
    pass

def enum_add(*args, **kwargs): # real signature unknown
    pass

def enum_register_new_gtype_and_add(*args, **kwargs): # real signature unknown
    pass

def flags_add(*args, **kwargs): # real signature unknown
    pass

def flags_register_new_gtype_and_add(*args, **kwargs): # real signature unknown
    pass

def hook_up_vfunc_implementation(*args, **kwargs): # real signature unknown
    pass

def io_channel_read(*args, **kwargs): # real signature unknown
    pass

def list_properties(*args, **kwargs): # real signature unknown
    pass

def new(*args, **kwargs): # real signature unknown
    pass

def register_interface_info(*args, **kwargs): # real signature unknown
    pass

def require_foreign(*args, **kwargs): # real signature unknown
    pass

def signal_accumulator_true_handled(*args, **kwargs): # real signature unknown
    pass

def signal_new(*args, **kwargs): # real signature unknown
    pass

def source_new(*args, **kwargs): # real signature unknown
    pass

def source_set_callback(*args, **kwargs): # real signature unknown
    pass

def spawn_async(argv, envp=None, working_directory=None, flags=0, child_setup=None, user_data=None, standard_input=None, standard_output=None, standard_error=None): # real signature unknown; restored from __doc__
    """
    spawn_async(argv, envp=None, working_directory=None,
                flags=0, child_setup=None, user_data=None,
                standard_input=None, standard_output=None,
                standard_error=None) -> (pid, stdin, stdout, stderr)
    
    Execute a child program asynchronously within a glib.MainLoop()
    See the reference manual for a complete reference.
    """
    pass

def type_from_name(*args, **kwargs): # real signature unknown
    pass

def type_is_a(*args, **kwargs): # real signature unknown
    pass

def type_name(*args, **kwargs): # real signature unknown
    pass

def type_register(*args, **kwargs): # real signature unknown
    pass

def variant_type_from_string(*args, **kwargs): # real signature unknown
    pass

def _gvalue_get(*args, **kwargs): # real signature unknown
    pass

def _gvalue_set(*args, **kwargs): # real signature unknown
    pass

def _install_metaclass(*args, **kwargs): # real signature unknown
    pass

# classes

from .BaseInfo import BaseInfo
from .ArgInfo import ArgInfo
from .ArrayType import ArrayType
from .Boxed import Boxed
from .CallableInfo import CallableInfo
from .CallbackInfo import CallbackInfo
from .CCallback import CCallback
from .ConstantInfo import ConstantInfo
from .Direction import Direction
from .RegisteredTypeInfo import RegisteredTypeInfo
from .EnumInfo import EnumInfo
from .ErrorDomainInfo import ErrorDomainInfo
from .FieldInfo import FieldInfo
from .FieldInfoFlags import FieldInfoFlags
from .FunctionInfo import FunctionInfo
from .FunctionInfoFlags import FunctionInfoFlags
from .GObject import GObject
from .GObjectWeakRef import GObjectWeakRef
from .InfoType import InfoType
from .InterfaceInfo import InterfaceInfo
from .ObjectInfo import ObjectInfo
from .OptionContext import OptionContext
from .OptionGroup import OptionGroup
from .Pid import Pid
from .PropertyInfo import PropertyInfo
from .PyGIDeprecationWarning import PyGIDeprecationWarning
from .PyGIWarning import PyGIWarning
from .Repository import Repository
from .RepositoryError import RepositoryError
from .ResultTuple import ResultTuple
from .ScopeType import ScopeType
from .SignalInfo import SignalInfo
from .Struct import Struct
from .StructInfo import StructInfo
from .Transfer import Transfer
from .TypeInfo import TypeInfo
from .TypeTag import TypeTag
from .UnionInfo import UnionInfo
from .UnresolvedInfo import UnresolvedInfo
from .ValueInfo import ValueInfo
from .VFuncInfo import VFuncInfo
from .VFuncInfoFlags import VFuncInfoFlags
# variables with complex values

features = {
    'generic-c-marshaller': True,
}

pygobject_version = (
    3,
    26,
    1,
)

TYPE_GSTRING = None # (!) real value is '<GType GString (19248096)>'

TYPE_INVALID = None # (!) real value is '<GType invalid (0)>'

_API = None # (!) real value is '<capsule object "gi._API" at 0x7efebb7d1330>'

_PyGObject_API = None # (!) real value is '<capsule object "gobject._PyGObject_API" at 0x7efebb7d12d0>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7efebb2e3518>'

__spec__ = None # (!) real value is "ModuleSpec(name='gi._gi', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7efebb2e3518>, origin='/usr/lib/python3/dist-packages/gi/_gi.cpython-36m-x86_64-linux-gnu.so')"

