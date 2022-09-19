import streamlit as st



#criando um menu

st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Slecione a página', ['Página 1', 'Página 2'])


if paginaSelecionada == 'Página 1':
    st.title('Página 01')
    st.selectbox('Escolha uma das opções', ['Opção 01', 'Opção 02'])  

    start_color, end_color = st.select_slider(
        'Select a range of color wavelength',
        options=['vermelho', 'orange', 'yellow', 'green', 'azul', 'indigo', 'violet'],
        value=('vermelho', 'azul'))
    st.write('Você selecionou comprimentos de onda entre', start_color, 'and', end_color)





elif paginaSelecionada == 'Página 2':
    st.title('Página 02')
    color = st.select_slider(
        'Selecione uma cor',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('Minha cor favorita é', color)
