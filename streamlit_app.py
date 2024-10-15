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
    username = st.text_input("Username")  # 사용자 이름은 마스킹하지 않음
    
    # HTML로 비밀번호 입력 필드 생성 (CSS 적용을 위해)
    password_html = '''
    <input type="text" id="password_input" style="-webkit-text-security: disc;" placeholder="Password" />
    '''
    st.markdown(password_html, unsafe_allow_html=True)  # 비밀번호 필드에만 CSS 적용

 
    if st.button("Login"):
        st.write(f"Login 2 Submitted! Username: {username}, Password: [Masked]")