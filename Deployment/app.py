# Import Libraries that are going to be used
import streamlit as st
import eda
import model

# Create the sidebar navigation
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploratory Data Analysis', 'Recommendation Based on Cluster'])

# Creating the features for each page
# Creating the home page features which includes title, informations, objective, background, conclusion, and recommendations
if page == 'Home Page':
    st.header('Welcome Page')
    st.write('')
    st.title('Ecorse')

    st.subheader('Kelompok Kami: ')
    name = '''Gracia Valerine  
    Ryan Trisnadi  
    Syihabuddin Ahmad Satisma  
    Vincent Kaunang  
    '''
    st.markdown(name)

    st.subheader('HCK 017 - Kelompok 2')
    st.write('')
    st.caption('Select page')
    st.write('')
    st.write('')

    with st.expander("Tujuan"):
        st.caption(""" Tujuan dari pembuatan model rekomendasi alat keperluan elektronik adalah untuk meningkatkan pengalaman belanja pelanggan dengan memberikan saran produk yang lebih relevan dan personal. Model ini bertujuan untuk menganalisis data historis pembelian, preferensi pelanggan, serta pola perilaku konsumen guna mengidentifikasi produk yang paling sesuai dengan kebutuhan dan minat masing-masing individu. Dengan rekomendasi yang lebih tepat sasaran, diharapkan dapat meningkatkan tingkat kepuasan pelanggan, mengurangi waktu yang diperlukan untuk menemukan produk yang diinginkan, serta mendorong peningkatan penjualan dan loyalitas pelanggan. 
        """)

    with st.expander("Latar Belakang"):
        st.caption(""" 
        Latar belakang kami mengangkat proyek ini adalah karena tingginya penjualan barang elektronik yang terus meningkat seiring berjalannya waktu. Untuk meningkatkan performa dan kualitas toko elektronik kami, kami membuat model machine learning yang bertujuan untuk memberikan rekomendasi produk terkait atau serupa berdasarkan riwayat pencarian customer di toko elektronik. Dengan demikian, kami berharap dapat meningkatkan pengalaman belanja customer dan mendorong penjualan lebih lanjut.
        """)

    with st.expander("Kesimpulan"):
        st.caption(""" Berdasarkan data penjualan barang elektronik, dapat diketahui bahwa pembeli lebih banyak membeli produk dengan kategori audio & devices, charging cable, dan batterie. Tren penjualan menunjukkan bahwa Wired Headphone selalu menjadi produk yang paling banyak terjual setiap bulan selama tahun 2019, mencerminkan tingginya minat pelanggan pada kategori Audio & Devices.

Produk terlaris berdasarkan jumlah yang dipesan termasuk Baterai AAA dan AA (paket isi 4) serta kabel pengisian daya (USB-C dan Lightning), menunjukkan kebutuhan signifikan untuk aksesori smartphone. Headphone berkabel dan nirkabel, seperti Apple Airpods dan Bose SoundSport, juga sangat diminati. Selain itu, monitor 27 inci (baik FHD maupun 4K gaming) dan iPhone termasuk dalam produk terlaris, mencerminkan permintaan untuk peralatan tampilan berkualitas tinggi dan popularitas iPhone yang terus berlanjut.

Selama satu tahun terakhir, San Francisco mencatat nilai penjualan tertinggi dibandingkan kota lainnya, kemungkinan karena kota ini merupakan pusat pembelanjaan utama. Grafik penjualan menunjukkan bahwa transaksi paling sering terjadi pada siang dan sore hari, dengan produk yang lebih sering dibeli adalah laptop dan komputer, karena harga produk-produk ini cenderung lebih tinggi.

Distribusi jumlah pesanan per transaksi menunjukkan bahwa sebagian besar transaksi melibatkan pembelian satu unit, dengan sangat sedikit transaksi yang memesan lebih dari dua unit, menandakan bahwa pembelian dalam jumlah besar relatif jarang. Selain itu, distribusi harga per unit menunjukkan sebagian besar barang dihargai antara 0 dan 250, dengan beberapa puncak pada titik harga 500, 750, dan 1000, serta adanya produk premium dengan harga hingga 1750.

Penjualan mencapai puncaknya pada bulan Desember, yang dapat dikaitkan dengan promosi akhir tahun, sehingga meningkatkan total penjualan secara signifikan dibandingkan bulan lainnya.""")

# Creating the exploratory data analysis page that will run the eda.py file
elif page == 'Exploratory Data Analysis':
    eda.run()

# Creating the page that will predict the cluster and will recommend products
else:
    model.run()
