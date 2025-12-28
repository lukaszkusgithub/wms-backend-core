# project_wms/main.py
import sys

sys.path.append("..")

from project_wms.models import Product
from project_wms.system import (
    WMSController,
    ProductNotFoundError,
    InsufficientStockError,
    DuplicateProductError,
)


def run_cli():
    controller = WMSController()

    # --- SEED DATA ---
    print("Initializing System...")
    try:
        p1 = Product(
            id=1, sku="LAP-001", name="Laptop Gaming", price=5000.0, _stock_qty=10
        )
        p2 = Product(
            id=2, sku="MOU-001", name="Mouse Wireless", price=100.0, _stock_qty=50
        )
        controller.add_product(p1)
        controller.add_product(p2)
        print("✅ Added initial products.")
    except Exception as e:
        print(f"❌ Init Error: {e}")

    # --- MAIN LOOP ---
    order_counter = 100

    while True:
        print("\n--- WAREHOUSE MENU ---")
        print("1. Show Inventory")
        print("2. Add Product")
        print("3. Create Order")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            print("\n CURRENT INVENTORY:")
            if not controller.warehouse.inventory:
                print("   (Empty)")
            for sku, prod in controller.warehouse.inventory.items():
                print(
                    f"   - [{sku}] {prod.name} | Stock: {prod.stock_qty} | Price: ${prod.price}"
                )

        elif choice == "2":
            sku = input("SKU: ")
            name = input("Name: ")
            try:
                qty = int(input("Qty: "))
                price = float(input("Price: "))
                new_prod = Product(
                    id=0, sku=sku, name=name, price=price, _stock_qty=qty
                )
                controller.add_product(new_prod)
                print("✅ Product added!")
            except ValueError:
                print("❌ Invalid number format!")
            except DuplicateProductError as e:
                print(f"❌ Error: {e}")
            except Exception as e:
                print(f"❌ Unexpected Error: {e}")

        elif choice == "3":
            print("Creating Order (Type 'done' as SKU to finish)")
            items_to_order = {}
            while True:
                sku = input("Product SKU: ")
                if sku == "done":
                    break
                if not sku:
                    continue

                try:
                    qty = int(input(f"Quantity for {sku}: "))
                    items_to_order[sku] = qty
                except ValueError:
                    print("❌ Invalid quantity.")

            if items_to_order:
                try:
                    order = controller.create_order(order_counter, items_to_order)
                    print(f"✅ Order #{order.id} created successfully!")
                    print(f"Items: {order.products}")
                    order_counter += 1
                except (ProductNotFoundError, InsufficientStockError) as e:
                    print(f"❌ ORDER FAILED: {e}")
                    print("(Transaction rolled back - no stock changed)")

        elif choice == "4":
            print("Bye!")
            break


if __name__ == "__main__":
    run_cli()
