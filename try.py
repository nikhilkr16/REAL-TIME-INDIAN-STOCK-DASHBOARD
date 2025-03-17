import nselib
from nselib import capital_market
from nselib import derivatives
import streamlit as st 


try:
    from nselib import capital_market
    print("nselib imported successfully.")
except ImportError as e:
    print(f"Error importing nselib: {e}")
try:
    # Attempt to access a function from capital_market
    data = capital_market.equity_list()  # Replace with an actual function
    print("Function executed successfully, data retrieved.")
except Exception as e:
    print(f"Error executing function: {e}")
print(f"nselib version: {nselib.__version__}")  # Check if __version__ exists
print(dir(nselib))
