import os
import shutil

import pytest

from applications.Crawler.models import Crawler


def get_unittest_repo():
    directory = "unittest_repo"
    parent_dir = "applications/repos/"

    path = os.path.abspath(os.path.join(parent_dir, directory))
    return path


def write_new_file(path, file_name, content):
    with open(path + file_name, "a") as writer:
        writer.write(content)
    return writer


@pytest.fixture()
def create_folder_and_files():
    path = get_unittest_repo()
    is_folder = os.path.isdir(path)
    if is_folder:
        shutil.rmtree(path)
        os.makedirs(path)
    else:
        os.makedirs(path)

    write_new_file(path + '/', "example.py", "print('hi from new python file !')")
    write_new_file(path + '/', "example2.py", "print('hi from second new python file !')")
    write_new_file(path + '/', "example.txt", "print('hi from second new python file !')")

    path_rec = path + '/rec1'
    os.makedirs(path_rec)

    write_new_file(path_rec + '/', "example.py", "print('hi from new python file recursively !')")
    write_new_file(path_rec + '/', "example2.py", "print('hi from second new python file recursively !')")
    write_new_file(path_rec + '/', "example.txt", "print('hi from second new python file recursively!')")

    yield
    # teardown
    shutil.rmtree(path)


def test_crawl_all_python_files_of_folder(create_folder_and_files):
    crawler_obj = Crawler()
    path = get_unittest_repo() + '/'

    file_list = crawler_obj.get_all_python_files_in_folder(path)
    assert file_list == [path + 'example.py', path + 'example2.py', path + 'rec1/example.py',
                         path + 'rec1/example2.py']

    for f in file_list:
        crawler_obj.read_file(f, '')
