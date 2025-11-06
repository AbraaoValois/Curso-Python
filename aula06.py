# conversão de tipos, coerção
# type convertion, type casting, coercion
# é um ato de converter um tipo de dado em outro tipo de dado
# tipos imutáveis (imutability) e primitivos em Python:
# int, float, bool, str

# convertendo int para float
num_int = 10
print( type(num_int) )  # <class 'int'>
num_float = float(num_int)
print( num_float )       # 10.0
print( type(num_float) )  # <class 'float'>

# convertendo float para int
num_float2 = 3.14
print( type(num_float2) )  # <class 'float'>
num_int2 = int(num_float2)
print( num_int2 )         # 3
print( type(num_int2) )   # <class 'int'>

# convertendo int para str
num_int3 = 42
print( type(num_int3) )   # <class 'int'>

num_str = str(num_int3)
print( num_str )          # '42'
print( type(num_str) )    # <class 'str'>

# convertendo str para int
num_str2 = "100"
print( type(num_str2) )   # <class 'str'>
num_int4 = int(num_str2)
print( num_int4 )         # 100
print( type(num_int4) )   # <class 'int'>

# convertendo float para str
num_float3 = 2.71
print( type(num_float3) )  # <class 'float'>
num_str2 = str(num_float3)
print( num_str2 )         # '2.71'
print( type(num_str2) )    # <class 'str'>

# convertendo str para float
num_str3 = "3.14"
print( type(num_str3) )    # <class 'str'>
num_float4 = float(num_str3)
print( num_float4 )        # 3.14
print( type(num_float4) )   # <class 'float'>

# convertendo bool para int
bool_var = True
print( type(bool_var) )    # <class 'bool'>
int_from_bool = int(bool_var)
print( int_from_bool )     # 1
print( type(int_from_bool) )  # <class 'int'>

# convertendo int para bool
int_var = 0
print( type(int_var) )     # <class 'int'>
bool_from_int = bool(int_var)
print( bool_from_int )      # False
print( type(bool_from_int) )  # <class 'bool'>

# convertendo bool para str
bool_var2 = False
print( type(bool_var2) )    # <class 'bool'>
str_from_bool = str(bool_var2)
print( str_from_bool )      # 'False'
print( type(str_from_bool) )  # <class 'str'>

# convertendo str para bool
str_var = ""
print( type(str_var) )      # <class 'str'>
bool_from_str = bool(str_var)
print( bool_from_str )       # False
print( type(bool_from_str) )   # <class 'bool'>

# convertendo float para bool
float_var = 0.0
print( type(float_var) )     # <class 'float'>
bool_from_float = bool(float_var)
print( bool_from_float )      # False
print( type(bool_from_float) )   # <class 'bool'>



