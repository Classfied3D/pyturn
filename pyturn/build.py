# python build stubs for package turn
# File is generated by gopy. Do not edit.
# gopy build --output=pyturn -vm=python3 .

from pybindgen import retval, param, Function, Module
import sys

class CheckedFunction(Function):
    def __init__(self, *a, **kw):
        super(CheckedFunction, self).__init__(*a, **kw)
        self._failure_expression = kw.get('failure_expression', '')
        self._failure_cleanup = kw.get('failure_cleanup', '')

    def set_failure_expression(self, expr):
        self._failure_expression = expr

    def set_failure_cleanup(self, expr):
        self._failure_cleanup = expr

    def generate_call(self):
        super(CheckedFunction, self).generate_call()
        check = "PyErr_Occurred()"
        if self._failure_expression:
            check = "{} && {}".format(self._failure_expression, check)
        failure_cleanup = self._failure_cleanup or None
        self.before_call.write_error_check(check, failure_cleanup)

def add_checked_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

def add_checked_string_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_cleanup('if (retval != NULL) free(retval);')
    fn.after_call.add_cleanup_code('free(retval);')
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

mod = Module('_turn')
mod.add_include('"turn_go.h"')
mod.add_function('GoPyInit', None, [])
mod.add_function('DecRef', None, [param('int64_t', 'handle')])
mod.add_function('IncRef', None, [param('int64_t', 'handle')])
mod.add_function('NumHandles', retval('int'), [])
mod.add_function('stun_Attributes_CTor', retval('int64_t'), [])
mod.add_function('stun_Attributes_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('stun_Attributes_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('stun_Attributes_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('stun_Attributes_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('stun_Attributes_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('stun_Realm_CTor', retval('int64_t'), [])
mod.add_function('stun_Realm_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('stun_Realm_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('stun_Realm_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('stun_Realm_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('stun_Realm_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('stun_Username_CTor', retval('int64_t'), [])
mod.add_function('stun_Username_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('stun_Username_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('stun_Username_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('stun_Username_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('stun_Username_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('net_IP_CTor', retval('int64_t'), [])
mod.add_function('net_IP_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('net_IP_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('net_IP_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('net_IP_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('net_IP_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('net_IPMask_CTor', retval('int64_t'), [])
mod.add_function('net_IPMask_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('net_IPMask_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('net_IPMask_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('net_IPMask_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('net_IPMask_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_bool_CTor', retval('int64_t'), [])
mod.add_function('Slice_bool_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_bool_elem', retval('bool'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_bool_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_bool_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('bool', 'value')])
mod.add_function('Slice_bool_append', None, [param('int64_t', 'handle'), param('bool', 'value')])
mod.add_function('Slice_byte_CTor', retval('int64_t'), [])
mod.add_function('Slice_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_byte_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_byte_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_error_CTor', retval('int64_t'), [])
mod.add_function('Slice_error_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_error_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_error_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_error_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_error_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_float32_CTor', retval('int64_t'), [])
mod.add_function('Slice_float32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float32_elem', retval('float'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('float', 'value')])
mod.add_function('Slice_float32_append', None, [param('int64_t', 'handle'), param('float', 'value')])
mod.add_function('Slice_float64_CTor', retval('int64_t'), [])
mod.add_function('Slice_float64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float64_elem', retval('double'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('double', 'value')])
mod.add_function('Slice_float64_append', None, [param('int64_t', 'handle'), param('double', 'value')])
mod.add_function('Slice_int_CTor', retval('int64_t'), [])
mod.add_function('Slice_int_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int16_CTor', retval('int64_t'), [])
mod.add_function('Slice_int16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int16_elem', retval('int16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int16_t', 'value')])
mod.add_function('Slice_int16_append', None, [param('int64_t', 'handle'), param('int16_t', 'value')])
mod.add_function('Slice_int32_CTor', retval('int64_t'), [])
mod.add_function('Slice_int32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int32_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_int32_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_int64_CTor', retval('int64_t'), [])
mod.add_function('Slice_int64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int64_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int64_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int8_CTor', retval('int64_t'), [])
mod.add_function('Slice_int8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int8_elem', retval('int8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int8_t', 'value')])
mod.add_function('Slice_int8_append', None, [param('int64_t', 'handle'), param('int8_t', 'value')])
mod.add_function('Slice_rune_CTor', retval('int64_t'), [])
mod.add_function('Slice_rune_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_rune_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_rune_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_rune_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_rune_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_string_CTor', retval('int64_t'), [])
mod.add_function('Slice_string_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_string_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_string_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_string_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_string_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_uint_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint16_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint16_elem', retval('uint16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint16_t', 'value')])
mod.add_function('Slice_uint16_append', None, [param('int64_t', 'handle'), param('uint16_t', 'value')])
mod.add_function('Slice_uint32_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint32_elem', retval('uint32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint32_t', 'value')])
mod.add_function('Slice_uint32_append', None, [param('int64_t', 'handle'), param('uint32_t', 'value')])
mod.add_function('Slice_uint64_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint64_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint64_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint8_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint8_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_uint8_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Array_12_byte_CTor', retval('int64_t'), [])
mod.add_function('Array_12_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Array_12_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Array_12_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Array_16_byte_CTor', retval('int64_t'), [])
mod.add_function('Array_16_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Array_16_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Array_16_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Array_4_byte_CTor', retval('int64_t'), [])
mod.add_function('Array_4_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Array_4_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Array_4_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_stun_Checker_CTor', retval('int64_t'), [])
mod.add_function('Slice_stun_Checker_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_stun_Checker_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_stun_Checker_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_stun_Checker_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_stun_Checker_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_stun_Getter_CTor', retval('int64_t'), [])
mod.add_function('Slice_stun_Getter_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_stun_Getter_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_stun_Getter_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_stun_Getter_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_stun_Getter_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_stun_Setter_CTor', retval('int64_t'), [])
mod.add_function('Slice_stun_Setter_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_stun_Setter_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_stun_Setter_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_stun_Setter_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_stun_Setter_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_turn_ListenerConfig_CTor', retval('int64_t'), [])
mod.add_function('Slice_turn_ListenerConfig_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_turn_ListenerConfig_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_turn_ListenerConfig_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_turn_ListenerConfig_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_turn_ListenerConfig_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_turn_PacketConnConfig_CTor', retval('int64_t'), [])
mod.add_function('Slice_turn_PacketConnConfig_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_turn_PacketConnConfig_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_turn_PacketConnConfig_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_turn_PacketConnConfig_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_turn_PacketConnConfig_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_net_Addr_CTor', retval('int64_t'), [])
mod.add_function('Slice_net_Addr_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_net_Addr_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_net_Addr_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_net_Addr_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_net_Addr_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
add_checked_function(mod, 'turn_RelayAddressGenerator_Validate', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('turn_PacketConnConfig_CTor', retval('int64_t'), [])
mod.add_function('turn_PacketConnConfig_PacketConn_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_PacketConnConfig_PacketConn_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_PacketConnConfig_RelayAddressGenerator_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_PacketConnConfig_RelayAddressGenerator_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_RecievedPacket_CTor', retval('int64_t'), [])
mod.add_function('turn_RecievedPacket_N_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RecievedPacket_N_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_RecievedPacket_Addr_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RecievedPacket_Addr_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_RelayAddressGeneratorPortRange_CTor', retval('int64_t'), [])
mod.add_function('turn_RelayAddressGeneratorPortRange_RelayAddress_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorPortRange_RelayAddress_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_RelayAddressGeneratorPortRange_MinPort_Get', retval('uint16_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorPortRange_MinPort_Set', None, [param('int64_t', 'handle'), param('uint16_t', 'val')])
mod.add_function('turn_RelayAddressGeneratorPortRange_MaxPort_Get', retval('uint16_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorPortRange_MaxPort_Set', None, [param('int64_t', 'handle'), param('uint16_t', 'val')])
mod.add_function('turn_RelayAddressGeneratorPortRange_MaxRetries_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorPortRange_MaxRetries_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_RelayAddressGeneratorPortRange_Rand_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorPortRange_Rand_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_RelayAddressGeneratorPortRange_Address_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorPortRange_Address_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_RelayAddressGeneratorPortRange_Net_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorPortRange_Net_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'turn_RelayAddressGeneratorPortRange_Validate', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('turn_RelayAddressGeneratorStatic_CTor', retval('int64_t'), [])
mod.add_function('turn_RelayAddressGeneratorStatic_RelayAddress_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorStatic_RelayAddress_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_RelayAddressGeneratorStatic_Address_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorStatic_Address_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_RelayAddressGeneratorStatic_Net_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorStatic_Net_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'turn_RelayAddressGeneratorStatic_Validate', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('turn_ServerConfig_CTor', retval('int64_t'), [])
mod.add_function('turn_ServerConfig_PacketConnConfigs_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ServerConfig_PacketConnConfigs_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ServerConfig_ListenerConfigs_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ServerConfig_ListenerConfigs_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ServerConfig_LoggerFactory_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ServerConfig_LoggerFactory_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ServerConfig_Realm_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_ServerConfig_Realm_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_ServerConfig_ChannelBindTimeout_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ServerConfig_ChannelBindTimeout_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ServerConfig_InboundMTU_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ServerConfig_InboundMTU_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ClientConfig_CTor', retval('int64_t'), [])
mod.add_function('turn_ClientConfig_STUNServerAddr_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_STUNServerAddr_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_ClientConfig_TURNServerAddr_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_TURNServerAddr_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_ClientConfig_Username_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_Username_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_ClientConfig_Password_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_Password_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_ClientConfig_Realm_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_Realm_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_ClientConfig_Software_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_Software_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_ClientConfig_RTO_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_RTO_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ClientConfig_Conn_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_Conn_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ClientConfig_Net_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_Net_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ClientConfig_LoggerFactory_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ClientConfig_LoggerFactory_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ListenerConfig_CTor', retval('int64_t'), [])
mod.add_function('turn_ListenerConfig_Listener_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ListenerConfig_Listener_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_ListenerConfig_RelayAddressGenerator_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_ListenerConfig_RelayAddressGenerator_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('turn_RelayAddressGeneratorNone_CTor', retval('int64_t'), [])
mod.add_function('turn_RelayAddressGeneratorNone_Address_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorNone_Address_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('turn_RelayAddressGeneratorNone_Net_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('turn_RelayAddressGeneratorNone_Net_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'turn_RelayAddressGeneratorNone_Validate', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('turn_STUNConn_CTor', retval('int64_t'), [])
add_checked_function(mod, 'turn_STUNConn_WriteTo', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'p'), param('int64_t', '_')])
add_checked_function(mod, 'turn_STUNConn_Close', retval('char*'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_STUNConn_LocalAddr', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_STUNConn_SetDeadline', retval('char*'), [param('int64_t', '_handle'), param('int64_t', 't')])
add_checked_function(mod, 'turn_STUNConn_SetReadDeadline', retval('char*'), [param('int64_t', '_handle'), param('int64_t', 't')])
add_checked_function(mod, 'turn_STUNConn_SetWriteDeadline', retval('char*'), [param('int64_t', '_handle'), param('int64_t', 't')])
mod.add_function('turn_Server_CTor', retval('int64_t'), [])
add_checked_function(mod, 'turn_Server_AllocationCount', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Server_Close', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('turn_Client_CTor', retval('int64_t'), [])
add_checked_function(mod, 'turn_Client_TURNServerAddr', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Client_STUNServerAddr', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Client_Username', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Client_Realm', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Client_WriteTo', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'data'), param('int64_t', 'to')])
add_checked_function(mod, 'turn_Client_Listen', retval('char*'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Client_Close', None, [param('int64_t', '_handle'), param('bool', 'goRun')])
add_checked_function(mod, 'turn_Client_SendBindingRequestTo', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'to')])
add_checked_function(mod, 'turn_Client_SendBindingRequest', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Client_Allocate', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Client_AllocateTCP', retval('int64_t'), [param('int64_t', '_handle')])
add_checked_function(mod, 'turn_Client_CreatePermission', retval('char*'), [param('int64_t', '_handle'), param('int64_t', 'addrs')])
add_checked_function(mod, 'turn_Client_PerformTransaction', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'msg'), param('int64_t', 'to'), param('bool', 'ignoreResult')])
add_checked_function(mod, 'turn_Client_OnDeallocated', None, [param('int64_t', '_handle'), param('int64_t', 'arg_0'), param('bool', 'goRun')])
add_checked_function(mod, 'turn_Client_HandleInbound', retval('bool'), [param('int64_t', '_handle'), param('int64_t', 'data'), param('int64_t', 'myfrom')])
add_checked_function(mod, 'turn_NetConnReadFrom', retval('int64_t'), [param('int64_t', 'conn'), param('int64_t', 'p')])
add_checked_function(mod, 'turn_NewSTUNConn', retval('int64_t'), [param('int64_t', 'nextConn')])
add_checked_function(mod, 'turn_NewServer', retval('int64_t'), [param('int64_t', 'config')])
add_checked_function(mod, 'turn_NewClient', retval('int64_t'), [param('int64_t', 'config')])
add_checked_function(mod, 'turn_DefaultPermissionHandler', retval('bool'), [param('int64_t', 'arg_0'), param('int64_t', 'arg_1')])
add_checked_function(mod, 'turn_NetConnGetLocalAddr', retval('int64_t'), [param('int64_t', 'conn')])
add_checked_function(mod, 'turn_NetConnWriteTo', retval('int64_t'), [param('int64_t', 'conn'), param('int64_t', 'p'), param('int64_t', 'addr')])
add_checked_function(mod, 'turn_NetResolveUDPAddr', retval('int64_t'), [param('char*', 'network'), param('char*', 'address')])
add_checked_function(mod, 'turn_NetConnSetTimeout', retval('char*'), [param('int64_t', 'conn'), param('int64_t', 'sec')])
add_checked_function(mod, 'turn_GenerateAuthKey', retval('int64_t'), [param('char*', 'username'), param('char*', 'realm'), param('char*', 'password')])
add_checked_string_function(mod, 'turn_NetAddrString', retval('char*'), [param('int64_t', 'addr')])
add_checked_function(mod, 'turn_NetConnClose', retval('char*'), [param('int64_t', 'conn')])
add_checked_function(mod, 'turn_NetListenPacket', retval('int64_t'), [param('char*', 'network'), param('char*', 'address')])
add_checked_function(mod, 'turn_NetUDPAddrChangePort', retval('char*'), [param('int64_t', 'addr'), param('int64_t', 'port')])

mod.generate(open('turn.c', 'w'))

