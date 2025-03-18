import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Personal Library Manager", layout="wide")

# Initialize session state for book storage
if "books" not in st.session_state:
    st.session_state.books = []

# Sidebar navigation
st.sidebar.title("📚 Personal Library Manager")
page = st.sidebar.selectbox("Select an option", ["Add Book", "View Library", "Search Book", "Delete Book"])

# Apply blue background color
st.markdown("""
    <style>
    body{
    background-color: #90EE90;
}
        .stApp {
            background-color: #90EE90;
        }
    </style>
""", unsafe_allow_html=True)

if page == "Add Book":
    st.markdown("""
        <h1 style='text-align: center;'>📚 Personal Library Manager</h1>
        <h3 style='text-align: center;'>➕ Add a New Book</h3>
    """, unsafe_allow_html=True)
    
    book_title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author")
    publication_year = st.number_input("Enter Publication Year", min_value=0, step=1)
    genre = st.text_input("Enter Genre")
    read_status = st.radio("Have you read this book?", ["Yes", "No"])
    
    if st.button("Add Book"):
        if book_title and author and genre:
            new_book = {"Title": book_title, "Author": author, "Year": publication_year, "Genre": genre, "Read": read_status}
            st.session_state.books.append(new_book)
            st.success("📖 Book added successfully!")
        else:
            st.warning("⚠️ Please fill in all fields!")

elif page == "View Library":
    st.markdown("<h1 style='text-align: center;'>📚 Your Library</h1>", unsafe_allow_html=True)
    
    if st.session_state.books:
        df = pd.DataFrame(st.session_state.books)
        st.dataframe(df)
    else:
        st.info("📭 No books added yet!")

elif page == "Search Book":
    st.markdown("<h1 style='text-align: center;'>🔍 Search for a Book</h1>", unsafe_allow_html=True)
    search_query = st.text_input("Enter book title or author")
    if search_query:
        results = [book for book in st.session_state.books if search_query.lower() in book["Title"].lower() or search_query.lower() in book["Author"].lower()]
        if results:
            st.dataframe(pd.DataFrame(results))
        else:
            st.warning("⚠️ No matching books found!")

elif page == "Delete Book":
    st.markdown("<h1 style='text-align: center;'>🗑 Delete a Book</h1>", unsafe_allow_html=True)
    if st.session_state.books:
        book_titles = [book["Title"] for book in st.session_state.books]
        book_to_delete = st.selectbox("Select a book to delete", book_titles)
        if st.button("Delete Book"):
            st.session_state.books = [book for book in st.session_state.books if book["Title"] != book_to_delete]
            st.success("🗑 Book deleted successfully!")
    else:
        st.info("📭 No books available to delete!")

