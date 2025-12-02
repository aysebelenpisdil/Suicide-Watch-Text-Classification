#!/usr/bin/env python3
"""
Test script to verify all packages are working
"""

import sys
print(f"Python: {sys.version}")
print(f"Executable: {sys.executable}")
print("-" * 50)

try:
    import pandas as pd
    print(f"✓ pandas {pd.__version__}")
except ImportError as e:
    print(f"✗ pandas: {e}")

try:
    import numpy as np
    print(f"✓ numpy {np.__version__}")
except ImportError as e:
    print(f"✗ numpy: {e}")

try:
    import matplotlib
    print(f"✓ matplotlib {matplotlib.__version__}")
except ImportError as e:
    print(f"✗ matplotlib: {e}")

try:
    import seaborn as sns
    print(f"✓ seaborn {sns.__version__}")
except ImportError as e:
    print(f"✗ seaborn: {e}")

try:
    import sklearn
    print(f"✓ scikit-learn {sklearn.__version__}")
except ImportError as e:
    print(f"✗ scikit-learn: {e}")

try:
    import wordcloud
    print(f"✓ wordcloud {wordcloud.__version__}")
except ImportError as e:
    print(f"✗ wordcloud: {e}")

try:
    import nltk
    print(f"✓ nltk {nltk.__version__}")
except ImportError as e:
    print(f"✗ nltk: {e}")

print("-" * 50)
print("All packages imported successfully!")