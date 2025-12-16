import asyncio
from typing import Dict, List, Optional
import google.generativeai as genai
from config.settings import settings
from core.constants import GEMINI_TEMPERATURE, GEMINI_MAX_OUTPUT_TOKENS, NO_RELEVANT_CONTENT_FOUND


class GenerationService:
    def __init__(self):
        genai.configure(api_key=settings.gemini_api_key)
        self.model = genai.GenerativeModel(settings.gemini_model)

    async def generate_response(self, context: str, query: str, refusal_mode: bool = False) -> Dict:
        """
        Generate a response based on the provided context and query using Gemini
        """
        if refusal_mode:
            return {
                "generated_text": NO_RELEVANT_CONTENT_FOUND,
                "confidence_score": 0.0,
                "refusal_response": True
            }

        # Construct the prompt
        prompt = f"""
        You are an AI assistant for the "Physical AI & Humanoid Robotics Learning" book.
        Your task is to answer questions based strictly on the provided book content.
        Do not make up information or go beyond what is provided in the context.

        Context: {context}

        Question: {query}

        Please provide a detailed answer based only on the information in the context.
        If the context does not contain sufficient information to answer the question,
        please state that clearly.
        """

        try:
            # Generate content using Gemini
            response = await self.model.generate_content_async(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=GEMINI_TEMPERATURE,
                    max_output_tokens=GEMINI_MAX_OUTPUT_TOKENS,
                )
            )

            # Extract text from response
            generated_text = response.text if response.text else "I couldn't generate a response based on the provided context."

            # In a real implementation, you'd have a way to determine confidence
            # For now, we'll use a placeholder confidence score
            confidence_score = 0.85

            return {
                "generated_text": generated_text,
                "confidence_score": confidence_score,
                "refusal_response": False
            }

        except Exception as e:
            return {
                "generated_text": f"Error generating response: {str(e)}",
                "confidence_score": 0.0,
                "refusal_response": True
            }

    async def generate_selected_text_response(self, selected_text: str, query: str, refusal_mode: bool = False) -> Dict:
        """
        Generate a response specifically for selected-text mode
        """
        if refusal_mode:
            return {
                "generated_text": "No relevant content found in the selected text to answer this question.",
                "confidence_score": 0.0,
                "refusal_response": True
            }

        # Construct the prompt for selected text mode
        prompt = f"""
        You are an AI assistant for the "Physical AI & Humanoid Robotics Learning" book.
        Your task is to answer the question based ONLY on the following selected text.
        Do not use any other information beyond what is provided in the selected text.

        Selected Text: {selected_text}

        Question: {query}

        Please provide an answer based only on the selected text.
        If the selected text does not contain information to answer the question,
        please state that clearly.
        """

        try:
            # Generate content using Gemini
            response = await self.model.generate_content_async(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=GEMINI_TEMPERATURE,
                    max_output_tokens=GEMINI_MAX_OUTPUT_TOKENS,
                )
            )

            # Extract text from response
            generated_text = response.text if response.text else "I couldn't generate a response based on the selected text."

            # Placeholder confidence score
            confidence_score = 0.80

            return {
                "generated_text": generated_text,
                "confidence_score": confidence_score,
                "refusal_response": False
            }

        except Exception as e:
            return {
                "generated_text": f"Error generating response: {str(e)}",
                "confidence_score": 0.0,
                "refusal_response": True
            }


# Singleton instance
generation_service = GenerationService()