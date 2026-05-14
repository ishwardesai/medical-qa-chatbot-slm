"""
Medical QA Chatbot - Main Class
Combines RAG retrieval, QA model, and safety guardrails.
"""

from src.safety import is_high_risk, has_red_flags, safety_check
from src.safety import ESCALATION_MESSAGE

BLOCKED_RESPONSE = (
    "I'm sorry, I cannot provide information on that topic. "
    "Please consult a qualified healthcare professional."
)

class MedicalChatbot:
    def __init__(self, retriever, qa_model):
        self.retriever = retriever
        self.qa_model = qa_model
        self.conversation_history = []
        self.session_stats = {
            'total_questions': 0,
            'blocked': 0,
            'flagged': 0,
            'safe': 0,
            'sources_used': []
        }
    
    def chat(self, question: str) -> dict:
        """Process a question and return a safe, grounded answer"""
        self.session_stats['total_questions'] += 1
        
        # Block high risk queries immediately
        if is_high_risk(question):
            self.session_stats['blocked'] += 1
            result = {
                'question': question,
                'answer': BLOCKED_RESPONSE,
                'source': 'Safety Filter',
                'safe': False,
                'blocked': True,
                'retrieval_score': 0.0,
                'flags': []
            }
            self.conversation_history.append(result)
            return result
        
        # Retrieve relevant context
        retrieved = self.retriever.retrieve(question, top_k=1)
        best_context = retrieved[0]['content']
        best_title = retrieved[0]['title']
        retrieval_score = retrieved[0]['score']
        
        # Extract answer
        answer = self.qa_model.extract_answer(question, best_context)
        
        if not answer or len(answer) < 2:
            answer = (
                "I need more context to answer this accurately. "
                "Please consult a healthcare professional."
            )
        
        # Safety check
        check = safety_check(question, answer)
        
        # Add escalation if needed
        for flag in check['flags']:
            if flag['type'] == 'MISSING_ESCALATION':
                answer += ESCALATION_MESSAGE
        
        # Update stats
        if not check['safe']:
            self.session_stats['flagged'] += 1
        else:
            self.session_stats['safe'] += 1
        self.session_stats['sources_used'].append(best_title)
        
        result = {
            'question': question,
            'answer': answer,
            'source': best_title,
            'safe': check['safe'],
            'blocked': False,
            'retrieval_score': retrieval_score,
            'flags': check['flags']
        }
        self.conversation_history.append(result)
        return result
    
    def get_stats(self) -> dict:
        """Return current session statistics"""
        return self.session_stats
    
    def clear_history(self):
        """Reset conversation history and stats"""
        self.conversation_history = []
        self.session_stats = {
            'total_questions': 0,
            'blocked': 0,
            'flagged': 0,
            'safe': 0,
            'sources_used': []
        }
