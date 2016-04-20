csv2vcd
=======

Signal analyzer CSV to IEEE 1364-2001 VCD file format converter.

This small scripts allows to convert CSV sampling outputs from several signal
analyzers to IEEE 1364-2001 VCD. Value Change Dump is the format used by
GtkWave http://gtkwave.sourceforge.net/.

Note: Currently there is 3 executables, the main supports integer variables,
      another supports real variables, and the last one supports vector
      variables.

Usage
-----

    csv2vcd [input csv] [output vcd]

Example files can be found in the ``examples`` folder.

License
-------

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

Improvements
------------

- Merge all executables to support integer, real and vector variables with the
  same codebase.
- Allow to setup CSV input clock resolution in the command line.
