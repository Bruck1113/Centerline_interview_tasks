# File monitoring System
This repo is served as a reference for my application project of Centerline's interview. It will constantly check if a specified file appears under a specified directory

## Packages requirement
- json
- logging
- os
- asyncio
- datetime
- pandas as pd
- sys

## Config file content
| Key       | Key function |
| --------- | ------- |
| Path      |  For recording the mother directory of each file that we are monitoring for|
| file name | For recording the file that we are searching for|
| Others    | For demonstration purpose|

## Functions description
| Function name| Params |Description |
| --------- | ------- | ------- | 
| check_file_exists | `directory`, `filename`      |  To check whether a filename exists under that directory|
| job| `record`, `directory`, `filename` | Asynchronous function to output log messages to the log|
| Main| None| main function|
