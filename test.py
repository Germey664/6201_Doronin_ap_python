import math
import tomllib
import pathlib


def calc_func(a, b, c, xmin, xmax, step):
    for x in range(xmin, xmax, step):
        y = a * math.sqrt(1 + (2 * x) / (math.e**(b*x) + c**2))
        print(y)


def parser_file_toml():
    # Read units from file
    with pathlib.Path("config.toml").open(mode="rb") as file:
        base_units = tomllib.load(file)

    units = {}
    for unit, unit_info in base_units.items():
        units[unit] = unit_info
        for alias in unit_info:
            units[alias] = unit_info[alias]
    return units


units = parser_file_toml()
calc_func(units['a'], units['b'], units['c'], units['xmin'], units['xmax'], units['step'])
