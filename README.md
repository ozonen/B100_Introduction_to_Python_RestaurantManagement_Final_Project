# Ramen Shop Management System

B100 Introduction to Computer Programming with Python  
Gisma University of Applied Sciences 

**Student:** Ozgur Onen - **Student ID:** GH1044899

---

## About

A Python-based management system for a ramen restaurant. This project handles menu management, table reservations, order processing, and billing with CSV data storage.

## Project Structure

| File | Description |
|------|-------------|
| `menu_item.py` | MenuItem class - manages individual menu items |
| `table.py` | Table class - handles table status and reservations |
| `order.py` | Order class - processes customer orders |
| `restaurant.py` | Restaurant class - main system controller |
| `main.py` | Main program - user interface and menu system |
| `data/menu.csv` | Menu data storage file |

## Features

- Menu management (20 items: ramen, toppings, soups, drinks)
- Table status tracking (7 tables)
- Order processing with tax calculation
- CSV file save/load functionality
- Interactive menu  interface
- Error handling for invalid inputs

## Requirements

- Python 3.8 or higher
- No external libraries are required

## Installation & Usage

1. Clone the repository
2. Navigate to project folder:
```bash
   cd restaurant_management
```
3. Run the program:
```bash
   python main.py
```
## Example Usage

### Create an order
```
Main Menu → 3 (Orders) → 1 (New Order)
Enter table: 1
```
### Add items

1. Select: `Orders → 2 (Add Item)`
2. Enter Order ID: `1`
3. Enter Item ID: `3` (Tonkotsu Ramen for example)
4. Enter Quantity: `2`

### View total

1. Select: `Orders → 3 (It shows the order)`
2. Enter Order ID: `1`

**Result:**
```
2x Tonkotsu Ramen - €13.50 = €27.00
Subtotal: €27.00
Tax (19%): €5.13
TOTAL: €32.13
```
## Menu Items

- **Ramen:** Shoyu, Miso, Tonkotsu, Spicy Tan Tan, Vegetable
- **Toppings:** Chashu Pork, Egg, Noodles, Corn, Seaweed, Green Onion, Bamboo
- **Soup:** Rich Broth, Spicy Broth, Garlic Oil
- **Drinks:** Green Tea, Iced Tea, Ramune, Beer, Sake

## Technical Details

**Classes:** 4 classes with 24 total methods  
**Concepts:** OOP, File I/O, Exception Handling, Control Structures  
**Data Storage:** CSV format for menu persistence

## Python Concepts Used

- Classes & Objects (4 classes)  
- Methods (24 methods)  
- Loops & Conditionals  
- File I/O (CSV)  
- Exception Handling  
- Modules (5 files)

---
