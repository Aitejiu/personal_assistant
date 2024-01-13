from openxlab.model import download
download(model_repo='aitejiu/personal_assistant', output='/home/xlab-app-center/personal_assistant')

import os

os.system('streamlit run app.py --server.address=0.0.0.0 --server.port 7860')
