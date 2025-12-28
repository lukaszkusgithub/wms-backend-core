from typing import Dict
from project_wms.models import Warehouse, Order, Product


class ProductNotFoundError(Exception):
    pass


class InsufficientStockError(Exception):
    pass


class DuplicateProductError(Exception):
    pass


class WMSController:
    def __init__(self):
        self.warehouse = Warehouse()

    def add_product(self, product: Product):
        if product.sku in self.warehouse.inventory:
            raise DuplicateProductError(
                f"Product with SKU {product.sku} already exists."
            )
        self.warehouse.inventory[product.sku] = product

    def create_order(self, order_id: int, items: Dict[str, int]) -> Order:
        for sku, requested_qty in items.items():
            if sku not in self.warehouse.inventory:
                raise ProductNotFoundError(f"Product with SKU {sku} not found.")

            product = self.warehouse.inventory[sku]

            if product.stock_qty < requested_qty:
                raise InsufficientStockError(
                    f"Insufficient stock for SKU {sku}. "
                    f"Requested: {requested_qty}, Available: {product.stock_qty}"
                )

        new_order = Order(id=order_id)

        for sku, requested_qty in items.items():
            product = self.warehouse.inventory[sku]

            product.stock_qty -= requested_qty

            new_order.products[sku] = requested_qty

        return new_order
