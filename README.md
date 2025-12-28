# Warehouse Management System (WMS) - Core Engine

A robust, transactional backend engine for warehouse management simulation, built with modern Python.

## 🚀 Key Features

* **Atomic Transactions (Two-Phase Commit):** Prevents inventory corruption. Orders are only created if *all* requested items are available and valid. If one check fails, the entire transaction rolls back.
* **Type Safety:** 100% type-hinted codebase, validated with `mypy` in strict mode.
* **Fail-Fast Architecture:** Domain models (`Product`) enforce data integrity (e.g., non-negative stock) immediately upon initialization.
* **Clean Architecture:** Separation of concerns between Data Models (`dataclasses`), Business Logic (`WMSController`), and Presentation Layer (CLI).

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Data Structures:** `dataclasses` (stdlib), `dict` (O(1) lookups), `set`.
* **Static Analysis:** `mypy` (Type Checking), `black` (Formatter).
* **Paradigms:** OOP, Composition, Fail-Fast.

## 📦 Project Structure

```text
project_wms/
├── models.py      # Data Models with validation logic (@dataclass)
├── system.py      # WMSController with transaction logic
├── main.py        # CLI Interface for user interaction
└── __init__.py    # Package initialization
```


## 💻 How to Run
1. Clone the repository:

```bash
git clone https://github.com/lukaszkusgithub/wms-backend-core.git

cd wms-backend-core
```

2. Run the application:

```bash
python3 -m project_wms.main
```

## 🔍 Code Quality

The code enforces strict typing and formatting standards:

```bash
# Check types
python3 -m mypy project_wms/

# Check formatting
python3 -m black --check project_wms/
```

## 🧠 Engineering Decisions
- Why `dataclasses`? To reduce boilerplate code while maintaining strict data typing and immutability options.

- Why Custom Exceptions? To handle specific business logic failures (`InsufficientStockError`) gracefully in upper layers, rather than relying on generic ValueErrors.

- Logic Separation: The `Warehouse` class acts as a data store, while `WMSController` handles the business logic, making the system testable and modular.