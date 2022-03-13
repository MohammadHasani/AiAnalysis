import re
from pathlib import Path


class Crawler:
    model_name_regex = r"([a-zA-Z]+([a-zA-Z0-9_])*)\s*=\s*Sequential\(\s*\)"

    relu_regex = r"%s\.\s*(\\\s*){0,1}add(\\\s*){0,1}\s*\((\\\s*){0,1}\s*\w*\s*\(\s*\d+\s*.*\s*\,\s*(\\\s*){0,1}activation\s*(\\\s*){0,1}=(\\\s*){0,1}\s*(\\\s*){0,1}'relu'\s*(\\\s*){0,1}\)\s*\)"
    sigmoid_regex = r"%s\.\s*(\\\s*){0,1}add(\\\s*){0,1}\s*\((\\\s*){0,1}\s*\w*\s*\(\s*\d+\s*.*\s*\,\s*(\\\s*){0,1}activation\s*(\\\s*){0,1}=(\\\s*){0,1}\s*(\\\s*){0,1}'sigmoid'\s*(\\\s*){0,1}\)\s*\)"

    @staticmethod
    def read_file(file_path: str, ):
        with open(file_path, 'r') as reader:
            return reader.read()

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
            model_pattern = re.compile(self.model_name_regex)
            model_name_result = model_pattern.findall(read_file)
            model_name_result = [i[0] for i in model_name_result]

            # remove duplicate values
            model_name_result = list(dict.fromkeys(model_name_result))

            pattern_list = [re.compile(regex % (i)) for i in model_name_result]

            result = [pattern.findall(read_file) for pattern in pattern_list]
            result_len = [len(i) for i in result]

            return sum(result_len)
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
