import streamlit as st
import requests as r
from goto import with_goto
# from goto import goto, label
name = st.text_input('Name')

response = r.post("https://web-production-07d4.up.railway.app/getusers",{"name" : name})
response1 = response.json()
# st.button("search")
# st.text("hello")
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if (st.button("search") and response.ok) or st.session_state.current_index != 0:
    articles = response1["articles"]
    i = 0 
    col1, col2 = st.columns([0.15,1])
#     # label .start
    if st.session_state.current_index < len(articles)-1:
        with col2:
            show_next = st.button("next")
    else:
        show_next = False
    # if st.session_state.current_index > 0:
    #     with col1:
    #         show_prev = st.button("prev")
    if st.session_state.current_index ==0:
        with st.container():
            col3, col4 = st.columns([3,2])
            #     while True:
            with col3:
                st.write(articles[st.session_state.current_index]["test"])
            with col4:
                st.write(articles[st.session_state.current_index]["sentiment"])
        st.session_state.current_index += 1
    col3, col4 = st.columns([3,2])   
    if show_next and st.session_state.current_index< len(articles) :
        # with col1:
        #     if st.button('previous'):
        #         i = i - 1

       with st.container():
        
        #     while True:
        with col3:
            st.write(articles[st.session_state.current_index]["test"])
        with col4:
            st.write(articles[st.session_state.current_index]["sentiment"])
        st.session_state.current_index += 1
        # with col2:
        #     if st.button('next'):
        #         i = i + 1

    # elif show_prev:
    #     with st.container():
    #     # col3, col4 = st.columns([3,2])
    #     #     while True:
    #         with col3:
    #             st.write(articles[st.session_state.current_index]["test"])
    #         with col4:
    #             st.write(articles[st.session_state.current_index]["sentiment"])
    #     st.session_state.current_index -= 1 



    




# my_list = ["a", "b", "c"]
# show_next = st.button("next")

# # Initialize the current index
# if "current_index" not in st.session_state:
#     st.session_state.current_index = 0
   
# # Whenever someone clicks on the button
# if show_next:
#     # Show next element in list
#     st.write(my_list[st.session_state.current_index])
#     # Update and store the index
#     st.session_state.current_index += 1
