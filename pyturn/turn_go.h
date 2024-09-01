/* Code generated by cmd/cgo; DO NOT EDIT. */

/* package github.com/pion/turn/v4/pyturn */


#line 1 "cgo-builtin-export-prolog"

#include <stddef.h>

#ifndef GO_CGO_EXPORT_PROLOGUE_H
#define GO_CGO_EXPORT_PROLOGUE_H

#ifndef GO_CGO_GOSTRING_TYPEDEF
typedef struct { const char *p; ptrdiff_t n; } _GoString_;
#endif

#endif

/* Start of preamble from import "C" comments.  */


#line 9 "turn.go"





// #define Py_LIMITED_API // need full API for PyRun*
#include <Python.h>
typedef uint8_t bool;
// static inline is trick for avoiding need for extra .c file
// the following are used for build value -- switch on reflect.Kind
// or the types equivalent
static inline PyObject* gopy_build_bool(uint8_t val) {
	return Py_BuildValue("b", val);
}
static inline PyObject* gopy_build_int64(int64_t val) {
	return Py_BuildValue("k", val);
}
static inline PyObject* gopy_build_uint64(uint64_t val) {
	return Py_BuildValue("K", val);
}
static inline PyObject* gopy_build_float64(double val) {
	return Py_BuildValue("d", val);
}
static inline PyObject* gopy_build_string(const char* val) {
	return Py_BuildValue("s", val);
}
static inline void gopy_decref(PyObject* obj) { // macro
	Py_XDECREF(obj);
}
static inline void gopy_incref(PyObject* obj) { // macro
	Py_XINCREF(obj);
}
static inline int gopy_method_check(PyObject* obj) { // macro
	return PyMethod_Check(obj);
}
static inline void gopy_err_handle() {
	if(PyErr_Occurred() != NULL) {
		PyErr_Print();
	}
}


#line 1 "cgo-generated-wrapper"


/* End of preamble from import "C" comments.  */


/* Start of boilerplate cgo prologue.  */
#line 1 "cgo-gcc-export-header-prolog"

#ifndef GO_CGO_PROLOGUE_H
#define GO_CGO_PROLOGUE_H

typedef signed char GoInt8;
typedef unsigned char GoUint8;
typedef short GoInt16;
typedef unsigned short GoUint16;
typedef int GoInt32;
typedef unsigned int GoUint32;
typedef long long GoInt64;
typedef unsigned long long GoUint64;
typedef GoInt64 GoInt;
typedef GoUint64 GoUint;
typedef size_t GoUintptr;
typedef float GoFloat32;
typedef double GoFloat64;
#ifdef _MSC_VER
#include <complex.h>
typedef _Fcomplex GoComplex64;
typedef _Dcomplex GoComplex128;
#else
typedef float _Complex GoComplex64;
typedef double _Complex GoComplex128;
#endif

/*
  static assertion to make sure the file is being used on architecture
  at least with matching size of GoInt.
*/
typedef char _check_for_64_bit_pointer_matching_GoInt[sizeof(void*)==64/8 ? 1:-1];

#ifndef GO_CGO_GOSTRING_TYPEDEF
typedef _GoString_ GoString;
#endif
typedef void *GoMap;
typedef void *GoChan;
typedef struct { void *t; void *v; } GoInterface;
typedef struct { void *data; GoInt len; GoInt cap; } GoSlice;

#endif

/* End of boilerplate cgo prologue.  */

#ifdef __cplusplus
extern "C" {
#endif

extern void GoPyInit();

// DecRef decrements the reference count for the specified handle
// and deletes it it goes to zero.
//
extern void DecRef(long long handle);

// IncRef increments the reference count for the specified handle.
//
extern void IncRef(long long handle);

// NumHandles returns the number of handles currently in use.
//
extern GoInt NumHandles();

// --- wrapping slice: stun.Attributes ---
//
extern long long stun_Attributes_CTor();
extern GoInt stun_Attributes_len(long long handle);
extern long long stun_Attributes_elem(long long handle, GoInt _idx);
extern long long stun_Attributes_subslice(long long handle, GoInt _st, GoInt _ed);
extern void stun_Attributes_set(long long handle, GoInt _idx, long long _vl);
extern void stun_Attributes_append(long long handle, long long _vl);

// --- wrapping slice: stun.Realm ---
//
extern long long stun_Realm_CTor();
extern GoInt stun_Realm_len(long long handle);
extern char stun_Realm_elem(long long handle, GoInt _idx);
extern long long stun_Realm_subslice(long long handle, GoInt _st, GoInt _ed);
extern void stun_Realm_set(long long handle, GoInt _idx, char _vl);
extern void stun_Realm_append(long long handle, char _vl);

// --- wrapping slice: stun.Username ---
//
extern long long stun_Username_CTor();
extern GoInt stun_Username_len(long long handle);
extern char stun_Username_elem(long long handle, GoInt _idx);
extern long long stun_Username_subslice(long long handle, GoInt _st, GoInt _ed);
extern void stun_Username_set(long long handle, GoInt _idx, char _vl);
extern void stun_Username_append(long long handle, char _vl);

// --- wrapping slice: net.IP ---
//
extern long long net_IP_CTor();
extern GoInt net_IP_len(long long handle);
extern char net_IP_elem(long long handle, GoInt _idx);
extern long long net_IP_subslice(long long handle, GoInt _st, GoInt _ed);
extern void net_IP_set(long long handle, GoInt _idx, char _vl);
extern void net_IP_append(long long handle, char _vl);

// --- wrapping slice: net.IPMask ---
//
extern long long net_IPMask_CTor();
extern GoInt net_IPMask_len(long long handle);
extern char net_IPMask_elem(long long handle, GoInt _idx);
extern long long net_IPMask_subslice(long long handle, GoInt _st, GoInt _ed);
extern void net_IPMask_set(long long handle, GoInt _idx, char _vl);
extern void net_IPMask_append(long long handle, char _vl);

// --- wrapping slice: []bool ---
//
extern long long Slice_bool_CTor();
extern GoInt Slice_bool_len(long long handle);
extern char Slice_bool_elem(long long handle, GoInt _idx);
extern long long Slice_bool_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_bool_set(long long handle, GoInt _idx, char _vl);
extern void Slice_bool_append(long long handle, char _vl);

// --- wrapping slice: []byte ---
//
extern long long Slice_byte_CTor();
extern GoInt Slice_byte_len(long long handle);
extern char Slice_byte_elem(long long handle, GoInt _idx);
extern long long Slice_byte_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_byte_set(long long handle, GoInt _idx, char _vl);
extern void Slice_byte_append(long long handle, char _vl);

// --- wrapping slice: []error ---
//
extern long long Slice_error_CTor();
extern GoInt Slice_error_len(long long handle);
extern char* Slice_error_elem(long long handle, GoInt _idx);
extern long long Slice_error_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_error_set(long long handle, GoInt _idx, char* _vl);
extern void Slice_error_append(long long handle, char* _vl);

// --- wrapping slice: []float32 ---
//
extern long long Slice_float32_CTor();
extern GoInt Slice_float32_len(long long handle);
extern float Slice_float32_elem(long long handle, GoInt _idx);
extern long long Slice_float32_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_float32_set(long long handle, GoInt _idx, float _vl);
extern void Slice_float32_append(long long handle, float _vl);

// --- wrapping slice: []float64 ---
//
extern long long Slice_float64_CTor();
extern GoInt Slice_float64_len(long long handle);
extern double Slice_float64_elem(long long handle, GoInt _idx);
extern long long Slice_float64_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_float64_set(long long handle, GoInt _idx, double _vl);
extern void Slice_float64_append(long long handle, double _vl);

// --- wrapping slice: []int ---
//
extern long long Slice_int_CTor();
extern GoInt Slice_int_len(long long handle);
extern long long Slice_int_elem(long long handle, GoInt _idx);
extern long long Slice_int_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_int_set(long long handle, GoInt _idx, long long _vl);
extern void Slice_int_append(long long handle, long long _vl);

// --- wrapping slice: []int16 ---
//
extern long long Slice_int16_CTor();
extern GoInt Slice_int16_len(long long handle);
extern short Slice_int16_elem(long long handle, GoInt _idx);
extern long long Slice_int16_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_int16_set(long long handle, GoInt _idx, short _vl);
extern void Slice_int16_append(long long handle, short _vl);

// --- wrapping slice: []int32 ---
//
extern long long Slice_int32_CTor();
extern GoInt Slice_int32_len(long long handle);
extern long Slice_int32_elem(long long handle, GoInt _idx);
extern long long Slice_int32_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_int32_set(long long handle, GoInt _idx, long _vl);
extern void Slice_int32_append(long long handle, long _vl);

// --- wrapping slice: []int64 ---
//
extern long long Slice_int64_CTor();
extern GoInt Slice_int64_len(long long handle);
extern long long Slice_int64_elem(long long handle, GoInt _idx);
extern long long Slice_int64_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_int64_set(long long handle, GoInt _idx, long long _vl);
extern void Slice_int64_append(long long handle, long long _vl);

// --- wrapping slice: []int8 ---
//
extern long long Slice_int8_CTor();
extern GoInt Slice_int8_len(long long handle);
extern char Slice_int8_elem(long long handle, GoInt _idx);
extern long long Slice_int8_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_int8_set(long long handle, GoInt _idx, char _vl);
extern void Slice_int8_append(long long handle, char _vl);

// --- wrapping slice: []rune ---
//
extern long long Slice_rune_CTor();
extern GoInt Slice_rune_len(long long handle);
extern long Slice_rune_elem(long long handle, GoInt _idx);
extern long long Slice_rune_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_rune_set(long long handle, GoInt _idx, long _vl);
extern void Slice_rune_append(long long handle, long _vl);

// --- wrapping slice: []string ---
//
extern long long Slice_string_CTor();
extern GoInt Slice_string_len(long long handle);
extern char* Slice_string_elem(long long handle, GoInt _idx);
extern long long Slice_string_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_string_set(long long handle, GoInt _idx, char* _vl);
extern void Slice_string_append(long long handle, char* _vl);

// --- wrapping slice: []uint ---
//
extern long long Slice_uint_CTor();
extern GoInt Slice_uint_len(long long handle);
extern unsigned long long Slice_uint_elem(long long handle, GoInt _idx);
extern long long Slice_uint_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_uint_set(long long handle, GoInt _idx, unsigned long long _vl);
extern void Slice_uint_append(long long handle, unsigned long long _vl);

// --- wrapping slice: []uint16 ---
//
extern long long Slice_uint16_CTor();
extern GoInt Slice_uint16_len(long long handle);
extern unsigned short Slice_uint16_elem(long long handle, GoInt _idx);
extern long long Slice_uint16_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_uint16_set(long long handle, GoInt _idx, unsigned short _vl);
extern void Slice_uint16_append(long long handle, unsigned short _vl);

// --- wrapping slice: []uint32 ---
//
extern long long Slice_uint32_CTor();
extern GoInt Slice_uint32_len(long long handle);
extern unsigned long Slice_uint32_elem(long long handle, GoInt _idx);
extern long long Slice_uint32_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_uint32_set(long long handle, GoInt _idx, unsigned long _vl);
extern void Slice_uint32_append(long long handle, unsigned long _vl);

// --- wrapping slice: []uint64 ---
//
extern long long Slice_uint64_CTor();
extern GoInt Slice_uint64_len(long long handle);
extern unsigned long long Slice_uint64_elem(long long handle, GoInt _idx);
extern long long Slice_uint64_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_uint64_set(long long handle, GoInt _idx, unsigned long long _vl);
extern void Slice_uint64_append(long long handle, unsigned long long _vl);

// --- wrapping slice: []uint8 ---
//
extern long long Slice_uint8_CTor();
extern GoInt Slice_uint8_len(long long handle);
extern unsigned char Slice_uint8_elem(long long handle, GoInt _idx);
extern long long Slice_uint8_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_uint8_set(long long handle, GoInt _idx, unsigned char _vl);
extern void Slice_uint8_append(long long handle, unsigned char _vl);

// --- wrapping slice: [12]byte ---
//
extern long long Array_12_byte_CTor();
extern GoInt Array_12_byte_len(long long handle);
extern char Array_12_byte_elem(long long handle, GoInt _idx);
extern void Array_12_byte_set(long long handle, GoInt _idx, char _vl);

// --- wrapping slice: [16]byte ---
//
extern long long Array_16_byte_CTor();
extern GoInt Array_16_byte_len(long long handle);
extern char Array_16_byte_elem(long long handle, GoInt _idx);
extern void Array_16_byte_set(long long handle, GoInt _idx, char _vl);

// --- wrapping slice: [4]byte ---
//
extern long long Array_4_byte_CTor();
extern GoInt Array_4_byte_len(long long handle);
extern char Array_4_byte_elem(long long handle, GoInt _idx);
extern void Array_4_byte_set(long long handle, GoInt _idx, char _vl);

// --- wrapping slice: []stun.Checker ---
//
extern long long Slice_stun_Checker_CTor();
extern GoInt Slice_stun_Checker_len(long long handle);
extern long long Slice_stun_Checker_elem(long long handle, GoInt _idx);
extern long long Slice_stun_Checker_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_stun_Checker_set(long long handle, GoInt _idx, long long _vl);
extern void Slice_stun_Checker_append(long long handle, long long _vl);

// --- wrapping slice: []stun.Getter ---
//
extern long long Slice_stun_Getter_CTor();
extern GoInt Slice_stun_Getter_len(long long handle);
extern long long Slice_stun_Getter_elem(long long handle, GoInt _idx);
extern long long Slice_stun_Getter_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_stun_Getter_set(long long handle, GoInt _idx, long long _vl);
extern void Slice_stun_Getter_append(long long handle, long long _vl);

// --- wrapping slice: []stun.Setter ---
//
extern long long Slice_stun_Setter_CTor();
extern GoInt Slice_stun_Setter_len(long long handle);
extern long long Slice_stun_Setter_elem(long long handle, GoInt _idx);
extern long long Slice_stun_Setter_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_stun_Setter_set(long long handle, GoInt _idx, long long _vl);
extern void Slice_stun_Setter_append(long long handle, long long _vl);

// --- wrapping slice: []turn.ListenerConfig ---
//
extern long long Slice_turn_ListenerConfig_CTor();
extern GoInt Slice_turn_ListenerConfig_len(long long handle);
extern long long Slice_turn_ListenerConfig_elem(long long handle, GoInt _idx);
extern long long Slice_turn_ListenerConfig_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_turn_ListenerConfig_set(long long handle, GoInt _idx, long long _vl);
extern void Slice_turn_ListenerConfig_append(long long handle, long long _vl);

// --- wrapping slice: []turn.PacketConnConfig ---
//
extern long long Slice_turn_PacketConnConfig_CTor();
extern GoInt Slice_turn_PacketConnConfig_len(long long handle);
extern long long Slice_turn_PacketConnConfig_elem(long long handle, GoInt _idx);
extern long long Slice_turn_PacketConnConfig_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_turn_PacketConnConfig_set(long long handle, GoInt _idx, long long _vl);
extern void Slice_turn_PacketConnConfig_append(long long handle, long long _vl);

// --- wrapping slice: []net.Addr ---
//
extern long long Slice_net_Addr_CTor();
extern GoInt Slice_net_Addr_len(long long handle);
extern long long Slice_net_Addr_elem(long long handle, GoInt _idx);
extern long long Slice_net_Addr_subslice(long long handle, GoInt _st, GoInt _ed);
extern void Slice_net_Addr_set(long long handle, GoInt _idx, long long _vl);
extern void Slice_net_Addr_append(long long handle, long long _vl);
extern char* turn_RelayAddressGenerator_Validate(long long _handle);

// --- wrapping struct: turn.ClientConfig ---
//
extern long long turn_ClientConfig_CTor();
extern char* turn_ClientConfig_STUNServerAddr_Get(long long handle);
extern void turn_ClientConfig_STUNServerAddr_Set(long long handle, char* val);
extern char* turn_ClientConfig_TURNServerAddr_Get(long long handle);
extern void turn_ClientConfig_TURNServerAddr_Set(long long handle, char* val);
extern char* turn_ClientConfig_Username_Get(long long handle);
extern void turn_ClientConfig_Username_Set(long long handle, char* val);
extern char* turn_ClientConfig_Password_Get(long long handle);
extern void turn_ClientConfig_Password_Set(long long handle, char* val);
extern char* turn_ClientConfig_Realm_Get(long long handle);
extern void turn_ClientConfig_Realm_Set(long long handle, char* val);
extern char* turn_ClientConfig_Software_Get(long long handle);
extern void turn_ClientConfig_Software_Set(long long handle, char* val);
extern long long turn_ClientConfig_RTO_Get(long long handle);
extern void turn_ClientConfig_RTO_Set(long long handle, long long val);
extern long long turn_ClientConfig_Conn_Get(long long handle);
extern void turn_ClientConfig_Conn_Set(long long handle, long long val);
extern long long turn_ClientConfig_Net_Get(long long handle);
extern void turn_ClientConfig_Net_Set(long long handle, long long val);
extern long long turn_ClientConfig_LoggerFactory_Get(long long handle);
extern void turn_ClientConfig_LoggerFactory_Set(long long handle, long long val);

// --- wrapping struct: turn.ListenerConfig ---
//
extern long long turn_ListenerConfig_CTor();
extern long long turn_ListenerConfig_Listener_Get(long long handle);
extern void turn_ListenerConfig_Listener_Set(long long handle, long long val);
extern long long turn_ListenerConfig_RelayAddressGenerator_Get(long long handle);
extern void turn_ListenerConfig_RelayAddressGenerator_Set(long long handle, long long val);

// --- wrapping struct: turn.RecievedPacket ---
//
extern long long turn_RecievedPacket_CTor();
extern long long turn_RecievedPacket_N_Get(long long handle);
extern void turn_RecievedPacket_N_Set(long long handle, long long val);
extern long long turn_RecievedPacket_Addr_Get(long long handle);
extern void turn_RecievedPacket_Addr_Set(long long handle, long long val);

// --- wrapping struct: turn.RelayAddressGeneratorPortRange ---
//
extern long long turn_RelayAddressGeneratorPortRange_CTor();
extern long long turn_RelayAddressGeneratorPortRange_RelayAddress_Get(long long handle);
extern void turn_RelayAddressGeneratorPortRange_RelayAddress_Set(long long handle, long long val);
extern unsigned short turn_RelayAddressGeneratorPortRange_MinPort_Get(long long handle);
extern void turn_RelayAddressGeneratorPortRange_MinPort_Set(long long handle, unsigned short val);
extern unsigned short turn_RelayAddressGeneratorPortRange_MaxPort_Get(long long handle);
extern void turn_RelayAddressGeneratorPortRange_MaxPort_Set(long long handle, unsigned short val);
extern long long turn_RelayAddressGeneratorPortRange_MaxRetries_Get(long long handle);
extern void turn_RelayAddressGeneratorPortRange_MaxRetries_Set(long long handle, long long val);
extern long long turn_RelayAddressGeneratorPortRange_Rand_Get(long long handle);
extern void turn_RelayAddressGeneratorPortRange_Rand_Set(long long handle, long long val);
extern char* turn_RelayAddressGeneratorPortRange_Address_Get(long long handle);
extern void turn_RelayAddressGeneratorPortRange_Address_Set(long long handle, char* val);
extern long long turn_RelayAddressGeneratorPortRange_Net_Get(long long handle);
extern void turn_RelayAddressGeneratorPortRange_Net_Set(long long handle, long long val);
extern char* turn_RelayAddressGeneratorPortRange_Validate(long long _handle);

// --- wrapping struct: turn.STUNConn ---
//
extern long long turn_STUNConn_CTor();
extern long long turn_STUNConn_WriteTo(long long _handle, long long p, long long q);
extern char* turn_STUNConn_Close(long long _handle);
extern long long turn_STUNConn_LocalAddr(long long _handle);
extern char* turn_STUNConn_SetDeadline(long long _handle, long long t);
extern char* turn_STUNConn_SetReadDeadline(long long _handle, long long t);
extern char* turn_STUNConn_SetWriteDeadline(long long _handle, long long t);

// --- wrapping struct: turn.ServerConfig ---
//
extern long long turn_ServerConfig_CTor();
extern long long turn_ServerConfig_PacketConnConfigs_Get(long long handle);
extern void turn_ServerConfig_PacketConnConfigs_Set(long long handle, long long val);
extern long long turn_ServerConfig_ListenerConfigs_Get(long long handle);
extern void turn_ServerConfig_ListenerConfigs_Set(long long handle, long long val);
extern long long turn_ServerConfig_LoggerFactory_Get(long long handle);
extern void turn_ServerConfig_LoggerFactory_Set(long long handle, long long val);
extern char* turn_ServerConfig_Realm_Get(long long handle);
extern void turn_ServerConfig_Realm_Set(long long handle, char* val);
extern long long turn_ServerConfig_ChannelBindTimeout_Get(long long handle);
extern void turn_ServerConfig_ChannelBindTimeout_Set(long long handle, long long val);
extern long long turn_ServerConfig_InboundMTU_Get(long long handle);
extern void turn_ServerConfig_InboundMTU_Set(long long handle, long long val);

// --- wrapping struct: turn.Client ---
//
extern long long turn_Client_CTor();
extern long long turn_Client_TURNServerAddr(long long _handle);
extern long long turn_Client_STUNServerAddr(long long _handle);
extern long long turn_Client_Username(long long _handle);
extern long long turn_Client_Realm(long long _handle);
extern long long turn_Client_WriteTo(long long _handle, long long data, long long to);
extern char* turn_Client_Listen(long long _handle);
extern void turn_Client_Close(long long _handle, char goRun);
extern long long turn_Client_SendBindingRequestTo(long long _handle, long long to);
extern long long turn_Client_SendBindingRequest(long long _handle);
extern long long turn_Client_Allocate(long long _handle);
extern long long turn_Client_AllocateTCP(long long _handle);
extern char* turn_Client_CreatePermission(long long _handle, long long addrs);
extern long long turn_Client_PerformTransaction(long long _handle, long long msg, long long to, char ignoreResult);
extern void turn_Client_OnDeallocated(long long _handle, long long arg_0, char goRun);
extern char turn_Client_HandleInbound(long long _handle, long long data, long long myfrom);

// --- wrapping struct: turn.RelayAddressGeneratorNone ---
//
extern long long turn_RelayAddressGeneratorNone_CTor();
extern char* turn_RelayAddressGeneratorNone_Address_Get(long long handle);
extern void turn_RelayAddressGeneratorNone_Address_Set(long long handle, char* val);
extern long long turn_RelayAddressGeneratorNone_Net_Get(long long handle);
extern void turn_RelayAddressGeneratorNone_Net_Set(long long handle, long long val);
extern char* turn_RelayAddressGeneratorNone_Validate(long long _handle);

// --- wrapping struct: turn.RelayAddressGeneratorStatic ---
//
extern long long turn_RelayAddressGeneratorStatic_CTor();
extern long long turn_RelayAddressGeneratorStatic_RelayAddress_Get(long long handle);
extern void turn_RelayAddressGeneratorStatic_RelayAddress_Set(long long handle, long long val);
extern char* turn_RelayAddressGeneratorStatic_Address_Get(long long handle);
extern void turn_RelayAddressGeneratorStatic_Address_Set(long long handle, char* val);
extern long long turn_RelayAddressGeneratorStatic_Net_Get(long long handle);
extern void turn_RelayAddressGeneratorStatic_Net_Set(long long handle, long long val);
extern char* turn_RelayAddressGeneratorStatic_Validate(long long _handle);

// --- wrapping struct: turn.Server ---
//
extern long long turn_Server_CTor();
extern long long turn_Server_AllocationCount(long long _handle);
extern char* turn_Server_Close(long long _handle);

// --- wrapping struct: turn.PacketConnConfig ---
//
extern long long turn_PacketConnConfig_CTor();
extern long long turn_PacketConnConfig_PacketConn_Get(long long handle);
extern void turn_PacketConnConfig_PacketConn_Set(long long handle, long long val);
extern long long turn_PacketConnConfig_RelayAddressGenerator_Get(long long handle);
extern void turn_PacketConnConfig_RelayAddressGenerator_Set(long long handle, long long val);
extern long long turn_NetConnReadFrom(long long conn, long long p);
extern long long turn_NewSTUNConn(long long nextConn);
extern long long turn_NewClient(long long config);
extern long long turn_NewServer(long long config);
extern long long turn_NetResolveUDPAddr(char* network, char* address);
extern char turn_DefaultPermissionHandler(long long arg_0, long long arg_1);
extern long long turn_GenerateAuthKey(char* username, char* realm, char* password);
extern long long turn_NetConnGetLocalAddr(long long conn);
extern char* turn_NetConnSetTimeout(long long conn, long long sec);
extern long long turn_NetConnWriteTo(long long conn, long long p, long long addr);
extern long long turn_NetListenPacket(char* network, char* address);
extern char* turn_NetAddrString(long long addr);
extern char* turn_NetConnClose(long long conn);
extern char* turn_NetUDPAddrChangePort(long long addr, long long port);

#ifdef __cplusplus
}
#endif