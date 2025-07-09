# Pixela Habit Tracker

![Pixela Example Graph](https://pixe.la/v1/users/shoaib27/graphs/shoaib4)

A Python script to track habits using the Pixela API, featuring create/update/delete functionality with visual progress tracking.

## 📌 Features
- **Daily habit tracking** with quantitative measurement
- **Full CRUD operations** (Create, Read, Update, Delete)
- **Visual progress calendar** with color-coded intensity
- **Customizable metrics** (km, pages, minutes, etc.)
- **Streak maintenance** to build consistent habits

## ⚙️ Technologies
- Python 3
- Requests library
- Pixela API
- JSON data formatting

## 🚀 Setup

### Prerequisites
- Python 3.x installed
- Pixela account (created automatically by script)
- Requests library (`pip install requests`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pixela-habit-tracker.git
   cd pixela-habit-tracker
   ```

2. Edit the script with your credentials:
   ```bash
   USERNAME = "your_username"  # Lowercase letters, numbers, hyphens
   TOKEN = "your_secret_token"  # 8-128 characters
   GRAPH_ID = "graph1"  # ID for your habit graph
   ```

## 🛠️ Usage
Run the script:
```bash
python main.py
```

### Available Functions:
1. **Create User** (uncomment lines 10-11)
2. **Create Graph** (uncomment lines 23-24)
3. **Add Today's Entry** (lines 32-38)
4. **Update Entry** (uncomment lines 44-46)
5. **Delete Entry** (uncomment lines 52-54)

## 📊 Customization
Modify `graph_config` to change tracking parameters:
```python
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",  # Your habit name
    "unit": "Km",            # Measurement unit
    "type": "float",         # "float" or "int"
    "color": "ajisai"        # Graph color scheme
}
```

Available colors: `shibafu` (green), `momiji` (red), `sora` (blue), `ichou` (yellow), `ajisai` (purple), `kuro` (black)

## 📈 Example Use Cases
- Track daily cycling/running distance
- Log coding practice hours
- Monitor pages read per day
- Record meditation minutes
- Count daily glasses of water

## 📜 License
MIT License

## 🤝 Contributing
Pull requests welcome! For major changes, please open an issue first.

## ✉️ Contact
soaebhasan04@gmail.com  