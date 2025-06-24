import os

def get_files_path(path: str = None):
    if path is None:
        path = os.path.abspath(os.sep)
    else:
        path = os.path.abspath(os.path.join('..', '..', path))
        return os.walk(path, topdown=True, onerror=None, followlinks=False)

obj_path = get_files_path('Module_26')
for i in obj_path:
    print(i)






