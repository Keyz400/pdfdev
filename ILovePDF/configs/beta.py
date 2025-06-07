# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/configs/beta.py"

# Beta functionality has been removed as requested
# This file is kept for compatibility but beta features are disabled

# Empty beta users list - no beta features
BETA = []

# Beta configuration disabled
BETA_ENABLED = False
BETA_FEATURES = []

# Legacy support for existing code
def is_beta_user(user_id):
    """Always returns False since beta features are removed"""
    return False

def add_beta_user(user_id):
    """No-op function for compatibility"""
    pass

def remove_beta_user(user_id):
    """No-op function for compatibility"""
    pass

def get_beta_users():
    """Returns empty list"""
    return []
