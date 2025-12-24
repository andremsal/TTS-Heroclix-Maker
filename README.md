## Summary

A script that helps to convert [HCunits](https://hcunits.net/) data into Tabletop Simulator figures.\
It's `main.py` function is to convert data from [HCunits API](https://hcunits.net/api/v1/units/) into Tabletop Simulator `.json` files.
It can also get hcunit card renders and save them as images into a local folder using the `scraper.py` file.

## Main Function
In the first part of the logic, the program will ask for the following input:
- Collection ID (e.g. _wk25_)

With the Collection ID it will fetch the collection Name automatically.

In the second part of the logic, it generates a list based on the previous inputs, filtering it to contain only `character` type units from the same `set_id` as the `Collection ID` input.

You also have the option to choose in which position of the list you want to start.

Then, the program will iterate that list, asking for other two inputs for each character:
- Card Image URL
- Figure Image URL

At the end of each iteration, the program will export and save a ready-to-use `.json` file into the working directory.
Simply paste the file into Tabletop Simulator `/Saved Objects` folder.

## Scraper Function
This is a more simple script that also asks for one input:
- Collection ID (e.g. _wk25_), which is used to fetch the units inside this collection and Collection Name, which will create the folder with same name to store files.

Then it will save `.png` files with unit id as it's name.

## Special Thanks
Many thanks to `Henrique Mauler` and `Clay Wood` for the huge collaboration.