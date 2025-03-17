from nselib import capital_market
from nselib import derivatives
import streamlit as st 
import pandas as pd
from datetime import datetime, timedelta

# FIRST OF ALL I HAD CHECKED THE NSELIB PROPERLY IMPORTED OR NOT
try:
    from nselib import capital_market
    print("nselib imported successfully.")
except ImportError as e:
    print(f"Error importing nselib: {e}")

# HEADING PART OF MY DASHBOARD
st.header("INDIAN STOCK  DASHBOARD 2025")

# SELECT BOX CREATED
instrument = st.sidebar.selectbox("Instrument Type", options=("NSE Equity Market", "NSE Derivative Market"))

# CONDITION APPLYING IF SELECT THIS THEN THIS

if instrument == "NSE Equity Market":
    data_info = st.sidebar.selectbox("Data to extract", options=(
        "price_volume_and_deliverable_position_data",
        "price_volume_data",
        "deliverable_position_data",
         "bhav_copy_with_delivery",
        "bhav_copy_equities",
        "equity_list",
        "fno_equity_list",
        "fno_index_list",
        "nifty50_equity_list",
        "india_vix_data",
        "market_watch_all_indices",
        "Historical Data",
        "bulk_deal_data",
        "block_deals_data",
        "short_selling_data",
        "index_data",
        "var_begin_day",
        "var_1st_intra_day",
        "var_2nd_intra_day",
        "var_3rd_intra_day",
        "var_4th_intra_day",
        "var_end_of_day"
       
       
    ))

    # Initialize data to None
    data = None

    if (data_info == "equity_list") or (data_info == "fno_equity_list") or (data_info == "market_watch_all_indices") or (data_info == "nifty50_equity_list"):
        data = getattr(capital_market, data_info)()

    elif data_info in ["price_volume_and_deliverable_position_data", "price_volume_data", "deliverable_position_data"]:
        symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., SBIN)", "SBIN")
        period = st.sidebar.selectbox("Select Period", ["1M", "3M", "6M", "1Y"])

        # GETTING VALUE ERROR SO I USE TRY EXCEPT TO RESOLVE IT
        try:
            data = getattr(capital_market, data_info)(symbol=symbol, period=period)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.write("Please check the symbol and try again.")

    elif (data_info == "bhav_copy_equities") or (data_info == "bhav_copy_with_delivery"):
        date = st.sidebar.text_input("Date", "1-01-2025")
        data = getattr(capital_market, data_info)(date)

    elif (data_info == "block_deals_data") or (data_info == "bulk_deal_data") or (data_info == "india_vix_data") or (data_info == "short_selling_data"):
        try:
            period = st.sidebar.selectbox("Select Period", ["1M", "3M", "6M", "1Y"])
            data = getattr(capital_market, data_info)(period=period)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.write("Please check the period format and try again.")

    elif data_info in ["var_begin_day", "var_1st_intra_day", "var_2nd_intra_day", "var_3rd_intra_day", "var_4th_intra_day", "var_end_of_day"]:
        trade_date = st.sidebar.date_input("Select Trade Date", datetime.now())
        formatted_date = trade_date.strftime("%d-%m-%Y")
        try:
            data = getattr(capital_market, data_info)(trade_date=formatted_date)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.write("Please check the trade date and try again.")

    elif data_info == "Historical Data":
        symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., SBIN)", "SBIN")
        period = st.sidebar.selectbox("Select Period", ["1M", "3M", "6M", "1Y"])
        try:
            data = capital_market.price_volume_and_deliverable_position_data(symbol=symbol, period=period)
            if data is not None:
                st.write(f"Historical data for {symbol} over {period}:")
                st.write(data)
            else:
                st.warning("No data available for the selected symbol and period.")
        except Exception as e:
            st.error(f"Error fetching historical data: {str(e)}")
    else:
        try:
            data = getattr(capital_market, data_info)()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.write("No data available for the selected option.")

    # Display data if it exists
    if data is not None and data_info != "Historical Data":
        st.write(data)

#NSE DERIVATIVE MARKET CONDITIONS START

elif  instrument == "NSE Derivative Market":
    data_info = st.sidebar.selectbox("Data to extract", options = (
    "fno_bhav_copy",
    "participant_wise_open_interest",
    "participant_wise_trading_volume",
    "expiry_dates_future",
    "expiry_dates_option_index",
    "nse_live_option_chain",
    "future_price_volume_data",
    "option_price_volume_data"
))
     # Initialize data to None
    data = None

    if (data_info == "expiry_dates_future") or (data_info == "expiry_dates_option_index") :
        data = getattr(derivatives, data_info)()
    
    elif  (data_info=="participant_wise_trading_volume") or (data_info=="participant_wise_open_interest") or (data_info=="fno_bhav_copy"):
        date=st.sidebar.text_input("Date","1-02-2025")
        data= getattr(derivatives,data_info)(date)

    elif (data_info=="nse_live_option_chain"):
        ticker= st.sidebar.text_input("Ticker","BANKNIFTY")
        expiry_date=st.sidebar.text_input("Expiry Date","1-01-2025")
        data= derivatives.nse_live_option_chain(ticker,expiry_date=expiry_date)
    
    elif (data_info=="future_price_volume_data"):
        ticker=st.sidebar.text_input("Ticker","SBIN")
        type_=st.sidebar.text_input("Intrument Type","FUTSTK")
        period_=st.sidebar.text_input("Period","1M")
        data= derivatives.future_price_volume_data(ticker,type_,period=period_)

    elif(data_info=="option_price_volume_data"):
        ticker=st.sidebar.text_input("Ticker","BANKNIFTY")
        type_=st.sidebar.text_input("Intrument Type","OPTIDX")
        period_=st.sidebar.text_input("Period","1M")
        data=derivatives.option_price_volume_data(ticker,type_,period=period_)
# TICKER MEANS particular stock on a stock exchange
    else:
        try:
            data = getattr(capital_market, data_info)()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.write("No data available for the selected option.")

    # Display data if it exists
    if data is not None and data_info != "Historical Data":
            st.write(data)


