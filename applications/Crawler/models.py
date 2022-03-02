from pathlib import Path


class Crawler:
    def read_file(self, path: str, name):
        path = path + name
        with open(path, 'r') as reader:
            return reader.read()

    def get_number_of_py_files(self, path):
        return {"files": 2, "folders": 4}

    def get_all_python_files_in_folder(self, path):
        file_list = list(Path(path).rglob("*.[pP][yY]"))
        file_list = [str(f) for f in file_list]
        file_list.sort()

        return file_list
