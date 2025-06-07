#!/usr/bin/env python3
"""
Quick fix for common issues in iLovePDF bot
"""

import os
import sys

def fix_config_issues():
    """Fix configuration issues"""
    # Add to environment if missing
    env_vars = {
        'DONATE_UPI': 'upi://pay?pn=UPAYI&pa=loxbots@airtel&cu=INR',
        'DEFAULT_LANG': 'eng',
        'MULTI_LANG_SUP': 'True',
        'SEND_RESTART_MESSAGE': 'True',
        'PROTECT_CONTENT': 'False'
    }
    
    for key, value in env_vars.items():
        if not os.environ.get(key):
            os.environ[key] = value
            print(f"Set {key} = {value}")

def fix_imports():
    """Fix import issues"""
    try:
        # Ensure lang module can be imported
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from lang import eng
        print("✅ Language module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Language import error: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Fixing iLovePDF Bot Issues...")
    fix_config_issues()
    
    if fix_imports():
        print("✅ All fixes applied successfully!")
    else:
        print("❌ Some issues remain. Check the error messages above.")
