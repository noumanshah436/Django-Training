import os
import re

def to_snake_case(name):
    # Replace spaces and other non-alphanumeric characters with a single underscore
    name_with_underscores = re.sub(r'[\W]+', '_', name)
    # Convert camelCase or PascalCase to snake_case
    snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name_with_underscores).lower()
    # Remove any leading or trailing underscores
    snake_case_name = snake_case_name.strip('_')
    # Replace multiple underscores with a single underscore
    snake_case_name = re.sub(r'__+', '_', snake_case_name)
    return snake_case_name

def rename_dirs_to_snake_case(root_dir='.'):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for dir_name in dirs:
            current_path = os.path.join(root, dir_name)
            new_dir_name = to_snake_case(dir_name)
            new_path = os.path.join(root, new_dir_name)
            if current_path != new_path:
                os.rename(current_path, new_path)

if __name__ == '__main__':
    rename_dirs_to_snake_case()
