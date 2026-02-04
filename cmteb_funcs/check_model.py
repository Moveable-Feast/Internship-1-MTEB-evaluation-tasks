from huggingface_hub import model_info

def successfully_imported():
    print('Successfully imported \'check_model.py\'!')

def model_exists(model_name):
    try:
        info = model_info(model_name)
        print("模型存在")
    except Exception as e:
        print(f"模型不存在或无法访问: {e}")