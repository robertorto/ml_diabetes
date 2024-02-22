"""Este código visa implementar funcionalidades de autenticação simples em uma aplicação streamlit."""

import hmac
import streamlit as st
"""O modulo hmac é usado aqui para fazer uma comparação segura entre a senha inserida e a armazenada"""

# defininco a função que vai implementar a funcionalidade de autenticação
def check_password():
    """Retorna verdadeiro se o usuário tiver a senha correta."""

    def passwor_entered():
        """Faz o check se a senha colocada pelo usuário for correta."""
        
        if hmac.compare_digest(st.session_state['password'], st.secrets['password']):
            st.session_state['password_correct'] = True
            del st.session_state['password']
        else:
            st.session_state['password_correct'] = False
    
    # Retorna True se o password for validado.
    if st.session_state.get('password_correct', False):
        return True
    
    # Mostra o valor do input da senha.
    st.text_input(
        'Password', type='password', on_change=passwor_entered, key='password'
    )
    if 'password_correct' in st.session_state:
        st.error('😕 Password incorrect')
    return False