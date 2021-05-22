import os
import argparse #to read the command line inputs
import yaml #to read the configurations from yasml files
import logging  #to handle the logs


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main(config_path, datasource):
    config = read_params(config_path)
    print(config)
    
if __name__=="__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config", "params.yaml")
    args.add_argument("--config", default=default_config_path)  #Add configuration file
    args.add_argument("--datasource", default=None) #Add data source

    parsed_args = args.parse_args() #Parse the arguments
    main(config_path=parsed_args.config , datasource=parsed_args.datasource)