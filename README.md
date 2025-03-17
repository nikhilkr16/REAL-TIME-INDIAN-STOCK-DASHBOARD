# 🚀 Real-Time Indian Stock Market Dashboard

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![NSELib](https://img.shields.io/badge/NSELib-Latest-green)

A powerful and interactive dashboard for real-time monitoring of Indian stock market data. Built with Streamlit and NSELib, this dashboard provides comprehensive market insights and analysis tools.

**Live Demo**: [View the Dashboard](https://real-time-indian-stock-dash.streamlit.app/)

**Reference Repository**: [NSELib by RuchiTanmay](https://github.com/RuchiTanmay/nselib)

---

## ✨ Features

### 📊 NSE Equity Market Data
- Real-time price and volume data
- Deliverable positions tracking
- Bulk and Block deals monitoring
- Historical data analysis
- Market indices tracking
- Equity and F&O lists

### 📈 NSE Derivative Market Data
- F&O Bhav copy
- Participant-wise open interest
- Live option chain analysis
- Future price volume data
- Option price volume data
- Trading volume analytics

### 🎯 Key Highlights
- Real-time data updates
- Interactive user interface
- Comprehensive market coverage
- Easy-to-use filters and selectors
- Detailed analytical views

---

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/nikhilkr16/REAL-TIME-INDIAN-STOCK-DASHBOARD.git
cd REAL-TIME-INDIAN-STOCK-DASHBOARD
 ```

2. Create and activate virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install required packages
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Run the Streamlit app
```bash
streamlit run nse_dashboard.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## 📊 Available Data Types

### Equity Market
- Price Volume Data
- Deliverable Position Data
- Bhav Copy
- Market Indices
- Bulk/Block Deals
- Short Selling Data
- VIX Data
- VAR Data

### Derivative Market
- F&O Bhav Copy
- Option Chain Analysis
- Future Price Volume
- Option Price Volume
- Trading Statistics

## 💡 Tips for Usage

1. **For Stock Data:**
   - Use correct stock symbols (e.g., SBIN, TCS)
   - Select appropriate time periods
   - Check for working days only

2. **For Derivative Data:**
   - Use valid expiry dates
   - Check instrument types carefully
   - Monitor period selections

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Nikhil Kumar**
- GitHub: [@nikhilkr16](https://github.com/nikhilkr16)

## 🙏 Acknowledgments

- NSELib for providing the data interface
- Streamlit for the amazing web framework
- Indian National Stock Exchange for the market data
- RuchiTanmay for the NSELib reference repository



---
⭐ Star this repository if you find it helpful!
