import os

current_dir = os.path.dirname(__file__)
style_path = os.path.join(current_dir, "resources", "base")
print(os.path.exists(style_path))

