from dataclasses import dataclass, field


@dataclass
class Product:
    id: int
    sku: str
    name: str
    price: float
    _stock_qty: int = field(default=0, repr=False)

    def __post_init__(self):
        if self._stock_qty < 0:
            raise ValueError(
                f"CRITICAL: Initial stock for {self.sku} cannot be negative!"
            )

    @property
    def stock_qty(self) -> int:
        return self._stock_qty

    @stock_qty.setter
    def stock_qty(self, value: int):
        if value < 0:
            raise ValueError(
                f"Cannot set negative stock for {self.sku}. Attempted: {value}"
            )
        self._stock_qty = value


@dataclass
class Order:
    id: int
    status: str = "PENDING"
    products: dict[str, int] = field(default_factory=dict)


@dataclass
class Warehouse:
    inventory: dict[str, Product] = field(default_factory=dict)
