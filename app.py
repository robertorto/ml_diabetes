import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import data_handler
import util
import pickle

# print('Abriu a página')

# verificar se a senha de acesso está correta
if not util.check_password():
    # se a senha estiver errada, para o processamento do app.
    print('usuário não logado')
    st.stop()

print('Carregou a página')



# vamos carregar os dados do dataset de diabetes
dados = data_handler.load_data()

# carrega o modelo de predição já treinado do dataset de diabetes ## modelo que já usei em outra disciplina.
model = pickle.load(open('./models/model.pkl', 'rb')) 

# começa a estrutura da interface do sistema
st.title('App dos dados de diabetes')

data_analyses_on = st.toggle('Exibir análise dos dados')

if data_analyses_on:
    st.header('Dados do dataset Diabetes')

    # exibir o dataframe
    st.dataframe(dados)

    # plota um histórico das idades dos pacientes

    st.header('Histograma de idades')
    fig = plt.figure()
    plt.hist(dados['Age'], bins=10)
    plt.xlabel('Idade')
    plt.ylabel('Quantidade')
    st.pyplot(fig)

    # plota um gráfico de barras com a contagem dos pacientes com diabetes
    st.header('Diabéticos')
    st.bar_chart(dados.Outcome.value_counts())

# daqui em diante vamos montar a inteface para capturar os dados de input do usuário para realizar a predição
# que vai identificar se um paciente possui ou não diabetes
st.header('Preditor de pacientes com diabetes')


# Atributos exibidos e utilizados pelo modelo de previsão:

# Pregnancies - 'int'
# Glucose - 'int'
# BloodPressure - 'int'
# Insulin - 'int'
# BMI - 'float'
# DiabetesPedigreeFunction - 'float'
# Age - 'int'
# Outcome - 'int' objetivo da previsão

# ordem ['Pregnancies', 'Glucose', 'BloodPressure', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# essas foram as informações utilizadas para treinar o modelo
# assim, todas essas informações também devem ser passadas para o modelo realizar a predição

# define a linha 1 de inputs com 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    # pregnancies -- digitar o número de gravidez que a paciente (se mulher)
    pregnancies = st.slider('How many pregnancies?', min_value=0, max_value=17, step=1 )

with col2:
    # glucose -- digitar o valor da glucose
    glucose = st.slider('What is the glucose level?', 0, 200, 120)

with col3:
    # BloodPressure -- digitar a pressão arterial do paciente
    blood_pressure = st.slider('Blood pressure level?', 0, 120, 60)



# define a linha 2 de inputs também com 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    # Insulin -- digitar o valor da glucose
    insulin = st.slider("Pacient's insulin level", 0, 900, 100)

with col2:
    # BloodPressure -- digitar a pressão arterial do paciente
    bmi = st.slider("Patient's BMI?", 0.0, 70.0, 30.0)

with col3:
    # DiabetesPedigreeFunction -- entrar com o valor da função pedigree
    diabetes_pedigree_function = st.slider("Pacient's PedigreeFunction", 0.00, 2.50, 0.05)


# define a linha 3 de inputs com 2 colunas
col1, col2 = st.columns(2)

with col1:
    # age -- digitar a idade em anos
    age = st.slider('How old are the patient?', 0, 100, 25)

with col2:
    # Botão que serve pra fazer a verificação
    submit = st.button('Verificar')



# Como todos os valores deste dataset já são numéricos, não precisamos fazer o data mapping
# Vamos criar um dicionário para armazenar todos os dados do paciente

paciente = {}


# verificar se o botão submit foi pressionado e se o campo Outcome está em cache
if submit or 'outcome' in st.session_state:


    # setando todos os attributos dos paciente na ordem do modelo de previsão
    paciente = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': diabetes_pedigree_function,
        'Age': age,
    }
    print(paciente)

    # converte o paciente para dataframe do pandas para ter o mesmo tipo de dados usado para o treino do modelo
    values = pd.DataFrame([paciente])
    print(values)

    # realiza a predição de diabetes dos pacientes com base nos dados inseridos pelo usuário
    results = model.predict(values)
    print(results)

    
    # o modelo foi treinado para retornar uma lista com 0 ou 1, onde cada posição da lista indica se o paciente tem Diabetes (1) ou não (0)
    # como estamos realizando a predição de somente um paciente por vez, o modelo deverá retornar somente um elemento na lista
    if len(results) == 1:
        # converte o valor retornado para inteiro
        outcome = int(results[0])
        
        # verifica se o paciente tem diabetes ou não
        if outcome == 1:
            # se sim, exibe uma mensagem que o paciente apresente diabetes
            st.subheader('Paciente diagnosticado com Diabetes 😢')
            if 'outcome' not in st.session_state:
                st.snow()
        else:
            # se não, exibe uma mensagem que o paciente não apresenta diabetes
            st.subheader('Paciente NÃO apresenta Diabetes! 😃🙌🏻')
            if 'outcome' not in st.session_state:
                st.balloons()
        
        # salva no cache da aplicação se o paciente tem diabetes
        st.session_state['outcome'] = outcome



    # verifica se existe um paciente e se já foi verificado se ele possui ou não diabetes
    if paciente and 'outcome' in st.session_state:
        # se sim, pergunta ao usuário se a predição está certa e salva essa informação
        st.write("A predição está correta?")
        col1, col2, col3 = st.columns([1,1,5])
        with col1:
            correct_prediction = st.button('👍🏻')
        with col2:
            wrong_prediction = st.button('👎🏻')
        
        # exibe uma mensagem para o usuário agradecendo o feedback
        if correct_prediction or wrong_prediction:
            message = "Muito obrigado pelo feedback"
            if wrong_prediction:
                message += ", iremos usar esses dados para melhorar as predições"
            message += "."
            
            # adiciona no dict do paciente se a predição está correta ou não
            if correct_prediction:
                paciente['CorrectPrediction'] = True
            elif wrong_prediction:
                paciente['CorrectPrediction'] = False
                
            # adiciona no dict do paciente se ele sobreviveu ou não
            paciente['Outcome'] = st.session_state['outcome']
            
            # escreve a mensagem na tela
            st.write(message)
            print(message)
            
            # salva a predição no JSON para cálculo das métricas de avaliação do sistema
            data_handler.save_prediction(paciente)
    
    st.write('')
    # adiciona um botão para permitir o usuário realizar uma nova análise
    col1, col2, col3 = st.columns(3)
    with col2:
        new_test = st.button('Iniciar Nova Análise')
        
        # se o usuário pressionar no botão e já existe um paciente, remove ele do cache
        if new_test and 'outcome' in st.session_state:
            del st.session_state['outcome']
            st.rerun()


# calcula e exibe as métricas de avaliação do modelo aqui, somente a acurária está sendo usada
# TODO: adicionar as mesmas métricas utilizadas na disciplina de treinamento e validação do modelo (recall, precision, F1-score)
accuracy_predictions_on = st.toggle('Exibir acurácia')

if accuracy_predictions_on:
    # pega todas as predições salvas no JSON
    predictions = data_handler.get_all_predictions()
    # salva o número total de predições realizadas
    num_total_predictions = len(predictions)
    
    # calcula o número de predições corretas e salva os resultados conforme as predições foram sendo realizadas
    accuracy_hist = [0]
    # salva o numero de predições corretas
    correct_predictions = 0
    # percorre cada uma das predições, salvando o total móvel e o número de predições corretas
    for index, paciente in enumerate(predictions):
        total = index + 1
        if paciente['CorrectPrediction'] == True:
            correct_predictions += 1
            
        # calcula a acurracia movel
        temp_accuracy = correct_predictions / total if total else 0
        # salva o valor na lista de historico de acuracias
        accuracy_hist.append(round(temp_accuracy, 2)) 
    
    # calcula a acuracia atual
    accuracy = correct_predictions / num_total_predictions if num_total_predictions else 0
    
    # exibe a acuracia atual para o usuário
    st.metric(label='Acurácia', value=round(accuracy, 2))
    # TODO: usar o attr delta do st.metric para exibir a diferença na variação da acurácia
    
    # exibe o histórico da acurácia
    st.subheader("Histórico de acurácia")
    st.line_chart(accuracy_hist)