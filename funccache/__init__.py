"""
True to its name, `funccache` implements the cache function. Cache the return
value of a callable object or all methods defined in a class.

    >>> import funccache

    >>> class Alpha(metaclass=funccache):
    >>>     ...

    >>> @funccache
    >>> def alpha():
    >>>     ...

    @version: 1.4.0
    @author: 竹永康 <gqylpy@outlook.com>
    @source: https://github.com/gqylpy/funccache

────────────────────────────────────────────────────────────────────────────────
Copyright (c) 2022, 2023 GQYLPY <http://gqylpy.com>. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


class _xe6_xad_x8c_xe7_x90_xaa_xe6_x80_xa1_xe7_x8e_xb2_xe8_x90_x8d_xe4_xba_x91:
    import sys

    __import__(f'{__name__}.i {__name__}')
    gcode = globals()[f'i {__name__}']

    for gname, gvalue in globals().items():
        if gname[:2] == '__' and gname != '__builtins__':
            setattr(gcode.FuncCache, gname, gvalue)

    gcode.FuncCache.__module__ = __package__
    gcode.FuncCache.FuncCache = gcode.FuncCache

    sys.modules[__name__] = gcode.FuncCache
