<p align="center">
  <img src="Icon/My little Python Scripts.png" alt="My Little Python Scripts logo" width="256">
</p>
<h1 align="center">My Little Python Scripts</h1>

A collection of small Python scripts and apps solving specific problems.  
Each folder contains the source code, executables, and related files.

---

## 📁 Contents

### Lorem Ipsum Generator
Generates placeholder text (Lorem Ipsum) of custom length. Useful for testing layouts, documents, or web designs quickly.

**Features:**
- Customizable text length
- Copy to clipboard functionality
- Simple and fast GUI

### TXT Comparison
Compares two `.txt` files and highlights differences. Handy for quickly spotting changes in text data or code files.

**Features:**
- Side-by-side file comparison
- Highlights added, removed, and modified lines
- Easy file selection interface

### Fan Airflow Calculator
Calculates fan statistics and creates visualization charts for airflow analysis.

**Features:**
- Fan performance calculations
- Chart generation for data visualization
- Export results to file

---

### QR Code Generator
Generates QR codes from any text or link and allows saving them as image files. Ideal for quickly creating QR codes for URLs, Wi-Fi credentials, or any custom text.

**Features:**
- Generates QR codes from user input
- Live preview of the generated QR code
- Save QR codes as `.png` files
- Simple and intuitive GUI


## 🚀 Quick Start

### Running Scripts

Each script folder contains:
- **Source code** (`.py` files) - run with Python
- **Executables** (`.exe` files) - ready to run on Windows

### Requirements

For running from source:
```bash
python 3.8+
```

Individual scripts may have additional dependencies listed in their respective folders.

---

## ⬇️ How to get a specific script

If you want to download just one script instead of the whole repository, you can use Git's sparse checkout feature:

### 1. Clone the repository without checking out files

```bash
git clone --no-checkout https://github.com/vGiacomov/My-Little-Python-Scripts.git MLPS
cd MLPS
```

### 2. Enable sparse checkout

```bash
git sparse-checkout init --cone
```

### 3. Choose the folder you want

#### To get Lorem Ipsum Generator:
```bash
git sparse-checkout set "Lorem Ipsum Generator"
```

#### To get TXT Comparison:
```bash
git sparse-checkout set "TXT Comparison"
```

#### To get Fan Airflow Calculator:
```bash
git sparse-checkout set "Fan Airflow Calculator"
```

### 4. Checkout the main branch

```bash
git checkout main
```

Now you will have only the folder you need, without downloading the entire repository.

---

## 📂 Repository Structure

```
My-Little-Python-Scripts/
├── Icon/
│   └── My little Python Scripts.png
├── Lorem Ipsum Generator/
│   ├── source files
│   └── executable
├── TXT Comparison/
│   ├── source files
│   └── executable
├── Fan Airflow Calculator/
│   ├── source files
│   └── executable
└── QR Code Generator
    ├── source files
    └── executable
```

---

## 🤔 Purpose

These are ready-to-use scripts that may come in handy someday.  
Instead of writing quick scripts from scratch or asking an AI, you can just grab them and run.  
Think of this as a personal toolbox of small, situational solutions — sometimes messy, sometimes experimental, but often useful.

---

## 🛠️ Contributing

Feel free to:
- Report bugs via GitHub Issues
- Suggest new features or improvements
- Fork and create pull requests

This is a personal collection, but contributions are welcome if you have similar small utilities to share.

---

## ⚠️ Warning

No guarantees. Some of these scripts are old, some are messy, and some are just plain unnecessary.  
But they worked once. That's good enough for me.

---

## 🔗 Links

- **GitHub Repository**: [My Little Python Scripts](https://github.com/vGiacomov/My-Little-Python-Scripts)
- **Issues & Feature Requests**: Use GitHub Issues tab
- **Author**: [vGiacomov](https://github.com/vGiacomov)

---

## 📄 License

This project is for personal use and educational purposes.  
Feel free to use, modify, and distribute as needed.

---

**Last Updated**: December 2025
