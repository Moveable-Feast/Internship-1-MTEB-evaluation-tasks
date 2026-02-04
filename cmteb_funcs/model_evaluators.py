import mteb

def successfully_imported():
    print('Successfully imported \'model_evaluators.py\'!')

def evaluation_evaluator(model_name, evaluation_tasks):
    model = mteb.get_model(model_name)

    tasks = mteb.get_tasks(tasks=evaluation_tasks)
    evaluator = mteb.MTEB(tasks)
    evaluator.run(model, output_folder=f'results/{evaluation_tasks}/{model_name}')