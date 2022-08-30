from functions import *

# config layout
st.set_page_config(page_title='Article summarization',
                   #layout = 'wide',
                   page_icon = 'img/icon.png',
                   initial_sidebar_state = 'collapsed'
                   )

# hold missing questions
missing_questions = st.sidebar.empty()

st.header('✂️ Article summarization')

st.write("""
          One of the most fantastic things about Transformers is its ability to summarize the text out-of-the-box. 
          This project shows how we can produce summaries from news articles using a model trained on news articles.
        """)
     
#load the model and the data
info = st.empty()
info.info('⏳ Loading model: it may take a few seconds. Please, wait...')
model = load_model()
info.empty()

# ------------------------------------------------------------------------------------
st.markdown("""---""")
st.subheader('🔽 Enter the article link or the text itself')
text = st.text_area('', placeholder="Type here the text or the url to the article. Links MUST start with \"http\" or \"www\"")

if text != None:

  # check if is link or text
  if text.startswith('http') or text.startswith('www'):
    
    # we will need to get the text using requests...
    text = get_text(text)
    
    if text:

      title = text[0]
      text  = text[1:]

    else:

      st.error('We are having problems to crawl this website. Try a different website or coppy the text manually.')
      st.stop()
  
  else:

    title = 'Article summary'
    st.code(str(len(text)) + ' characters' , language="python")
    text  = text.split("\n")
    text  = ['placeholder'] + [t for t in text if t != '']

if len(text) > 1:

    text  = merge_text(text)
    text  = text[:1000]

    if len(text) > 100:

      # summarize
      outputs = model(text, min_length=30, max_length=150, clean_up_tokenization_spaces=True)
      summary = outputs[0]['summary_text']
      summary = '🌈🎩🪄 Summary: \n\n__' + title + "__\n\n" + summary
      st.info(summary)

    else:

      st.error('This text is too short to be summarized.')
    









# ------------------------------------------------------------------------------------
st.markdown("""---""")
st.subheader('To go further')
st.write("[A Gentle Introduction to Vector Space Models](https://machinelearningmastery.com/a-gentle-introduction-to-vector-space-models/)")
st.write("[Measuring Text Similarity Using BERT](https://www.analyticsvidhya.com/blog/2021/05/measuring-text-similarity-using-bert/)")

st.subheader('Other projects')
st.write("[Job description generator](https://vallantin-jobdescriptiongenerator-app-5wz0u4.streamlitapp.com/)")
st.write("[NLP Resources dashboard](https://vallantin-nlp-resources-app-1c6nvk.streamlitapp.com/)")
st.write("[Fashion brands similarity dashboard](https://vallantin-fashion-brands-app-b9zllh.streamlitapp.com/)")
st.write("[Document similarity](https://vallantin-textsimilarity-app-gopds6.streamlitapp.com/)")

# ------------------------------------------------------------------------------------
st.markdown("""---""")
st.image('img/icon.png', width=80)
st.markdown("<h6 style='text-align: left; color: grey;'>Made by <a href='https://wila.me/' target='_blank'>wila.me</a></h6>", unsafe_allow_html=True)



















