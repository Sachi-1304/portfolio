import streamlit as st
from PIL import Image  # To handle images
import os

# Set page title and favicon
st.set_page_config(page_title="My Portfolio", page_icon="🌟", layout="wide")

# Sidebar
#import os
#image_path = os.path.abspath("static/profile.jpg")  # Get full path
#st.sidebar.image(image_path, width=150)
#st.sidebar.image("static/profile.jpg", width=150)


st.sidebar.image("C:/Users/91724/Desktop/Projects/Portfolio/static/vaishnya.jpeg",width=150)
st.sidebar.title("Contact Me")
st.sidebar.write("📧 Email:chikyabhai6162@gmail.com")
st.sidebar.write("📞 Phone: +91 7058452004")
st.sidebar.write("🔗 [Instagram](https://www.instagram.com/vaish.navvvvvv?igsh=cmtsazdjMGt2cWlm)")

st.title("Hello, I'm Vaishnav👋- UI/UX Designer")
st.write("")
st.write("")
st.subheader("Aspiring UI/UX Developer | Designer | Figma Beginner")
st.markdown("<p style='font-size:18px;'>Crafting Beautiful & User-Friendly Experiences</p>",unsafe_allow_html=True)
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.subheader("🖼️ Featured Projects")
projects = [
    {"title": "E-commerce web design", "image1": "C:/Users/91724/Desktop/Projects/Portfolio/static/page1.jpeg",
     "image2":"C:/Users/91724/Desktop/Projects/Portfolio/static/page2.jpeg" , "image3":"C:/Users/91724/Desktop/Projects/Portfolio/static/page3.jpeg",
     "image4":"C:/Users/91724/Desktop/Projects/Portfolio/static/end.jpeg",
     "description": "Revamped the UI of leading Sneaker Brand."},
    
]

for project in projects:
    col1, col2 , col3 ,col4= st.columns([1, 2 , 3 , 4])
    with col1:
        img = Image.open(project["image1"])
        st.image(img, use_container_width=True)
    with col2:
        img = Image.open(project["image2"])
        st.image(img, use_container_width=True)
    with col3:
        img = Image.open(project["image3"])
        st.image(img, use_container_width=True)
    with col4:
        img = Image.open(project["image4"])
        st.image(img, use_container_width=True)


st.subheader("🛠️ Skills & Tools")
skills = [
    "🎨 UI/UX Design",
    "🖍️ Wireframing & Prototyping",
    "📱 Mobile & Web Design",
    "🖌️ Tools: Figma, Adobe XD, Sketch"
]
for skill in skills:
    st.write(f"- {skill}")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")


st.subheader("📩 Get in Touch")
contact_form = """
<form action="https://formspree.io/f/1" method="POST">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)