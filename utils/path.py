from pathlib import Path
import files_for_test


def to_resource(relative_path):
    return str(Path(files_for_test.__file__).parent.joinpath(relative_path).absolute())