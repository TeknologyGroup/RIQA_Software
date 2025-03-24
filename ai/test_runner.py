import unittest
import importlib.util
import sys

def test_regenerated_code(file_path):
    try:
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules["module.name"] = module
        spec.loader.exec_module(module)
        print(f"✅ Test superato per {file_path}")
        return True
    except Exception as e:
        print(f"❌ Test fallito per {file_path}: {str(e)}")
        return False