import streamlit as st

st.title("Football Players")

col1, col2 = st.columns(2)

with col1:
    st.header("Cristiano Ronaldo")
    st.image("https://media.gettyimages.com/id/962792890/photo/real-madrid-v-liverpool-uefa-champions-league-final.jpg?s=594x594&w=gi&k=20&c=WhQNV-XBm7BX-SGE8KQByviIif2jz8buNYGm3zISfc4=")
    vote1= st.button("Vote for Cristiano Ronaldo")

with col2:
    st.header("Lionel Messi")
    st.image("https://wallpapers.com/images/featured/messi-4k-ultra-hd-t7otmb1xwl662a0r.jpg")
    vote2 = st.button("Vote for Lionel Messi")

if vote1:
    st.success("You voted for Cristiano Ronaldo!")
if vote2:
    st.success("You voted for Lionel Messi!")

