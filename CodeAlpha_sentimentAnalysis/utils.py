import re
from datetime import datetime

class TextUtils:
    @staticmethod
    def get_sentiment_color(sentiment):
        """
        Get Bootstrap color class based on sentiment
        """
        colors = {
            'Positive': 'success',
            'Negative': 'danger',
            'Neutral': 'info'
        }
        return colors.get(sentiment, 'secondary')
    
    @staticmethod
    def get_emotion_color(emotion):
        """
        Get color for emotion
        """
        colors = {
            'Happy': 'warning',
            'Sad': 'primary',
            'Angry': 'danger',
            'Fearful': 'dark',
            'Surprised': 'info',
            'Neutral': 'secondary'
        }
        return colors.get(emotion, 'secondary')
    
    @staticmethod
    def get_sample_texts():
        """
        Get sample texts for demonstration
        """
        return [
            "I absolutely love this product! It's amazing and works perfectly. Best purchase ever! 😊",
            "This is the worst service I've ever experienced. Very disappointed and frustrated. 😠",
            "The product arrived on time and works as expected. Nothing special but it's okay. 😐",
            "I'm really happy with my purchase. The quality is excellent and delivery was fast! 👍",
            "Terrible customer support. They never responded to my complaints. Very angry! 👎",
            "It's an average product. Does what it's supposed to do, but could be better. 🤷‍♂️",
            "Absolutely fantastic experience! Will definitely recommend to all my friends! 😍",
            "Waste of money. Product stopped working after 2 days. Never buying again! 😡",
            "Good value for money. Satisfied with the performance. Could improve packaging. 🙂"
        ]
    
    @staticmethod
    def format_text_for_display(text, max_length=300):
        """
        Format text for display with ellipsis if too long
        """
        if len(text) > max_length:
            return text[:max_length] + '...'
        return text
    
    @staticmethod
    def extract_source_info(text):
        """
        Extract potential source information from text
        """
        sources = []
        
        # Check for e-commerce patterns
        if any(word in text.lower() for word in ['amazon', 'flipkart', 'ebay', 'etsy', 'product', 'purchase']):
            sources.append('E-commerce')
        
        # Check for social media patterns
        if any(word in text.lower() for word in ['tweet', 'facebook', 'instagram', 'post', 'like', 'share', 'follow']):
            sources.append('Social Media')
        
        # Check for news patterns
        if any(word in text.lower() for word in ['news', 'article', 'report', 'headline', 'journal', 'media']):
            sources.append('News')
        
        # Check for customer feedback patterns
        if any(word in text.lower() for word in ['customer', 'service', 'support', 'feedback', 'complaint', 'review']):
            sources.append('Customer Feedback')
        
        return sources if sources else ['General Text']
