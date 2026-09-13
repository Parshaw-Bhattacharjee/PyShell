import os

def locate_exec(args: str) -> None:
    '''
    locate executable files & returns filepath otherwise returns None
    '''

    dir_path = os.environ.get('PATH', '').split(os.pathsep)

    for dir_file in dir_path:
        file_path = os.path.join(dir_file, args)

        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path # handles unrecognized commands