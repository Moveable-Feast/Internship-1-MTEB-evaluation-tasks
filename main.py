import cmteb_funcs.model_evaluators as eval

models_list = [
    'BAAI/bge-large-zh',
    'IEITYuan/Yuan-embedding-1.0',
    'Qwen/Qwen3-Embedding-0.6B',
    'moka-ai/m3e-large'
]

retrieval_tasks = [
    'CmedqaRetrieval',
    'CovidRetrieval', 
    'DuRetrieval',
    'EcomRetrieval',
    'MedicalRetrieval',
    'MMarcoRetrieval',
    'T2Retrieval',
    'VideoRetrieval'
]

reranking_tasks = [
    'CMedQAv1-reranking',
    'CMedQAv2-reranking',
    'MMarcoReranking',
    'T2Reranking'
]

sts_tasks = [
    'AFQMC',
    'PAWSX',
    'ATEC',
    'QBQTC',
    'BQ',
    'STS22',
    'LCQMC',
    'STSB'
]

all_tasks = [retrieval_tasks, reranking_tasks, sts_tasks]

for model_name in models_list:
    for evaluation_tasks in all_tasks:
        eval.evaluation_evaluator(model_name, evaluation_tasks)