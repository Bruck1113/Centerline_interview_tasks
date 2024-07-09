# Import necessary packages
import json
import logging
import os
import asyncio
import datetime
import pandas as pd
import sys

# Define the config level
logging.basicConfig(level=logging.INFO)

# Method to check if a file exists in a given directory
def check_file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)

# Method to connect the found messages to the log
async def job(record, directory, filename: list) -> None:
    if check_file_exists(directory, filename):
        if filename not in record:
            info = "Time created: " +  str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " Filename create: " + filename + " Mother directory: " + directory
            
            # ERROR handling: Possible missing record document
            try:
                f = open("record.txt", "a")
                f.write(info + "\n")
                f.close()  
            except:
                logging.info("record file not found")
                sys.exit()

            # Record the found filename to avoid repeat report and record
            record.append(filename)
            logging.info(info)


async def main():
    # defining necessary constant values
    directories = []
    cooldown = 10 # cooldown time for each monitoring search
    record = []    

    # ERROR handling: possible missing config file or other file operation error    
    try:
        with open("config.json") as jsonfile:
            reports_dict = json.load(jsonfile)
            for report in reports_dict:
                directories.append(reports_dict[report])
    except:
        logging.info("config file missing")
        sys.exit()

    # SIGNAL: Start the monitoring pogress
    logging.info("Monitoring started")

    # ERROR handling: Keyboard interruption
    try:
        while True:
            logging.info("relistening...")
            tasks = []
            for dir in directories:
                for target in dir["File names"]:
                    tasks.append(job(record, dir["Path"], target))
            await asyncio.gather(*tasks)
            await asyncio.sleep(cooldown)
    except KeyboardInterrupt:
        logging.info("Monitoring stop")


if __name__ == "__main__":
    asyncio.run(main())
