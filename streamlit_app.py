import streamlit as st
import base64
from PIL import Image
from io import StringIO
from similarity import Code
from plot import draw_plot, sim_marker
    
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
  st.write('Similarity: ' + str(c1.similarity(c2)))
  plotHeight = max([len(c1), len(c2)]) * 10
  s = sim_marker()
  a = st.sidebar.slider("Select similarity threshold", value=90, min_value=1)
  s.set_threshold(a / 100)
  st.plotly_chart(draw_plot(c1, c2, s).update_layout(height=plotHeight, width=850))

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def computeCode(files):
  if None in files:
    return 0,0
  fileOne = files[0].read().decode(errors='ignore')
  fileTwo = files[1].read().decode(errors='ignore')

  c1 = Code(fileOne)
  c2 = Code(fileTwo)
  return c1, c2 

def run_app():
  st.set_page_config('Pygiator', layout='centered')
  files = fileSelect()
  st.title("Plagiat Scanner for Python Source Code")

  c1, c2 = computeCode(files)

  if 0 not in [c1, c2]:
    if st.checkbox("Swap Scripts"):
      c1, c2 = c2, c1
    showResult(c1, c2)
  else:
    st.write("Enter the source file paths in the sidebar.")
    logo = open('logo.svg')
    source = logo.read()
    st.write(renderSvg(source), unsafe_allow_html=True)

  

run_app()