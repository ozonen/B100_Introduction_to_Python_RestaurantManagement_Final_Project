# Ramen Shop Management System

A Python-based management system for a ramen restaurant. This project was created for the B100 Introduction to Computer Programming course at Gisma University.

## About This Project

This system helps manage a ramen shop's daily operations including:
- Menu management (ramen bowls, toppings, soups, beverages)
- Table management (tracking availability and reservations)
- Order processing (creating orders, adding items, calculating bills)
- Data storage (saving and loading menu from CSV files)

## Features

- **Menu Management**: Add, view, and update ramen dishes, toppings, and drinks
- **Table Tracking**: Monitor table status (free, busy, reserved)
- **Order System**: Create orders, add multiple items, calculate totals with tax
- **File Storage**: Save and load menu data using CSV files
- **Interactive Interface**: Easy-to-use menu-driven system

## Project Structure
restaurant_management/
│
├── menu_item.py       # MenuItem class - represents menu items
├── table.py           # Table class - manages restaurant tables
├── order.py           # Order class - handles customer orders
├── restaurant.py      # Restaurant class - main controller
├── main.py            # Main program with user interface
│
└── data/
└── menu.csv       # Menu data file

## Menu Items

The ramen shop offers:

**Ramen Bowls:**
- Shoyu Ramen (€12.00)
- Miso Ramen (€12.50)
- Tonkotsu Ramen (€13.50)
- Spicy Tan Tan Ramen (€13.00)
- Vegetable Ramen (€11.00)

**Toppings:**
- Extra Chashu Pork, Soft Boiled Egg, Extra Noodles, Corn, Seaweed, Green Onion, Bamboo Shoots

**Soup Options:**
- Extra Rich Broth, Spicy Broth, Garlic Oil

**Beverages:**
- Green Tea, Iced Tea, Ramune Soda, Asahi Beer, Sake

## Installation

### Requirements
- Python 3.8 or higher
- No external libraries needed (uses only Python standard library)

### Setup

1. **Download the project**
```bash
   git clone https://github.com/YOUR_USERNAME/ramen-shop-management.git
   cd ramen-shop-management
```

2. **Check Python version**
```bash
   python --version
```
   Should show Python 3.8 or higher

3. **No installation needed!** All required libraries are built into Python.

## How to Run

### Starting the Program

1. Open your terminal/command prompt
2. Navigate to the project folder
3. Run the main program:
```bash
python main.py
```

### First Time Setup

When you run the program:
1. Enter your ramen shop name (or press Enter for default: "Ichiraku Ramen House")
2. Type `yes` when asked "Load ramen menu?"
3. The system will automatically set up:
   - 20 menu items (ramen, toppings, soups, drinks)
   - 7 tables (4 tables with 4 seats, 3 tables with 2 seats)

## Usage Examples

### Example 1: View the Menu
