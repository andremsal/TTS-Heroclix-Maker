## Summary

A simple script to convert data from [HCunits API](https://hcunits.net/api/v1/units/) json files into Tabletop Simulator json files.

## How it Works
In the first part of the logic, the program will ask for two inputs:
- Collection ID (e.g. _wk25_)
- Collection Name (e.g. _Wizkids 2025_)

In the second part of the logic, generates a list based on the previous inputs, filtering it to contain only `character` type units from the same `set_id` as the `Collection ID` input. Then, the program will iterate that list, asking for other two inputs for each character:
- Card Image URL
- Figure Image URL 
At the end of each iteration, the program will export and save a ready-to-use `.json` file into the working directory.
Simply paste the file into Tabletop Simulator `/Saved Objects` folder.

## Special Thanks
Many thanks to `Henrique Mauler` and `Clay Wood` for the huge collaboration.