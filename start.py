from openxlab.model import download
download(model_repo='aitejiu/personal_assistant', output='/home/xlab-app-center/personal_assistant_hf')
download(model_repo='OpenLMLab/InternLM-7b', output='/home/xlab-app-center/internlm-chat-7b')

import os

os.system("cd /home/xlab-app-center")
os.system("git clone -b v0.1.9  https://github.com/InternLM/xtuner")
os.system("cd xtuner")
os.system("pip install -e '.[all]'")
os.system("cd ..")
os.system("export MKL_SERVICE_FORCE_INTEL=1")
os.system("export MKL_THREADING_LAYER='GNU'")
os.system("mkdir merged")
os.system("xtuner convert merge \
    /home/xlab-app-center/internlm-chat-7b \
    /home/xlab-app-center/personal_assistant_hf \
    /home/xlab-app-center/merged \
    --max-shard-size 2GB")

os.system('streamlit run app.py --server.address=0.0.0.0 --server.port 7860')
