import streamlit as st
import hashlib
import json
import time
from cryptography.fernet import Fernet
import base64

if 'failed attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"
if 'last_attempt_time' not in st.session_state:
    st.session_state.last_attempt_time = 0
    
    # function to Hash passkey
def hash_passkey(passkey):
        return hashlib.sha256(passkey.encode()).hexdigest()
    
    #Function to generate a key from passkey (for encryption)

def generate_key_from_passkey(passkey):
    hashed = hashlib.sha256(passkey.encode()).digest()

    return base64.urlsafe_b64encode(hashed[:32])
    
    #Function to encrypt data
def encrypt_data(text, passkey):
    key = generate_key_from_passkey(passkey)
    cipher = Fernet(key)
    return cipher.encrypt(text.encode()).decode()

    #Function to decrypt data
def decrypt(encrypted_text, passkey, data_id):
    try:
            # check if the passkey matches
        hashed_passkey = hash_passkey(passkey)
    if data_id in st.session_state.stored_data and st.session_state.stored_
            # if passkey matches decrypt data
            key = generate_key_from_passkey(passkey)
            cipher = Fernet(key)
            decrypted = cipher.decrypt(encrypted_text.encode()).decode()
            st.session_state.failed_attempt = 0
            return decrypted
        else:
            #increent failed
            st.session_state.failed_attempts += 1
            st.session_state.last_attempt_time = time.time()
            return None
    except Exception as e:
            # if decryption fails, increment failed attempts
        st.session_state.failed_atttempts += 1
        st.session_state.last_attempt_time = time.time()
        return None

            # Function to g neratea unique ID for data
def generate_data_id():
    import uuid
    return str(uuid.uuid4())

#Function to reset failed attempts
def reset_failed_attempts():
    st.session_state.failed_attempts = 0

     # Function to change the page
def change_page(page):
 ✨ st.session_state.current_page = page

    #Streamlit UI
st.title("🔒 Secure Data Encryption System")

#Navigation
menu = ["home", "Store Data", "Retrive Data", "Login" ]
choice = st.sidebar.selectbox("Navigation", menu, index=menu.index(st.session_state.current_page))

# Update current page base on selection
st.session_state.current_page = choice

#Check if too many failed attempts
st.session_state.failed_attempts >= 3:

#force redirect to login page
st.session_state.current_page = "Login"
st.warning("🔒 too many failed attempts! Reauthorization required.")

#Display current page
if st.session_state.current_page =="Home":
     st.subheader("🏠 Welcome to the Secure Data System")
     st.write("Use this app to **Security store and retrieve data** using unique")

     col1, col2 = st.columns(2)
     with col1:
          if st.button("Store New Data", use_container_width=True):
               change_page("Store Data")
    with col2:
        if st.button("Retrive Data", use_container_width=True):
            change_page("Retrive Data")
    # Display Store data count
    st.info(f" Currently storing {len(st.session_state.stored_data)}encrypted data")

st.session_state.current_page == "Store Data":
st.subheader("📁Store Data Securely")
user_data = st.text_area("Enter Data: ")
passkey = st.text_input("Enter Passkey:", type="password")
confirm_passkey = st.text_input("Confirm Passkey:", type="Password")

if st.button("Encrypt & Save"):
    if user_data and passkey and confirm_passkey:
        if passkey != confirm_passkey:
            st.error("⚠ Passkeys do not match")
        else:
            #Generate a unique ID for this data
            data_id = generate_data_id()

            #Hash the Passkey
            hashed_passkey = hash_passkey(passkey)    

            (variable) encrypted_text: str
            encrypted_text = encrypt_data(user_data, passkey)

            st.session_state.stored_data(data_id) = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success("✅ Data Stored Securely!")
            st.code(data_id, language="text")
            st.info("⚠ Save this Data ID! You'll need to it to retrive your")
        else: 
            st.error("⚠ All fields are required!")    

    elif st.session_state.current_page == "Retrieve Data":
        st.subheader("🔍 Retrieve Your Data")

        # Show attempts remaining 
        attempts_remaining = 3 - st.session_state.field_attempts
        st.info(f"Attempts remaining: {attempts_remaining}")

        data_id = st.text_input("Enter Data ID:")
        passkey = st.text_input("Enter_passkey:", type="password")

        if st.button(("Decrypt"))
            if data_id and passkey:
                if data_id in st.session_state.stored data:
                    encrypted_text = st.session_state.stored_data[data_id]["encrypted_text"]
                    decrypted_text = decrypt_data (encrypted_text, passkey, data_id)

                    if decrypted_text:
                        st.success("✅ Decryption successful!")
                        st.markdown("### Your Decrypted Data:")
                        st.code(decrypted_text, language="text")
                    else:
                        st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - st.session_state.failed_attempts}")
                else:
                    st.error ("❌ Data ID not found!")

                # Check if too many failed attempts after this attempt
                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.session_state.current_page = "Login"
                    st.return() # Update from experimental_rerun()
            else:
                st,error(" ⚠ Both fields are required!")

            elif st.session_state.current_page =="Login":
                st.subheader("🔑 Reauthorization Required")

                # Add a simple timeout mechanism
                if time.time() - st.session_state.last_attempt_time < 10 and st.session_state.failed_attempts >= 3:
                    remaining_time = int(10 - (time.time() - st.session_state.last_attempt))
                    st.warning(f"⌚ Please wait {remaining_time} seconds before trying again.")
                else:
                    login_pass = st.text_input("Enter Master Password:", type="password")

                    if st.button("Login"):
                        if login_pass == "admin123": #Hardcoded for demo, replace with
                            reset_failed_attempts()
                            st.success("✅ Reauthorized successfully!")
                            st.session_state.current_page = "Home"
                            st.return() #Updated from experimental_rerun()
                        else:
                            st.error("❌ Incorrect password!")

            # Add a a footer
            st.markdown("------")
            st.markdown("🔒 Secure Data Encryption System! Educational Project")






        else:
            st.error("")    













            


          


