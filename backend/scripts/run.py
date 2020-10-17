import platform
import os
from generate_constants import *

os.system("rm -rf pickled")
os.system("mkdir pickled")

scripts = [
    "scripts/generate_constants/run.py",
    "scripts/generate_country_similarity_matrix/run.py"
]

ex = "python3"
if platform.system() == "Windows":
    ex = "python"

for script in scripts:
    """
    auto-detects platform used, as "python" is used in windows and "python3" is used otherwise
    """
    os.system(ex + " " + script)

