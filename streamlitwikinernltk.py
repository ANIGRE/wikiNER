# -*- coding: utf-8 -*-
"""STREAMLITWIKINERNLTK

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/ANIGRE/9a3678bcbce915303813deff6caced0b/streamlitwikinernltk.ipynb
"""



import streamlit as st 
import os

from textblob import TextBlob 
import spacy
import en_core_web_md
from gensim.summarization import summarize


from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

def text_analyzer(my_text):
	nlp = en_core_web_md.load()
	docx = nlp(my_text)

	allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
	return allData

def entity_analyzer(my_text):
	nlp = en_core_web_md.load()
	docx = nlp(my_text)
	tokens = [ token.text for token in docx]
	entities = [(entity.text,entity.label_)for entity in docx.ents]
	allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
	return allData

def main():
	


	st.title("wiki nlp streamlit")
	st.subheader("wiki on the go with NER..")
	st.markdown("""
    	#### Description
    	+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task
    	Tokenization,NER,Sentiment,Summarization
    	""")

if st.checkbox("Show Tokens and Lemma"):
		st.subheader("Tokenize Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Analyze"):
			nlp_result = text_analyzer(message)
			st.json(nlp_result)

if st.checkbox("Show Named Entities"):
		st.subheader("Analyze Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Extract"):
			entity_result = entity_analyzer(message)
			st.json(entity_result)

if st.checkbox("Show Sentiment Analysis"):
		st.subheader("Analyse Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Analyze"):
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			st.success(result_sentiment)

if st.checkbox("Show Text Summarization"):
		st.subheader("Summarize Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
		if st.button("Summarize"):
			if summary_options == 'sumy':
				st.text("Using Sumy Summarizer ..")
				summary_result = sumy_summarizer(message)
			elif summary_options == 'gensim':
				st.text("Using Gensim Summarizer ..")
				summary_result = summarize(rawtext)
			else:
				st.warning("Using Default Summarizer")
				st.text("Using Gensim Summarizer ..")
				summary_result = summarize(rawtext)

		
			st.success(summary_result)

st.sidebar.subheader("About WIKINERNLTK APP")
st.sidebar.text("NER NLTK APP")
st.sidebar.info("CUDOS TO THE BOOARD INFINITY TEAM")

st.sidebar.subheader("By")
st.sidebar.text("GREGO SHIBOO ANCHEARY")
st.sidebar.text("MACHINE LEARNING ENGINEER")

if __name__ == '__main__':
	main()
