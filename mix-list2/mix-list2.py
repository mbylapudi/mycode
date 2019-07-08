#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['1', '2', '3']
print(proto)
print(protoa)
proto.append('dns')
print(proto)
proto.append('dns')
protoa.append('dns')
print('proto')
proto2 = [11,22,33,44]
protoa.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)
