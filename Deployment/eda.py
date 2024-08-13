# Import the libraries that are going to used
import streamlit as st
import pandas as pd
from PIL import Image

# Create a funtion that will read and show the data from the csv file
@st.cache_data
def load_data():
    return pd.read_csv('df_clean_eda2.csv')

def run():
    # Title caption
    st.title('Welcome to Exploratory Data Analysis')

    # Create Product Categories Distribution
    st.title('Product Categories Distribution')
    image = Image.open('image.png')
    st.image(image, caption='Product Categories Distribution')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Berdasarkan data yang diperoleh, dapat diketahui bahwa dari penjualan barang elektronik, pembeli lebih banyak membeli barang dengan kategori audio & devices, charging cable & Batterie.')

    # Create Monthly Sales Trend
    st.title('Monthly Sales Trend')
    image = Image.open('image3.png')
    st.image(image, caption='Monthly Sales Trend')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Jika dilihat trend dari produk apa yang sering dibeli, didapatkan bahwa Wired Headphone adalah product yang penjualannya selalu berada di atas di setiap bulannya selama tahun 2019. Hal ini berkaitan dengan banyaknya customer yang membeli pada kategori Audio & Devices.')

    # Create Top Selling Products
    st.title('Top Selling Products')
    image = Image.open('image4.png')
    st.image(image, caption='Top Selling Products')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Produk terlaris berdasarkan jumlah yang dipesan termasuk Baterai AAA dan AA (paket isi 4), yang memiliki permintaan tinggi karena sering digunakan dalam berbagai perangkat. Kabel pengisian daya (USB-C dan Lightning) juga populer, menunjukkan kebutuhan signifikan untuk aksesori smartphone. Baik headphone berkabel maupun nirkabel, termasuk Apple Airpods dan Bose SoundSport, memiliki permintaan tinggi, menunjukkan pasar yang kuat untuk aksesori audio. Selain itu, monitor 27 inci (baik FHD maupun 4K gaming) termasuk dalam produk terlaris, menunjukkan permintaan untuk peralatan tampilan berkualitas tinggi. Yang perlu diperhatikan, iPhone juga berada di antara produk terlaris, mencerminkan popularitasnya yang terus berlanjut.')
    
    # Create Sales by City
    st.title('Sales by City')
    image = Image.open('image5.png')
    st.image(image, caption='Sales by City')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Selama 1 tahun terakhir, San Francisco adalah kota yang memiliki nilai penjualan tertinggi di antara kota lainnya. Hal ini dapat disebabkan oleh kemungkinan faktor pusat pembelanjaan yang terdapat pada kota San Francisco, karena dari grafik berikut tentang Count of Product by City, didapatkan bahwa San Francisco memiliki kecenderungan lebih unggul dari yang lainnya dalam produk distribusi.')
    
    # Create Sales by Category and Time of Day
    st.title(' Sales by Category and Time of Day')
    image = Image.open('image6.png')
    st.image(image, caption=' Sales by Category and Time of Day')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Pada grafik tersebut dapat disimpulkan bahwa, customer lebih sering melakukan pembelian pada saat Afternoon dan Evening. Lalu ada juga ditampilkan produk yang lebih sering dibeli adalah laptop and computers, hal ini dapat terjadi karena metrics yang digunakan adalah sum sales, dimana sales tersebut adalah total harga suatu product, dan hal ini sangatlah wajar karena produk laptop and computers cenderung memiliki harga yang lebih tinggi dibanding barang lainnya dalam satuan unit.')

    # Create Distribution Quantity Ordered
    st.title('Distribution Quantity Ordered')
    image = Image.open('image7.png')
    st.image(image, caption='Distribution Quantity Ordered')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Distribusi jumlah yang dipesan per transaksi sangat condong ke pembelian satu unit, menunjukkan bahwa sebagian besar transaksi melibatkan pembelian satu unit. Ada sangat sedikit transaksi di mana jumlah yang dipesan melebihi dua, yang menunjukkan bahwa pembelian dalam jumlah besar relatif jarang. Tren ini menyoroti preferensi utama untuk membeli barang tunggal per transaksi.')

    # Create Total Sales by hour
    st.title('Total Sales by hour')
    image = Image.open('image8.png')
    st.image(image, caption='Total Sales by hour')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Proses transaksi, pada toko elektronik secara online dapat terjadi selama 24 jam, dibuktikan dengan grafik berikut, namun total sales tertinggi ada pada siang hari dan sore hari menjelang malam.')

    # Create Distribution of Price Each
    st.title('Distribution of Price Each')
    image = Image.open('image9.png')
    st.image(image, caption='Distribution of Price Each')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Distribusi harga per unit menunjukkan bahwa sebagian besar barang dihargai antara 0 dan 250, menunjukkan bahwa barang dengan harga lebih rendah merupakan sebagian besar penjualan. Ada puncak yang terlihat pada berbagai titik harga, terutama sekitar 500, 750, dan 1000, menunjukkan bahwa barang dengan harga lebih tinggi juga terjual dengan baik. Selain itu, ada beberapa barang dengan harga tinggi, hingga 1750, yang menunjukkan keberadaan produk premium di pasar.')
    
    # Create Total Sales by Month
    st.title('Total Sales by Month')
    image = Image.open('image10.png')
    st.image(image, caption='Total Sales by Month')

    # Show Insights
    with st.expander('Insights:'):
        st.caption('Total penjualan dalam satuan harga produk memiliki peningkatan yang pesat pada bulan ke-12, hal ini dapat disangkut pautkan dengan promo akhir tahun, sehingga banyak barang yang promo yang jika ditotal memiliki penjualan yang jauh lebih signifikan dibanding bulan yang lainnya.')