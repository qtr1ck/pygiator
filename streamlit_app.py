import streamlit as st
import base64
from PIL import Image
from io import StringIO
from similarity import Code
from plot import draw_plot
    
def renderSvg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    return html

def fileSelect():
  files = ['', '']
  with st.beta_container():
    col1_1, col2_1 = st.beta_columns(2)
    with col1_1:
      files[0] = st.sidebar.file_uploader('First File', key='file1in', type=['py'])

    with col2_1:
      files[1] = st.sidebar.file_uploader('Second File', key='file2in', type=['py'])

  return files

def showResult(c1, c2):
  st.write(c1.similarity(c2))
  st.plotly_chart(draw_plot(c1, c2), use_container_width=True)


def run_app():
  files = fileSelect()
  select = st.sidebar.radio('Compare direction', ('First -> Second', 'Second -> First'))
  st.title("Plagiat Scanner for Python Source Code")
  if st.sidebar.button('Enter'):
    if None in files or '' in files:
      st.error('Please enter two scripts or refer to two python files.')
    else:
      fileOne = files[0].read().decode(errors='ignore')
      fileTwo = files[1].read().decode(errors='ignore')
      if select == 'Second -> First':
        fileOne, fileTwo = fileTwo, fileOne

      c1 = Code(fileOne)
      c2 = Code(fileTwo)
      showResult(c1, c2)


  else:
    st.write("Enter the source file paths in the sidebar.")
    logo = open('logo.svg')
    source = logo.read()
    st.write(renderSvg(source), unsafe_allow_html=True)


run_app()