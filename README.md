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
