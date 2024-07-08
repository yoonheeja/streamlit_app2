import streamlit as st
# import openai
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import LLMChain

# OpenAI API 키 설정




st.title('ChatGPT with Streamlit')
st.write('This is a simple chatbot interface using Streamlit and OpenAI GPT-3.')

# # 객체 생성
# llm = ChatOpenAI(
#     temperature=0.1,  # 창의성 (0.0 ~ 2.0)
#     max_tokens=2048,  # 최대 토큰수
#     model_name="gpt-3.5-turbo",  # 모델명
# )


# # 초기 세션 상태 설정
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # 사용자의 입력을 받고 처리하는 함수
# def get_response(prompt):
#     llm_chain = LLMChain(prompt=prompt, llm=llm)
#     return response.choices[0].text.strip()

# # 사용자의 입력 받기
# user_input = st.text_input("You:", key="input")

# # 사용자 입력 처리
# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     response = get_response(user_input)
#     st.session_state.messages.append({"role": "assistant", "content": response})

# # 메시지 출력
# for message in st.session_state.messages:
#     if message['role'] == 'user':
#         st.write(f'**You:** {message["content"]}')
#     else:
#         st.write(f'**Chatbot:** {message["content"]}')