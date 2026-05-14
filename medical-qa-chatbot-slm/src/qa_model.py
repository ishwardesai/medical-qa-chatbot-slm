"""
QA Model - Fine-tuned DistilBERT for Medical Question Answering
Extracts precise answer spans from retrieved medical context.
"""

import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

class MedicalQAModel:
    def __init__(self, model_path: str = "distilbert-base-uncased"):
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu'
        )
        print(f"Loading model on {self.device}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForQuestionAnswering.from_pretrained(
            model_path
        )
        self.model.to(self.device)
        self.model.eval()
        print(f"✓ Model loaded: {sum(p.numel() for p in self.model.parameters()):,} parameters")
    
    def extract_answer(self, question: str, context: str) -> str:
        """Extract answer span from context for given question"""
        inputs = self.tokenizer(
            question,
            context,
            return_tensors='pt',
            truncation=True,
            max_length=512,
            padding=True
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        start_logits = outputs.start_logits[0]
        end_logits = outputs.end_logits[0]
        
        best_score = float('-inf')
        best_start = 0
        best_end = 0
        
        for start in range(len(start_logits)):
            for end in range(start, min(start + 50, len(end_logits))):
                score = start_logits[start] + end_logits[end]
                if score > best_score:
                    best_score = score
                    best_start = start
                    best_end = end
        
        answer_tokens = inputs['input_ids'][0][
            best_start:best_end+1
        ].cpu()
        answer = self.tokenizer.decode(
            answer_tokens, skip_special_tokens=True
        )
        return answer.strip()
