import streamlit as st

# Streamlit 웹 애플리케이션 제목
st.title("Secure login Page Example")

# 두 가지 로그인 페이지 선택
login_option = st.selectbox("Choose Login Page:", ["Login Page 1", "Login Page 2 with masking"])

# Login Page 1: 표준 비밀번호 필드 사용 (type="password")
if login_option == "Login Page 1":
    st.subheader("Login with Password Field")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")  # 비밀번호 필드를 사용
    if st.button("Login"):
        st.write(f"Login 1 Submitted! Username: {username}, Password: {password}")

# Login Page 2: type="text"로 마스킹된 비밀번호 필드 사용
elif login_option == "Login Page 2 with masking":
    st.subheader("Login with Text Field and Masking")
    username = st.text_input("Username")
    password = st.text_input("Password (Masked as Text)", type="default")  # 일반 텍스트 필드
    if st.button("Login"):
        st.write(f"Login 2 Submitted! Username: {username}, Password: {password}")

    # CSS를 이용한 마스킹 처리 (-webkit-text-security: disc 유사 효과)
    st.markdown("""
        <style>
        input[type="text"] {
            -webkit-text-security: disc;
        }
        </style>
        """, unsafe_allow_html=True)
