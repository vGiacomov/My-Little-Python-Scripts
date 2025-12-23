# 🗃️ My Little Python Sctipts

A collection of small Python scripts and apps solving specific problems. 
Each folder contains the source code, executables, and related files



## 📁 Contents

#### Lorem Ipsum Generator <br>
Generates placeholder text (Lorem Ipsum) of custom length. Useful for testing layouts, documents, or web designs quickly.

#### TXT Comparison <br>
Compares two `.txt` files and highlights differences. Handy for quickly spotting changes in text data or code files.

## 🤔 Purpose

These are ready-to-use scripts that may come in handy someday.  
Instead of writing quick scripts from scratch or asking an AI, 
you can just grab them and run.

Think of this as a personal toolbox of small, situational solutions — sometimes messy, sometimes experimental, but often useful.


ChatGPT może popełniać błędy. Sprawdź ważne informacje. Zobacz Preferencje dotyczące plików cookie.

Zawsze pokazuj szczegóły

# Wygenerowanie pliku README.md w katalogu /mnt/data, żeby można go było pobrać
readme_content = """# 🗃️ My Little Python Scripts

A collection of small Python scripts and apps solving specific problems.  
Each folder contains the source code, executables, and related files.

## 📁 Contents

#### Lorem Ipsum Generator <br>
Generates placeholder text (Lorem Ipsum) of custom length. Useful for testing layouts, documents, or web designs quickly.

#### TXT Comparison <br>
Compares two `.txt` files and highlights differences. Handy for quickly spotting changes in text data or code files.

## 🤔 Purpose

These are ready-to-use scripts that may come in handy someday.  
Instead of writing quick scripts from scratch or asking an AI, you can just grab them and run.  
Think of this as a personal toolbox of small, situational solutions — sometimes messy, sometimes experimental, but often useful.

## ⬇️ How to get a specific script

If you want to download just one script instead of the whole repository, you can use Git's sparse checkout feature:

1. **Clone the repository without checking out files:**
```bash
git clone --no-checkout https://github.com/vGiacomov/My-Little-Python-Scripts.git MLPS
cd MLPS 
```

2. **Enable sparse checkout:**

```bash
git sparse-checkout init --cone
```
**Choose the folder you want:**

##### ***To get Lorem Ipsum Generator:***

```
git sparse-checkout set "Lorem Ipsum Generator"
```
##### ***To get TXT Comparison:***

```
git sparse-checkout set "TXT Comparison"
```


##### Checkout the main branch:

```
git checkout main
```
Now you will have only the folder you need, without downloading the entire repository.

## ⚠️ Warning


No guarantees. Some of these scripts are old, some are messy, and some are just plain unnecessary.  
But they worked once. That’s good enough for me.

