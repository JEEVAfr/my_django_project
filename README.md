# Django REST Framework (DRF) Project

## Overview
This project implements a RESTful API using Django REST Framework (DRF) for managing products, categories, and subcategories. The API provides CRUD operations and search/filter functionality for each model while ensuring that only active records are returned.

## Models
The project consists of three main models:

### 1. Category
- **Fields:**
  - `id`: Auto-generated identifier.
  - `uuid`: Unique identifier for the category.
  - `category_name`: Name of the category.

### 2. Subcategory
- **Fields:**
  - `id`: Auto-generated identifier.
  - `uuid`: Unique identifier for the subcategory.
  - `category`: ForeignKey to the `Category` model.
  - `sub_category_name`: Name of the subcategory.

### 3. Product
- **Fields:**
  - `id`: Auto-generated identifier.
  - `uuid`: Unique identifier for the product.
  - `category`: ForeignKey to the `Category` model.
  - `sub_category`: ForeignKey to the `Subcategory` model.
  - `product_name`: Name of the product.
  - `price`: Price of the product.
  - `is_active`: Boolean indicating whether the product is active.

## Functionality
### CRUD Operations
- Implemented CRUD operations for the following models:
  - **Category**
  - **Subcategory**
  - **Product**

### Filtering and Search Capabilities
- Added filtering and search capabilities for each model to facilitate easy data retrieval based on various parameters.

### Active Records
- Ensured that the List API only returns active records (where `is_active` is True).

## Web Functionality
1. **Product Listing**
   - Implemented functionality to list all products filtered by `Category` and `Subcategory`, ensuring only active products (where `is_active` is True) are displayed.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/JEEVAfr/my_django_project.git
   cd my_django_project
