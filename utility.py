import json
import os

class FileUtils:
    """
    A utility class for reading and writing files, including JSON and plain text files.
    """

    @staticmethod
    def read_json(file_path):
        """
        Reads a JSON file and returns its contents.

        :param file_path: Path to the JSON file.
        :return: Parsed JSON data (dict or list).
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file is not valid JSON.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path, data):
        """
        Writes data to a JSON file.

        :param file_path: Path to the JSON file.
        :param data: Data to write (must be serializable to JSON).
        """
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def read_text(file_path):
        """
        Reads the contents of a plain text file.

        :param file_path: Path to the text file.
        :return: The content of the file as a string.
        :raises FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_text(file_path, content):
        """
        Writes content to a plain text file.

        :param file_path: Path to the text file.
        :param content: Content to write to the file.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
