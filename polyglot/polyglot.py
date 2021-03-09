from .exceptions import *
import os as os
import logging as Logger
import requests as Requests
import yaml as YamlLoader
import pprint as pprint

printer = pprint.PrettyPrinter()

class PolyglotExtensions(object):
    def __init__(self, param):
        assert isinstance(param, str), "Expected a string"

        self.parameter = param

        self.directory_name = self.__get_dir_name(self.parameter)
        

    def __get_dir_name(self, param):
        """Get the directory name pased on the parameter"""
        if param == ".":
            return os.getcwd()
        else:
            if os.path.isabs(param):
                return param
            else:
                return os.path.join(os.getcwd(), param)

    def find_files(self, yaml_file):
        if yaml_file == None:
            Logger.error("Cannot find the language file")
            yaml_file = self.__install_language_file()
        with open(yaml_file, "r") as yaml_reader:
            file_content = YamlLoader.load(
                yaml_reader,
                Loader=YamlLoader.FullLoader
            )
        
        for language in dict(file_content):
            pass

    def __install_language_file(self):
        filename = os.path.join(os.getcwd(), "language.yml")
        url = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
        Logger.info(f"Installing file from {url} to {filename}")
        try:
            open(
                filename,
                "wb"
            ).write(
                Requests.get(url, allow_redirects=True).content
            )
        except Exception as exception:
            Logger.info("Process failed")
            raise exception

        return filename



class Polyglot(object):
    def __init__(self, command="init", command_argument=".", language_yml=None):
        assert isinstance(command, str), "Expected a string"
        assert isinstance(command_argument, str), "Expected a strng"

        self.command = command
        self.parameters = command_argument

        self.language_yaml = language_yml

        self.files = {}

    def show(self):
        """
        Parse the results and show(return)
        the reuslts as an array(list)
        """
        if self.command == "init":
            poly = PolyglotExtensions(self.parameters).find_files(self.language_yaml)
