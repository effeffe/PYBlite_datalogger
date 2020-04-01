# PYBoard lite_datalogger
Datalogger for a magnetometer out of a MicroPython PYBoard lite 1.0 board and a TI DRV5055A1
The data are acquired over two input channels for 4 seconds, running at 5KHz each.
The output is given in two csv files, with 20000 entries, one every 0.2ms. The voltage is given as well, written in a separate file and measured in mV.

This datalogger has been built to be used in a 2nd year Physics project about the Thomson jumping ring experiment.
It samples the magnetic field on two probes, which where used perpendicular one another to acquire the horizontal and vertical components of the magnetic field.

In principle, this datalogger can be used for any application.

## License notes
Author: Filippo Falezza, ¢2020 released under GPLv3. \
Contributor and co-writer: Eric Liu, with authorship rights, ¢ 2020

## Notes
The code has been written in less than a weekend, so please feel free to modify it accordingly to the GPL license :)
