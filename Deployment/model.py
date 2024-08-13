# Import all the libraries that are going to be used
import streamlit as st
import pandas as pd
import pickle

# Create a 
def run():
    # Load the file that will be used to predict the cluster
    with open('pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)

    # Create the input for each label to find the cluster
    order_id = st.number_input(label='Input Order ID!', min_value=000001.0, max_value=999999.0)
    product_category = st.selectbox(label='Choose Product Category!', options=['Laptops and Computers', 'Home Appliances', 'Charging Cables', 'Monitors', 'Batterie', 'Audio Devices', 'Phones and Accessories', 'Entertainment Devices'])
    product = st.selectbox(label='Choose Product!', options=['Macbook Pro Laptop', 'LG Washing Machine', 'USB-C Charging Cable', '27in FHD Monitor', 'AA Batteries (4-pack)', 'Bose SoundSport Headphones', 'AAA Batteries (4-pack)', 'ThinkPad Laptop', 'Lightning Charging Cable', 'Google Phone', 'Wired Headphones', 'Apple Airpods Headphones', 'Vareebadd Phone', 'iPhone', '20in Monitor', '34in Ultrawide Monitor', 'Flatscreen TV', '27in 4K Gaming Monitor', 'LG Dryer'])
    quantity_ordered = st.number_input(label='Input Quantity Ordered!', min_value=1.0, max_value=30.0)
    price_each = st.number_input(label='Input Price Each Ordered Item!', min_value=1.0, max_value=5000.0)
    order_date = st.date_input("When's the Order Date?", value=None)    
    purchase_address = st.text_input("Enter Purchase Address!", "")
    month = st.selectbox(label='What Month is the Order Made in?', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    sales = st.number_input(label='Input Amount of Sales!', min_value=1.0, max_value=510000.0)
    city  = st.selectbox(label='In Which City Was the Order Made?', options=[' New York City', ' San Francisco', ' Atlanta', ' Portland', ' Dallas', ' Los Angeles', ' Boston', ' Austin', ' Seattle'])
    hour  = st.selectbox(label='In Which Hour Was the Order Made?', options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24])
    time_of_day = st.selectbox(label='Which Time of Day Was the Order Made?', options=['Night', 'Morning', 'Evening', 'Afternoon'])

    # Telling user the next part
    st.write('The following is the result:')

    # Labeling the inputs as the data inference to be clustered
    data_inf = pd.DataFrame({
        'order_id': [order_id],
        'product_category': [product_category],
        'product': [product],
        'quantity_ordered': [quantity_ordered],
        'price_each': [price_each],
        'order_date': [order_date],
        'purchase_address': [purchase_address],
        'month': [month],
        'sales': [sales],
        'city': [city],
        'hour': [hour],
        'time_of_day': [time_of_day]
    })

    # Putting the data inference as a label
    st.table(data_inf)

    # Make a button that will show the cluster
    if st.button(label='Cluster'):
        # Data Dummy prediction
        cluster = pipeline.predict(data_inf)
        st.metric(label="Here is the Cluster:", value=cluster[0])

        product0 = '''USB-C Charging Cable    
        Lightning Charging Cable  
        AAA Batteries (4-pack)  
        AA Batteries (4-pack)  
        Wired Headphones
        '''

        product1 = '''Macbook Pro Laptop  
        LG Washing Machine  
        27in FHD Monitor  
        ThinkPad Laptop  
        Apple Airpods Headphones
        '''

        if cluster[0] == 0:
            st.write("Cluster 0 adalah customer yang melakukan pembelian pada waktu tengah malam hingga menjelang sore atau sebelum jam 15:00. Kemungkinan adalah cluster ini untuk para customer yang memiliki urgensi membeli barang elektronik yang dibutuhkan disaat sudah tidak memiliki persediaan cadangan dan customer pada cluster ini memiliki lebih banyak waktu luang untuk membeli barang elektronik.")
            st.write(f"##### Recommended products: ")
            st.markdown(product0)
        else:
            st.write("Cluster 1 adalah customer yang melakukan pembelian pada waktu sore hari hingga menjelang tengah malam, atau pada jam 15:00 hingga mendekati jam 00:00. Kemungkinan customer pada cluster ini adalah customer yang sibuk bekerja di luar rumah, karena jam pembelian cluster ini dapat disimpulkan berada pada jam luar kantor. Jadi kemungkinan adalah customer pada cluster ini biasanya melakukan pembelian berbarengan dengan pulang kantor.")
            st.write(f"##### Recommended products: ")
            st.markdown(product1)

# Running the function
if __name__ == "__main__":
    run()