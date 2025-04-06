# custom_handler.py
import litellm
from litellm import CustomLLM, ModelResponse, EmbeddingResponse
from typing import List, Optional, Dict, Any

class MyCustomLLM(CustomLLM):
    def __init__(self):
        pass

    def completion(self, model: str, messages: List[Dict[str, str]], **kwargs) -> ModelResponse:
        response_text = "Hello! This is a custom LLM response."
        return ModelResponse(
            choices=[{"message": {"role": "assistant", "content": response_text}}],
            model=model
        )
    
    async def acompletion(self, *args, **kwargs) -> litellm.ModelResponse:
        return self.completion(*args, **kwargs)

    def embedding(self, model: str, input: List[str], **kwargs) -> EmbeddingResponse:
        print(f"Embedding called with model={model}, input={input}")  # Debug
        dummy_embedding = [0.1, 0.2, 0.3]
        embeddings = [dummy_embedding for _ in input]
        return litellm.EmbeddingResponse(
            object="list",
            data=[{"embedding": emb, "index": idx} for idx, emb in enumerate(embeddings)],
            model=model,
            usage={"prompt_tokens": len(input), "total_tokens": len(input)}
        )
    
    async def aembedding(self, *args, **kwargs) -> litellm.EmbeddingResponse:
        return self.embedding(*args, **kwargs)

my_custom_llm = MyCustomLLM()