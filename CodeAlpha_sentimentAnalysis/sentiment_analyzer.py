import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

class SentimentAnalyzer:
    def __init__(self):
        """
        Initialize the sentiment analyzer with NLTK's VADER and TextBlob
        """
        # Download required NLTK data
        self.download_nltk_data()
        
        self.sia = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))
        
        # Emotion keywords dictionary
        self.emotion_keywords = {
            'happy': ['happy', 'joy', 'excited', 'great', 'wonderful', 'awesome', 
                     'fantastic', 'amazing', 'love', 'lovely', 'excellent', 'best'],
            'sad': ['sad', 'unhappy', 'depressed', 'miserable', 'terrible', 
                   'horrible', 'awful', 'bad', 'worst', 'disappointed'],
            'angry': ['angry', 'mad', 'annoyed', 'frustrated', 'irritated', 
                     'upset', 'hate', 'rage', 'furious'],
            'fearful': ['scared', 'afraid', 'fear', 'worried', 'anxious', 
                       'nervous', 'terrified'],
            'surprised': ['surprised', 'shocked', 'amazed', 'astonished'],
            'neutral': ['okay', 'fine', 'alright', 'average', 'normal']
        }
    
    def download_nltk_data(self):
        """Download required NLTK datasets"""
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except LookupError:
            nltk.download('vader_lexicon', quiet=True)
        
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
    
    def preprocess_text(self, text):
        """
        Clean and preprocess the text
        """
        if not text:
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        
        # Remove mentions and hashtags
        text = re.sub(r'@\w+|#\w+', '', text)
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and short words
        tokens = [word for word in tokens if word not in self.stop_words and len(word) > 2]
        
        return ' '.join(tokens)
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of the input text
        Returns: Dictionary with sentiment scores and classification
        """
        if not text or text.strip() == '':
            return self._get_empty_result()
        
        # Preprocess text
        processed_text = self.preprocess_text(text)
        
        # Analyze with VADER
        vader_scores = self.sia.polarity_scores(text)
        
        # Analyze with TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Determine sentiment based on compound score
        compound_score = vader_scores['compound']
        
        if compound_score >= 0.05:
            sentiment = 'Positive'
            confidence = compound_score
            sentiment_icon = '😊'
            color = 'success'
        elif compound_score <= -0.05:
            sentiment = 'Negative'
            confidence = abs(compound_score)
            sentiment_icon = '😠'
            color = 'danger'
        else:
            sentiment = 'Neutral'
            confidence = abs(compound_score)
            sentiment_icon = '😐'
            color = 'info'
        
        # Detect emotion
        emotion, emotion_icon = self.detect_emotion(text)
        
        # Calculate text statistics
        word_count = len(text.split())
        char_count = len(text)
        
        # Prepare result
        result = {
            'sentiment': sentiment,
            'sentiment_icon': sentiment_icon,
            'color': color,
            'confidence': round(confidence * 100, 2),
            'polarity': round(polarity, 3),
            'subjectivity': round(subjectivity, 3),
            'emotion': emotion,
            'emotion_icon': emotion_icon,
            'processed_text': processed_text,
            'word_count': word_count,
            'char_count': char_count,
            'vader_scores': vader_scores,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'text_preview': (text[:200] + '...') if len(text) > 200 else text
        }
        
        return result
    
    def _get_empty_result(self):
        """Return empty result structure"""
        return {
            'sentiment': 'Neutral',
            'sentiment_icon': '😐',
            'color': 'info',
            'confidence': 0.0,
            'polarity': 0.0,
            'subjectivity': 0.0,
            'emotion': 'Neutral',
            'emotion_icon': '😐',
            'processed_text': '',
            'word_count': 0,
            'char_count': 0,
            'vader_scores': {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0},
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'text_preview': ''
        }
    
    def detect_emotion(self, text):
        """
        Detect specific emotion from text using keyword matching
        """
        text_lower = text.lower()
        emotion_scores = {}
        
        # Count emotion keyword occurrences
        for emotion, keywords in self.emotion_keywords.items():
            count = sum(1 for keyword in keywords if keyword in text_lower)
            if count > 0:
                emotion_scores[emotion] = count
        
        # Return emotion with highest count
        if emotion_scores:
            emotion = max(emotion_scores.items(), key=lambda x: x[1])[0]
        else:
            emotion = 'neutral'
        
        # Get emotion icon
        emotion_icons = {
            'happy': '😊',
            'sad': '😢',
            'angry': '😠',
            'fearful': '😨',
            'surprised': '😲',
            'neutral': '😐'
        }
        
        return emotion.capitalize(), emotion_icons.get(emotion, '😐')
    
    def analyze_multiple(self, texts):
        """
        Analyze multiple texts and return aggregated results
        """
        results = []
        for text in texts:
            if text and text.strip():
                results.append(self.analyze_sentiment(text))
        
        # Calculate overall statistics
        if results:
            sentiments = [r['sentiment'] for r in results]
            sentiment_counts = {
                'Positive': sentiments.count('Positive'),
                'Negative': sentiments.count('Negative'),
                'Neutral': sentiments.count('Neutral')
            }
            
            # Determine overall sentiment
            overall_sentiment = max(sentiment_counts.items(), key=lambda x: x[1])[0]
            
            # Calculate percentages
            total = len(results)
            percentages = {
                sentiment: round((count / total) * 100, 2)
                for sentiment, count in sentiment_counts.items()
            }
            
            return {
                'overall_sentiment': overall_sentiment,
                'total_reviews': total,
                'sentiment_distribution': sentiment_counts,
                'percentages': percentages,
                'individual_results': results
            }
        
        return None
