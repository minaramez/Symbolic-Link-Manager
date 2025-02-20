## **Symbolic Link Manager**

### **Description**
This Python script automates the creation, deletion, and reporting of symbolic links in the user's home directory on **CentOS 8 Linux**. It provides an easy-to-use menu-driven interface, allowing users to manage symbolic links without needing to use command-line tools like `ln`, `find`, and `readlink`.

### **Features**
- **Create symbolic links** for files in the system.
- **Delete symbolic links** from the home directory.
- **Generate a summary report** of all symbolic links, including their target paths.
- **User-friendly menu** for easy interaction.

---

## **Prerequisites**
- Python 3 installed
- **CentOS 8** or a similar Linux-based system

---

## **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/minaramez/Symbolic-Link-Manager.git
   cd Symbolic-Link-Manager
   ```
2. Ensure the script has execute permissions:
   ```bash
   chmod +x shortcut.py
   ```

---

## **Usage**
Run the script using:
```bash
./shortcut.py
```
or
```bash
python3 shortcut.py
```

### **Menu Options**
| Option | Description |
|--------|-------------|
| 1 | Create a symbolic link |
| 2 | Delete a symbolic link |
| 3 | Generate a summary report of symbolic links |
| quit | Exit the script |

---

## **Example Output**
### **Creating a Symbolic Link**
```
Select an option:
1. Create symbolic link
2. Delete symbolic link
3. Generate summary report
Type 'quit' to exit
Enter option (1-3), or 'quit' to exit: 1

Enter filename or path: /home/student/file.txt
File found in directory '/home/student/'
Do you wish to proceed? (Y/N): Y
Symbolic link created.
```

### **Deleting a Symbolic Link**
```
Enter filename: file.txt
File found in directory '/home'
Do you wish to proceed? (Y/N): Y
Symbolic link deleted.
```

### **Generating a Summary Report**
```
Summary report:
Number     Symbolic link                                      Target path                                        
1          file.txt                                          /home/student/file.txt                              
2          example_link                                      /var/www/html/index.html                           
```

---

### License
This script is released under the **MIT License**, which allows modification, distribution, and use with minimal restrictions.
