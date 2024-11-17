import openai

class ChatGPTStoryGenerator:
    def __init__(self, api_key):
        """
        Initializes the ChatGPTStoryGenerator with the OpenAI API key.

        Args:
            api_key (str): OpenAI API key.
        """
        self.api_key = api_key
        openai.api_key = api_key

    def generate_story_segment(self, prompt, max_tokens=1000, temperature=0.7, top_p=0.95):
        """
        Generates a story segment in Arabic using ChatGPT.

        Args:
            prompt (str): Arabic text prompt for the story.
            max_tokens (int): Maximum tokens for the response.
            temperature (float): Sampling temperature for diversity.
            top_p (float): Top-p sampling for diversity.

        Returns:
            str: Generated Arabic story segment.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "أنت راوي قصص عربي متخصص في كتابة حكايات مثل ألف ليلة وليلة."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error generating story: {e}")
            return None
