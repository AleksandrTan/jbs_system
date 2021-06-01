"""
    Context processor for collecting data from models to display on the main page
    Added to backend/settings.py -> TEMPLATES ->'OPTIONS' -> context_processors'
"""

from mainsystem.modelswork.order_work import OrderWork


def main_data(request) -> dict:
    admin_data = dict()
    admin_data['active_bots'] = OrderWork.get_active_orders()

    return admin_data
