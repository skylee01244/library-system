# A Library Management System
This Library Management System is a robust application built using Python **PyQt6** and integrated with a **MySQL** database. The system offers comprehensive features to manage library operations efficiently

## Build Instructions
**1) Install Required Packages**  
```
pip install PyQt6 xlrd xlsxwriter mysql-connector-python pyinstaller
```
**2) Install MySQL Server & MySQL WorkBench**  
Download MySQL Server [here](https://dev.mysql.com/downloads/mysql/)  
Download MySQL Workbench [here](https://www.mysql.com/products/workbench/)  

**3) Import Data into the Database**  
To create the database, import the `library_data.sql` file into SQL Workbench.  

**4) Navigate to Your Project Directory**  
Open your terminal and navigate to the project directory where `index.py` is located.  

**5) Build the Executable**  
> For a multi-configuration generator (Windows)
```
pyinstaller --name=LibrarySystem --windowed --onefile --icon=icons/library.ico --add-data "home.ui;." --add-data "login.ui;." --add-data "library_data.db;." --add-data "themes/*;themes/" --add-data "icons/*;icons/" --add-data "icons.qrc;." --hidden-import=icons_rc --exclude PySide6 index.py
```
> For a single-configuration generator (LINUX & MACOS) 
```
pyinstaller --name=LibrarySystem --windowed --onefile --icon=icons/library.icns --add-data "home.ui:." --add-data "login.ui:." --add-data "library_data.db:." --add-data "themes/*:themes/" --add-data "icons/*:icons/" --add-data "icons.qrc:." --hidden-import=icons_rc --exclude-module PySide6 index.py
```
→ PyInstaller will create a `dist` folder inside your project directory. Your executable will be located inside `dist/LibrarySystem.exe`.

**6) Relocate the Executable**  
 Move the executable file out of the `dist` directory and place it in your project directory (where `index.py` is located).

**7) Run the Application**  
 To run the application, execute the `LibrarySystem.exe` file in your project directory.  

## Pre-Built Applications
For your convenience, the repository includes pre-built executables for both major operating systems:  
- `library-system-windows/` Contains the ready-to-run .exe application for Windows.  
- `library-system-mac/`  Contains the pre-compiled .app bundle for macOS.  
Simply download the appropriate folder for your system, open it, and launch the application directly—no manual build process required.  

## Usage
Login with 
```
username: admin
password: 123
```

## Capabilities and Functionalities
- **User Authentication and Management**: Seamlessly login, create, edit, and delete user accounts ensuring robust security and user privacy.  
- **Client Management**: Efficiently add, update, and remove client records with comprehensive details to enhance customer relations.  
- **Book Inventory Management**: Flawlessly manage the library's book inventory by adding, updating, and deleting book records, ensuring accurate and up-to-date cataloging.  
- **Borrowing and Returning Management**: Record and track book borrowing and return transactions effortlessly, ensuring accurate and real-time updates of the library's collection.  
- **Category, Author, and Publisher Management**: Maintain a meticulously organized library database by managing book categories, authors, and publishers.  
- **Data Exportation**: Easily export all data to an Excel sheet for systematic record-keeping and analytical purposes.  