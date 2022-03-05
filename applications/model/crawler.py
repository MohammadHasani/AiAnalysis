import re
from pathlib import Path


class Crawler:
    relu_regex = r"model\.\s*(\\\s*){0,1}add(\\\s*){0,1}\s*\((\\\s*){0,1}\s*\w*\s*\(\s*\d+\s*.*\s*\,\s*(\\\s*){0,1}activation\s*(\\\s*){0,1}=(\\\s*){0,1}\s*(\\\s*){0,1}'relu'\s*(\\\s*){0,1}\)\s*\)"
    sigmoid_regex = r"model\.\s*(\\\s*){0,1}add(\\\s*){0,1}\s*\((\\\s*){0,1}\s*\w*\s*\(\s*\d+\s*.*\s*\,\s*(\\\s*){0,1}activation\s*(\\\s*){0,1}=(\\\s*){0,1}\s*(\\\s*){0,1}'sigmoid'\s*(\\\s*){0,1}\)\s*\)"

    @staticmethod
    def read_file(file_path: str, ):
        with open(file_path, 'r') as reader:
            return reader.read()

    # TODO remove this method
    def get_number_of_py_files(self, path):
        return {"files": 2, "folders": 4}

    @staticmethod
    def get_all_python_files_in_folder(path):
        file_list = list(Path(path).rglob("*.[pP][yY]"))
        file_list = [str(f) for f in file_list]
        file_list.sort()

        return file_list

    @staticmethod
    def is_file_python(file_path: str):
        return file_path.endswith(".py")

    def analysis_python_file(self, file_path: str, regex):
        if self.is_file_python(file_path):
            read_file = self.read_file(file_path)
            pattern = re.compile(regex)
            result = pattern.findall(read_file)

            return len(result)
        return False

    def classify_file(self, file_path):
        relu_result = self.analysis_python_file(file_path, self.relu_regex)
        sigmoid_result = self.analysis_python_file(file_path, self.sigmoid_regex)
        final_result = relu_result + sigmoid_result
        if 1 <= final_result <= 9:
            return 'low'

        if 10 <= final_result <= 19:
            return 'medium'

        if 20 <= final_result:
            return 'high'

        return None
