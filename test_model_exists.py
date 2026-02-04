import cmteb_funcs.check_model as cm

models_list = [
    'BAAI/bge-large-zh',
    'IEITYuan/Yuan-embedding-1.0',
    'Qwen/Qwen3-Embedding-0.6B',
    'moka-ai/m3e-large'
]

for model_name in models_list:
    cm.model_exists(model_name)