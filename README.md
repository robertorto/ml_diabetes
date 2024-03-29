# ml_diabetes


## Descrição geral do projeto

Este é o projeto de avaliação da disciplina de Implantação da primeira turma da pós graduação em Big Data e Data Science.
Visa cumprir os requisitos do trabalho descritos no arquivo Trabalho.pdf

## Equipe do trabalho
Roberto Torres de Almeida & Wagner Chiodi

## Escolha da aplicação
Escolhemos a sugestão do professor, que é um previsor para pacientes com diabetes.

## Selecionar um modelo treinado
Selecionamos um modelo que o Roberto trabalhou na disciplina de "Análise de Desempenho de Modelos"
Na trabalho avaliamos os seguintes modelos: KNN, Regressão Logística, Decision Tree e Random Forest. 
Entre eles o melhor score otimizado foi obtido no modelo RF (Random Forest), por isso o escolhem opara fazer nossas previsões.
Importamos ele usando o Pickle e tomamos cuidados com os requerimentos das bibliotecas usadas.

## O projeto
Usamos o VS Code para criar o projeto, conforme orientações das aulas.
Usamos o streamlit para nos ajudar com as questões de front-end e comunicação com back-end.
Criamos uma máquina free tier na Amazon EC2, configuramos para poder usar python e clonamos o projeto do git para lá.
Através do Screen deixamos o projeto funcionado mesmo sem conexão 
Enviamos os links do github e do endereço externo para acessar o streamlit

# Acesso
http://34.228.81.245:8501/
senha: streamlit1234

## App
Através da pagina do streamlit fizemos:
    - controle de entrada por senha
    - interação do usuario para entrada de novos dados
Usamos json para passar os dados para o modelo de previsão
Devolvemos os resultados da previsão e pedimos o feedback do usuário sobre a previsão.
Ainda apresentamos a acurária recalculada após feedback.

## Curiosidades
Grupo formado por dois alunos sem formação formal na área (Engenheiro Mecânico e Mecatrônico)
Primeira vez de uso do VS CODE.
Primeira vez usando máquina EC2.
Primeira vez com Ubuntu.
Primeira vez usando Git.

## Agradecimentos
Agradecemos todo o conhecimento passado, foi uma disciplina muito importante pelo link entre teoria e aplicação prática.
Excelente conhecimento, didática e compromisso com os alunos.
Muito obrigado!!!!