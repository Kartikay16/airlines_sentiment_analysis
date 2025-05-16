from Inference_pipeline.inference_model_inference import ModelInference

class InferMain:

    def __init__(self):
        model_infer = ModelInference()
        self.final_inference = model_infer.get_inference()
        
    
    def get_inference(self):
        return self.final_inference
    

    