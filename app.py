import streamlit as st

# Mengatur judul tab browser
st.set_page_config(page_title="Aplikasi Pertamaku", page_icon="+")

# menampilkan judul dan teks diweb
st.title("Aplikasi Streamlit Pertamaku!")
st.write("Halo dunia! Jika kamu bisa melihat halaman ini,berarti kamu sudah **BERHASIL** meng-upload dan mendeploy aplikasi Streamlit dari GitHub.")

st.divider() #Garis pembatas

#Input sederhana
nama = st.text_input("Siapa namamu?")

# Tombol interaktif 
if st.button("Klik Saya!"):
    if nama:
        st.succes(f"Halo, {nama}! Selamat belajar Streamlit. Kamu hebat!")
        st.ballons() #Memunculkan animasi balon
    else:
        st.warning("Isi namamu dulu di kotak atas ya!")
