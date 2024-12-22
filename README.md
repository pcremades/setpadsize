# ![icon](resources/icon.png) Set Pad Size plugin for KiCad

## Description
The `Set Pad Size` plugin is a KiCad action plugin that edits the pad size of all pads in the PCB to a unique size. The default value is 1.6mm. 

**Why?** When manufacturing and drilling PCBs by hand, it can happen that holes are drilled that are smaller than the holes in the original footprints. In this case, drilling leaves a small ring of PCB base material without copper around the hole. This will cause problems when soldering. Setting all holes to a minimum diameter will ensure that each hole is surrounded by copper.

## Installation

### Manual Installation

1. Clone this repository or download the latest release.
2. Copy the `plugins` subdirectory to your KiCad plugins directory. eg
   
```
cp -rp plugins <your_kicad_plugin_directory>/setpadsize
```

3. Restart KiCad or use `Tools > External Plugins > Refresh Plugins` from the PCB Editors menu

## Usage
1. Open your PCB project in the KiCad PCB editor.
2. Go to `Tools > External Plugins > Set Pad Size` to run the plugin.

## License
This project is licensed under the GNU GPL Version 3 License - see the [LICENSE](LICENSE) file for details.

## Author
Pablo Cremades (based on [Set Hole Diameter](https://github.com/seigedigital/setholediameterpluginforkicad/tree/main) plugin by Leander Seige, seige.digital GbR)
