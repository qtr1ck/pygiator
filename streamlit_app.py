import streamlit as st
import base64
from io import StringIO
from src.similarity import Code
from src.plot import CodePlot

# renders the logo, so it can be printed 
@st.cache  
def renderSvg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img id="pygiatorLogo" src="data:image/svg+xml;base64,%s"/>' % b64
    return html

# outputs the heatmaps
def printResult(c1, c2):
  st.markdown('Similarity: **%.2f**' %(c1.similarity(c2)))
  sliderValue = st.sidebar.slider("Select similarity threshold", 1, 100, 90)
  # creates the plot 
  p = CodePlot(c1, c2, sliderValue/100) 
  st.plotly_chart(p.fig, use_container_width=True)

# saves the result in the cache and only recalculates when something is changed
@st.cache(allow_output_mutation=True)
def computeCode(f1, f2):
  if None in [f1,f2]:
    return 0,0
  fileOne = f1.read().decode(errors='ignore')
  fileTwo = f2.read().decode(errors='ignore')

  c1 = Code(fileOne, f1.name)
  c2 = Code(fileTwo, f2.name)
  return c1, c2 

def blankLine():
  st.write("")

def appStyle():
  st.markdown(
    f"""
      <style>
          .reportview-container .main .block-container{{
              max-width: 90%;
              padding-top: 0rem;
              padding-right: 1rem;
              padding-left: 1rem;
              padding-bottom: 1rem;
              margin-left: auto;
              margin-right: auto;
          }}
          .reportview-container .main {{
              color: black;
              background-color: white;
          }}
          #pygiatorLogo{{
            width: 70%;
            height: auto;
          }}
      </style>
    """,
    unsafe_allow_html=True,
  )

def run_app():
  st.set_page_config('Pygiator', layout='centered')
  appStyle()

  # sidebar
  file_1 = st.sidebar.file_uploader('First File', key='file1in', type=['py'])
  file_2 = st.sidebar.file_uploader('Second File', key='file2in', type=['py'])

  # main page
  st.title('Pygiator - Plagiat Scanner for Python Source Code')

  c1, c2 = computeCode(file_1, file_2)

  if 0 not in [c1, c2]: 
    # Show similarity using winnowing algorithm
    winnowing_expander = st.beta_expander("Similarity using Winnowing Algorithm")
    with winnowing_expander:
      k_size = st.slider("KGrams Size", 2, 15, 5)
      win_size = st.slider("Sliding Window Size", 2, 15, 4)
      st.markdown('Winnowing-Similarity: **%.2f**' % c1.winnowing_similarity(c2, k_size, win_size)) 
    blankLine()

    # Show similarity using custom algorithm and pyplot for visualization
    if st.checkbox("Swap Files"):
      c1, c2 = c2, c1
    printResult(c1, c2)

  else: # home page is printed if not two files selected
    a = st.beta_container()
    logo = open('./misc/logo.svg')
    source = logo.read()
    st.write(renderSvg(source), unsafe_allow_html=True)
    logo.close()
    a.write("Enter the source file paths in the sidebar.")
  
run_app()